#Source: https://stackoverflow.com/questions/73786282/typeerror-in-threading-function-takes-1-argument-but-2-were-given-in-python
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from threading import Thread
from pynput.keyboard import Listener
from keyboard import is_pressed as pressed
from keyboard import press
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.messagebox import showwarning
from tkinter.messagebox import askyesno
from python_imagesearch.imagesearch import imagesearch as search
from functools import cache
from GUI import *
import time
import os
import sys
import pyautogui as pyg
import playsound

class ImageSearch(QtWidgets.QWidget):
    def thread(function):
       def wrapper(*values, **kwvalues):
           t1 = Thread(target=function, args=values, kwargs=kwvalues)
           t1.start()
       return wrapper

    @thread
    def Listen(self):
        with Listener(on_press=self.onpress) as listener:
            press(chr(92))
            listener.join()


    # It is the function that I am getting the error
    @thread
    def Start(self):
        if self.ui.btnStartSearching.text() == "Search":
            self.ui.btnStartSearching.setText("Stop")
            self.ui.groupBox.setEnabled(False)