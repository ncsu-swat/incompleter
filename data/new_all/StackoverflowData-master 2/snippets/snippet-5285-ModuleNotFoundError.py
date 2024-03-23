#Source: https://stackoverflow.com/questions/73452408/how-to-fix-my-attributeerror-in-python-tkinter
import http.client as client
from tkinter import *
import json

root = Tk()
root.geometry('500x500')

conn = client.HTTPSConnection("realstonks.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "[CLASSIFIED]",
    'X-RapidAPI-Host': "realstonks.p.rapidapi.com"
}
root.destroy()
root = Tk()
root.geometry('500x500')
inputbox = Text(root, padx = 40, pady = 30).pack()
name = ""

def layout(data_obj):
  vol = data_obj['total_vol']
  price = data_obj['price']
  percent = data_obj['change_percentage']
  if percent < 0:
      fg = 'red'
  elif percent > 0:
      fg = 'green'
  elif percent == 0:
      fg = 'gray'
  title_widget = Label(root, text = name, font = ("arial bold", 50), underline = True).pack()
  vol_widget = Label(root, text = vol + " in total.", font = ("arial bold", 40)).pack()
  price_widget = Label(root, text = str(price) + " dollars per share.", font = ("arial bold", 30)).pack()
  percent_widget = Label(root, text = str(percent) + "%", font = ("arial bold", 20), fg = fg).pack()

def search_function():
  name = inputbox.get("1.0","end-1c")
  conn.request("GET", "/" + name.upper(), headers=headers)
  res = conn.getresponse()
  data = res.read()
  # print(data)
  data_obj = json.loads(data.decode('utf-8'))
  layout(data_obj)

search = Button(root, text = "Search Info", background = "gray", command = search_function).pack()

root.mainloop()