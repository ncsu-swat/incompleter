# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73786282/typeerror-in-threading-function-takes-1-argument-but-2-were-given-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5 import QtWidgets
    _l_(538086)

except ImportError:
    pass
try:
    from PyQt5 import QtCore
    _l_(538088)

except ImportError:
    pass
try:
    from PyQt5 import QtGui
    _l_(538090)

except ImportError:
    pass
try:
    from threading import Thread
    _l_(538092)

except ImportError:
    pass
try:
    from pynput.keyboard import Listener
    _l_(538094)

except ImportError:
    pass
try:
    from keyboard import is_pressed as pressed
    _l_(538096)

except ImportError:
    pass
try:
    from keyboard import press
    _l_(538098)

except ImportError:
    pass
try:
    from tkinter.messagebox import showinfo
    _l_(538100)

except ImportError:
    pass
try:
    from tkinter.messagebox import showerror
    _l_(538102)

except ImportError:
    pass
try:
    from tkinter.messagebox import showwarning
    _l_(538104)

except ImportError:
    pass
try:
    from tkinter.messagebox import askyesno
    _l_(538106)

except ImportError:
    pass
try:
    from python_imagesearch.imagesearch import imagesearch as search
    _l_(538108)

except ImportError:
    pass
try:
    from functools import cache
    _l_(538110)

except ImportError:
    pass
try:
    from GUI import *
    _l_(538112)

except ImportError:
    pass
try:
    import time
    _l_(538114)

except ImportError:
    pass
try:
    import os
    _l_(538116)

except ImportError:
    pass
try:
    import sys
    _l_(538118)

except ImportError:
    pass
try:
    import pyautogui as pyg
    _l_(538120)

except ImportError:
    pass
try:
    import playsound
    _l_(538122)

except ImportError:
    pass

class ImageSearch(_a_(538124, _n_(538123, "QtWidgets", lambda: QtWidgets), "QWidget")):
    _l_(538173)

    def thread(function):
        _l_(538138)

        def wrapper(*values, **kwvalues):
            _l_(538135)

            t1 = _c_(538129, _n_(538125, "Thread", lambda: Thread), target=_n_(538126, "function", lambda: function), args=_n_(538127, "values", lambda: values), kwargs=_n_(538128, "kwvalues", lambda: kwvalues))
            _l_(538130)
            _c_(538133, _a_(538132, _n_(538131, "t1", lambda: t1), "start"))
            _l_(538134)
        aux = _n_(538136, "wrapper", lambda: wrapper)
        _l_(538137)
        return aux

    @thread
    def Listen(self):
        _l_(538153)

        with _c_(538142, _n_(538139, "Listener", lambda: Listener), on_press=_a_(538141, _n_(538140, "self", lambda: self), "onpress")) as listener:
            _l_(538152)

            _c_(538146, _n_(538143, "press", lambda: press), _c_(538145, _n_(538144, "chr", lambda: chr), 92))
            _l_(538147)
            _c_(538150, _a_(538149, _n_(538148, "listener", lambda: listener), "join"))
            _l_(538151)


    # It is the function that I am getting the error
    @thread
    def Start(self):
        _l_(538172)

        if _c_(538158, _a_(538157, _a_(538156, _a_(538155, _n_(538154, "self", lambda: self), "ui"), "btnStartSearching"), "text")) == "Search":
            _l_(538171)

            _c_(538163, _a_(538162, _a_(538161, _a_(538160, _n_(538159, "self", lambda: self), "ui"), "btnStartSearching"), "setText"), "Stop")
            _l_(538164)
            _c_(538169, _a_(538168, _a_(538167, _a_(538166, _n_(538165, "self", lambda: self), "ui"), "groupBox"), "setEnabled"), False)
            _l_(538170)