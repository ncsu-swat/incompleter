# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65215221/attributeerror-str-object-has-no-attribute-set-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(347075)

except ImportError:
    pass
try:
    from tkinter import font as tkFont
    _l_(347077)

except ImportError:
    pass
try:
    from tkinter import StringVar, Entry, Button
    _l_(347079)

except ImportError:
    pass
try:
    from tkinter.ttk import *
    _l_(347081)

except ImportError:
    pass
try:
    import math
    _l_(347083)

except ImportError:
    pass
root = _c_(347086, _a_(347085, _n_(347084, "tk", lambda: tk), "Tk"))
_l_(347087)
_c_(347090, _a_(347089, _n_(347088, "root", lambda: root), "title"), "Simple Calculator")
_l_(347091)
mathValue = ""
_l_(347092)
def pressBtn(number):
    _l_(347103)

    global mathValue
    _l_(347093)
    mathValue+=_c_(347096, _n_(347094, "str", lambda: str), _n_(347095, "number", lambda: number))
    _l_(347097)
    _c_(347101, _a_(347099, _n_(347098, "mathValue", lambda: mathValue), "set"), _n_(347100, "mathValue", lambda: mathValue))
    _l_(347102)
def mainCalc():
    _l_(347148)

    mathValue = _c_(347105, _n_(347104, "StringVar", lambda: StringVar))
    _l_(347106)
    fontBtn = _c_(347109, _a_(347108, _n_(347107, "tkFont", lambda: tkFont), "Font"), family="Helvetica",size=15,weight='bold')
    _l_(347110)
    inputMath = _c_(347114, _n_(347111, "Label", lambda: Label), _n_(347112, "root", lambda: root),textvariable=_n_(347113, "mathValue", lambda: mathValue),relief='sunken')
    _l_(347115)
    _c_(347118, _a_(347117, _n_(347116, "inputMath", lambda: inputMath), "config"), text="Enter Your Calculation...", width=50)
    _l_(347119)
    _c_(347122, _a_(347121, _n_(347120, "inputMath", lambda: inputMath), "grid"), columnspan=4,ipadx=100,ipady=15) 
    _l_(347123) 
    btn1 = _c_(347130, _a_(347125, _n_(347124, "tk", lambda: tk), "Button"), _n_(347126, "root", lambda: root),text='1',height=0,width=5,font=_n_(347127, "fontBtn", lambda: fontBtn),command=lambda:_c_(347129, _n_(347128, "pressBtn", lambda: pressBtn), 1))
    _l_(347131)
    _c_(347134, _a_(347133, _n_(347132, "btn1", lambda: btn1), "grid"), row=1,column=0)
    _l_(347135)
    btn2 = _c_(347142, _a_(347137, _n_(347136, "tk", lambda: tk), "Button"), _n_(347138, "root", lambda: root),text='2',height=0,width=5,font=_n_(347139, "fontBtn", lambda: fontBtn),command=lambda:_c_(347141, _n_(347140, "pressBtn", lambda: pressBtn), 2))
    _l_(347143)
    _c_(347146, _a_(347145, _n_(347144, "btn2", lambda: btn2), "grid"), row=1,column=1)
    _l_(347147)
_c_(347150, _n_(347149, "mainCalc", lambda: mainCalc))
_l_(347151)
_c_(347154, _a_(347153, _n_(347152, "root", lambda: root), "mainloop"))
_l_(347155)