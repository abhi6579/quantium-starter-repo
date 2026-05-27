import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv('processed_sales.csv')

# Create the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select Region:"),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': 20}
        )
    ], style={'textAlign': 'center', 'marginBottom': 30}),
    
    dcc.Graph(id='sales-line-chart')
])

# Callback to update chart based on region selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f'Pink Morsels Sales - {selected_region.title()} Region',
        labels={'date': 'Date', 'sales': 'Sales (USD)'}
    )
    
    fig.add_vline(
        x='2021-01-15',
        line_width=2,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top"
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
