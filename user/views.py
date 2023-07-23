from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms.registration_form import RegistrationForm


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse("index")


class CustomLogoutView(LogoutView):
    template_name = "logout.html"


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            last_name = form.cleaned_data["last_name"]
            first_name = form.cleaned_data["first_name"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            print("ok")

            if password != password_confirmation:
                messages.error(
                    request, "Les mots de passe saisis ne correspondent pas."
                )
                return render(request, "registration.html", {"form": form})

            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    last_name=last_name,
                    first_name=first_name,
                    password=password,
                )
                print(user)

                user.save()

                return HttpResponseRedirect("login.html")
            else:
                messages.error(request, "Le nom d'utilisateur existe déjà.")
                return render(request, "registration.html", {"form": form})

    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})
