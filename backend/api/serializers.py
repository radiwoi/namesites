from django.db.models import Count
from rest_framework import serializers
from rest_framework import status
from rest_framework.fields import SerializerMethodField

from .models import BoyName, GirlName, PopularName, Variant, FooterTexts, PojknamnFooterText, FlicknamnFooterText


class BoysNamesSerializer(serializers.ModelSerializer):
    variants = SerializerMethodField()
    popular = SerializerMethodField()

    def get_variants(self, boy_name):
        query = Variant.objects.raw("""
            SELECT max(`api_variant`.`id`) as id, group_concat(name SEPARATOR ', ') AS `variants`, `api_variant`.`language`, COUNT(`api_variant`.`language`) AS `cnt`
            FROM `api_variant`
            INNER JOIN `api_boyname_variants`
            ON (`api_variant`.`id` = `api_boyname_variants`.`variant_id`)
            WHERE `api_boyname_variants`.`boyname_id` = %s 
            AND   `api_variant`.`id` NOT IN (
                SELECT `api_variant`.`id` FROM `api_variant` WHERE `api_variant`.`name` = %s
            ) 
            GROUP BY `api_variant`.`language` ORDER BY NULL
        """, [boy_name.pk, boy_name.name])

        return VariantNamesSerializer(query, many=True).data

    def get_popular(self, boy_name):
        d = None
        if self.context.get("request"):
            # try:
            d = boy_name.popular.filter(year=self.context.get("request").data.get("popular_year")).first()
        return PopularNamesSerializer(d).data

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
    variants = SerializerMethodField()
    popular = SerializerMethodField()

    def get_variants(self, girl_name):
        query = Variant.objects.raw("""
            SELECT max(`api_variant`.`id`) as id, group_concat(name SEPARATOR ', ') AS `variants`, `api_variant`.`language`, COUNT(`api_variant`.`language`) AS `cnt`
            FROM `api_variant`
            INNER JOIN `api_girlname_variants`
            ON (`api_variant`.`id` = `api_girlname_variants`.`variant_id`)
            WHERE `api_girlname_variants`.`girlname_id` = %s
            AND   `api_variant`.`id` NOT IN (
                SELECT `api_variant`.`id` FROM `api_variant` WHERE `api_variant`.`name` = %s
            ) 
            GROUP BY `api_variant`.`language` ORDER BY NULL
        """, [girl_name.pk, girl_name.name])

        return VariantNamesSerializer(query, many=True).data

    def get_popular(self, girl_name):
        d = None
        if self.context.get("request"):
            # try:
            d = girl_name.popular.filter(year=self.context.get("request").data.get("popular_year")).first()
        return PopularNamesSerializer(d).data

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


class FooterTextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterTexts
        fields = '__all__'


class PojknamnFooterTextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PojknamnFooterText
        fields = '__all__'


class FlicknamnFooterTextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlicknamnFooterText
        fields = '__all__'
