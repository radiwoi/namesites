from django.urls import path

from .views import BoysNamesList, GirlsNamesList, VariationsNamesList, PopularNamesList


urlpatterns = [
    path("test/", BoysNamesList.as_view()),
    path("girls-names/", GirlsNamesList.as_view()),
    path("variant-names/", VariationsNamesList.as_view()),
    path("popular-names/", PopularNamesList.as_view()),
]
