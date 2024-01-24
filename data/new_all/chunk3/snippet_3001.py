# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55213354/pystray-with-tkinter-typeerror-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pystray import MenuItem as item
    _l_(536637)

except ImportError:
    pass
try:
    import pystray
    _l_(536639)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(536641)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(536643)

except ImportError:
    pass
class Program:
    _l_(536723)

    def __init__(self):
        _l_(536666)

        _n_(536644, "self", lambda: self).window = _c_(536647, _a_(536646, _n_(536645, "tk", lambda: tk), "Tk"))
        _l_(536648)
        _c_(536652, _a_(536651, _a_(536650, _n_(536649, "self", lambda: self), "window"), "title"), "Welcome")
        _l_(536653)
        _c_(536659, _a_(536656, _a_(536655, _n_(536654, "self", lambda: self), "window"), "protocol"), 'WM_DELETE_WINDOW', _a_(536658, _n_(536657, "self", lambda: self), "withdraw_window"))
        _l_(536660)
        _c_(536664, _a_(536663, _a_(536662, _n_(536661, "self", lambda: self), "window"), "mainloop"))
        _l_(536665)

    def quit_window(self):
        _l_(536677)

        _c_(536670, _a_(536669, _a_(536668, _n_(536667, "self", lambda: self), "icon"), "stop"))
        _l_(536671)
        _c_(536675, _a_(536674, _a_(536673, _n_(536672, "self", lambda: self), "window"), "destroy"))
        _l_(536676)

    def show_window(self):
        _l_(536691)

        _c_(536681, _a_(536680, _a_(536679, _n_(536678, "self", lambda: self), "icon"), "stop"))
        _l_(536682)
        _c_(536689, _a_(536685, _a_(536684, _n_(536683, "self", lambda: self), "window"), "after"), 0, _a_(536688, _a_(536687, _n_(536686, "self", lambda: self), "window"), "deiconify"))
        _l_(536690)

    def withdraw_window(self):
        _l_(536722)

        _c_(536695, _a_(536694, _a_(536693, _n_(536692, "self", lambda: self), "window"), "withdraw"))
        _l_(536696)
        image = _c_(536699, _a_(536698, _n_(536697, "Image", lambda: Image), "open"), "microphone.ico")
        _l_(536700)
        menu = (_c_(536704, _n_(536701, "item", lambda: item), 'Quit', _a_(536703, _n_(536702, "self", lambda: self), "quit_window")), _c_(536708, _n_(536705, "item", lambda: item), 'Show', _a_(536707, _n_(536706, "self", lambda: self), "show_window")))
        _l_(536709)
        _n_(536710, "self", lambda: self).icon = _c_(536715, _a_(536712, _n_(536711, "pystray", lambda: pystray), "Icon"), "name", _n_(536713, "image", lambda: image), "title", _n_(536714, "menu", lambda: menu))
        _l_(536716)
        _c_(536720, _a_(536719, _a_(536718, _n_(536717, "self", lambda: self), "icon"), "run"))
        _l_(536721)

run=_c_(536725, _n_(536724, "Program", lambda: Program))
_l_(536726)