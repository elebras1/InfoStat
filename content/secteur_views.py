from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Secteur, Infographie, Article
from datetime import datetime, timedelta


def liste_secteur(request):
    secteurs = Secteur.objects.order_by("nom")
    return render(request, "liste_secteur.html", {"secteurs": secteurs})


def secteur(request, id):
    secteur = get_object_or_404(Secteur, id=id)

    today = datetime.now().date()
    five_years_ago = today - timedelta(days=1825)
    themes = secteur.themes.all()
    infographies_populaires = Infographie.objects.filter(
        theme__in=themes, pub_date__gte=five_years_ago
    ).order_by("-compteur")[:10]

    articles_populaires = Article.objects.filter(
        theme__in=themes, pub_date__gte=five_years_ago
    ).order_by("-compteur")[:10]

    infographies_recentes = Infographie.objects.all().order_by("-pub_date")[:10]

    return render(
        request,
        "secteur.html",
        {
            "secteur": secteur,
            "infographies_populaires": infographies_populaires,
            "infographies_recentes": infographies_recentes,
            "articles_populaires": articles_populaires,
        },
    )
