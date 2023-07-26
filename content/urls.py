from .views import (
    article_views,
    infographie_views,
    secteur_views,
    views,
    theme_views,
)
from django.urls import path

urlpatterns = [
    path("secteur/", secteur_views.liste_secteur, name="liste_secteur"),
    path("secteur/<int:id>/", secteur_views.secteur, name="secteur"),
    path("infographie/<int:id>/", infographie_views.infographie, name="infographie"),
    path("article/<int:id>/", article_views.article, name="article"),
    path("theme/<int:id>/", theme_views.theme, name="theme"),
    path("recherche/", views.recherche, name="recherche"),
]
