# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51086074/typeerror-object-takes-no-parameters-trex-dino-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(700968)

except ImportError:
    pass
try:
    from PIL import ImageGrab
    _l_(700970)

except ImportError:
    pass
try:
    import pyautogui
    _l_(700972)

except ImportError:
    pass

class Cordinates():
    _l_(700975)

    replayBtn = (340,420)
    _l_(700973)
    dinosaur = (422,170)
    _l_(700974)

def restartGame():
    _l_(700982)

    _c_(700980, _a_(700977, _n_(700976, "pyautogui", lambda: pyautogui), "click"), _a_(700979, _n_(700978, "Cordinates", lambda: Cordinates), "replayBtn"))
    _l_(700981)

def pressSapce():
    _l_(700994)

    _c_(700985, _a_(700984, _n_(700983, "pyautogui", lambda: pyautogui), "keyDown"), 'space')
    _l_(700986)
    _c_(700989, _a_(700988, _n_(700987, "time", lambda: time), "sleep"), 0.05)
    _l_(700990)
    _c_(700992, _n_(700991, "print", lambda: print), "Jump")
    _l_(700993)
_c_(700997, _a_(700996, _n_(700995, "pyautogui", lambda: pyautogui), "KeyUp"), 'space')
_l_(700998)

_c_(701000, _n_(700999, "restartGame", lambda: restartGame))
_l_(701001)
_c_(701004, _a_(701003, _n_(701002, "time", lambda: time), "sleep"), 1)
_l_(701005)
_c_(701007, _n_(701006, "pressSapce", lambda: pressSapce))
_l_(701008)