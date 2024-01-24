# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65215221/attributeerror-str-object-has-no-attribute-set-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(357994)

except ImportError:
    pass
try:
    from tkinter import font as tkFont
    _l_(357996)

except ImportError:
    pass
try:
    from tkinter import StringVar, Entry, Button
    _l_(357998)

except ImportError:
    pass
try:
    from tkinter.ttk import *
    _l_(358000)

except ImportError:
    pass
try:
    import math
    _l_(358002)

except ImportError:
    pass
root = _c_(358005, _a_(358004, _n_(358003, "tk", lambda: tk), "Tk"))
_l_(358006)
_c_(358009, _a_(358008, _n_(358007, "root", lambda: root), "title"), "Simple Calculator")
_l_(358010)
mathValue = ""
_l_(358011)
def pressBtn(number):
    _l_(358022)

    global mathValue
    _l_(358012)
    mathValue+=_c_(358015, _n_(358013, "str", lambda: str), _n_(358014, "number", lambda: number))
    _l_(358016)
    _c_(358020, _a_(358018, _n_(358017, "mathValue", lambda: mathValue), "set"), _n_(358019, "mathValue", lambda: mathValue))
    _l_(358021)
def mainCalc():
    _l_(358067)

    mathValue = _c_(358024, _n_(358023, "StringVar", lambda: StringVar))
    _l_(358025)
    fontBtn = _c_(358028, _a_(358027, _n_(358026, "tkFont", lambda: tkFont), "Font"), family="Helvetica",size=15,weight='bold')
    _l_(358029)
    inputMath = _c_(358033, _n_(358030, "Label", lambda: Label), _n_(358031, "root", lambda: root),textvariable=_n_(358032, "mathValue", lambda: mathValue),relief='sunken')
    _l_(358034)
    _c_(358037, _a_(358036, _n_(358035, "inputMath", lambda: inputMath), "config"), text="Enter Your Calculation...", width=50)
    _l_(358038)
    _c_(358041, _a_(358040, _n_(358039, "inputMath", lambda: inputMath), "grid"), columnspan=4,ipadx=100,ipady=15) 
    _l_(358042) 
    btn1 = _c_(358049, _a_(358044, _n_(358043, "tk", lambda: tk), "Button"), _n_(358045, "root", lambda: root),text='1',height=0,width=5,font=_n_(358046, "fontBtn", lambda: fontBtn),command=lambda:_c_(358048, _n_(358047, "pressBtn", lambda: pressBtn), 1))
    _l_(358050)
    _c_(358053, _a_(358052, _n_(358051, "btn1", lambda: btn1), "grid"), row=1,column=0)
    _l_(358054)
    btn2 = _c_(358061, _a_(358056, _n_(358055, "tk", lambda: tk), "Button"), _n_(358057, "root", lambda: root),text='2',height=0,width=5,font=_n_(358058, "fontBtn", lambda: fontBtn),command=lambda:_c_(358060, _n_(358059, "pressBtn", lambda: pressBtn), 2))
    _l_(358062)
    _c_(358065, _a_(358064, _n_(358063, "btn2", lambda: btn2), "grid"), row=1,column=1)
    _l_(358066)
_c_(358069, _n_(358068, "mainCalc", lambda: mainCalc))
_l_(358070)
_c_(358073, _a_(358072, _n_(358071, "root", lambda: root), "mainloop"))
_l_(358074)