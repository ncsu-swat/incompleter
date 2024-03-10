#Source: https://stackoverflow.com/questions/70967843/how-to-deal-with-typeerror-cannot-concatenate-object-of-type-str
import os
import shutil
import pandas as pd

src_dir_path = r'D:\1. SEC EDGAR年报数据' 
to_dir_path = r'D:\12 年报提取尝试'  
df = pd.read_excel(r'D:\11. 年报提取尝试\CIK代码.xlsx')
ciklist = list(map(str, df['cik_full'].tolist()))
key1 = ciklist 

filelist = os.listdir(src_dir_path)  
for row in df:
    df.append(row)


def printallfiles(dirs, abspath):
    for file in dirs:
        sub_path = os.path.join(abspath, file)  
        if (os.path.isdir(sub_path)): 
            temppath = os.listdir(sub_path)
            printallfiles(temppath, sub_path)  
        else:
            if key1 in file:
                shutil.copy(sub_path, to_dir_path)


printallfiles(filelist, src_dir_path) 