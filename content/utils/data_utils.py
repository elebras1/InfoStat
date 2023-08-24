from ..models import (
    Secteur,
    Theme,
    Infographie,
    Article,
    Region,
    Infographie_favori,
    Article_favori,
)
import pycountry
from user.models import UserProfile
from django.contrib.auth.models import User
from django.db import IntegrityError
from faker import Faker
from ..utils.graphique_utils import line, bar, pie, scatter
import random


# random.seed(10)
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
        nb_rand = random.randint(1, 4)
        if nb_rand == 1:
            illustration = "secteur/random1.jpeg"
        elif nb_rand == 2:
            illustration = "secteur/random2.jpeg"
        elif nb_rand == 3:
            illustration = "secteur/random3.jpeg"
        elif nb_rand == 4:
            illustration = "secteur/random4.jpeg"

        secteur = Secteur.objects.create(
            nom=fake.word(),
            description=fake.text(max_nb_chars=2500),
            illustration=illustration,
            pub_date=fake.date_time(),
        )
        secteurs.append(secteur)
        secteur.save()


def generate_theme(num):
    for _ in range(num):
        nb_rand = random.randint(1, 4)
        if nb_rand == 1:
            illustration = "theme/random1.jpg"
        elif nb_rand == 2:
            illustration = "theme/random2.jpg"
        elif nb_rand == 3:
            illustration = "theme/random3.jpg"
        elif nb_rand == 4:
            illustration = "theme/random4.jpg"

        theme = Theme.objects.create(
            nom=fake.word(),
            description=fake.text(max_nb_chars=2500),
            illustration=illustration,
            compteur=random.randint(0, 3000),
            pub_date=fake.date_time(),
            secteur=secteurs[random.randint(0, len(secteurs) - 1)],
        )
        themes.append(theme)
        theme.save()


def generate_region():
    countries = pycountry.countries

    for country in countries:
        region = Region.objects.create(nom=country.name)
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
    for i in range(num):
        graph_random = random.randint(0, 3)
        if graph_random == 0:
            graph = generate_line()
        elif graph_random == 1:
            graph = generate_pie()
        elif graph_random == 2:
            graph = generate_scatter()
        elif graph_random == 3:
            graph = generate_bar()

        enquete_year = random.randint(1950, 2023)
        enquete_nb_years = random.randint(0, 8)
        periode_enquete = str(enquete_year) + "-" + str(enquete_year + enquete_nb_years)

        infographie = Infographie.objects.create(
            titre=graph["titre"],
            description=fake.text(max_nb_chars=2500),
            graphique=graph["filename"],
            source="https://www.worldata.fr",
            periode_enquete=periode_enquete,
            compteur=random.randint(0, 3000),
            pub_date=fake.date(),
            theme=themes[random.randint(0, len(themes) - 1)],
            region=regions[random.randint(0, len(regions) - 1)],
            user=superusers[random.randint(0, len(superusers) - 1)],
        )
        infographies.append(infographie)
        infographie.save()
        print(str(i) + " / " + str(num))


def generate_line():
    x_values_list = []
    y_values_list = []
    noms_courbes = []
    titre = fake.sentence()

    rand_val = random.randint(1, 30)
    for nb_courbe in range(random.randint(1, 10)):
        x_values = []
        y_values = []
        noms_courbes.append(fake.word())

        for nb_valeur in range(rand_val):
            if nb_valeur == 0 and nb_courbe == 0:
                x_values.append(random.randint(1, 2000))
            elif nb_courbe == 0 and nb_valeur > 0:
                x_values.append(x_values[nb_valeur - 1] + 1)

            y_values.append(random.randint(1, 300))

        if nb_courbe > 0:
            x_values = x_values_list[0]

        x_values_list.append(x_values)
        y_values_list.append(y_values)

    filename = line(x_values_list, y_values_list, titre, "x", "y", noms_courbes, "save")

    return {"titre": titre, "filename": filename}


def generate_pie():
    values = []
    names = []

    nb_valeur = random.randint(1, 10)
    titre = fake.sentence()

    for i in range(nb_valeur):
        names.append(fake.word())
        values.append(random.randint(1, 200))

    filename = pie(values, names, titre, "save")

    return {"titre": titre, "filename": filename}


def generate_scatter():
    x_values_list = []
    y_values_list = []
    noms_points = []
    titre = fake.sentence()

    rand_val = random.randint(1, 30)
    for nb_point in range(random.randint(1, 10)):
        x_values = []
        y_values = []
        noms_points.append(fake.word())

        for nb_valeur in range(rand_val):
            if nb_valeur == 0 and nb_point == 0:
                x_values.append(random.randint(1, 2000))
            elif nb_point == 0 and nb_valeur > 0:
                x_values.append(x_values[nb_valeur - 1] + 1)

            y_values.append(random.randint(1, 300))

        if nb_point > 0:
            x_values = x_values_list[0]

        x_values_list.append(x_values)
        y_values_list.append(y_values)

    filename = scatter(
        x_values_list, y_values_list, titre, "x", "y", noms_points, "save"
    )

    return {"titre": titre, "filename": filename}


def generate_bar():
    titre = fake.word()
    valeurs_list = []
    titres = []

    rand_val = random.randint(1, 10)
    noms = []
    while len(noms) < rand_val:
        nom = fake.word()
        if nom not in noms:
            noms.append(nom)

    for nb_bar in range(random.randint(1, 10)):
        valeurs = []
        titres.append(fake.word())

        for nb_valeur in range(rand_val):
            valeurs.append(random.randint(0, 50))

        valeurs_list.append(valeurs)

    filename = bar(valeurs_list, titres, noms, titre, "x", "y", "save")

    return {"titre": titre, "filename": filename}


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
