import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as opy
import plotly.io as pio
import pandas as pd
import os
from django.conf import settings
from django.utils.text import slugify

media_root = settings.MEDIA_ROOT


def line(x_values_list, y_values_list, titre, x_titre, y_titre, noms_courbes, action):
    data = []
    for x_values, y_values, nom_courbe in zip(
        x_values_list, y_values_list, noms_courbes
    ):
        df = pd.DataFrame(dict(x=x_values, y=y_values))
        trace = go.Scatter(x=df["x"], y=df["y"], mode="lines", name=nom_courbe)
        data.append(trace)

    layout = go.Layout(
        title=titre, xaxis=dict(title=x_titre), yaxis=dict(title=y_titre)
    )
    fig = go.Figure(data=data, layout=layout)

    if action == "preview":
        graph_html = opy.plot(fig, auto_open=False, output_type="div")

        return graph_html

    elif action == "save":
        filename = f"{slugify(titre)}.svg"
        file_path = os.path.join(media_root, "graphique", filename)

        pio.write_image(fig, file_path, format="svg")

        return "graphique/" + filename


def pie(values, names, titre, action):
    df = pd.DataFrame(dict(value=values, name=names))
    fig = px.pie(df, values="value", names="name")

    if action == "preview":
        graph_html = opy.plot(fig, auto_open=False, output_type="div")

        return graph_html

    elif action == "save":
        filename = f"{slugify(titre)}.svg"
        file_path = os.path.join(media_root, "graphique", filename)

        pio.write_image(fig, file_path, format="svg")

        return "graphique/" + filename


def scatter(x_values_list, y_values_list, titre, x_titre, y_titre, nom_points, action):
    fig = go.Figure()

    for x_values, y_values, nom_point in zip(x_values_list, y_values_list, nom_points):
        scatter_trace = go.Scatter(
            x=x_values, y=y_values, mode="markers", name=nom_point
        )
        fig.add_trace(scatter_trace)

    fig.update_layout(title=titre, xaxis_title=x_titre, yaxis_title=y_titre)

    if action == "preview":
        graph_html = opy.plot(fig, auto_open=False, output_type="div")

        return graph_html

    elif action == "save":
        filename = f"{slugify(titre)}.svg"
        file_path = os.path.join(media_root, "graphique", filename)

        pio.write_image(fig, file_path, format="svg")

        return "graphique/" + filename


def bar(valeurs, titres, noms, titre, x_titre, y_titre, action):
    df = pd.DataFrame(valeurs, columns=noms, index=titres)
    print(y_titre)

    fig = px.bar(
        df, x=titres, y=noms, title=titre, labels={"x": x_titre, "value": y_titre}
    )

    if action == "preview":
        graph_html = opy.plot(fig, auto_open=False, output_type="div")

        return graph_html

    elif action == "save":
        filename = f"{slugify(titre)}.svg"
        file_path = os.path.join(media_root, "graphique", filename)

        pio.write_image(fig, file_path, format="svg")

        return "graphique/" + filename
