from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from names_project.settings import PER_PAGE, PER_PAGE_POPULAR
from .parser import dispatcher
from .models import BoyName, GirlName, PopularName, Variant
from .serializers import BoysNamesSerializer, GirlsNamesSerializer, VariantNamesSerializer, PopularNamesSerializer

from django.db.models import Transform
from django.db.models import CharField, TextField

from .email_sender import Mailer


class LowerCase(Transform):
    lookup_name = 'lower'
    function = 'LOWER'
    # bilateral = True


CharField.register_lookup(LowerCase)
TextField.register_lookup(LowerCase)


class ModelsMixin:
    model = BoyName
    serializer_class = BoysNamesSerializer

    def assign_model(self, request):
        if 'http://localhost:8082/' in request.META['HTTP_REFERER']:
            self.serializer_class = GirlsNamesSerializer
            self.model = GirlName


class QueryRepository:
    def __init__(self):
        pass

    @staticmethod
    def build_query(cls, request, model):
        """
        Method for search boys names
        :param request: JSON string
         search_phrase: str,
         age_distribution: list
         search_criteria: str (begin, end, middle)
         frequency: list (based on NamesModel frequency field)
         letters_range: str
         double_name: bool
         limit: int
         skip: int
        :return: Response object
        """
        # print(request.data)
        name = request.data.get("search_phrase")
        criteria = request.data.get("search_criteria")
        frequency = request.data.get("frequency")
        age_distribution = request.data.get("age_distribution")
        letters_range = request.data.get("letters_range")

        resp = model.objects.filter()

        if frequency is not None and len(frequency) > 0:
            resp = model.objects.filter(frequency__in=frequency).defer("double_name", "number_of_letters")

        double_name = True in letters_range

        # resp = resp.filter(double_name=True)

        if letters_range is not None and len(letters_range) > 0:
            if double_name:
                letters_range.remove(True)
                resp = resp.filter(Q(number_of_letters__in=letters_range) | Q(double_name=True))
            else:
                resp = resp.filter(double_name=False)
                resp = resp.filter(number_of_letters__in=letters_range)

        if age_distribution is not None and len(age_distribution) > 0:
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

        if criteria is not None and len(name) > 0:
            if criteria == "start":
                resp = resp.filter(name__lower__istartswith=name.lower())
            elif criteria == "middle":
                resp = resp.filter(name__lower__icontains=name.lower())
            elif criteria == "end":
                resp = resp.filter(name__lower__iendswith=name.lower())
            else:
                resp = resp.filter(name__lower=name)

        return resp


class BoysNamesList(generics.ListAPIView):
    parser_classes = (JSONParser,)
    serializer_class = BoysNamesSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        request = self.request
        resp = QueryRepository.build_query(QueryRepository, request, BoyName)
        # print(resp.query)
        return resp.all()

    def get(self, request, *args, **kwargs):
        boy_names = BoyName.objects.all()

        paginator = Paginator(boy_names, PER_PAGE)
        page = request.GET.get('page')
        if not page:
            page = 1
        boy_names = paginator.page(page)

        serializer = BoysNamesSerializer(boy_names, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GirlsNamesList(generics.ListAPIView):
    serializer_class = GirlsNamesSerializer
    pagination_class = LimitOffsetPagination
    parser_classes = (JSONParser,)

    def get_queryset(self):
        request = self.request
        resp = QueryRepository.build_query(QueryRepository, request, GirlName)
        # print(resp.query)
        return resp.all()

    def get(self, request, *args, **kwargs):
        girl_names = GirlName.objects.all()

        paginator = Paginator(girl_names, PER_PAGE)
        page = request.GET.get('page')
        if not page:
            page = 1
        girl_names = paginator.page(page)

        serializer = GirlsNamesSerializer(girl_names, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PopularNamesList(generics.ListAPIView, ModelsMixin):
    serializer_class = BoysNamesSerializer
    pagination_class = LimitOffsetPagination
    # model = BoyName

    def get_queryset(self):
        request = self.request
        self.assign_model(request)
        popular_name = request.data.get("popular_year", 2017)

        resp = QueryRepository.build_query(QueryRepository, request, self.model)

        resp = resp.filter(popular__year=popular_name)
        resp = resp.order_by('popular__position')
        # print(resp.query)
        return resp.all()

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.META['HTTP_REFERER'] == 'http://localhost:8082/':
            self.serializer_class = GirlsNamesSerializer
            self.model = GirlName
        order = request.GET.get('order')

        if order:
            popular_names = self.model.objects.order_by('?')[:PER_PAGE_POPULAR]
        else:
            popular_names = self.model.objects.all()
            paginator = Paginator(popular_names, PER_PAGE)
            page = request.GET.get('page', 1)
            popular_names = paginator.page(page)

        serializer = self.serializer_class(popular_names, many=True)

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


class FavoriteNamesList(generics.ListAPIView, ModelsMixin):
    serializer_class = BoysNamesSerializer
    pagination_class = LimitOffsetPagination
    model = BoyName

    def get_queryset(self):
        request = self.request
        self.assign_model(request)

        ids = request.data.get("ids")
        resp = QueryRepository.build_query(QueryRepository, request, self.model)

        resp = resp.filter(pk__in=ids)
        print(resp.query)
        return resp

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


def upload_file(request):
    print(repr(request.FILES['db_file']))
    model_name = request.POST.get("db_name")

    # TODO exception handler
    parser = dispatcher(model_name, request.FILES['db_file'], model_name)
    result, reason = parser.parse()
    print(result)
    if result:
        messages.success(request, 'Table {} updated. Write {} records'.format(model_name, result))
    else:
        messages.warning(request, 'Table {} does not updated. Reason {}'.format(model_name, reason))

    return redirect(reverse("admin:api_{}_changelist".format(model_name)))


