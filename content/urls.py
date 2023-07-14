from . import views, secteur_views, infographie_views, article_views, theme_views
from django.urls import include, path

urlpatterns = [
    path("secteur", secteur_views.secteur, name="secteur"),
    path("infographie/<int:id>/", infographie_views.infographie, name="infographie"),
    path("article/<int:id>/", article_views.article, name="article"),
    path("theme/<int:id>/", theme_views.theme, name="theme"),
]
