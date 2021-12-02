from dash import html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("DSCI 591 - Covid-19 Analytics", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This data is sourced from ourworldindata.org under a CC-BY license.'), className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='The analysis is split several categories, US, by continent, and an aggregate by country')
                    , className="mb-5")
        ])])])


# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)
