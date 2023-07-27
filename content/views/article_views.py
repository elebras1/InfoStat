from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models import Article, Infographie, Article_favori
from ..forms.article_form import ArticleForm


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

    if request.method == "POST" and user.is_authenticated:
        if not favori:
            new_favori = Article_favori.objects.create(
                user=user,
                article=article,
            )
            etat_favori = True
            print("insert")
        else:
            Article_favori.objects.filter(
                user=user,
                article=article,
            ).delete()
            etat_favori = False
            print("delete")

    print(etat_favori)

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
            article.user = user
            article.save()
            return redirect(reverse("article", args=[article.id]))
    else:
        form = ArticleForm(instance=article)

    return render(request, "article_new.html", {"form": form})
