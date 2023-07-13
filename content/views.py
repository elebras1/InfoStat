from django.shortcuts import render
from django.http import Http404
from .models import Theme, Infographie, Secteur
from datetime import datetime, timedelta

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

    return render(
        request,
        "index.html",
        {
            "themes_popular": themes_popular,
            "infographies": infographies,
            "themes_random": themes_random,
            "themes_new": themes_new,
        },
    )
