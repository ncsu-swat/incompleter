# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51086074/typeerror-object-takes-no-parameters-trex-dino-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(697188)

except ImportError:
    pass
try:
    from PIL import ImageGrab
    _l_(697190)

except ImportError:
    pass
try:
    import pyautogui
    _l_(697192)

except ImportError:
    pass

class Cordinates():
    _l_(697195)

    replayBtn = (340,420)
    _l_(697193)
    dinosaur = (422,170)
    _l_(697194)

def restartGame():
    _l_(697202)

    _c_(697200, _a_(697197, _n_(697196, "pyautogui", lambda: pyautogui), "click"), _a_(697199, _n_(697198, "Cordinates", lambda: Cordinates), "replayBtn"))
    _l_(697201)

def pressSapce():
    _l_(697214)

    _c_(697205, _a_(697204, _n_(697203, "pyautogui", lambda: pyautogui), "keyDown"), 'space')
    _l_(697206)
    _c_(697209, _a_(697208, _n_(697207, "time", lambda: time), "sleep"), 0.05)
    _l_(697210)
    _c_(697212, _n_(697211, "print", lambda: print), "Jump")
    _l_(697213)
_c_(697217, _a_(697216, _n_(697215, "pyautogui", lambda: pyautogui), "KeyUp"), 'space')
_l_(697218)

_c_(697220, _n_(697219, "restartGame", lambda: restartGame))
_l_(697221)
_c_(697224, _a_(697223, _n_(697222, "time", lambda: time), "sleep"), 1)
_l_(697225)
_c_(697227, _n_(697226, "pressSapce", lambda: pressSapce))
_l_(697228)