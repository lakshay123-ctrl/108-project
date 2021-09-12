import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("108data.csv")
fig = ff.create_distplot([df["Rating"].tolist()],["Rating"],show_hist = False)
fig.show()