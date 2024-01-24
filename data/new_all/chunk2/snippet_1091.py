# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27876683/mac-os-x-urwid-attributeerror-selectableicon-object-has-no-attribute-select
# hellotest.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urwid
    _l_(452629)

except ImportError:
    pass

txt = _c_(452632, _a_(452631, _n_(452630, "urwid", lambda: urwid), "Text"), u"Hello World")
_l_(452633)
fill = _c_(452637, _a_(452635, _n_(452634, "urwid", lambda: urwid), "Filler"), _n_(452636, "txt", lambda: txt), 'top')
_l_(452638)
loop = _c_(452642, _a_(452640, _n_(452639, "urwid", lambda: urwid), "MainLoop"), _n_(452641, "fill", lambda: fill))
_l_(452643)
_c_(452646, _a_(452645, _n_(452644, "loop", lambda: loop), "run"))
_l_(452647)