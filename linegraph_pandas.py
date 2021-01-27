import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib

download_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")

df = pd.read_csv(download_url)
#print(df.head())
rank = df["Rank"]
#print(rank)
College_jobs = df["College_jobs"]
#print(College_jobs)
Non_college_jobs = df["Non_college_jobs"]
#print(Non_college_jobs)
Full_time = df["Full_time"]
Part_time = df["Part_time"]
Unemployment_rate = df["Unemployment_rate"]
#print(df.head())

rcParams["figure.figsize"]= 10,10

df.plot(x="Rank", y=["Full_time", "Part_time", "Unemployment_rate"], kind="line")

plt.grid(True, color="k", linestyle=":")

plt.show()
