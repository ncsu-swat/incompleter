#Source: https://stackoverflow.com/questions/57053149/typeerror-list-indices-must-be-integers-or-slices-not-str-python
import os
import pandas as pd
import matplotlib.pyplot as plt
new_df=[]
temp_cols=['Hour','Minute','Second','x_second','RTD_sensor']
### Set your path to the folder containing the .csv files
PATH = 'C:\\Users\\UserName\\Documents\\python\\NASA\\FEMTOBearingDataSet\\Training_set\\Bearing1_1\\temp\\' # Use your path

### Fetch all files in path
fileNames = os.listdir(PATH)

### Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

### Loop over all files
for file in fileNames:

    ### Read .csv file and append to list
    df = pd.read_csv(PATH + file, sep=',', header=None, names=temp_cols, index_col = None)
    for column in range(0,len(temp_cols)):
        new_df['Mean'].append(df.iloc[:,column].mean())

new_df.head()