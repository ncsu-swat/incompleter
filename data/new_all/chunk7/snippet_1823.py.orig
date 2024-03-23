#Source: https://stackoverflow.com/questions/51717503/python3-x-typeerror-expected-str-bytes-or-os-pathlike-object-not-list
import xlwt
import os
import fnmatch

path='Z:\Data\13-output'
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('data')
row = 0


for files in os.walk(path):
     for file in files:
         if fnmatch.fnmatch(file, '*.txt'):
             L = open(os.path.join( file), "r").read()
             sheet.write(row,5,L)
             row += 1

wbk.save('all_values_in_txt.xls')