#Source: https://stackoverflow.com/questions/51086074/typeerror-object-takes-no-parameters-trex-dino-bot
import time

from PIL import ImageGrab
import pyautogui

class Cordinates():
    replayBtn = (340,420)
    dinosaur = (422,170)
    #215= xcordinate to check for tree

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSapce():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
pyautogui.KeyUp('space')

restartGame()
time.sleep(1)
pressSapce()