#Source: https://stackoverflow.com/questions/65054216/exception-has-occurred-typeerror-cannot-unpack-non-iterable-nonetype-object
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

eyeloc = 997, 456

while keyboard.is_pressed('q') == False:
    eyeloc = 997, 456
    if pyautogui.locateOnScreen('pink.png', region=(576, 160, 842, 592), confidence=0.8)  != None:
        eyeloc = pyautogui.locateCenterOnScreen('pink.png', region=(576, 160, 842, 592), confidence=0.8)
        print("pink")
        px, py = eyeloc  
        pyautogui.moveTo(px, py+130, 0.2)
        time.sleep(0.4)
    elif pyautogui.locateOnScreen('gold.png', region=(576, 160, 842, 593), confidence=0.8)  != None:
        eyeloc = pyautogui.locateCenterOnScreen('gold.png', region=(576, 160, 842, 592), confidence=0.8)
        print("gold")
        gx, gy = eyeloc
        pyautogui.moveTo(gx, gy+130, 0.2)
        time.sleep(0.4)     