"""
Candlestick Visualization Dash App
"""

import yfinance as yf
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output, State

app = Dash()

app.layout = html.Div(
    style = {'backgroundColor': '#111111', 'color': '#FFFFFF', 'padding': '20px'},
    children = [
            html.H1("Stock Candlestick Chart Tool", 
                    style={'textAlign':'center',
                           'color': '#FFFFFF'}),
    html.Div([
            html.Label('Enter Stock Ticker Symbol:', 
                       style={'color': '#FFFFFF'}),
            dcc.Input(id='ticker-input', type='text', value='AAPL',
                      style={'backgroundColor': '#333333',
                             'color': '#FFFFFF'})
        ], style={'padding': '10px'}),
    
    html.Div([
            html.Label('Select Start Date', 
                       style={'color': '#FFFFFF'}),
            dcc.DatePickerSingle(id='start-date-picker', 
                                 date='2022-01-01')
        ], style={'padding': '10px'}),
    
    html.Div([
            html.Label('Select End Date', 
                       style={'color': '#FFFFFF'}),
            dcc.DatePickerSingle(id='end-date-picker', 
                                 date='2023-01-01')
        ], style={'padding': '10px'}),
    
    html.Div([
            html.Button('Submit', id='submit-button', 
                        n_clicks=0, 
                        style={'backgroundColor': '#444444',
                               'color': '#FFFFFF'})
        ], style={'padding': '10px', 'textAlign': 'center'}),
    
    html.Div(id='chart-container', style={'visibility': 'hidden'},
             children=[dcc.Graph(id='candlestick-chart', 
                                 style={'backgroundColor': '#111111'})
    ])
])

@app.callback(
    [Output('candlestick-chart', 'figure'),
     Output('chart-container', 'style')],
    [Input('submit-button', 'n_clicks')],
    [State('ticker-input', 'value'),
     State('start-date-picker', 'date'),
     State('end-date-picker', 'date')]
)
def update_chart(n_clicks, ticker, start_date, end_date):
    if n_clicks > 0:
        df = yf.download(ticker, start = start_date,
                         end= end_date)
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                                             open=df['Open'],
                                             close=df['Close'],
                                             high=df['High'],
                                             low=df["Low"])])

        fig.update_layout(
            title=f'CandleStick Chart of {ticker}',
            xaxis_title='Date',
            yaxis_title='Price (USD)',
            xaxis_rangeslider_visible = False,
            template='plotly_dark'
        )
    
        return fig, {'visibility': 'visible'}
    return go.Figure(), {'visibility': 'hidden'}


if __name__=='__main__':
    app.run(debug=True)




