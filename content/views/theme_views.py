from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from ..models import Theme, Infographie, Article
from ..forms.rechercheForm import RechercheForm
from ..forms.theme_form import ThemeForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test


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
        "theme/theme.html",
        {
            "theme": theme,
            "infographies": infographies,
            "articles": articles,
            "form": form,
        },
    )


@login_required
@user_passes_test(lambda user: user.is_superuser)
def theme_new(request):
    if request.method == "POST":
        form = ThemeForm(request.POST, request.FILES)
        if form.is_valid():
            illustration = request.FILES.get("illustration")
            theme = form.save(commit=False)
            theme.illustration = illustration
            theme.save()
            return redirect(reverse("theme", args=[theme.id]))
    else:
        form = ThemeForm()
    return render(request, "theme/theme_new.html", {"form": form})


@login_required
@user_passes_test(lambda user: user.is_superuser)
def theme_edit(request, id):
    theme = get_object_or_404(Theme, pk=id)
    if request.method == "POST":
        form = ThemeForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            illustration = request.FILES.get("illustration")
            theme = form.save(commit=False)
            theme.illustration = illustration
            theme.save()
            return redirect(reverse("theme", args=[theme.id]))
    else:
        form = ThemeForm(instance=theme)
    return render(request, "theme/theme_edit.html", {"form": form})
