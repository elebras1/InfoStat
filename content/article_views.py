from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Article, Infographie


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    theme = article.theme
    article_selection = Article.objects.filter(theme=theme).order_by("-pub_date")[:4]
    infographie_selection = Infographie.objects.filter(theme=theme).order_by(
        "-pub_date"
    )[:4]
    article.compteur += 1
    article.save()

    return render(
        request,
        "article.html/",
        {
            "article": article,
            "article_selection": article_selection,
            "infographie_selection": infographie_selection,
        },
    )
