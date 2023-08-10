from ..models import (
    Secteur,
    Theme,
    Infographie,
    Article,
    Region,
    Infographie_favori,
    Article_favori,
)

from user.models import UserProfile
from django.contrib.auth.models import User

from django.db import IntegrityError


from faker import Faker
import random


random.seed(10)
fake = Faker()
secteurs = []
themes = []
users = []
infographies = []
articles = []
regions = []
superusers = []


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


def generate_region(num):
    for _ in range(num):
        region = Region.objects.create(nom=fake.word())
        regions.append(region)
        region.save()


def generate_user(num):
    for _ in range(num):
        user = User.objects.create_user(
            password="password",
            is_superuser=False,
            username=fake.word(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            is_staff=False,
            is_active=True,
            date_joined=fake.date(),
        )

        user_profile = UserProfile.objects.create(user=user)

        users.append(user)
        user.save()
        user_profile.save()

    for i in range(5):
        # admin
        if i == 0:
            user = User.objects.create_user(
                password="password",
                is_superuser=True,
                username=fake.word(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                is_staff=True,
                is_active=True,
                date_joined=fake.date(),
            )
        # superuser
        else:
            user = User.objects.create_user(
                password="password",
                is_superuser=True,
                username=fake.word(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                is_staff=False,
                is_active=True,
                date_joined=fake.date(),
            )
        user_profile = UserProfile.objects.create(user=user)

        superusers.append(user)

        users.append(user)
        user.save()
        user_profile.save()


def generate_infographie(num):
    for _ in range(num):
        infographie = Infographie.objects.create(
            titre=fake.sentence(),
            description=fake.text(max_nb_chars=2500),
            graphique="graphique/default_graphique.svg",
            source="https://www.cairn.fr",
            periode_enquete="2018 - 2022",
            compteur=random.randint(0, 3000),
            pub_date=fake.date(),
            theme=themes[random.randint(0, len(themes) - 1)],
            region=regions[random.randint(0, len(regions) - 1)],
            user=superusers[random.randint(0, len(superusers) - 1)],
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
            region=regions[random.randint(0, len(regions) - 1)],
            user=superusers[random.randint(0, len(superusers) - 1)],
        )
        articles.append(article)
        article.save()


def generate_favori():
    for ifg in infographies:
        favori_values = random.choices([0, 1], weights=[9, 1], k=random.randint(0, 3))
        for value in favori_values:
            if value == 1:
                try:
                    user_idx = random.randint(0, len(users) - 1)
                    Infographie_favori.objects.get_or_create(
                        infographie=ifg, user=users[user_idx]
                    )
                except IntegrityError:
                    pass

    for article in articles:
        favori_values = random.choices([0, 1], weights=[9, 1], k=random.randint(0, 3))
        for value in favori_values:
            if value == 1:
                try:
                    user_idx = random.randint(0, len(users) - 1)
                    Article_favori.objects.get_or_create(
                        article=article, user=users[user_idx]
                    )
                except IntegrityError:
                    pass
