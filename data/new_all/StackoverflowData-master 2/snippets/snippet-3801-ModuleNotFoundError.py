#Source: https://stackoverflow.com/questions/67757892/typeerror-cannot-convert-the-series-to-class-int-in-to-date
import pandas as pd
import glob
from datetime import datetime, timedelta
from pymongo import MongoClient

client = MongoClient()
col = client['right']['abcde']

listFileNames = (glob.glob(r"C:\Users\%username%\Desktop\Book1.csv"))

# print(len(listFileNames))

cols = ["start_time", "end_time", "source_Ip", "source_Mac", "destination_Ip", "destination_Mac"]


def get_merged_data_frame(list_file_names, p_index_col=False, p_header=None, columns=None):
    if columns is None:
        columns = cols
    if len(list_file_names) == 1:
        return pd.read_csv(list_file_names[0], index_col=p_index_col, header=p_header, low_memory=False,
                           names=columns,
                           usecols=[6, 7, 8, 9, 10, 11])
    else:
        df_from_each_file = (pd.read_csv(f, index_col=p_index_col, header=p_header, low_memory=False, names=columns,
                                         usecols=[6, 7, 8, 9, 10, 11])
                             for f in list_file_names)
        concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
        return concatenated_df


def to_date(x):
    return datetime.strftime(datetime.fromtimestamp(int(x)/1000).strftime("%d-%b-%Y"), "%d-%b-%Y")




df = get_merged_data_frame(listFileNames)
print(df)
df['start_data'] = df['start_time'].apply(to_date)
print(to_date(df['start_time']))
print(type(df))
print(df)
data = df.to_dict(orient='records')
print(data)
col.insert_many(data)