print('index.py')
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app, server
# from app import server

import os, sys; sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

# Connect to your app pages
from apps.dash_global import dash_global
from data.load_data import load_data
# from ... import data
print('Setting data_raw')
dash_global['data_raw'] = load_data()

from apps import data_load, data_overview, modeling

sidenav = html.Div([
    html.H1('🚀 Data App', style={"textAlign": "center"}),

    dbc.ButtonGroup(    # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button_group/
        [
            dbc.Button(children=[dbc.NavItem(dbc.NavLink('Data Load', href='/apps/data_load'))]),
            dbc.Button(children=[dbc.NavItem(dbc.NavLink('Data Overview', href='/apps/data_overview'))]),
            dbc.Button(children=[dbc.NavItem(dbc.NavLink('Modeling', href='/apps/modeling'))]),
        ],
        vertical=True,
    )
], className="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark")

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col([
            sidenav
        ], width={'size':3}),
        dbc.Col([
            html.Div(id='page-content', children=[]),
        ], width={'size':9}),
    ]),
    dcc.Store(id='data-raw'),   # https://dash.plotly.com/sharing-data-between-callbacks
    dcc.Store(id='data-filtered')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/data_load':
        return data_load.layout
    if pathname == '/apps/data_overview':
        return data_overview.layout
    if pathname == '/apps/modeling':
        return modeling.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(port=8051, debug=True, host='0.0.0.0')