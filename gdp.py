import psycopg2
import psycopg2.extras
from configparser import ConfigParser
import pandas as pd
import plotly.express as px 
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import re



       
df = pd.read_csv("/Users/matanatmammadli/Desktop/DBS Projekt/gdp.csv")


fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.05,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]]
)

fig.add_trace(
    go.Scatter(
        x = df["Indicator Name"],
        y=df["1960", "1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984" ,"1985" ,"1986","1987" ,"1988" ,"1989" ,"1990" ,"1991" ,"1992" ,"1993" ,"1994" ,"1995" ,"1996" ,"1997" ,"1998" ,"1999" ,"2000" ,"2001" ,"2002" ,"2003","2004" ,"2005" ,"2006" ,"2007" ,"2008" ,"2009","2010" ,"2011" ,"2012" ,"2013","2014" ,"2015","2016" ,"2017" ,"2018" ,"2019" ,"2020"],
        mode="lines",
        name="gdp"
    ),
    row=3, col=1
)

fig.update_layout(
    height=800,
    showlegend=False,
    title_text="GDP",
)

fig.show()