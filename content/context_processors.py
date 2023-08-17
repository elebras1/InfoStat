from .models import Theme, Infographie, Article
from django.http import Http404


def header_data(request):
    try:
        themes_nav = Theme.objects.order_by("-compteur")[:6]
    except Theme.DoesNotExist:
        raise Http404("Aucun thème n'a été trouvé.")

    try:
        infographies_nav = Infographie.objects.order_by("-pub_date")[:3]
    except Theme.DoesNotExist:
        raise Http404("Aucune infographie n'a été trouvé.")

    try:
        articles_nav = Article.objects.order_by("-pub_date")[:2]
    except Theme.DoesNotExist:
        raise Http404("Aucun article n'a été trouvé.")

    return {
        "themes_nav": themes_nav,
        "infographies_nav": infographies_nav,
        "articles_nav": articles_nav,
    }
