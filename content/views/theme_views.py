from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from ..models import Theme, Infographie, Article
from ..forms.rechercheForm import RechercheForm
from django.urls import reverse


def theme(request, id):
    theme = get_object_or_404(Theme, pk=id)

    infographies = Infographie.objects.filter(theme=theme).order_by("-pub_date")[:6]
    articles = Article.objects.filter(theme=theme).order_by("-pub_date")[:6]

    theme.compteur += 1
    theme.save()

    form = RechercheForm(request.POST)
    if form.is_valid():
        recherche = form.cleaned_data.get("result", None)
        if recherche:
            url = reverse("recherche") + f"?result={recherche}" + f"&theme={theme.id}"
            return redirect(url)

    print("ok")
    return render(
        request,
        "theme.html",
        {
            "theme": theme,
            "infographies": infographies,
            "articles": articles,
            "form": form,
        },
    )
