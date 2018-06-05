from rest_framework import serializers
from rest_framework import status

from .models import *


class BoysNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoyName
        fields = "__all__"


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
        fields = "__all__"
