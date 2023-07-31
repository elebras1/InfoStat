from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Secteur(models.Model):
    nom = models.CharField(max_length=80)
    description = models.TextField(max_length=3000)
    illustration = models.CharField(max_length=120, null=True)
    pub_date = models.DateField("date de publication", default=date.today)

    def __str__(self):
        return str(self.nom)


class Theme(models.Model):
    secteur = models.ForeignKey(
        Secteur, on_delete=models.CASCADE, related_name="themes"
    )
    nom = models.CharField(max_length=80)
    description = models.CharField(max_length=3000)
    illustration = models.CharField(max_length=120, null=True)
    compteur = models.IntegerField(null=True, default=0)
    pub_date = models.DateField("date de publication", default=date.today)

    def __str__(self):
        return str(self.nom)


class Region(models.Model):
    nom = models.CharField(max_length=80)

    def __str__(self):
        return str(self.nom)


class Infographie(models.Model):
    theme = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="infographies"
    )
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    titre = models.CharField(max_length=80)
    description = models.TextField(max_length=3000)
    graphique = models.CharField(max_length=120)
    source = models.CharField(max_length=120)
    periode_enquete = models.CharField(max_length=12)
    compteur = models.IntegerField(null=True, default=0)
    pub_date = models.DateField("date de publication", default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    @property
    def type(self):
        return "infographie"

    def __str__(self):
        return str(self.titre)


class Article(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="articles")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    titre = models.CharField(max_length=80)
    description = models.TextField(max_length=15000)
    source = models.CharField(max_length=120)
    compteur = models.IntegerField(null=True, default=0)
    pub_date = models.DateField("date de publication", default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    @property
    def type(self):
        return "article"

    def __str__(self):
        return str(self.titre)


class Article_favori(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("article", "user")


class Infographie_favori(models.Model):
    infographie = models.ForeignKey(Infographie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("infographie", "user")
