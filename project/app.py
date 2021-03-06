import dash
import dash_bootstrap_components as dbc
from dash import html

# bootstrap theme
external_stylesheets = [dbc.themes.DARKLY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True