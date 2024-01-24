# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68753814/attributeerror-str-object-has-no-attribute-tk-when-running-tkinter
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from spleeter.separator import Separator
    _l_(462618)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(462620)

except ImportError:
    pass
try:
    from tkinter.ttk import *
    _l_(462622)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(462624)

except ImportError:
    pass

window = _c_(462626, _n_(462625, "Tk", lambda: Tk))
_l_(462627)
screen_width,screen_height = _c_(462630, _a_(462629, _n_(462628, "window", lambda: window), "maxsize"))
_l_(462631)
_c_(462634, _a_(462633, _n_(462632, "window", lambda: window), "title"), "Spleeter GUI Version")
_l_(462635)
w = _c_(462638, _n_(462636, "int", lambda: int), (_n_(462637, "screen_width", lambda: screen_width)-700)/2)
_l_(462639)
h = _c_(462642, _n_(462640, "int", lambda: int), (_n_(462641, "screen_height", lambda: screen_height)-400)/2)
_l_(462643)
_c_(462648, _a_(462645, _n_(462644, "window", lambda: window), "geometry"), f'700x400+{_n_(462646, "w", lambda: w)}+{_n_(462647, "h", lambda: h)}')
_l_(462649)

lbl = _c_(462652, _n_(462650, 'Label', lambda: Label), _n_(462651, 'window', lambda: window), text="File Path:")
_l_(462653)
_c_(462656, _a_(462655, _n_(462654, 'lbl', lambda: lbl), 'grid'), column=0, row=0)
_l_(462657)

txt = _c_(462660, _n_(462658, 'Entry', lambda: Entry), _n_(462659, 'window', lambda: window), width=10)
_l_(462661)
_c_(462664, _a_(462663, _n_(462662, 'txt', lambda: txt), 'grid'), column=1, row=0)
_l_(462665)

lbl2 = _c_(462668, _n_(462666, 'Label', lambda: Label), _n_(462667, 'window', lambda: window), text="Stems:")
_l_(462669)
_c_(462672, _a_(462671, _n_(462670, 'lbl2', lambda: lbl2), 'grid'), column=0, row=1)
_l_(462673)

combo = _c_(462676, _n_(462674, 'Combobox', lambda: Combobox), _n_(462675, 'window', lambda: window))
_l_(462677)
_n_(462678, 'combo', lambda: combo)['values'] = (2,4,5)
_l_(462679)
_c_(462682, _a_(462681, _n_(462680, 'combo', lambda: combo), 'current'), 0)
_l_(462683)
_c_(462686, _a_(462685, _n_(462684, 'combo', lambda: combo), 'grid'), column=1, row=1)
_l_(462687)

def Separation():
    _l_(462709)

    File_name=_c_(462690, _a_(462689, _n_(462688, 'txt', lambda: txt), 'get'));
    _l_(462691)
    stems='spleeter:'+_c_(462694, _a_(462693, _n_(462692, 'combo', lambda: combo), 'get'))+'stems'
    _l_(462695)
    separator = _c_(462698, _n_(462696, 'Separator', lambda: Separator), _n_(462697, 'stems', lambda: stems))
    _l_(462699)
    _c_(462703, _a_(462701, _n_(462700, 'separator', lambda: separator), 'separate_to_file'), _n_(462702, 'File_name', lambda: File_name), 'out')
    _l_(462704)
    _c_(462707, _a_(462706, _n_(462705, 'messagebox', lambda: messagebox), 'showinfo'), "Notification", "Separation Finished!")
    _l_(462708)


def clicked():
    _l_(462713)

    _c_(462711, _n_(462710, 'Separation', lambda: Separation))
    _l_(462712)

btn = _c_(462717, _n_(462714, 'Button', lambda: Button), _n_(462715, 'window', lambda: window), text="Separate", command=_n_(462716, 'clicked', lambda: clicked))
_l_(462718)
_c_(462721, _a_(462720, _n_(462719, 'btn', lambda: btn), 'grid'), column=2, row=0)
_l_(462722)

def main():
    _l_(462727)

    _c_(462725, _a_(462724, _n_(462723, 'window', lambda: window), 'mainloop'))
    _l_(462726)


if _n_(462728, '__name__', lambda: __name__)=='__main__':
    _l_(462732)

    _c_(462730, _n_(462729, 'main', lambda: main))
    _l_(462731)