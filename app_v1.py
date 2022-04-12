import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input
import pandas as pd


poverty_data = pd.read_csv('data/PovStatsData.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([        
    html.H1('Banco de Dados de Pobreza e Patrimônio',
            style={'color':'blue',
                    'fontSize':'40px'}),
    html.H2('O Banco Mundial'),
    dcc.Dropdown(id='country',
                    options=[{'label': country, 'value': country}
                            for country in poverty_data['Country Name'].unique()]),
    html.Br(),
    html.Div(id='report'),                        
    dbc.Tabs([
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Número de economisa: 170'),
                html.Li('Cobertura Temporal: 1974 - 2019'),
                html.Li('Frequência de atualização: Trimestral'),
                html.Li('Última atualização: 18 de março de 2020'),
                html.Li([
                    'Fonte: ',
                    html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                        href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                ])             
            ])
        ], label='Principais fatos'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Título do livro: Painéis interativos e aplicativos de dados com plotagem e traço'),
                html.Li(['Github repositório: ',
                        html.A('https://github.com/LeandroHerdy/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                            href='https://github.com/LeandroHerdy/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')
                        ])
            ])                       
        ], label='Informações do Projeto')
    ]),   
])

@app.callback(Output('report', 'children'),
                Input('country', 'value'))
def display_country_report(country):
    if country is None:
        return ""
    filtered_df  = poverty_data[(poverty_data['Country Name']==country) & 
                    (poverty_data['Indicator Name']=='Population, total')]
    Population = filtered_df.loc[:, '2010'].values[0]
    return [html.H3(country), f' A população do {country} em 2010 tinha {Population:,.0f}.'.replace(",", ".")]                


if __name__ =='__main__':
    app.run_server(debug=True, port=1234)