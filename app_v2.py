import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input


app = dash.Dash(__name__)

app.layout = html.Div([    
    dcc.Dropdown(id='color_dropdown',
                    options=[{'label': color, 'value': color}
                          for color in ['azul', 'verde', 'amarelo']]),
    html.Br(),
    html.Div(id='color_output')            
])

@app.callback(Output('color_output', 'children'),
              Input('color_dropdown', 'value'))
def display_selected_color(color):
    if color is None:
        color = 'nothing'
    return 'Você selecionou '+ color    

if __name__ =='__main__':
    app.run_server()