import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as opy
import pandas as pd


def scatter(x_valeurs, y_valeurs, titre, x_titre, y_titre):
    df = pd.DataFrame(dict(x=x_valeurs, y=y_valeurs))

    fig = px.line(df, x="x", y="y", title=titre, labels={"x": x_titre, "y": y_titre})

    graph_html = opy.plot(fig, auto_open=False, output_type="div")

    return graph_html
