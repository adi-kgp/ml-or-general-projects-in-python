"""
Build Data Apps in Python with Plotly Dash
"""

# Dataset csv generation
# from sklearn.datasets import fetch_california_housing
# df = fetch_california_housing(as_frame=True).frame
# df.to_csv('housing.csv', index=None)

## Importing libraries
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input

df = pd.read_csv('housing.csv')

app = Dash()

app.layout = [
        html.Div(children='Dashboard'),
        dash_table.DataTable(data=df.to_dict('records'), page_size=20),
        html.Div([
                html.Label('Select Feature:'),
                dcc.Dropdown(
                        id = 'feature-dropdown',
                        options = [{'label': col, 'value': col} for col in df.columns],
                        value = df.columns[0]
                    )
            ]),
        dcc.Graph(id='histogram')
    ]


@app.callback(
        Output('histogram', 'figure'),
        Input('feature-dropdown', 'value')
    )
def update_histogram(selected_feature):
    fig = px.histogram(df, x = selected_feature)
    fig.update_layout(title=f"Histogram of {selected_feature}",
                      xaxis_title=selected_feature, 
                      yaxis_title="Frequency")
    return fig


if __name__ == '__main__':
    app.run(debug=True)
