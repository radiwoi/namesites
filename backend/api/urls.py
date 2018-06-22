from django.urls import path

from .views import BoysNamesList, GirlsNamesList, PopularNamesList, FavoriteNamesList, FooterTextsList


urlpatterns = [
    path("test/", BoysNamesList.as_view()),
    path("footer-texts/", FooterTextsList.as_view()),
    path("girls-names/", GirlsNamesList.as_view()),
    path("popular-names/", PopularNamesList.as_view()),
    path("favorite-names/", FavoriteNamesList.as_view()),
]
