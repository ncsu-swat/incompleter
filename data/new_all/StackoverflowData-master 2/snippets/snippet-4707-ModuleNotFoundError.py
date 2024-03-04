#Source: https://stackoverflow.com/questions/51819971/tkinter-attributeerror-nonetype-object-has-no-attribute-insert
from tkinter import * 
import json
import requests 


accessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
query = r'xxxxxxx/?fields=posts.limit(20)'

window = Tk()
window.title('The Sakht Launday')
pagePicture = PhotoImage(file= 'pagePicture.GIF')
Label (window, image = pagePicture).grid(row = 0, column = 0, sticky = 'E')

#Text To Display Inside
listbox = Text(window, width = 50, height = 25, wrap = WORD, background ='White').grid(row = 0, column = 1)

reQ = requests.get('https://graph.facebook.com/v3.1/' + query, {'access_token': accessToken})
tempData = reQ.json()
json.dumps(tempData)
data = tempData['posts']['data']
for results in data:
    caption = results['message']
    timeUploaded = results['created_time']
    urlID = results['id']
    finalPost = 'Caption: {0}\nTime Uploaded: {1}\nURL: {2}\n\n'.format(caption, timeUploaded, urlID)
    listbox.insert(0, finalPost)