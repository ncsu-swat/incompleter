# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55876187/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(458059)

except ImportError:
    pass

window9 = _c_(458062, _a_(458061, _n_(458060, "tk", lambda: tk), "Tk"))
_l_(458063)
msrp = _c_(458066, _a_(458065, _n_(458064, "tk", lambda: tk), "IntVar"))
_l_(458067)
amgpage = _c_(458073, _a_(458072, _c_(458071, _a_(458069, _n_(458068, "tk", lambda: tk), "Label"), _n_(458070, "window9", lambda: window9), text="Mercedes Benz AMG Depreciation Calculator"), "pack"), anchor='center')
_l_(458074)

amgpage = _c_(458078, _a_(458076, _n_(458075, "tk", lambda: tk), "Label"), _n_(458077, "window9", lambda: window9), text="What is the MSPR of the car?: ")
_l_(458079)
_c_(458082, _a_(458081, _n_(458080, "amgpage", lambda: amgpage), "pack"))
_l_(458083)

msrp = _c_(458087, _a_(458085, _n_(458084, "tk", lambda: tk), "Entry"), _n_(458086, "window9", lambda: window9))
_l_(458088)
_c_(458091, _a_(458090, _n_(458089, "msrp", lambda: msrp), "pack"))
_l_(458092)

_c_(458095, _a_(458094, _n_(458093, "msrp", lambda: msrp), "focus_set"))
_l_(458096)

def callback():
    _l_(458101)

    value=_c_(458099, _a_(458098, _n_(458097, "msrp", lambda: msrp), "get"))
    _l_(458100)

b = _c_(458106, _a_(458103, _n_(458102, "tk", lambda: tk), "Button"), _n_(458104, "window9", lambda: window9), text="Save your msrp value", command=_n_(458105, "callback", lambda: callback),fg="red")
_l_(458107)
_c_(458110, _a_(458109, _n_(458108, "b", lambda: b), "pack"))
_l_(458111)
amgpage = _c_(458115, _a_(458113, _n_(458112, "tk", lambda: tk), "Label"), _n_(458114, "window9", lambda: window9), text="What is the age of the car?: ")
_l_(458116)
_c_(458119, _a_(458118, _n_(458117, "amgpage", lambda: amgpage), "pack"))
_l_(458120)

old = _c_(458124, _a_(458122, _n_(458121, "tk", lambda: tk), "Entry"), _n_(458123, "window9", lambda: window9))
_l_(458125)
_c_(458128, _a_(458127, _n_(458126, "old", lambda: old), "pack"))
_l_(458129)
_c_(458132, _a_(458131, _n_(458130, "old", lambda: old), "focus_set"))
_l_(458133)
def callback2():
    _l_(458138)

    age=_c_(458136, _a_(458135, _n_(458134, "old", lambda: old), "get"))
    _l_(458137)

b = _c_(458143, _a_(458140, _n_(458139, "tk", lambda: tk), "Button"), _n_(458141, "window9", lambda: window9), text="Save the age of the car", command=_n_(458142, "callback2", lambda: callback2),fg="blue")
_l_(458144)
_c_(458147, _a_(458146, _n_(458145, "b", lambda: b), "pack"))    
_l_(458148)    
amgpage = _c_(458152, _a_(458150, _n_(458149, "tk", lambda: tk), "Label"), _n_(458151, "window9", lambda: window9), text="")
_l_(458153)
_c_(458156, _a_(458155, _n_(458154, "amgpage", lambda: amgpage), "pack"), anchor='w')
_l_(458157)
def msrpv():
    _l_(458185)

    m = _c_(458159, _n_(458158, "callback", lambda: callback))
    _l_(458160)
    p = _c_(458163, _n_(458161, "int", lambda: int), _n_(458162, "m", lambda: m))
    _l_(458164)
    a = _c_(458166, _n_(458165, "callback2", lambda: callback2))
    _l_(458167)
    n = _c_(458170, _n_(458168, "int", lambda: int), _n_(458169, "a", lambda: a))
    _l_(458171)
    a=_n_(458172, "p", lambda: p)*(1-0.15)**_n_(458173, "n", lambda: n)
    _l_(458174)
    amgpage=_c_(458179, _a_(458176, _n_(458175, "tk", lambda: tk), "Label"), _n_(458177, "window9", lambda: window9),text="$"+_n_(458178, "a", lambda: a))
    _l_(458180)
    _c_(458183, _a_(458182, _n_(458181, "amgpage", lambda: amgpage), "pack"))
    _l_(458184)


amgmsrp = _c_(458190, _a_(458187, _n_(458186, "tk", lambda: tk), "Button"), _n_(458188, "window9", lambda: window9), text="Get the current value of the car.", command=_n_(458189, "msrpv", lambda: msrpv),fg="green")
_l_(458191)
_c_(458194, _a_(458193, _n_(458192, "amgmsrp", lambda: amgmsrp), "pack"))
_l_(458195)


_c_(458198, _a_(458197, _n_(458196, "window9", lambda: window9), "geometry"), "400x400")
_l_(458199)

_c_(458202, _a_(458201, _n_(458200, "window9", lambda: window9), "title"), "Mercedes Benz AMG Depreciation Calculator")
_l_(458203)

_c_(458206, _a_(458205, _n_(458204, "window9", lambda: window9), "mainloop"))
_l_(458207)