from django.contrib import admin
from .models import Secteur, Theme, Infographie, Article, Region


@admin.register(Secteur)
class SecteurAdmin(admin.ModelAdmin):
    list_display = ("nom", "pub_date")

    search_fields = ["nom", "pub_date"]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("nom", "pub_date")

    search_fields = ["nom", "pub_date"]


@admin.register(Infographie)
class InfographieAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "source",
        "periode_enquete",
        "compteur",
        "pub_date",
        "user",
    )

    list_filter = ["region"]

    search_fields = ["titre", "source", "pub_date"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "source",
        "compteur",
        "pub_date",
        "user",
    )

    search_fields = ["titre", "source", "pub_date"]

    list_filter = ["region"]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass
