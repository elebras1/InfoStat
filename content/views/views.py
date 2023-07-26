from django.shortcuts import render, redirect
from django.http import Http404
from ..models import Theme, Infographie, Article
from user.models import UserProfile
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from ..forms.rechercheForm import RechercheForm
from django.db.models import Q
from django.urls import reverse

import random


def index(request):
    try:
        themes_popular = Theme.objects.order_by("-compteur")[:30]
        themes = Theme.objects.all()
        themes_random = random.sample(list(themes), 10)
        themes_new = Theme.objects.order_by("-pub_date")[:3]

    except Theme.DoesNotExist:
        raise Http404("Aucun thème n'a été trouvé.")

    try:
        today = datetime.now().date()
        one_years_ago = today - timedelta(days=365)
        infographies = Infographie.objects.filter(pub_date__gte=one_years_ago).order_by(
            "-compteur"
        )[:5]
    except Infographie.DoesNotExist:
        raise Http404("Aucun graphique n'a été trouvé.")

    form = RechercheForm(request.POST)
    if form.is_valid():
        recherche = form.cleaned_data.get("result", None)
        if recherche:
            url = reverse("recherche") + f"?result={recherche}"
            return redirect(url)

    try:
        superusers = UserProfile.objects.filter(user__is_superuser=True)
    except UserProfile.DoesNotExist:
        raise Http404("")

    return render(
        request,
        "index.html",
        {
            "themes_popular": themes_popular,
            "infographies": infographies,
            "themes_random": themes_random,
            "themes_new": themes_new,
            "form": form,
            "superusers": superusers,
        },
    )


def recherche(request):
    form = RechercheForm(request.GET)

    theme_id = request.GET.get("theme", None)
    secteur_id = request.GET.get("secteur", None)
    recherche = request.GET.get("result", None)
    selection = request.GET.get("selection", None)

    if theme_id:
        articles = Article.objects.filter(theme__id=theme_id).order_by("-pub_date")
        infographies = Infographie.objects.filter(theme__id=theme_id).order_by(
            "-pub_date"
        )
    elif secteur_id:
        articles = Article.objects.filter(theme__secteur__id=secteur_id).order_by(
            "-pub_date"
        )
        infographies = Infographie.objects.filter(
            theme__secteur__id=secteur_id
        ).order_by("-pub_date")
    else:
        articles = Article.objects.order_by("-pub_date")
        infographies = Infographie.objects.order_by("-pub_date")

    if recherche:
        articles = articles.filter(
            Q(titre__istartswith=recherche) | Q(titre__icontains=" " + recherche)
        )
        infographies = infographies.filter(
            Q(titre__istartswith=recherche) | Q(titre__icontains=" " + recherche)
        )

    results = list(articles) + list(infographies)

    if selection == "populaire":
        results.sort(key=lambda x: x.compteur, reverse=True)
    else:
        results.sort(key=lambda x: x.pub_date, reverse=True)

    nombre_total = len(articles) + len(infographies)

    results_per_page = 10
    paginator = Paginator(results, results_per_page)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)

    return render(
        request,
        "recherche.html",
        {
            "nombre_total": nombre_total,
            "results": results,
            "page": page,
            "form": form,
            "recherche": recherche,
            "selection": selection,
            "theme_id": theme_id,
        },
    )
