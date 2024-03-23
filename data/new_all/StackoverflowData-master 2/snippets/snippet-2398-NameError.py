#Source: https://stackoverflow.com/questions/46591421/typeerror-str-object-is-not-callable-and-renaming-files
import os 
import re

def rename_file():
    file_list = os.listdir(r"C:\Users\mdvek\Desktop\Pyton Secret Message\prank")
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\mdvek\Desktop\Pyton Secret Message\prank")
    print (saved_path)
    for file_name in file_list:
        file_name = re.sub('[0-9]','', file_name)

    for file_name in file_list:    
        os.rename(file_name, re.sub('[0-9]','', file_name))
        os.chdir(saved_path)

rename_file()