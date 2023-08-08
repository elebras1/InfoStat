import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as opy
import pandas as pd


def line(x_values_list, y_values_list, titre, x_titre, y_titre, noms_courbes):
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

    graph_html = opy.plot(fig, auto_open=False, output_type="div")

    return graph_html


def pie(values, names):
    df = pd.DataFrame(dict(value=values, name=names))
    fig = px.pie(df, values="value", names="name")

    graph_html = opy.plot(fig, auto_open=False, output_type="div")

    return graph_html


def scatter():
    df = px.data.iris()  # iris is a pandas DataFrame
    fig = px.scatter(df, x="sepal_width", y="sepal_length")

    graph_html = opy.plot(fig, auto_open=False, output_type="div")

    return graph_html
