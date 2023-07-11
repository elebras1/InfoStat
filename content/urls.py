from . import views
from django.urls import include, path

urlpatterns = [path("secteur", views.secteur, name="secteur")]
