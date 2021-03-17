from dash import Dash
import dash_core_components as dcc
import dash_html_components as html

def init_login(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/login/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
        ]
    )

    # Create Dash Layout
    dash_app.layout = html.H1(
        children='Login Page',
        style={
            'textAlign': 'center',
            'color': "black"
        }
    )

    return dash_app.server