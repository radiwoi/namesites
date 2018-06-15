from rest_framework import serializers
from rest_framework import status
from rest_framework.fields import SerializerMethodField

from .models import BoyName, GirlName, PopularName, Variant


class BoysNamesSerializer(serializers.ModelSerializer):
    variants = SerializerMethodField()
    popular = SerializerMethodField()

    def get_variants(self, boy_name):
        return VariantNamesSerializer(boy_name.variants.all(), many=True).data

    def get_popular(self, boy_name):
        return PopularNamesSerializer(boy_name.popular.get(year=self.context["request"].data.get("popular_year"))).data

    class Meta:
        model = BoyName
        fields = ('id',
                  'name',
                  'frequency',
                  'average_age',
                  'variants',
                  'popular',
                  'total_bearing_name',
                  'meaning'
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
    class Meta:
        model = Variant
        fields = ('language', 'name',)
