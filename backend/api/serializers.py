from django.db.models import Count
from rest_framework import serializers
from rest_framework import status
from rest_framework.fields import SerializerMethodField

from .models import BoyName, GirlName, PopularName, Variant


class BoysNamesSerializer(serializers.ModelSerializer):
    variants = SerializerMethodField()
    popular = SerializerMethodField()

    def get_variants(self, boy_name):
        # query = boy_name.variants.all().extra(select={"variants": "concat(name,',')"}).values("language", "variants").annotate(cnt=Count("language"))
        # print(query.query)
        # print(boy_name.variants)
        query = Variant.objects.raw("""
            SELECT max(`api_variant`.`id`) as id, group_concat(name SEPARATOR ', ') AS `variants`, `api_variant`.`language`, COUNT(`api_variant`.`language`) AS `cnt`
            FROM `api_variant`
            INNER JOIN `api_boyname_variants`
            ON (`api_variant`.`id` = `api_boyname_variants`.`variant_id`)
            WHERE `api_boyname_variants`.`boyname_id` = %s GROUP BY `api_variant`.`language` ORDER BY NULL
        """, [boy_name.pk])
        # print(list(query))
        # print(boy_name.variants.values_list('id', flat=True))
        # query = boy_name.variants.all()\
        #     .extra(select={"variants": "group_concat(name)"}) \
        #     .values("language", "variants") \
        #     .order_by("language") \
        #     .annotate(cnt=Count("language"))
        # print(query.query)

        return VariantNamesSerializer(query, many=True).data

    def get_popular(self, boy_name):
        d = None
        if self.context.get("request"):
            # try:
            d = boy_name.popular.filter(year=self.context.get("request").data.get("popular_year")).first()
        #     except PopularName.DoesNotExist:
        #         d = boy_name.popular.first()
        # else:
        #     d = boy_name.popular.first()
        return PopularNamesSerializer(d).data
        # return PopularNamesSerializer(boy_name.popular.first()).data

    class Meta:
        model = BoyName
        fields = ('id',
                  'name',
                  'frequency',
                  'average_age',
                  'variants',
                  'popular',
                  'total_bearing_name',
                  'meaning',
                  'age_distribution_10',
                  'age_distribution_20',
                  'age_distribution_30',
                  'age_distribution_50',
                  'age_distribution_70',
                  'age_distribution_71',
                  )


class GirlsNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GirlName
        fields = '__all__'


class PopularNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularName
        fields = ('year', 'position',)


class VariantNamesSerializer(serializers.ModelSerializer):
    variants = SerializerMethodField()

    def get_variants(self, variant):
        return variant.variants

    class Meta:
        model = Variant
        fields = ('language', 'variants',)
