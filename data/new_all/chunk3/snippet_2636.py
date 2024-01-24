# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68196436/attributeerror-event-object-has-no-attribute-x-win-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(558854)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(558856)

except ImportError:
    pass
try:
    import time
    _l_(558858)

except ImportError:
    pass
root = _c_(558860, _n_(558859, "Tk", lambda: Tk))
_l_(558861)
x = 0
_l_(558862)
y = 0
_l_(558863)
def move_window(event):
    _l_(558881)

    # global x, y
    _c_(558867, _n_(558864, "print", lambda: print), _n_(558865, "x", lambda: x), _n_(558866, "y", lambda: y))
    _l_(558868)
    _c_(558879, _a_(558870, _n_(558869, "root", lambda: root), "geometry"), _c_(558878, _a_(558871, '+{0}+{1}', "format"), _a_(558873, _n_(558872, "event", lambda: event), "x_root") - _n_(558874, "x", lambda: x), _a_(558876, _n_(558875, "event", lambda: event), "y_root") - _n_(558877, "y", lambda: y)))
    _l_(558880)

_c_(558884, _a_(558883, _n_(558882, "root", lambda: root), "overrideredirect"), True) # turns off title bar, geometry
_l_(558885) # turns off title bar, geometry
_c_(558888, _a_(558887, _n_(558886, "root", lambda: root), "geometry"), '400x200+200+200') # set new geometry
_l_(558889) # set new geometry

# make a frame for the title bar
title_bar = _c_(558892, _n_(558890, "Frame", lambda: Frame), _n_(558891, "root", lambda: root), bg='white', relief='raised', bd=2)
_l_(558893)

# put a close button on the title bar
close_button = _c_(558898, _n_(558894, "Button", lambda: Button), _n_(558895, "title_bar", lambda: title_bar), text='X', command=_a_(558897, _n_(558896, "root", lambda: root), "destroy"))
_l_(558899)

# a canvas for the main area of the window
window = _c_(558902, _n_(558900, "Canvas", lambda: Canvas), _n_(558901, "root", lambda: root), bg='black')
_l_(558903)

# pack the widgets
_c_(558907, _a_(558905, _n_(558904, "title_bar", lambda: title_bar), "pack"), expand=1, fill=_n_(558906, "X", lambda: X))
_l_(558908)
_c_(558912, _a_(558910, _n_(558909, "close_button", lambda: close_button), "pack"), side=_n_(558911, "RIGHT", lambda: RIGHT))
_l_(558913)
_c_(558917, _a_(558915, _n_(558914, "window", lambda: window), "pack"), expand=1, fill=_n_(558916, "BOTH", lambda: BOTH))
_l_(558918)

# bind title bar motion to the move window function
def setxy(event):
    _l_(558935)

    global x,y
    _l_(558919)
    x=_a_(558921, _n_(558920, "event", lambda: event), "x_root") - _c_(558924, _a_(558923, _n_(558922, "root", lambda: root), "winfo_x"))
    _l_(558925)
    y=_a_(558927, _n_(558926, "event", lambda: event), "y_root") - _c_(558930, _a_(558929, _n_(558928, "root", lambda: root), "winfo_y"))
    _l_(558931)
    aux = _n_(558932, "x", lambda: x),_n_(558933, "y", lambda: y)
    _l_(558934)
    # print(x,y)
    return aux
_c_(558939, _a_(558937, _n_(558936, "title_bar", lambda: title_bar), "bind"), '<1>',_n_(558938, "setxy", lambda: setxy))
_l_(558940)

_c_(558944, _a_(558942, _n_(558941, "title_bar", lambda: title_bar), "bind"), '<B1-Motion>', _n_(558943, "move_window", lambda: move_window))
_l_(558945)

_c_(558948, _a_(558947, _n_(558946, "root", lambda: root), "mainloop"))
_l_(558949)