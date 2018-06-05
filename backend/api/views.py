from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from names_project.settings import PER_PAGE
from .parser import dispatcher
from .models import *
from .serializers import *


class BoysNamesList(APIView):
    parser_classes = (JSONParser,)

    def build_names_query(self):
        pass

    def get(self, request, format=None):
        boy_names = BoyName.objects.all()

        paginator = Paginator(boy_names, PER_PAGE)
        page = request.GET.get('page')
        if not page:
            page = 1
        boy_names = paginator.page(page)

        serializer = BoysNamesSerializer(boy_names, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        Method for search boys names
        :param request: JSON string
         search_phrase: str,
         age_distribution: list
         search_criteria: str (begin, end, middle)
         frequency: list (based on NamesModel frequency field)
         limit: int
         skip: int
        :return: Response object
        """

        print(request.data)
        name = request.data.get("search_phrase")
        criteria = request.data.get("search_criteria")
        frequency = request.data.get("frequency")
        age_distribution = request.data.get("age_distribution")
        double_name = request.data.get("double_name")
        letters_range = request.data.get("letters_range")
        limit = request.data.get("limit", PER_PAGE)
        skip = request.data.get("skip", 0)

        query = Q()

        if frequency is not None:
            q = [Q(frequency__exact=f) for f in frequency]

            query = q.pop()

            for item in q:
                query |= item

        resp = BoyName.objects.filter(query)

        if double_name:
            resp = resp.filter(double_name=True)

        if letters_range:
            resp = resp.filter(number_of_letters=letters_range)

        mask = "age_distribution_{}__gt"

        # AND age_distribution way
        # dd = {}
        #
        # for d in age_distribution:
        #     key = mask.format(d)
        #     dd[key] = 0
        # resp = resp.filter(**dd)

        # OR age_distribution way
        or_query_set = Q()
        for d in age_distribution:
            tmp = Q(**{mask.format(d): 0})
            or_query_set |= tmp

        resp = resp.filter(or_query_set)

        print(resp.query)

        if criteria == "begin":
            resp = resp.filter(name__istartswith=name)
        elif criteria == "middle":
            print(criteria)
            resp = resp.filter(name__icontains=name)
        elif criteria == "end":
            resp = resp.filter(name__iendswith=name)
        else:
            resp = resp.filter(name__iexact=name)

        resp = resp.all()[skip:limit]
        serializer = BoysNamesSerializer(resp, many=True)

        return Response(serializer.data)


class GirlsNamesList(APIView):
    def get(self, request, format=None):
        girl_names = GirlName.objects.all()

        paginator = Paginator(girl_names, PER_PAGE)
        page = request.GET.get('page')
        if not page:
            page = 1
        girl_names = paginator.page(page)

        serializer = GirlsNamesSerializer(girl_names, many=True)

        return Response(serializer.data)


class PopularNamesList(APIView):
    def get(self, request, format=None):
        popular_names = PopularName.objects.all()

        paginator = Paginator(popular_names, PER_PAGE)
        page = request.GET.get('page')
        if not page:
            page = 1
        popular_names = paginator.page(page)

        serializer = PopularNamesSerializer(popular_names, many=True)

        return Response(serializer.data)


class VariationsNamesList(APIView):
    def get(self, request, format=None):
        variation_names = Variant.objects.all()

        paginator = Paginator(variation_names, PER_PAGE)
        page = request.GET.get('page')
        if not page:
            page = 1
        variation_names = paginator.page(page)

        serializer = VariantNamesSerializer(variation_names, many=True)

        return Response(serializer.data)


def upload_file(request):
    print(repr(request.FILES['db_file']))
    model_name = request.POST.get("db_name")

    parser = dispatcher(model_name)
    parser(file_obj=request.FILES['db_file'], sheet_name=model_name)

    messages.success(request, 'Table {} updated.'.format(model_name))
    return redirect(reverse("admin:api_{}_changelist".format(model_name)))

