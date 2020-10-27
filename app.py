
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as po
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#-----------------------------------------------------------------------------------------------------------------------
### Data

df_basics = pd.read_csv("",
                        sep = "")





#-----------------------------------------------------------------------------------------------------------------------
### Initialize the dashboard
app = dash.Dash(name = __name__,
                external_stylesheets = ["assets/bootstrap.css"])
server = app.server

#-----------------------------------------------------------------------------------------------------------------------
### Layout
app.layout = html.Div(
    [
        "Dashboard of Imdb Movies"
    ]
)

#-----------------------------------------------------------------------------------------------------------------------
### Run the dashboard

app.run_server(debug = True)
# if __name__ == "__main__":
#     app.run_server(debug = True)




