import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [10, 15, 7, 12]
})

# Create a sample figure
fig = px.bar(df, x="Category", y="Value", title="Sample Bar Chart")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Sample Dashboard'),

    html.Div(children='''
        A simple dashboard created with Dash.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)