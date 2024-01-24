# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56368746/typeerror-entry-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
painter = {}
_l_(372047)
title = {}
_l_(372048)
names = []
_l_(372049)
pnttoedit = ''
_l_(372050)
copyat = 1
_l_(372051)

def saveedit():
    _l_(372085)

    w = _c_(372055, _n_(372052, "str", lambda: str), _n_(372053, "title", lambda: title)[_n_(372054, "pnttoedit", lambda: pnttoedit)]) + " (" + _c_(372058, _n_(372056, "str", lambda: str), _n_(372057, "copyat", lambda: copyat)) + ")"
    _l_(372059)
    _c_(372063, _a_(372061, _n_(372060, "names", lambda: names), "append"), _n_(372062, "w", lambda: w))
    _l_(372064)
    v = _n_(372065, "painter", lambda: painter)[_n_(372066, "pnttoedit", lambda: pnttoedit)]
    _l_(372067)
    _n_(372068, "painter", lambda: painter)[_n_(372069, "w", lambda: w)] = _n_(372070, "v", lambda: v)
    _l_(372071)
    _c_(372077, _a_(372073, _n_(372072, "messagebox", lambda: messagebox), "showinfo"), "Painter's Inventory", "Copy of " + _c_(372076, _n_(372074, "str", lambda: str), _n_(372075, "pnttoedit", lambda: pnttoedit)) + " created.")
    _l_(372078)
    _c_(372083, _n_(372079, "print", lambda: print), _c_(372082, _n_(372080, "str", lambda: str), _n_(372081, "pnttoedit", lambda: pnttoedit)))
    _l_(372084)

def grabpaintingname():
    _l_(372094)

    global pnttoedit
    _l_(372086)
    pnttoedit = _c_(372089, _a_(372088, _n_(372087, "tvkare", lambda: tvkare), "get"))
    _l_(372090)
    _c_(372092, _n_(372091, "saveedit", lambda: saveedit))
    _l_(372093)

tvkare = _c_(372097, _n_(372095, "StringVar", lambda: StringVar), _n_(372096, "editers", lambda: editers))
_l_(372098)
_c_(372102, _a_(372100, _n_(372099, "tvkare", lambda: tvkare), "set"), _n_(372101, "names", lambda: names)[0])
_l_(372103)
e2 = _c_(372108, _n_(372104, "OptionMenu", lambda: OptionMenu), _n_(372105, "mainframe", lambda: mainframe), _n_(372106, "tvkare", lambda: tvkare), *_n_(372107, "names", lambda: names))
_l_(372109)
_c_(372112, _a_(372111, _n_(372110, "e2", lambda: e2), "grid"), row=3, column=1)
_l_(372113)
def change_dropdown(*args):
    _l_(372118)

    pnttoedit = _c_(372116, _a_(372115, _n_(372114, "tvkare", lambda: tvkare), "get"))
    _l_(372117)