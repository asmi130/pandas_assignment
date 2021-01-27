import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import pandas as pd


download_url =("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")
df = pd.read_csv(download_url)
df2 = (df.head())
rank = df["Rank"]
#print(rank)

College_jobs = df2["College_jobs"]
Non_college_jobs = df2["Non_college_jobs"]
Full_time = df2["Full_time"]
Part_time = df2["Part_time"]
Unemployment_rate = df2["Unemployment_rate"]


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        df.plot(x="Rank", y=["Full_time", "Part_time", "Unemployment_rate"], kind="line", ax=sc.axes) 
        
        self.setCentralWidget(sc)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()


