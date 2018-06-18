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
