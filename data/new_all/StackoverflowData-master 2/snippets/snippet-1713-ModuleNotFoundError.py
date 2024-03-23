#Source: https://stackoverflow.com/questions/61016046/pil-and-tkinter-error-typeerror-expected-str-bytes-or-os-pathlike-object-not
import tkinter as tk
from tkinter import *
import random
from PIL import Image
window=Tk()
window.geometry('500x550')
window.resizable(False, False)
f=tk.Frame()
f.config(bg='blue', height='500', width='500')
f.pack()
cat=tk.Button(window, text='Cat')
cat.config()
cat.pack(fill=X)
dog=tk.Button(window, text='Dog')
dog.config()
dog.pack(fill=X)
images=['cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'cube1.jpg', 'cube2.jpg', 'cube3.jpg']
imgimport = open(random.sample(images, 1))
img = PIL.Image.open(imgimport)
img.show()