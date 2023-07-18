from django.db import models


class Secteur(models.Model):
    nom = models.CharField(max_length=80)
    description = models.TextField(max_length=3000)
    illustration = models.CharField(max_length=120, null=True)
    pub_date = models.DateField("date de publication")

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
    pub_date = models.DateField("date de publication")

    def __str__(self):
        return str(self.nom)


class Infographie(models.Model):
    theme = models.ForeignKey(
        Theme, on_delete=models.CASCADE, related_name="infographies"
    )
    titre = models.CharField(max_length=80)
    description = models.TextField(max_length=3000)
    graphique = models.CharField(max_length=120)
    source = models.CharField(max_length=120)
    periode_enquete = models.TextField(max_length=12)
    compteur = models.IntegerField(null=True, default=0)
    pub_date = models.DateField("date de publication")

    @property
    def type(self):
        return "infographie"

    def __str__(self):
        return str(self.titre)


class Article(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="articles")
    titre = models.CharField(max_length=80)
    description = models.TextField(max_length=15000)
    source = models.CharField(max_length=120)
    compteur = models.IntegerField(null=True, default=0)
    pub_date = models.DateField("date de publication")

    @property
    def type(self):
        return "article"

    def __str__(self):
        return str(self.titre)


class Region(models.Model):
    nom = models.CharField(max_length=80)

    def __str__(self):
        return str(self.nom)


class Infographie_region(models.Model):
    infographie = models.ForeignKey(Infographie, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("infographie", "region")


class Article_region(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("article", "region")
