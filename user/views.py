from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.shortcuts import render
from .forms.registration_form import RegistrationForm


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse("index")


class CustomLogoutView(LogoutView):
    template_name = "logout.html"


def registration(request):
    form = RegistrationForm(request.POST)
    return render(request, "registration.html", {"form": form})
