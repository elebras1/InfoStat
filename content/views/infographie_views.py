from django.shortcuts import render, get_object_or_404, redirect, reverse
from ..models import Infographie, Article, Infographie_favori
from ..forms.infographie_form import InfographieForm, InfographieEditForm
from ..forms.chart_form import (
    LineFormSet,
    ScatterFormSet,
    BarFormSet,
    PieForm,
    BarNomsForm,
)
from ..utils.file_utils import generate_temporary_png_file
from ..utils.graphique_utils import line, pie, scatter, bar
from django.http import HttpResponse
import os


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

    if (
        request.method == "POST"
        and user.is_authenticated
        and request.POST.get("favori") == "favori"
    ):
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

    if request.method == "POST" and "download_format" in request.POST:
        format = request.POST.get("download_format")
        if format == "pdf":
            filepath_pdf = generate_temporary_png_file(
                infographie.graphique, infographie.titre
            )

            with open(filepath_pdf, "rb") as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type="application/pdf")
                response[
                    "Content-Disposition"
                ] = f'attachment; filename="{os.path.basename(filepath_pdf)}"'

            print("téléchargé")
            os.remove(filepath_pdf)

            return response

    return render(
        request,
        "infographie/infographie.html",
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
        form_info = InfographieForm(request.POST)
        formset_line = LineFormSet(request.POST, prefix="form_line")
        formset_scatter = ScatterFormSet(request.POST, prefix="form_scatter")
        formset_bar = BarFormSet(request.POST, prefix="form_bar")
        form_pie = PieForm(request.POST)
        form_barnoms = BarNomsForm(request.POST)

        errors = {"pie": 0, "line": 0, "scatter": 0, "bar": 0}

        if form_info.is_valid():
            titre = form_info.cleaned_data["titre"]
            type_graphique = form_info.cleaned_data["type_graphique"]
            x_titre = form_info.cleaned_data["x_titre"]
            y_titre = form_info.cleaned_data["y_titre"]

            if form_pie.is_valid():
                valeurs_pie = form_pie.cleaned_data["valeurs"]
                noms_pie = form_pie.cleaned_data["noms_pie"]

                validation = validation_digit(valeurs_pie)
                if validation == False:
                    errors["pie"] += 1

                if valeurs_pie is not "" and noms_pie is not "" and errors["pie"] == 0:
                    valeurs_pie = [float(valeur) for valeur in valeurs_pie.split("/")]
                    noms_pie = noms_pie.split("/")
                else:
                    errors["pie"] += 1

                    if len(noms_pie) != len(valeurs_pie):
                        errors["pie"] += 1

            if formset_line.is_valid():
                x_valeurs_line = []
                y_valeurs_line = []
                noms_courbes = []

                for form in formset_line.forms:
                    x_valeurs = form.cleaned_data.get("x_valeurs")
                    y_valeurs = form.cleaned_data.get("y_valeurs")
                    noms_courbes.append(form.cleaned_data.get("titre"))

                    validation = validation_digit(x_valeurs)
                    if validation == False:
                        errors["line"] += 1

                    validation = validation_digit(y_valeurs)
                    if validation == False:
                        errors["line"] += 1

                    if x_valeurs and y_valeurs and errors["line"] == 0:
                        x_valeurs = [float(valeur) for valeur in x_valeurs.split("/")]
                        y_valeurs = [float(valeur) for valeur in y_valeurs.split("/")]
                        x_valeurs_line.append(x_valeurs)
                        y_valeurs_line.append(y_valeurs)

                        if len(x_valeurs) != len(y_valeurs):
                            errors["line"] += 1
            else:
                errors["line"] += 1

            if formset_scatter.is_valid():
                x_valeurs_scatter = []
                y_valeurs_scatter = []
                noms_points = []

                for form in formset_scatter.forms:
                    x_valeurs = form.cleaned_data.get("x_valeurs")
                    y_valeurs = form.cleaned_data.get("y_valeurs")
                    noms_points.append(form.cleaned_data.get("titre"))

                    validation = validation_digit(x_valeurs)

                    if validation == False:
                        errors["scatter"] += 1

                    validation = validation_digit(y_valeurs)
                    if validation == False:
                        errors["scatter"] += 1

                    if x_valeurs and y_valeurs and errors["scatter"] == 0:
                        x_valeurs = [float(valeur) for valeur in x_valeurs.split("/")]
                        y_valeurs = [float(valeur) for valeur in y_valeurs.split("/")]
                        x_valeurs_scatter.append(x_valeurs)
                        y_valeurs_scatter.append(y_valeurs)

                        if len(x_valeurs) != len(y_valeurs):
                            errors["scatter"] += 1
            else:
                errors["scatter"] += 1

            if formset_bar.is_valid() and form_barnoms.is_valid():
                noms_bar = form_barnoms.cleaned_data["noms"]
                valeurs_bar = []
                titres_bar = []

                if len(noms_bar) != 0:
                    noms_bar = noms_bar.split("/")

                else:
                    errors["bar"] += 1

                for form in formset_bar.forms:
                    valeurs = form.cleaned_data.get("valeurs")
                    titre_bar = form.cleaned_data.get("titre")

                    if valeurs:
                        valeurs = [float(valeur) for valeur in valeurs.split("/")]
                        valeurs_bar.append(valeurs)
                        titres_bar.append(titre_bar)

                        if len(valeurs) != len(noms_bar):
                            errors["bar"] += 1
            else:
                errors["bar"] += 1

            submit_type = request.POST.get("submit_type")

            if submit_type == "preview":
                if type_graphique == "line" and errors["line"] == 0:
                    graph_html = line(
                        x_valeurs_line,
                        y_valeurs_line,
                        titre,
                        x_titre,
                        y_titre,
                        noms_courbes,
                        "preview",
                    )
                elif type_graphique == "pie" and errors["pie"] == 0:
                    graph_html = pie(valeurs_pie, noms_pie, titre, "preview")

                elif type_graphique == "scatter" and errors["scatter"] == 0:
                    graph_html = scatter(
                        x_valeurs_scatter,
                        y_valeurs_scatter,
                        titre,
                        x_titre,
                        y_titre,
                        noms_points,
                        "preview",
                    )

                elif type_graphique == "bar" and errors["bar"] == 0:
                    graph_html = bar(
                        valeurs_bar,
                        titres_bar,
                        noms_bar,
                        titre,
                        x_titre,
                        y_titre,
                        "preview",
                    )

                form_info = InfographieForm(request.POST)

            elif submit_type == "send":
                if type_graphique == "line" and errors["line"] == 0:
                    filename = line(
                        x_valeurs_line,
                        y_valeurs_line,
                        titre,
                        x_titre,
                        y_titre,
                        noms_courbes,
                        "save",
                    )
                elif type_graphique == "pie" and errors["pie"] == 0:
                    filename = pie(valeurs_pie, noms_pie, titre, "save")

                elif type_graphique == "scatter" and errors["scatter"] == 0:
                    filename = scatter(
                        x_valeurs_scatter,
                        y_valeurs_scatter,
                        titre,
                        x_titre,
                        y_titre,
                        noms_points,
                        "save",
                    )

                elif type_graphique == "bar" and errors["bar"] == 0:
                    filename = bar(
                        valeurs_bar,
                        titres_bar,
                        noms_bar,
                        titre,
                        x_titre,
                        y_titre,
                        "save",
                    )

                infographie = form_info.save(commit=False)
                infographie.graphique = filename
                infographie.user = user
                infographie.save()
                return redirect(reverse("infographie", args=[infographie.id]))
    else:
        form_info = InfographieForm()
        formset_line = LineFormSet(prefix="form_line")
        formset_scatter = ScatterFormSet(prefix="form_scatter")
        formset_bar = BarFormSet(prefix="form_bar")
        form_pie = PieForm()
        form_barnoms = BarNomsForm()

    return render(
        request,
        "infographie/infographie_new.html",
        {
            "form": form_info,
            "graph_html": graph_html,
            "formset_line": formset_line,
            "form_pie": form_pie,
            "formset_scatter": formset_scatter,
            "formset_bar": formset_bar,
            "form_barnoms": form_barnoms,
        },
    )


def infographie_edit(request, id):
    infographie = get_object_or_404(Infographie, id=id)
    user = request.user
    graph_html = None

    if request.method == "POST":
        form_info = InfographieEditForm(request.POST, instance=infographie)
        formset_line = LineFormSet(request.POST, prefix="form_line")
        formset_scatter = ScatterFormSet(request.POST, prefix="form_scatter")
        formset_bar = BarFormSet(request.POST, prefix="form_bar")
        form_pie = PieForm(request.POST)
        form_barnoms = BarNomsForm(request.POST)

        errors = {"pie": 0, "line": 0, "scatter": 0, "bar": 0}

        if form_info.is_valid():
            titre = form_info.cleaned_data["titre"]
            type_graphique = form_info.cleaned_data["type_graphique"]
            x_titre = form_info.cleaned_data["x_titre"]
            y_titre = form_info.cleaned_data["y_titre"]

            if form_pie.is_valid():
                valeurs_pie = form_pie.cleaned_data["valeurs"]
                noms_pie = form_pie.cleaned_data["noms_pie"]

                validation = validation_digit(valeurs_pie)
                if validation == False:
                    errors["pie"] += 1

                if valeurs_pie is not "" and noms_pie is not "" and errors["pie"] == 0:
                    valeurs_pie = [float(valeur) for valeur in valeurs_pie.split("/")]
                    noms_pie = noms_pie.split("/")
                else:
                    errors["pie"] += 1

                    if len(noms_pie) != len(valeurs_pie):
                        errors["pie"] += 1

            if formset_line.is_valid():
                x_valeurs_line = []
                y_valeurs_line = []
                noms_courbes = []

                for form in formset_line.forms:
                    x_valeurs = form.cleaned_data.get("x_valeurs")
                    y_valeurs = form.cleaned_data.get("y_valeurs")
                    noms_courbes.append(form.cleaned_data.get("titre"))

                    validation = validation_digit(x_valeurs)
                    if validation == False:
                        errors["line"] += 1

                    validation = validation_digit(y_valeurs)
                    if validation == False:
                        errors["line"] += 1

                    if x_valeurs and y_valeurs and errors["line"] == 0:
                        x_valeurs = [float(valeur) for valeur in x_valeurs.split("/")]
                        y_valeurs = [float(valeur) for valeur in y_valeurs.split("/")]
                        x_valeurs_line.append(x_valeurs)
                        y_valeurs_line.append(y_valeurs)

                        if len(x_valeurs) != len(y_valeurs):
                            errors["line"] += 1
            else:
                errors["line"] += 1

            if formset_scatter.is_valid():
                x_valeurs_scatter = []
                y_valeurs_scatter = []
                noms_points = []

                for form in formset_scatter.forms:
                    x_valeurs = form.cleaned_data.get("x_valeurs")
                    y_valeurs = form.cleaned_data.get("y_valeurs")
                    noms_points.append(form.cleaned_data.get("titre"))

                    validation = validation_digit(x_valeurs)

                    if validation == False:
                        errors["scatter"] += 1

                    validation = validation_digit(y_valeurs)
                    if validation == False:
                        errors["scatter"] += 1

                    if x_valeurs and y_valeurs and errors["scatter"] == 0:
                        x_valeurs = [float(valeur) for valeur in x_valeurs.split("/")]
                        y_valeurs = [float(valeur) for valeur in y_valeurs.split("/")]
                        x_valeurs_scatter.append(x_valeurs)
                        y_valeurs_scatter.append(y_valeurs)

                        if len(x_valeurs) != len(y_valeurs):
                            errors["scatter"] += 1
            else:
                errors["scatter"] += 1

            if formset_bar.is_valid() and form_barnoms.is_valid():
                noms_bar = form_barnoms.cleaned_data["noms"]
                valeurs_bar = []
                titres_bar = []

                if len(noms_bar) != 0:
                    noms_bar = noms_bar.split("/")

                else:
                    errors["bar"] += 1

                for form in formset_bar.forms:
                    valeurs = form.cleaned_data.get("valeurs")
                    titre_bar = form.cleaned_data.get("titre")

                    if valeurs:
                        valeurs = [float(valeur) for valeur in valeurs.split("/")]
                        valeurs_bar.append(valeurs)
                        titres_bar.append(titre_bar)

                        if len(valeurs) != len(noms_bar):
                            errors["bar"] += 1
            else:
                errors["bar"] += 1

            submit_type = request.POST.get("submit_type")

            if submit_type == "preview":
                if type_graphique == "line" and errors["line"] == 0:
                    graph_html = line(
                        x_valeurs_line,
                        y_valeurs_line,
                        titre,
                        x_titre,
                        y_titre,
                        noms_courbes,
                        "preview",
                    )
                elif type_graphique == "pie" and errors["pie"] == 0:
                    graph_html = pie(valeurs_pie, noms_pie, titre, "preview")

                elif type_graphique == "scatter" and errors["scatter"] == 0:
                    graph_html = scatter(
                        x_valeurs_scatter,
                        y_valeurs_scatter,
                        titre,
                        x_titre,
                        y_titre,
                        noms_points,
                        "preview",
                    )

                elif type_graphique == "bar" and errors["bar"] == 0:
                    graph_html = bar(
                        valeurs_bar,
                        titres_bar,
                        noms_bar,
                        titre,
                        x_titre,
                        y_titre,
                        "preview",
                    )

                form_info = InfographieEditForm(request.POST)

            elif submit_type == "send":
                filename = None
                if type_graphique == "line" and errors["line"] == 0:
                    filename = line(
                        x_valeurs_line,
                        y_valeurs_line,
                        titre,
                        x_titre,
                        y_titre,
                        noms_courbes,
                        "save",
                    )
                elif type_graphique == "pie" and errors["pie"] == 0:
                    filename = pie(valeurs_pie, noms_pie, titre, "save")

                elif type_graphique == "scatter" and errors["scatter"] == 0:
                    filename = scatter(
                        x_valeurs_scatter,
                        y_valeurs_scatter,
                        titre,
                        x_titre,
                        y_titre,
                        noms_points,
                        "save",
                    )

                elif type_graphique == "bar" and errors["bar"] == 0:
                    filename = bar(
                        valeurs_bar,
                        titres_bar,
                        noms_bar,
                        titre,
                        x_titre,
                        y_titre,
                        "save",
                    )

                infographie = form_info.save(commit=False)
                if filename:
                    infographie.graphique = filename
                infographie.user = user
                infographie.save()
                return redirect(reverse("infographie", args=[infographie.id]))
    else:
        form_info = InfographieEditForm(instance=infographie)
        formset_line = LineFormSet(prefix="form_line")
        formset_scatter = ScatterFormSet(prefix="form_scatter")
        formset_bar = BarFormSet(prefix="form_bar")
        form_pie = PieForm()
        form_barnoms = BarNomsForm()

    return render(
        request,
        "infographie/infographie_edit.html",
        {
            "form": form_info,
            "graph_html": graph_html,
            "formset_line": formset_line,
            "form_pie": form_pie,
            "formset_scatter": formset_scatter,
            "formset_bar": formset_bar,
            "form_barnoms": form_barnoms,
        },
    )


def validation_digit(liste):
    if liste:
        liste = liste.split("/")
        for value in liste:
            if not value.isdigit():
                return False
        return True
    return False
