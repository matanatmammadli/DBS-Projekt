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


connection = psycopg2.connect(database="DBS_Projekt", user="postgres", password="salvatore1994", host="localhost", port = "1025")

cursor = connection.cursor()
postgreSQL_select_Query = "SELECT * FROM CO2Emission"

cursor.execute(postgreSQL_select_Query)


print("Selecting rows from CO2Emission table using cursor.fetchall")
rows = cursor.fetchall()

print("Print each row and it's columns values")

for r in rows:
    print("Entity = ", r[0])
    print("Code = ", r[1])
    print("Year  = ", r[2])
    print("Annual CO2 Emissions = ", r[3])


cursor.close()

connection.close()
#except (Exception, psycopg2.Error) as error:
#    print(error)

#finally:
    #closing database connection.
#    if connection is not None:
#        cursor.close()
#        connection.close()
print("PostgreSQL connection is closed")
       
df = pd.read_csv("/Users/matanatmammadli/Desktop/DBS Projekt/co2_emission.csv")


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
        x=df["Year"],
        y=df["Annual CO emissions (tonnes )"],
        mode="lines",
        name="coemission"
    ),
    row=3, col=1
)

fig.update_layout(
    height=800,
    showlegend=False,
    title_text="Annual CO2 Emissions",
)

fig.show()