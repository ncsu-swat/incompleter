#Source: https://stackoverflow.com/questions/54496411/python-errortypeerror-findall-missing-1-required-positional-argument-stri
import re
#import csv

text = open(r'C:\Users\Vincent\Documents\python\theSortingHat\100000DirtyNames.txt') #open text file
for line in text: #iterate through every line
    #return list of names in that line
    x = re.findall ('^([a-zA-Z]-?$')
    #if an actual name is found
    if x != 0:
        print(x)