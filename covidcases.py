import csv 
import plotly.express as px

with open("Copy+of+data+-+data.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="cases",y= "country",color = "date")
    fig.show()