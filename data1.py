import plotly.figure_factory as ff
import pandas as pd
import csv
df = pd.read_csv("C:/Users/gogof/OneDrive/Desktop/coding/hi-main/c108/project/data.csv")
fig = ff.create_distplot([df["Mobile Brand"].tolist()],["mobile brand"],show_hist=False)
fig.show()