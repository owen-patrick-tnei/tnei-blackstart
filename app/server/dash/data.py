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
df = pd.read_csv(ROOT_DIR + '/app/data/Berlin_crimes.csv')

dfTotals = df.copy()
dfTotals = dfTotals.drop(columns=["Year", "Code", "District", "Location", "Local", "Drugs"])
sumOfLoc = dfTotals.sum(axis=1)
df["Sum"] = sumOfLoc

location = {}
location["Mitte"] = [52.531677, 13.381777]
location["Friedrichshain-Kreuzberg"] = [52.515816, 13.454293]
location["Pankow"] = [52.5929, 13.4317]
location["Charlottenburg-Wilmersdorf"] = [52.5053, 13.2600]
location["Steglitz-Zehlendorf"] = [52.4531, 13.3312]
location["Tempelhof-Schöneberg"] = [52.4695, 13.3856]
location["Neukölln"] = [52.4408, 13.4445]
location["Treptow-Köpenick"] = [52.4204, 13.6200]
location["Marzahn-Hellersdorf"] = [52.5229, 13.5766]
location["Lichtenberg"] = [52.5229, 13.4996]
location["Reinickendorf"] = [52.5790, 13.2805]
location["Spandau"] = [52.5352, 13.2003]



def init_data(server):


    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dash/data/',
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
                    go.Densitymapbox()
                    for i in df.District.unique()
                ],
                # 'layout': {
                #     'plot_bgcolor': colors['background'],
                #     'paper_bgcolor': colors['background'],
                #     'font': {
                #         'color': colors['text']
                #     }
                # }
            }
        ),

        html.H2(id = "axis", children="X-Axis"),

        dcc.Dropdown(
            id="x-axis",
            options=[
                ({"label": i, "value": i}) for i in df.columns
            ],
            value=df.columns[6]

        ),

        html.H2(children="Y-Axis"),

        dcc.Dropdown(
            id="y-axis",
            options=[
                ({"label": i, "value": i}) for i in df.columns],
            value=df.columns[6]
        ),

        dcc.Graph(
            id='MapBox',
            figure=generate_heat_map_figure(2012,"Sum")

        ),

        html.H2(id="data_title", children="Geo Data"),

        dcc.Dropdown(
            id="geo-data",
            options=[
                ({"label": i, "value": i}) for i in df.columns
            ],
            value=df.columns[6]

        ),

        html.H2(children="Year"),

        dcc.Dropdown(
            id="year",
            options=[
                ({"label": i, "value": i}) for i in df["Year"].unique()],
            value="2012"
        ),

    ])


    init_callbacks(dash_app)
    return dash_app.server


def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id="MapBox", component_property="figure"),
        [Input(component_id='geo-data', component_property='value'),
         Input(component_id="year", component_property="value")]
    )
    def update_data(input_value_data,input_value_year):
        return generate_heat_map_figure(input_value_year, input_value_data)

    @dash_app.callback(
        Output(component_id="Data", component_property="figure"),
        [Input(component_id='x-axis', component_property='value'),
         Input(component_id="y-axis", component_property="value")]
    )
    def update_mapBox(input_value_x,input_value_y):
        data = generate_data(df, input_value_x, input_value_y),

        return {
            'data': data[0],
            'layout':
            go.Layout(
                    title='Crimes by type in Berlin')

        }

def generate_data(df, x, y):
    data = []
    index=0
    for i in df.District.unique():
        data.append(go.Scatter(
            x=df[df["District"] == i][x],
            y=df[df["District"] == i][y],
            mode="markers", name=i
           ))
        index += 1
    return data

def generate_heat_map_figure(year,data):
#     #df needs to be the totals of each district for given year
    print("generating")
    dfYear = df.loc[df["Year"] == year]
    # return

    sums = []
    lats =[]
    longs=[]
    for district in dfYear.District.unique():
        dfYD = dfYear.loc[df["District"] == district]
        district_sum = dfYD[data].sum()
        sums.append(district_sum)
        lats.append(location[district][0])
        longs.append(location[district][1])

    figure = go.Figure(
        go.Densitymapbox(lat = lats, lon = longs, z =sums, radius=100))
    figure.update_layout(mapbox_center_lon = 13.381777, mapbox_center_lat = 52.531677)
    figure.update_layout(mapbox_style="open-street-map", uirevision = True	)
    figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # figure.update_geos(scope = "europe" , fitbounds='locations')
    return figure

