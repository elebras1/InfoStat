from django.urls import path

from django.conf import settings


from .views import (
    CustomLoginView,
    CustomLogoutView,
    registration,
    profil,
    profil_edit,
    password_edit,
)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("registration/", registration, name="registration"),
    path("profil/", profil, name="profil"),
    path("profil/edit", profil_edit, name="profil_edit"),
    path("profil/password_edit", password_edit, name="password_edit"),
]
