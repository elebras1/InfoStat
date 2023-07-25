from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from content.views.views import index
from django.conf.urls.static import static

urlpatterns = [
    path("content/", include("content.urls")),
    path("user/", include("user.urls")),
    path("admin/", admin.site.urls),
    path("", index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
