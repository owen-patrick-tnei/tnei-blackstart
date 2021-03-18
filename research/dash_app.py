import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('Berlin_crimes.csv')

colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
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

if __name__ == '__main__':
    app.run_server(debug=True)