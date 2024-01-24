# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72147577/python-gtk-3-24-attributeerror-type-object-gtk-has-no-attribute-builder
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gi
    _l_(589302)

except ImportError:
    pass
_c_(589305, _a_(589304, _n_(589303, "gi", lambda: gi), "require_version"), 'Gtk','3.0')
_l_(589306)
try:
    from gi.repository import Gtk
    _l_(589308)

except ImportError:
    pass

builder = _c_(589311, _a_(589310, _n_(589309, "Gtk", lambda: Gtk), "Builder"))
_l_(589312)
_c_(589315, _a_(589314, _n_(589313, "builder", lambda: builder), "add_from_file"), 'user_interface.glade')
_l_(589316)

class Manipulador(_n_(589317, "object", lambda: object)):
    _l_(589346)

    def __init__(self):
        _l_(589328)

        _n_(589318, "self", lambda: self).entry = _c_(589321, _a_(589320, _n_(589319, "builder", lambda: builder), "get_object"), 'entry')
        _l_(589322)
        _n_(589323, "self", lambda: self).label = _c_(589326, _a_(589325, _n_(589324, "builder", lambda: builder), "get_object"), 'label')
        _l_(589327)

    def on_button_clicked(self, button):
        _l_(589340)

        text = _c_(589332, _a_(589331, _a_(589330, _n_(589329, "self", lambda: self), "entry"), "get_text"))
        _l_(589333)
        _c_(589338, _a_(589336, _a_(589335, _n_(589334, "self", lambda: self), "label"), "set_text"), _n_(589337, "text", lambda: text))
        _l_(589339)

    def on_main_window_destroy(self, window):
        _l_(589345)

        _c_(589343, _a_(589342, _n_(589341, "Gtk", lambda: Gtk), "main_quit"))
        _l_(589344)

_c_(589351, _a_(589348, _n_(589347, "builder", lambda: builder), "connect_signals"), _c_(589350, _n_(589349, "Manipulador", lambda: Manipulador)))
_l_(589352)
window = _c_(589355, _a_(589354, _n_(589353, "builder", lambda: builder), "get_object"))
_l_(589356)
_c_(589359, _a_(589358, _n_(589357, "window", lambda: window), "show_all"))
_l_(589360)
_c_(589363, _a_(589362, _n_(589361, "Gtk", lambda: Gtk), "main"))
_l_(589364)