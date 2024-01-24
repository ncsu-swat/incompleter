#Source: https://stackoverflow.com/questions/67622575/typeerror-unsupported-operand-types-for-str-and-float-problem
# All constant value in the code:
G0 = 0.0000775  # Conductance quantum
v = 0.1           # Bias voltage
Time_of_Loops = 1399951  # Time collected by LabVIEW， unit is ms



# read data:
data = pd.read_csv(\
    'C:\\Users\\fq20881\\OneDrive - University of Bristol\\OneDrive\\Data Analysis\\Data.txt', \
    sep=',', names=['Current', 'Position', 'Current2', 'Time2', 'PZT Voltage'])


data.drop([0, 1], axis=0, inplace=True)
data.reset_index(drop=True, inplace=True)
nrows1 = data.shape[0]
print('row number of Current:')
print(nrows1)

data1 = pd.DataFrame(columns=['Time', 'Conductance'], index=range(0, nrows1))
Speed_Time = Time_of_Loops / (nrows1 * 1000)
data1['Time'] = data1.index * Speed_Time
print(data1)
data1['Conductance'] = data['Current'] / (G0 * v)
print(data1)