# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75634197/attributeerror-module-pywebkit-has-no-attribute-webview
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gi, pywebkit, webview
    _l_(583496)

except ImportError:
    pass
_c_(583499, _a_(583498, _n_(583497, "gi", lambda: gi), "require_version"), 'Gtk', '3.0')
_l_(583500)
try:
    from gi.repository import Gtk
    _l_(583502)

except ImportError:
    pass
try:
    from pywebkit import *
    _l_(583504)

except ImportError:
    pass

class Main(_a_(583506, _n_(583505, "Gtk", lambda: Gtk), "Window")):
    _l_(583584)

    
    def __init__(self):
        _l_(583571)

        _c_(583511, _a_(583509, _a_(583508, _n_(583507, "Gtk", lambda: Gtk), "Window"), "__init__"), _n_(583510, "self", lambda: self), title='Browser')
        _l_(583512)

        _c_(583515, _a_(583514, _n_(583513, "self", lambda: self), "set_border_width"), 10)
        _l_(583516)
        _c_(583519, _a_(583518, _n_(583517, "self", lambda: self), "set_size_request"), 200, 100)
        _l_(583520)
        _n_(583521, "self", lambda: self).button = _c_(583524, _a_(583523, _n_(583522, "Gtk", lambda: Gtk), "Button"), label='Go')
        _l_(583525)
        _c_(583531, _a_(583528, _a_(583527, _n_(583526, "self", lambda: self), "button"), "connect"), 'clicked', _a_(583530, _n_(583529, "self", lambda: self), "test"))
        _l_(583532)

        vbox = _c_(583538, _a_(583534, _n_(583533, "Gtk", lambda: Gtk), "Box"), orientation=_a_(583537, _a_(583536, _n_(583535, "Gtk", lambda: Gtk), "Orientation"), "VERTICAL"), spacing=8)
        _l_(583539)
        _c_(583543, _a_(583541, _n_(583540, "self", lambda: self), "add"), _n_(583542, "vbox", lambda: vbox))
        _l_(583544)
        _n_(583545, "self", lambda: self).user_input = _c_(583548, _a_(583547, _n_(583546, "Gtk", lambda: Gtk), "Entry"))
        _l_(583549)
        _c_(583553, _a_(583552, _a_(583551, _n_(583550, "self", lambda: self), "user_input"), "set_text"), 'https://')
        _l_(583554)
        _c_(583559, _a_(583556, _n_(583555, "vbox", lambda: vbox), "pack_start"), _a_(583558, _n_(583557, "self", lambda: self), "user_input"), expand=False, fill=False, padding=4)
        _l_(583560)
        _c_(583565, _a_(583562, _n_(583561, "vbox", lambda: vbox), "pack_start"), _a_(583564, _n_(583563, "self", lambda: self), "button"), expand=False, fill=False, padding=4)
        _l_(583566)

        web = _c_(583569, _a_(583568, _n_(583567, "pywebkit", lambda: pywebkit), "WebView"))
        _l_(583570)

    def test():
        _l_(583583)

        add = _c_(583575, _a_(583574, _a_(583573, _n_(583572, "self", lambda: self), "user_input"), "get_text"))
        _l_(583576)
        _c_(583581, _a_(583578, _n_(583577, "web", lambda: web), "open"), _a_(583580, _n_(583579, "self", lambda: self), "user_input"))
        _l_(583582)

win = _c_(583586, _n_(583585, "Main", lambda: Main))
_l_(583587)
_c_(583592, _a_(583589, _n_(583588, "win", lambda: win), "connect"), 'delete-event', _a_(583591, _n_(583590, "Gtk", lambda: Gtk), "main_quit"))
_l_(583593)
_c_(583596, _a_(583595, _n_(583594, "win", lambda: win), "show_all"))
_l_(583597)
_c_(583600, _a_(583599, _n_(583598, "Gtk", lambda: Gtk), "main"))
_l_(583601)