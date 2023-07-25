from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms.registration_form import RegistrationForm
from .forms.profil_form import ProfilForm
from .forms.password_form import PasswordForm
from content.models import Infographie, Article
from content.forms.rechercheForm import RechercheForm
from django.db.models import Q


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse("index")

    def form_invalid(self, form):
        # Appeler la méthode form_invalid() de la classe parent pour effectuer le traitement par défaut
        response = super().form_invalid(form)

        # Ajouter un message d'erreur personnalisé
        messages.error(
            self.request,
            "Désolé, votre nom d’utilisateur ou mot de passe est incorrect.",
        )

        return response


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

                user.save()

                return HttpResponseRedirect("login.html")
            else:
                messages.error(request, "Le nom d'utilisateur existe déjà.")
                return render(request, "registration.html", {"form": form})

    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})


def profil(request):
    user = request.user

    infographies = Infographie.objects.filter(infographie_favori__user=user).order_by(
        "-pub_date"
    )
    articles = Article.objects.filter(article_favori__user=user).order_by("-pub_date")

    form = RechercheForm(request.GET)

    recherche = request.GET.get("result", None)

    if recherche:
        infographies = infographies.filter(
            Q(titre__istartswith=recherche) | Q(titre__icontains=" " + recherche)
        )
        articles = articles.filter(
            Q(titre__istartswith=recherche) | Q(titre__icontains=" " + recherche)
        )

    return render(
        request,
        "profil.html",
        {
            "articles": articles,
            "infographies": infographies,
            "user": user,
            "form": form,
        },
    )


def profil_edit(request):
    user = request.user

    if request.method == "POST":
        form = ProfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profil")
    else:
        form = ProfilForm(instance=user)
    return render(request, "profil_edit.html", {"form": form})


def password_edit(request):
    user = request.user

    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            new_password = form.cleaned_data["new_password"]
            new_password_confirmation = form.cleaned_data["new_password_confirmation"]

            if user.check_password(password):
                if new_password == new_password_confirmation:
                    user.set_password(new_password)
                    user.save()
                    return redirect("login")
                else:
                    messages.error(
                        request,
                        "Le nouveau mot de passe saisis ne correspond pas celui de la confirmation.",
                    )
            else:
                messages.error(request, "Le mot de passe ne correspond pas.")
    else:
        form = PasswordForm()
    return render(request, "password_edit.html", {"form": form})
