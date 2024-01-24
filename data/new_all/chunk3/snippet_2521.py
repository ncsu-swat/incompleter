# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73786282/typeerror-in-threading-function-takes-1-argument-but-2-were-given-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyQt5 import QtWidgets
    _l_(562527)

except ImportError:
    pass
try:
    from PyQt5 import QtCore
    _l_(562529)

except ImportError:
    pass
try:
    from PyQt5 import QtGui
    _l_(562531)

except ImportError:
    pass
try:
    from threading import Thread
    _l_(562533)

except ImportError:
    pass
try:
    from pynput.keyboard import Listener
    _l_(562535)

except ImportError:
    pass
try:
    from keyboard import is_pressed as pressed
    _l_(562537)

except ImportError:
    pass
try:
    from keyboard import press
    _l_(562539)

except ImportError:
    pass
try:
    from tkinter.messagebox import showinfo
    _l_(562541)

except ImportError:
    pass
try:
    from tkinter.messagebox import showerror
    _l_(562543)

except ImportError:
    pass
try:
    from tkinter.messagebox import showwarning
    _l_(562545)

except ImportError:
    pass
try:
    from tkinter.messagebox import askyesno
    _l_(562547)

except ImportError:
    pass
try:
    from python_imagesearch.imagesearch import imagesearch as search
    _l_(562549)

except ImportError:
    pass
try:
    from functools import cache
    _l_(562551)

except ImportError:
    pass
try:
    from GUI import *
    _l_(562553)

except ImportError:
    pass
try:
    import time
    _l_(562555)

except ImportError:
    pass
try:
    import os
    _l_(562557)

except ImportError:
    pass
try:
    import sys
    _l_(562559)

except ImportError:
    pass
try:
    import pyautogui as pyg
    _l_(562561)

except ImportError:
    pass
try:
    import playsound
    _l_(562563)

except ImportError:
    pass

class ImageSearch(_a_(562565, _n_(562564, "QtWidgets", lambda: QtWidgets), "QWidget")):
    _l_(562614)

    def thread(function):
        _l_(562579)

        def wrapper(*values, **kwvalues):
            _l_(562576)

            t1 = _c_(562570, _n_(562566, "Thread", lambda: Thread), target=_n_(562567, "function", lambda: function), args=_n_(562568, "values", lambda: values), kwargs=_n_(562569, "kwvalues", lambda: kwvalues))
            _l_(562571)
            _c_(562574, _a_(562573, _n_(562572, "t1", lambda: t1), "start"))
            _l_(562575)
        aux = _n_(562577, "wrapper", lambda: wrapper)
        _l_(562578)
        return aux

    @thread
    def Listen(self):
        _l_(562594)

        with _c_(562583, _n_(562580, "Listener", lambda: Listener), on_press=_a_(562582, _n_(562581, "self", lambda: self), "onpress")) as listener:
            _l_(562593)

            _c_(562587, _n_(562584, "press", lambda: press), _c_(562586, _n_(562585, "chr", lambda: chr), 92))
            _l_(562588)
            _c_(562591, _a_(562590, _n_(562589, "listener", lambda: listener), "join"))
            _l_(562592)


    # It is the function that I am getting the error
    @thread
    def Start(self):
        _l_(562613)

        if _c_(562599, _a_(562598, _a_(562597, _a_(562596, _n_(562595, "self", lambda: self), "ui"), "btnStartSearching"), "text")) == "Search":
            _l_(562612)

            _c_(562604, _a_(562603, _a_(562602, _a_(562601, _n_(562600, "self", lambda: self), "ui"), "btnStartSearching"), "setText"), "Stop")
            _l_(562605)
            _c_(562610, _a_(562609, _a_(562608, _a_(562607, _n_(562606, "self", lambda: self), "ui"), "groupBox"), "setEnabled"), False)
            _l_(562611)