import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash import Dash


def init_data(server):
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/data/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
        ]
    )
    df = pd.read_csv('Berlin_crimes.csv')
    colors = {
        'background': '#FFFFFF',
        'text': '#111111'
    }
    dash_app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Berlin Crimes',

            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        dcc.Graph(
            id='Local Crimes vs violence',
            figure={
                'data': [
                    go.Scatter(x=df[df["District"]==i]["Local"],
                               y=df[df["District"]==i]["Robbery"],
                               mode="markers")
                    for i in df.District.unique()
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )

    ])
    return dash_app.server