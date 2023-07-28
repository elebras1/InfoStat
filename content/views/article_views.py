from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models import Article, Infographie, Article_favori
from ..forms.article_form import ArticleForm
import os
from ..utils.file_utils import generate_temporary_txt_file, generate_temporary_docx_file
from django.http import HttpResponse


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    theme = article.theme
    article_selection = Article.objects.filter(theme=theme).order_by("-pub_date")[:4]
    infographie_selection = Infographie.objects.filter(theme=theme).order_by(
        "-pub_date"
    )[:4]
    article.compteur += 1
    article.save()

    user = request.user

    if user.is_authenticated:
        favori = Article_favori.objects.filter(
            user=user,
            article=article,
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
            new_favori = Article_favori.objects.create(
                user=user,
                article=article,
            )
            etat_favori = True
        else:
            Article_favori.objects.filter(
                user=user,
                article=article,
            ).delete()
            etat_favori = False

    # Vérifiez si le formulaire de téléchargement a été soumis
    if request.method == "POST" and "download_format" in request.POST:
        format = request.POST.get("download_format")
        if format == "txt":
            txt_content = (
                article.description
            )  # Mettez le contenu approprié de l'article ici
            filepath = generate_temporary_txt_file(article.titre, txt_content)
            with open(filepath, "r", encoding="utf-8") as file:
                response = HttpResponse(file.read(), content_type="text/plain")
                response[
                    "Content-Disposition"
                ] = f'attachment; filename="{os.path.basename(filepath)}"'
            os.remove(filepath)
            return response

        if format == "docx":
            txt_content = (
                article.description
            )  # Mettez le contenu approprié de l'article ici
            filepath = generate_temporary_docx_file(article.titre, txt_content)
            with open(filepath, "rb") as file:
                response = HttpResponse(file.read(), content_type="text/plain")
                response[
                    "Content-Disposition"
                ] = f'attachment; filename="{os.path.basename(filepath)}"'
            os.remove(filepath)
            return response

    return render(
        request,
        "article.html",
        {
            "article": article,
            "article_selection": article_selection,
            "infographie_selection": infographie_selection,
            "etat_favori": etat_favori,
        },
    )


def article_new(request):
    user = request.user

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article.save()
            return redirect(reverse("article", args=[article.id]))
    else:
        form = ArticleForm()

    return render(request, "article_new.html", {"form": form})


def article_edit(request, id):
    article = get_object_or_404(Article, pk=id)
    user = request.user

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect(reverse("article", args=[article.id]))
    else:
        form = ArticleForm(instance=article)

    return render(request, "article_new.html", {"form": form})
