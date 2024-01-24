# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65054216/exception-has-occurred-typeerror-cannot-unpack-non-iterable-nonetype-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyautogui import *
    _l_(645816)

except ImportError:
    pass
try:
    import pyautogui
    _l_(645818)

except ImportError:
    pass
try:
    import time
    _l_(645820)

except ImportError:
    pass
try:
    import keyboard
    _l_(645822)

except ImportError:
    pass
try:
    import random
    _l_(645824)

except ImportError:
    pass
try:
    import win32api, win32con
    _l_(645826)

except ImportError:
    pass

def click(x,y):
    _l_(645845)

    _c_(645831, _a_(645828, _n_(645827, "win32api", lambda: win32api), "SetCursorPos"), (_n_(645829, "x", lambda: x),_n_(645830, "y", lambda: y)))
    _l_(645832)
    _c_(645837, _a_(645834, _n_(645833, "win32api", lambda: win32api), "mouse_event"), _a_(645836, _n_(645835, "win32con", lambda: win32con), "MOUSEEVENTF_LEFTDOWN"),0,0)
    _l_(645838)
    _c_(645843, _a_(645840, _n_(645839, "win32api", lambda: win32api), "mouse_event"), _a_(645842, _n_(645841, "win32con", lambda: win32con), "MOUSEEVENTF_LEFTUP"),0,0)
    _l_(645844)

eyeloc = 997, 456
_l_(645846)

while _c_(645849, _a_(645848, _n_(645847, "keyboard", lambda: keyboard), "is_pressed"), 'q') == False:
    _l_(645897)

    eyeloc = 997, 456
    _l_(645850)
    if _c_(645853, _a_(645852, _n_(645851, "pyautogui", lambda: pyautogui), "locateOnScreen"), 'pink.png', region=(576, 160, 842, 592), confidence=0.8)  != None:
        _l_(645896)

        eyeloc = _c_(645856, _a_(645855, _n_(645854, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), 'pink.png', region=(576, 160, 842, 592), confidence=0.8)
        _l_(645857)
        _c_(645859, _n_(645858, "print", lambda: print), "pink")
        _l_(645860)
        px, py = _n_(645861, "eyeloc", lambda: eyeloc)  
        _l_(645862)  
        _c_(645867, _a_(645864, _n_(645863, "pyautogui", lambda: pyautogui), "moveTo"), _n_(645865, "px", lambda: px), _n_(645866, "py", lambda: py)+130, 0.2)
        _l_(645868)
        _c_(645871, _a_(645870, _n_(645869, "time", lambda: time), "sleep"), 0.4)
        _l_(645872)
    elif _c_(645875, _a_(645874, _n_(645873, "pyautogui", lambda: pyautogui), "locateOnScreen"), 'gold.png', region=(576, 160, 842, 593), confidence=0.8)  != None:
        _l_(645895)

        eyeloc = _c_(645878, _a_(645877, _n_(645876, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), 'gold.png', region=(576, 160, 842, 592), confidence=0.8)
        _l_(645879)
        _c_(645881, _n_(645880, "print", lambda: print), "gold")
        _l_(645882)
        gx, gy = _n_(645883, "eyeloc", lambda: eyeloc)
        _l_(645884)
        _c_(645889, _a_(645886, _n_(645885, "pyautogui", lambda: pyautogui), "moveTo"), _n_(645887, "gx", lambda: gx), _n_(645888, "gy", lambda: gy)+130, 0.2)
        _l_(645890)
        _c_(645893, _a_(645892, _n_(645891, "time", lambda: time), "sleep"), 0.4)     
        _l_(645894)     