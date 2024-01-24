# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30797220/python-3-x-attributeerror-nonetype-object-has-no-attribute-groupdict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(362401)

except ImportError:
    pass

fmt = (r"\+((?P<day>\d+)d)?((?P<hrs>\d+)h)?((?P<min>\d+)m)?"
       r"((?P<sec>\d+)s)?((?P<ms>\d+)ms)?$")
_l_(362402)
p = _c_(362406, _a_(362404, _n_(362403, "re", lambda: re), "compile"), _n_(362405, "fmt", lambda: fmt))
_l_(362407)
match = _c_(362410, _a_(362409, _n_(362408, "p", lambda: p), "search"), 'Total run time: 9h 34m 9s 901ms realtime, 7h 6m 29s 699ms uptime')
_l_(362411)
try:
    _l_(362421)

    d = _c_(362414, _a_(362413, _n_(362412, "match", lambda: match), "groupdict"))
    _l_(362415)
except _n_(362416, "IndexError", lambda: IndexError):
    _l_(362420)

    _c_(362418, _n_(362417, "print", lambda: print), "exception here")
    _l_(362419)