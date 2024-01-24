# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30797220/python-3-x-attributeerror-nonetype-object-has-no-attribute-groupdict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(345093)

except ImportError:
    pass

fmt = (r"\+((?P<day>\d+)d)?((?P<hrs>\d+)h)?((?P<min>\d+)m)?"
       r"((?P<sec>\d+)s)?((?P<ms>\d+)ms)?$")
_l_(345094)
p = _c_(345098, _a_(345096, _n_(345095, "re", lambda: re), "compile"), _n_(345097, "fmt", lambda: fmt))
_l_(345099)
match = _c_(345102, _a_(345101, _n_(345100, "p", lambda: p), "search"), 'Total run time: 9h 34m 9s 901ms realtime, 7h 6m 29s 699ms uptime')
_l_(345103)
try:
    _l_(345113)

    d = _c_(345106, _a_(345105, _n_(345104, "match", lambda: match), "groupdict"))
    _l_(345107)
except _n_(345108, "IndexError", lambda: IndexError):
    _l_(345112)

    _c_(345110, _n_(345109, "print", lambda: print), "exception here")
    _l_(345111)