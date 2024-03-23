#Source: https://stackoverflow.com/questions/64342737/attributeerror-str-object-has-no-attribute-tk-in-tkinter-label
from bs4 import BeautifulSoup
import urllib.request
from tkinter import *

root = Tk()
print("Retrieving Source....")
site_data = urllib.request.urlopen("https://covidindia.org")
site_html = BeautifulSoup(site_data , 'html.parser')

data = site_html.find_all(style = "text-align: center;")
data2= site_html.find_all("h1")

# GUI Version

updated_as = Label("Updated As:-", data[0].get_text()[1:-1])
Total_Cases = Label(data2[1].get_text())
Active_Cases = Label("Active Cases:", data[2].get_text(), "("+data[3].get_text()+")")
Recov_Cases = Label("Recovered Cases:", data[5].get_text(), "("+data[6].get_text()+")")
Deaths = Label("Deaths:", data[8].get_text(), "("+data[9].get_text()+")")
Tests_Done = Label("Tests Done:", data[11].get_text(), "("+data[12].get_text()+")")

# Command Line Version

# print("Updated As:-", data[0].get_text()[1:-1])
# print(".................................................")
# print(data2[1].get_text())
# print("Active Cases:", data[2].get_text(), "("+data[3].get_text()+")")
# print("Recovered Cases:", data[5].get_text(), "("+data[6].get_text()+")")
# print("Deaths:", data[8].get_text(), "("+data[9].get_text()+")")
# print("Tests Done:", data[11].get_text(), "("+data[12].get_text()+")")
# input("Press Enter to Exit!")