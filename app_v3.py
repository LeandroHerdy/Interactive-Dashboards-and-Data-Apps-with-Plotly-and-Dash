import plotly.graph_objects as go
import dash
import dash_html_components as html 
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

poverty_data = pd.read_csv('data/PovStatsData.csv')

regions = ['East Asia & Pacific', 'Europe & CentralAsia',
            'Fragile and conflict affected situations', 'High income',
            'IDA countries classified as fragile situations', 'IDA total',
            'Latin America & Caribbean', 'Low & middle income',
            'Low income', 'Lower middle income', 'Middle East & North Africa',
            'Middle income', 'South Asia', 'Sub-Saharan Africa', 'Upper middle income', 'World']


population_df = poverty_data[~poverty_data['Country Name'].isin(regions) &
                            (poverty_data['Indicator Name']== 'Population, total')]


app.layout = html.Div([
    html.H1('Banco de Dados de Pobreza e Patrimônio'),
    html.H2('O Banco Mundial'),
    dcc.Dropdown(id='country',
                options=[{'label': country, 'value': country}
                            for country in poverty_data['Country Name'].unique()]),
    html.Br(),
    html.Div(id='report'),
    html.Br(),
    dcc.Dropdown(id='year_dropdown',
                value='2010',
                options=[{'label': year, 'value': str(year)}
                        for year in range(1974, 2019)]),
    dcc.Graph(id='population_chart'),

    dbc.Tabs([
        dbc.Tab([
            html.Ul([
                html.Br(),
                 html . Li ( 'Número de economias: 170' ),
                html . Li ( 'Cobertura Temporal: 1974 - 2019' ),
                html . Li ( 'Frequência de atualização: trimestral' ),
                html . Li ( 'Última atualização: 18 de março de 2020' ),
                html.Li([
                    'Source: ',
                       html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                          href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')           
                ])
            ])
        ], label='Principais fatos'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Título do livro: Painéis interativos e aplicativos de dados com Plotly e Dash'),
                html.Li(['Repositório do GitHub: ',
                         html.A('https://github.com/LeandroHerdy/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                                href='https://github.com/LeandroHerdy/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')
                         ])
            ])
        ], label='Informações do Projeto')
    ])                                            
])

@app.callback(Output('report', 'children'),
              Input('country', 'value'))
def display_country_report(country):
    if country is None:
        return ''              
    
    filtered_df = poverty_data[(poverty_data['Country Name']==country) &
                               (poverty_data['Indicator Name']=='Population, total')]
    population = filtered_df.loc[:, '2010'].values[0]

    return [html.H3(country),
            f'The population of {country} in 2010 was {population:,.0f}.']


@app.callback(Output('population_chart', 'figure'),
              Input('year_dropdown', 'value'))
def plot_countries_by_population(year):
    fig = go.Figure()
    year_df = population_df[['Country Name', year]].sort_values(year, ascending=False)[:20]
    fig.add_bar(x=year_df['Country Name'],
                y=year_df[year])
    fig.layout.title = f'Top 20 países por população - {year}'
    return fig


if __name__ =='__main__':
    app.run_server(debug=True)