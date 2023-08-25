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
3. Open your browser and and if it's local, use http://127.0.0.1:8000.


## Core Features
<a id="core_features" class="anchor"></a>
- The home page offers different features such as the display of the 5 most popular infographics over 1 year, the 25 most popular themes...
- Daily data offers the latest infographics and article added
- The infographic page allows you to view the chart with various associated information: author, theme and associated sector, title, region, publication date, source, survey period and description.
  The infographic can be downloaded in svg or pdf format and can be added to favorites.
- The article pag allows you to view a article with various associated information: author, source, title, publication date and associated region.
  The article can be downloaded in txt or docx format and can be added to favorites
- An infographic can be created and edited, all information must be filled in and it is possible to choose between 5 graphic curves, sectors, scatter plots, bars.
- An article can be add abd edit.
  



## Management rules
<a id="management_rules" class="anchor"></a>


## Licence

This project is licensed ![Licence MIT](https://img.shields.io/badge/Licence-MIT-blue.svg).

For more details, please see the file [LICENSE](LICENSE.md).

<a id="licence" class="anchor"></a>

