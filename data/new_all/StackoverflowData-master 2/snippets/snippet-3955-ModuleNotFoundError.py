#Source: https://stackoverflow.com/questions/64946094/typeerror-insert-results-missing-1-required-positional-argument-ergebnisse
import time
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from googlesearch import search

def search_():
    url = "werkzeug.de"
    keywords = ["Tauchsäge", "tauchsäge", "tAuchSäge"]
    ergebnisse = {}
    for e in keywords:
        erg = search(e, num_results=10, lang="de")[1:]
        time.sleep(3)
        for i in erg:
            if url in i:
                ind = erg.index(i)
                ergebnisse[e] = ind
    g.insert_results(ergebnisse)


class GUI():
    def __init__(self):
        self.gui_init()
    def gui_init(self):
        # create tkinter window
        root = tk.Tk()
        # window titel
        root.title("SEO-Ranking Tool")
        # window size and position
        root.geometry("750x600+30+30")
        Label(root, text="URL").grid(row=0, sticky=W,padx=(10, 10))
        Label(root, text="Keywords (Mit komma getrennt)").grid(row=2, sticky=W,padx=(10, 10))
        e1 = Entry(root, width=40)
        e2 = Entry(root, width=40)
        e1.grid(row=1,sticky=W,padx=(10, 10))
        e2.grid(row=3,sticky=W,padx=(10, 10))
        w1 = Button(root, width=34, text="Auswertung", command=search_)
        w1.grid(row=5 ,sticky=W ,padx=(10,10), pady=10)
        excel = 0
        c1 = Checkbutton(root, text="Export to Excel", variable=excel).place(x=300, y=80)
        c2 = Checkbutton(root, text="Blabla", variable=excel).place(x=300, y=50)
        c3 = Checkbutton(root, text="Blabla", variable=excel).place(x=300, y=20)
        self.t1 = Text(root,height=28, width=90)
        self.t1.grid(row=7, padx=(10,10), pady=10)
        root.mainloop()

    def insert_results(self,ergebnisse):
        for i in ergebnisse:
            self.t1.insert(i)
g=GUI()