from ..models import (
    Secteur,
    Theme,
    Infographie,
    Article,
    Region,
    Infographie_region,
    Article_region,
)
from faker import Faker
import random


random.seed(10)
fake = Faker()
secteurs = []
themes = []
infographies = []
articles = []
regions = []


def generate_secteurs(num):
    for _ in range(num):
        secteur = Secteur.objects.create(
            nom=fake.word(),
            description=fake.text(max_nb_chars=2500),
            illustration="flag.png",
            pub_date=fake.date_time(),
        )
        secteurs.append(secteur)
        secteur.save()


def generate_theme(num):
    for _ in range(num):
        theme = Theme.objects.create(
            nom=fake.word(),
            description=fake.text(max_nb_chars=2500),
            illustration="flag.png",
            compteur=random.randint(0, 3000),
            pub_date=fake.date_time(),
            secteur=secteurs[random.randint(0, len(secteurs) - 1)],
        )
        themes.append(theme)
        theme.save()


def generate_infographie(num):
    for _ in range(num):
        infographie = Infographie.objects.create(
            titre=fake.sentence(),
            description=fake.text(max_nb_chars=2500),
            graphique="default_graphique.svg",
            source="https://www.cairn.fr",
            periode_enquete="2018 - 2022",
            compteur=random.randint(0, 3000),
            pub_date=fake.date(),
            theme=themes[random.randint(0, len(themes) - 1)],
        )
        infographies.append(infographie)
        infographie.save()


def generate_article(num):
    for _ in range(num):
        article = Article.objects.create(
            titre=fake.sentence(),
            description=fake.text(max_nb_chars=14000),
            source="https://www.cairn.fr",
            compteur=random.randint(0, 3000),
            pub_date=fake.date(),
            theme=themes[random.randint(0, len(themes) - 1)],
        )
        articles.append(article)
        article.save()


def generate_region(num):
    for _ in range(num):
        region = Region.objects.create(nom=fake.word())
        regions.append(region)
        region.save()


def generate_link():
    for ifg in infographies:
        infographie_region = Infographie_region.objects.create(
            infographie=ifg, region=regions[random.randint(0, len(regions) - 1)]
        )
        infographie_region.save()

    for article in articles:
        article_region = Article_region.objects.create(
            article=article, region=regions[random.randint(0, len(regions) - 1)]
        )
        article_region.save()
