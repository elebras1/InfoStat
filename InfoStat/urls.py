from django.contrib import admin
from django.urls import include, path
from content.views.views import index

urlpatterns = [
    path("content/", include("content.urls")),
    path("user/", include("user.urls")),
    path("admin/", admin.site.urls),
    path("", index, name="index"),
]
