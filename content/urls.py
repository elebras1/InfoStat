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
    path("article/new/", article_views.article_new, name="article_new"),
    path("article/edit/<int:id>/", article_views.article_edit, name="article_edit"),
    path("infographie/new/", infographie_views.infographie_new, name="infographie_new"),
    path(
        "infographie/edit/<int:id>/",
        infographie_views.infographie_edit,
        name="infographie_edit",
    ),
    path("dailydata/", views.daily_data, name="daily_data"),
]
