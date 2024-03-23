#Source: https://stackoverflow.com/questions/54199187/error-when-trying-to-send-text-to-application-with-pywinauto-attributeerror
import pywinauto as pwa
from pywinauto import application
from pywinauto import keyboard

app = application.Application()
app = app.Connect(path=r"C:\path\program.exe")                 
win.Part.Click() #not completely sure why i do this
app['Insert password']['Edit'].send('password')