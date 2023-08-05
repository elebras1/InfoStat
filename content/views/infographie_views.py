from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from ..models import Infographie, Article, Infographie_favori
from ..forms.infographie_form import InfographieForm
from ..forms.chart_form import LineFormSet, PieForm
from ..utils.graphique_utils import line, pie


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


def infographie_new(request):
    user = request.user
    graph_html = None

    if request.method == "POST":
        form = InfographieForm(request.POST)
        formset_line = LineFormSet(request.POST, prefix="form")
        form_pie = PieForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data["titre"]
            type_graphique = form.cleaned_data["type_graphique"]
            x_titre = form.cleaned_data["x_titre"]
            y_titre = form.cleaned_data["y_titre"]

            if form_pie.is_valid():
                valeurs_pie = form_pie.cleaned_data["valeurs"]
                noms_pie = form_pie.cleaned_data["noms"]
                valeurs_pie = [float(valeur) for valeur in valeurs_pie.split("/")]
                noms_pie = [nom for nom in noms_pie.split("/")]

            if formset_line.is_valid():
                x_valeurs_list = []
                y_valeurs_list = []
                noms_courbes = []

                for form_data in formset_line.cleaned_data:
                    x_valeurs = form_data.get("x_valeurs")
                    y_valeurs = form_data.get("y_valeurs")
                    noms_courbes.append(form_data.get("titre"))

                    if x_valeurs and y_valeurs:
                        x_valeurs = [float(valeur) for valeur in x_valeurs.split("/")]
                        y_valeurs = [float(valeur) for valeur in y_valeurs.split("/")]
                        x_valeurs_list.append(x_valeurs)
                        y_valeurs_list.append(y_valeurs)

            submit_type = request.POST.get("submit_type")

            if submit_type == "preview":
                if type_graphique == "line":
                    graph_html = line(
                        x_valeurs_list,
                        y_valeurs_list,
                        titre,
                        x_titre,
                        y_titre,
                        noms_courbes,
                    )
                if type_graphique == "pie":
                    graph_html = pie(valeurs_pie, noms_pie)

            elif submit_type == "send":
                infographie = form.save(commit=False)
                infographie.user = user
                infographie.save()
                return redirect(reverse("infographie", args=[infographie.id]))
    else:
        form = InfographieForm()
        formset_line = LineFormSet(prefix="form")
        form_pie = PieForm()

    return render(
        request,
        "infographie_new.html",
        {
            "form": form,
            "graph_html": graph_html,
            "formset_line": formset_line,
            "form_pie": form_pie,
        },
    )
