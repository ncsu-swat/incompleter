# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49861600/why-am-i-getting-this-class-tkinter-entry-get-attributeerror-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class asd:
    _l_(348107)


    def gui(self, guiwindow, labelplacex, labelplacey, textx, texty, entryx, entryy):
        _l_(348106)

        _n_(348026, "self", lambda: self).root = _n_(348027, "tk", lambda: tk)
        _l_(348028)
        _n_(348029, "self", lambda: self).image = _c_(348033, _a_(348031, _n_(348030, "tk", lambda: tk), "PhotoImage"), file=_n_(348032, "aimage_path", lambda: aimage_path))
        _l_(348034)
        _n_(348035, "self", lambda: self).label = _c_(348040, _a_(348037, _n_(348036, "tk", lambda: tk), "Label"), image=_a_(348039, _n_(348038, "self", lambda: self), "image"))
        _l_(348041)
        _c_(348045, _a_(348044, _a_(348043, _n_(348042, "self", lambda: self), "label"), "pack"))
        _l_(348046)
        _c_(348052, _a_(348049, _a_(348048, _n_(348047, "self", lambda: self), "label"), "place"), x=_n_(348050, "labelplacex", lambda: labelplacex) , y=_n_(348051, "labelplacey", lambda: labelplacey))
        _l_(348053)
        _n_(348054, "self", lambda: self).text = _c_(348057, _n_(348055, "Label", lambda: Label), _n_(348056, "guiawindow", lambda: guiawindow), text="Code:")
        _l_(348058)
        _c_(348062, _a_(348061, _a_(348060, _n_(348059, "self", lambda: self), "text"), "pack"))
        _l_(348063)
        _c_(348069, _a_(348066, _a_(348065, _n_(348064, "self", lambda: self), "text"), "place"), x = _n_(348067, "textx", lambda: textx),y = _n_(348068, "texty", lambda: texty))
        _l_(348070)
        _n_(348071, "self", lambda: self).entry = _c_(348074, _n_(348072, "Entry", lambda: Entry), _n_(348073, "guiwindow", lambda: guiwindow))
        _l_(348075)
        _c_(348079, _a_(348078, _a_(348077, _n_(348076, "self", lambda: self), "entry"), "pack"))
        _l_(348080)
        _c_(348086, _a_(348083, _a_(348082, _n_(348081, "self", lambda: self), "entry"), "place"), x = _n_(348084, "entryx", lambda: entryx),y = _n_(348085, "entryy", lambda: entryy))
        _l_(348087)
        _n_(348088, "self", lambda: self).button = _c_(348094, _n_(348089, "Button", lambda: Button), _c_(348091, _n_(348090, "Tk", lambda: Tk)), text="Back Menu", command=_a_(348093, _n_(348092, "self", lambda: self), "asdfg"))
        _l_(348095)
        _c_(348099, _a_(348098, _a_(348097, _n_(348096, "self", lambda: self), "button"), "pack"))
        _l_(348100)
        _c_(348104, _a_(348103, _a_(348102, _n_(348101, "self", lambda: self), "root"), "mainloop"))
        _l_(348105)

_c_(348112, _a_(348111, _a_(348110, _a_(348109, _n_(348108, "asd", lambda: asd), "gui"), "entry"), "get"))
_l_(348113)