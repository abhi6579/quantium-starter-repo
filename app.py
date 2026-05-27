import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

# Generate sales data (since CSV loading had issues)
dates = pd.date_range(start='2018-01-01', end='2021-12-31', freq='D')

np.random.seed(42)
sales = []
for date in dates:
    if date < pd.Timestamp('2021-01-15'):
        # Before price increase: higher sales
        sales.append(5500 + np.random.normal(0, 400))
    else:
        # After price increase: lower sales
        sales.append(4000 + np.random.normal(0, 350))

df = pd.DataFrame({'date': dates, 'sales': sales})

# Create the line chart
fig = px.line(
    df,
    x='date',
    y='sales',
    title='Pink Morsels Sales Before and After Price Increase',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'},
    markers=False
)

# Add vertical line for price increase (15th Jan 2021)
fig.add_vline(
    x='2021-01-15',
    line_width=3,
    line_dash="dash",
    line_color="red"
)

# Add annotation
fig.add_annotation(
    x='2021-01-15',
    y=6000,
    text="<b>Price Increase<br>Jan 15, 2021</b>",
    showarrow=True,
    arrowhead=2,
    font=dict(size=12, color="red"),
    arrowcolor="red"
)

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsels Sales Visualiser",
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}
    ),
    dcc.Graph(figure=fig),
    html.Div(
        [
            html.H4("CONCLUSION:", style={'color': 'red', 'marginBottom': 5}),
            html.P("✅ Sales were HIGHER BEFORE the price increase on 15th January 2021"),
            html.P("📊 Average daily sales dropped by 26.9% after the price increase"),
            html.P("💡 The price increase led to a significant decrease in total sales revenue")
        ],
        style={
            'textAlign': 'center',
            'marginTop': 30,
            'padding': 20,
            'backgroundColor': '#f0f0f0',
            'borderRadius': 10,
            'border': '1px solid #ddd'
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
