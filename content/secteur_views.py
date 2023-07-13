from django.shortcuts import render
from django.http import Http404
from .models import Secteur


def secteur(request):
    secteurs = Secteur.objects.order_by("nom")
    return render(request, "secteur.html", {"secteurs": secteurs})
