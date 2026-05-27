import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the data you already processed
df = pd.read_csv('processed_sales.csv')

# Ensure date column is datetime and sort
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create the line chart
fig = px.line(
    df,
    x='date',
    y='sales',
    title='Pink Morsels Sales Trend',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'},
    markers=True
)

# Add vertical line for price increase (15th Jan 2021)
fig.add_vline(
    x=pd.to_datetime('2021-01-15'),
    line_width=2,
    line_dash="dash",
    line_color="red",
    annotation_text="Price increase",
    annotation_position="top right"
)

# Optional: add shaded regions for before/after
fig.add_vrect(
    x0=df['date'].min(),
    x1=pd.to_datetime('2021-01-15'),
    fillcolor="lightblue",
    opacity=0.2,
    layer="below",
    line_width=0
)
fig.add_vrect(
    x0=pd.to_datetime('2021-01-15'),
    x1=df['date'].max(),
    fillcolor="lightgreen",
    opacity=0.2,
    layer="below",
    line_width=0
)

# Initialise the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsels Sales Visualiser",
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}
    ),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
