# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40672396/attributeerror-module-urwid-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urwid
    _l_(387884)

except ImportError:
    pass
txt = _c_(387887, _a_(387886, _n_(387885, "urwid", lambda: urwid), "Text"), u"Hello World")
_l_(387888)
fill = _c_(387892, _a_(387890, _n_(387889, "urwid", lambda: urwid), "Filler"), _n_(387891, "txt", lambda: txt), 'top')
_l_(387893)
loop = _c_(387897, _a_(387895, _n_(387894, "urwid", lambda: urwid), "MainLoop"), _n_(387896, "fill", lambda: fill))
_l_(387898)
_c_(387901, _a_(387900, _n_(387899, "loop", lambda: loop), "run"))
_l_(387902)