from django.contrib import admin
from django.urls import include, path
from content import views

urlpatterns = [
    path("content/", include("content.urls")),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
]
