import dash
import dash_html_components as html
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
        
    html.H1('Banco de Dados de Pobreza e Patrimônio',
            style={'color':'blue',
                    'fontSize':'40px'}),
    html.H2('O Banco Mundial'),
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


if __name__ =='__main__':
    app.run_server(debug=True)