from rest_framework import serializers
from rest_framework import status
from rest_framework.fields import SerializerMethodField

from .models import BoyName, GirlName, PopularName, Variant


class BoysNamesSerializer(serializers.ModelSerializer):
    variants = SerializerMethodField()

    def get_variants(self, boy_name):
        return VariantNamesSerializer(boy_name.variants.all(), many=True).data

    class Meta:
        model = BoyName
        fields = ("name", "variants",)


class GirlsNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GirlName
        fields = "__all__"


class PopularNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularName
        fields = "__all__"


class VariantNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ("language", "name",)
