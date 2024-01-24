# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56368746/typeerror-entry-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
painter = {}
_l_(343695)
title = {}
_l_(343696)
names = []
_l_(343697)
pnttoedit = ''
_l_(343698)
copyat = 1
_l_(343699)

def saveedit():
    _l_(343733)

    w = _c_(343703, _n_(343700, "str", lambda: str), _n_(343701, "title", lambda: title)[_n_(343702, "pnttoedit", lambda: pnttoedit)]) + " (" + _c_(343706, _n_(343704, "str", lambda: str), _n_(343705, "copyat", lambda: copyat)) + ")"
    _l_(343707)
    _c_(343711, _a_(343709, _n_(343708, "names", lambda: names), "append"), _n_(343710, "w", lambda: w))
    _l_(343712)
    v = _n_(343713, "painter", lambda: painter)[_n_(343714, "pnttoedit", lambda: pnttoedit)]
    _l_(343715)
    _n_(343716, "painter", lambda: painter)[_n_(343717, "w", lambda: w)] = _n_(343718, "v", lambda: v)
    _l_(343719)
    _c_(343725, _a_(343721, _n_(343720, "messagebox", lambda: messagebox), "showinfo"), "Painter's Inventory", "Copy of " + _c_(343724, _n_(343722, "str", lambda: str), _n_(343723, "pnttoedit", lambda: pnttoedit)) + " created.")
    _l_(343726)
    _c_(343731, _n_(343727, "print", lambda: print), _c_(343730, _n_(343728, "str", lambda: str), _n_(343729, "pnttoedit", lambda: pnttoedit)))
    _l_(343732)

def grabpaintingname():
    _l_(343742)

    global pnttoedit
    _l_(343734)
    pnttoedit = _c_(343737, _a_(343736, _n_(343735, "tvkare", lambda: tvkare), "get"))
    _l_(343738)
    _c_(343740, _n_(343739, "saveedit", lambda: saveedit))
    _l_(343741)

tvkare = _c_(343745, _n_(343743, "StringVar", lambda: StringVar), _n_(343744, "editers", lambda: editers))
_l_(343746)
_c_(343750, _a_(343748, _n_(343747, "tvkare", lambda: tvkare), "set"), _n_(343749, "names", lambda: names)[0])
_l_(343751)
e2 = _c_(343756, _n_(343752, "OptionMenu", lambda: OptionMenu), _n_(343753, "mainframe", lambda: mainframe), _n_(343754, "tvkare", lambda: tvkare), *_n_(343755, "names", lambda: names))
_l_(343757)
_c_(343760, _a_(343759, _n_(343758, "e2", lambda: e2), "grid"), row=3, column=1)
_l_(343761)
def change_dropdown(*args):
    _l_(343766)

    pnttoedit = _c_(343764, _a_(343763, _n_(343762, "tvkare", lambda: tvkare), "get"))
    _l_(343765)