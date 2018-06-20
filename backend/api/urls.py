from django.urls import path

from .views import BoysNamesList, GirlsNamesList, VariationsNamesList, PopularNamesList, FavoriteNamesList, EmailSender


urlpatterns = [
    path("test/", BoysNamesList.as_view()),
    path("girls-names/", GirlsNamesList.as_view()),
    path("variant-names/", VariationsNamesList.as_view()),
    path("popular-names/", PopularNamesList.as_view()),
    path("favorite-names/", FavoriteNamesList.as_view()),
    path('send/email/', EmailSender.as_view()),
]
