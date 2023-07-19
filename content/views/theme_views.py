from django.shortcuts import render, get_object_or_404
from django.http import Http404
from ..models import Theme, Infographie, Article


def theme(request, id):
    theme = get_object_or_404(Theme, pk=id)
    infographies = Infographie.objects.filter(theme=theme).order_by("-pub_date")[:6]
    articles = Article.objects.filter(theme=theme).order_by("-pub_date")[:6]
    theme.compteur += 1
    theme.save()

    return render(
        request,
        "theme.html/",
        {"theme": theme, "infographies": infographies, "articles": articles},
    )
