import dash
from dash import html



print('Running Dash!')
app = dash.Dash('app')

app.layout = html.Div([
    html.P("Template Dash App!")
])

if __name__ == '__main__':
    app.run_server(port=8501, debug=True, host='0.0.0.0')