[![Langage](https://img.shields.io/badge/Langage-Python-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Django-green.svg)](https://www.djangoproject.com/)
[![Langage](https://img.shields.io/badge/Langage-HTML-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Langage](https://img.shields.io/badge/Langage-JavaScript-yellow.svg)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
[![Libraries](https://img.shields.io/badge/Library-Tailwind_CSS-blueviolet.svg)](https://tailwindcss.com/)
[![Libraries](https://img.shields.io/badge/Library-Plotly-0066CC.svg)](https://plotly.com/python/)

# InfoStat
A Django-based Python project that functions as a comprehensive platform for cataloging and generating various types of graphics like Statista.

# Summary

- [Install](#install)
- [Use](#use)
- [Core Features](#core_features)
- [Management rules](#management_rules)
- [Database](#database)
- [Licence](#licence)
## Install
<a id="install" class="anchor"></a>
1. Clone the repository to your local machine.
2. Make sure you have an web development platform installed on your system like Laragon or Wamp.
3. Create an sql database and change the DATABASES in the settings.py to yours.


## Use
<a id="use" class="anchor"></a>
1. Start your sql server and web server django, py manage.py runserver
2. Generate the realitic data with this command, py manage.py generate_data
3. Open your browser and and if it's local, use 127.0.0.1:8000.


## Core Features
<a id="core_features" class="anchor"></a>
- The home page offers different features such as the display of the 5 most popular infographics over 1 year, the 25 most popular themes...
- Daily data offers the latest infographics and article added
- The infographic page allows you to view the chart with various associated information: author, theme and associated sector, title, region, publication date, source, survey period and description.
  The infographic can be downloaded in svg or pdf format and can be added to favorites.
- The article page allows you to view a article with various associated information: author, source, title, publication date and associated region.
  The article can be downloaded in txt or docx format and can be added to favorites
- An infographic can be created and edited, all information must be filled in and it is possible to choose between 5 graphic curves, sectors, scatter plots, bars.
- An article can be add abd edit.
- the sector listing page lists all sectors with their associated themes.
  the sector page display many information : title, description, picture, theme associated, 10 popular/latest infographic and article.
  A sector can be add and edit.
- the theme page display the 6 latest infographic and article, and display theme who shared the same sector.
  A sector can be add and edit.
- the search page allows you to search for an infographic or the title of an article and display it in order of addition or popularity.
  if the user accesses this page using the sector or theme search space, the search will be filtered by sector or theme.
- the profil page display the information of user : pseudo, name, lastname, picture, email, creation date and display all of favorites infographic and article, if the superuser sees all their infographics and      articles added, the user can search by title of all favorites and added infographic and article.
  A user can be add and edit the informations and password.
- the contact page sends the input information to all super users.
- The administrator area allows you to administer the site

## Management rules
<a id="management_rules" class="anchor"></a>
- There are three types of users with an account: the basic user, the superuser, and administrator
- A basic user can consult his profile modify the information and the password, he can add infographic and article as favorite
- A superuser can add sector, theme, infographic, article and can edit them.
- A administrator access administrator area

## Database
<a id="database" class="anchor"></a>
- Secteur(PK:id_secteur, nom, description, illustration, pub_date)
- Theme(PK:id_theme, nom, description, illustration, compteur, pub_date, FK:id_secteur)
 -Region(PK:id_region, nom)
- Infographie(id_infographie, titre, description, graphique, source, periode_enquete, compteur, pub_date, FK:id_theme, FK:id_region, FK:id_user)
- Article(id_article, titre, description, source, compteur, pub_date, FK:id_theme, FK:id_region, FK:id_user)
- Infographie_favori(PK:id_info_fav, FK:id_infographie, FK:id_user)
- Article_favori(PK:id_art_fav, FK:id_article, FK:id_user)
- User(PK:id_user, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
- User_profile(PK:id_user_profile, photo, FK:id_user)

## Licence

This project is licensed ![Licence MIT](https://img.shields.io/badge/Licence-MIT-blue.svg).

For more details, please see the file [LICENSE](LICENSE.md).

<a id="licence" class="anchor"></a>

