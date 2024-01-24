# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72147577/python-gtk-3-24-attributeerror-type-object-gtk-has-no-attribute-builder
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gi
    _l_(639281)

except ImportError:
    pass
_c_(639284, _a_(639283, _n_(639282, "gi", lambda: gi), "require_version"), 'Gtk','3.0')
_l_(639285)
try:
    from gi.repository import Gtk
    _l_(639287)

except ImportError:
    pass

builder = _c_(639290, _a_(639289, _n_(639288, "Gtk", lambda: Gtk), "Builder"))
_l_(639291)
_c_(639294, _a_(639293, _n_(639292, "builder", lambda: builder), "add_from_file"), 'user_interface.glade')
_l_(639295)

class Manipulador(_n_(639296, "object", lambda: object)):
    _l_(639325)

    def __init__(self):
        _l_(639307)

        _n_(639297, "self", lambda: self).entry = _c_(639300, _a_(639299, _n_(639298, "builder", lambda: builder), "get_object"), 'entry')
        _l_(639301)
        _n_(639302, "self", lambda: self).label = _c_(639305, _a_(639304, _n_(639303, "builder", lambda: builder), "get_object"), 'label')
        _l_(639306)

    def on_button_clicked(self, button):
        _l_(639319)

        text = _c_(639311, _a_(639310, _a_(639309, _n_(639308, "self", lambda: self), "entry"), "get_text"))
        _l_(639312)
        _c_(639317, _a_(639315, _a_(639314, _n_(639313, "self", lambda: self), "label"), "set_text"), _n_(639316, "text", lambda: text))
        _l_(639318)

    def on_main_window_destroy(self, window):
        _l_(639324)

        _c_(639322, _a_(639321, _n_(639320, "Gtk", lambda: Gtk), "main_quit"))
        _l_(639323)

_c_(639330, _a_(639327, _n_(639326, "builder", lambda: builder), "connect_signals"), _c_(639329, _n_(639328, "Manipulador", lambda: Manipulador)))
_l_(639331)
window = _c_(639334, _a_(639333, _n_(639332, "builder", lambda: builder), "get_object"))
_l_(639335)
_c_(639338, _a_(639337, _n_(639336, "window", lambda: window), "show_all"))
_l_(639339)
_c_(639342, _a_(639341, _n_(639340, "Gtk", lambda: Gtk), "main"))
_l_(639343)