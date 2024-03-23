#Source: https://stackoverflow.com/questions/74285492/pandas-causing-nonetype-error-in-matplotlib-plt-savefig-and-plt-show
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv")

time =  [0,10,20]
vel = [0,1,2]
fig,axes = plt.subplots()
axes.plot(time,vel)
plt.show()
plt.savefig(fname = "pic.png" )