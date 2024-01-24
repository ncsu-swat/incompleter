# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64946094/typeerror-insert-results-missing-1-required-positional-argument-ergebnisse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(633925)

except ImportError:
    pass
try:
    import numpy as np
    _l_(633927)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(633929)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(633931)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(633933)

except ImportError:
    pass
try:
    from googlesearch import search
    _l_(633935)

except ImportError:
    pass

def search_():
    _l_(633968)

    url = "werkzeug.de"
    _l_(633936)
    keywords = ["Tauchsäge", "tauchsäge", "tAuchSäge"]
    _l_(633937)
    ergebnisse = {}
    _l_(633938)
    for e in _n_(633939, "keywords", lambda: keywords):
        _l_(633962)

        erg = _c_(633942, _n_(633940, "search", lambda: search), _n_(633941, "e", lambda: e), num_results=10, lang="de")[1:]
        _l_(633943)
        _c_(633946, _a_(633945, _n_(633944, "time", lambda: time), "sleep"), 3)
        _l_(633947)
        for i in _n_(633948, "erg", lambda: erg):
            _l_(633961)

            if _n_(633949, "url", lambda: url) in _n_(633950, "i", lambda: i):
                _l_(633960)

                ind = _c_(633954, _a_(633952, _n_(633951, "erg", lambda: erg), "index"), _n_(633953, "i", lambda: i))
                _l_(633955)
                _n_(633956, "ergebnisse", lambda: ergebnisse)[_n_(633957, "e", lambda: e)] = _n_(633958, "ind", lambda: ind)
                _l_(633959)
    _c_(633966, _a_(633964, _n_(633963, "g", lambda: g), "insert_results"), _n_(633965, "ergebnisse", lambda: ergebnisse))
    _l_(633967)


class GUI():
    _l_(634074)

    def __init__(self):
        _l_(633973)

        _c_(633971, _a_(633970, _n_(633969, "self", lambda: self), "gui_init"))
        _l_(633972)
    def gui_init(self):
        _l_(634064)

        # create tkinter window
        root = _c_(633976, _a_(633975, _n_(633974, "tk", lambda: tk), "Tk"))
        _l_(633977)
        # window titel
        _c_(633980, _a_(633979, _n_(633978, "root", lambda: root), "title"), "SEO-Ranking Tool")
        _l_(633981)
        # window size and position
        _c_(633984, _a_(633983, _n_(633982, "root", lambda: root), "geometry"), "750x600+30+30")
        _l_(633985)
        _c_(633991, _a_(633989, _c_(633988, _n_(633986, "Label", lambda: Label), _n_(633987, "root", lambda: root), text="URL"), "grid"), row=0, sticky=_n_(633990, "W", lambda: W),padx=(10, 10))
        _l_(633992)
        _c_(633998, _a_(633996, _c_(633995, _n_(633993, "Label", lambda: Label), _n_(633994, "root", lambda: root), text="Keywords (Mit komma getrennt)"), "grid"), row=2, sticky=_n_(633997, "W", lambda: W),padx=(10, 10))
        _l_(633999)
        e1 = _c_(634002, _n_(634000, "Entry", lambda: Entry), _n_(634001, "root", lambda: root), width=40)
        _l_(634003)
        e2 = _c_(634006, _n_(634004, "Entry", lambda: Entry), _n_(634005, "root", lambda: root), width=40)
        _l_(634007)
        _c_(634011, _a_(634009, _n_(634008, "e1", lambda: e1), "grid"), row=1,sticky=_n_(634010, "W", lambda: W),padx=(10, 10))
        _l_(634012)
        _c_(634016, _a_(634014, _n_(634013, "e2", lambda: e2), "grid"), row=3,sticky=_n_(634015, "W", lambda: W),padx=(10, 10))
        _l_(634017)
        w1 = _c_(634021, _n_(634018, "Button", lambda: Button), _n_(634019, "root", lambda: root), width=34, text="Auswertung", command=_n_(634020, "search_", lambda: search_))
        _l_(634022)
        _c_(634026, _a_(634024, _n_(634023, "w1", lambda: w1), "grid"), row=5 ,sticky=_n_(634025, "W", lambda: W) ,padx=(10,10), pady=10)
        _l_(634027)
        excel = 0
        _l_(634028)
        c1 = _c_(634034, _a_(634033, _c_(634032, _n_(634029, "Checkbutton", lambda: Checkbutton), _n_(634030, "root", lambda: root), text="Export to Excel", variable=_n_(634031, "excel", lambda: excel)), "place"), x=300, y=80)
        _l_(634035)
        c2 = _c_(634041, _a_(634040, _c_(634039, _n_(634036, "Checkbutton", lambda: Checkbutton), _n_(634037, "root", lambda: root), text="Blabla", variable=_n_(634038, "excel", lambda: excel)), "place"), x=300, y=50)
        _l_(634042)
        c3 = _c_(634048, _a_(634047, _c_(634046, _n_(634043, "Checkbutton", lambda: Checkbutton), _n_(634044, "root", lambda: root), text="Blabla", variable=_n_(634045, "excel", lambda: excel)), "place"), x=300, y=20)
        _l_(634049)
        _n_(634050, "self", lambda: self).t1 = _c_(634053, _n_(634051, "Text", lambda: Text), _n_(634052, "root", lambda: root),height=28, width=90)
        _l_(634054)
        _c_(634058, _a_(634057, _a_(634056, _n_(634055, "self", lambda: self), "t1"), "grid"), row=7, padx=(10,10), pady=10)
        _l_(634059)
        _c_(634062, _a_(634061, _n_(634060, "root", lambda: root), "mainloop"))
        _l_(634063)

    def insert_results(self,ergebnisse):
        _l_(634073)

        for i in _n_(634065, "ergebnisse", lambda: ergebnisse):
            _l_(634072)

            _c_(634070, _a_(634068, _a_(634067, _n_(634066, "self", lambda: self), "t1"), "insert"), _n_(634069, "i", lambda: i))
            _l_(634071)
g=_c_(634076, _n_(634075, "GUI", lambda: GUI))
_l_(634077)