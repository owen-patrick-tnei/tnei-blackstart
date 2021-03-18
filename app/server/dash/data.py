import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash import Dash
from dash.dependencies import Input, Output
from flask_login import current_user, login_required
from flask import redirect

ROOT_DIR = os.path.dirname(os.path.abspath("__file__"))
df = pd.read_csv(ROOT_DIR+'/app/data/Berlin_crimes.csv')


def init_data(server):

    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dash/data/',
        # external_stylesheets=[
        #     '/static/dist/css/styles.css',
        # ]
    )
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
            id='Data',
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
        ),

        html.H2(children="X-Axis"),

        dcc.Dropdown(
            id="x-axis",
            options=[
                ({"label": i, "value":i})for i in df.columns
            ],
        ),

        html.H2(children="Y-Axis"),

        dcc.Dropdown(
            id="y-axis",
            options=[
                ({"label": i, "value": i}) for i in df.columns
            ],
        )

    ])

    init_callbacks(dash_app)
    return dash_app.server


def init_callbacks(dash_app):
    @dash_app.callback(
    Output(component_id="Data", component_property="figure"),
    [Input(component_id='x-axis', component_property='value')]
    )
    def update_data(input_value):
        data = generate_data(df,input_value,"Threat"),
        return {"data":data}






def generate_data(df,x,y):
    try:
        data = [go.Scatter(x=df[df["District"] == i][x],
                   y=df[df["District"] == i]["Threat"],
                   mode="markers")
        for i in df.District.unique()]
    except:
        data=[go.Scatter(x=[1,2,3],y=[1,2,3])]
    return data





