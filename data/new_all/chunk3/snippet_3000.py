# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55213354/pystray-with-tkinter-typeerror-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pystray import MenuItem as item
    _l_(548093)

except ImportError:
    pass
try:
    import pystray
    _l_(548095)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(548097)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(548099)

except ImportError:
    pass

window = _c_(548102, _a_(548101, _n_(548100, "tk", lambda: tk), "Tk"))
_l_(548103)
_c_(548106, _a_(548105, _n_(548104, "window", lambda: window), "title"), "Welcome")
_l_(548107)

def quit_window(icon, item):
    _l_(548116)

    _c_(548110, _a_(548109, _n_(548108, "icon", lambda: icon), "stop"))
    _l_(548111)
    _c_(548114, _a_(548113, _n_(548112, "window", lambda: window), "destroy"))
    _l_(548115)

def show_window(icon, item):
    _l_(548127)

    _c_(548119, _a_(548118, _n_(548117, "icon", lambda: icon), "stop"))
    _l_(548120)
    _c_(548125, _a_(548122, _n_(548121, "window", lambda: window), "after"), 0,_a_(548124, _n_(548123, "window", lambda: window), "deiconify"))
    _l_(548126)

def withdraw_window():
    _l_(548153)

    _c_(548130, _a_(548129, _n_(548128, "window", lambda: window), "withdraw"))
    _l_(548131)
    image = _c_(548134, _a_(548133, _n_(548132, "Image", lambda: Image), "open"), "image.ico")
    _l_(548135)
    menu = (_c_(548138, _n_(548136, "item", lambda: item), 'Quit', _n_(548137, "quit_window", lambda: quit_window)), _c_(548141, _n_(548139, "item", lambda: item), 'Show', _n_(548140, "show_window", lambda: show_window)))
    _l_(548142)
    icon = _c_(548147, _a_(548144, _n_(548143, "pystray", lambda: pystray), "Icon"), "name", _n_(548145, "image", lambda: image), "title", _n_(548146, "menu", lambda: menu))
    _l_(548148)
    _c_(548151, _a_(548150, _n_(548149, "icon", lambda: icon), "run"))
    _l_(548152)

_c_(548157, _a_(548155, _n_(548154, "window", lambda: window), "protocol"), 'WM_DELETE_WINDOW', _n_(548156, "withdraw_window", lambda: withdraw_window))
_l_(548158)
_c_(548161, _a_(548160, _n_(548159, "window", lambda: window), "mainloop"))
_l_(548162)