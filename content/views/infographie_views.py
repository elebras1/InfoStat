from django.shortcuts import render, get_object_or_404
from django.http import Http404
from ..models import Infographie, Article, Infographie_favori


def infographie(request, id):
    infographie = get_object_or_404(Infographie, pk=id)
    theme = infographie.theme
    infographie_selection = Infographie.objects.filter(theme=theme).order_by(
        "-pub_date"
    )[:4]
    article_selection = Article.objects.filter(theme=theme).order_by("-pub_date")[:4]
    infographie.compteur += 1
    infographie.save()

    user = request.user

    if user.is_authenticated:
        favori = Infographie_favori.objects.filter(
            user=user,
            infographie=infographie,
        )

        etat_favori = favori.exists()

    else:
        etat_favori = False

    if request.method == "POST" and user.is_authenticated:
        if not favori:
            new_favori = Infographie_favori.objects.create(
                user_id=user.id,
                infographie_id=infographie.id,
            )
            etat_favori = True
        else:
            Infographie_favori.objects.filter(
                user=user,
                infographie=infographie,
            ).delete()
            etat_favori = False

    return render(
        request,
        "infographie.html",
        {
            "infographie": infographie,
            "infographie_selection": infographie_selection,
            "article_selection": article_selection,
            "etat_favori": etat_favori,
        },
    )
