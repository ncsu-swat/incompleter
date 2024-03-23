#Source: https://stackoverflow.com/questions/58420941/pandas-typeerror-list-indices-must-be-integers-or-slices-not-dataframe
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from scipy.interpolate import interp1d
import pandas as pd
import glob

user_info=[19,20,21,22,23] #number of charge states analyzed using fit.py 


path = r'C:\Users\my_folder' # use your path
all_files = glob.glob(path + "/*.csv")

data = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    data.append(df)

my_x=data[0].iloc[2:,0] #assuming that all the files have the same list of x for all data(1~200)

my_y=[]
for filenumber in range(len(all_files)):
    my_y.append(data[filenumber].iloc[2:,1:len(user_info)+1])