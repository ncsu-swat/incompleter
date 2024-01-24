# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21622193/python-3-2-coroutine-attributeerror-generator-object-has-no-attribute-next
#!/usr/bin/python3.2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(382997)

except ImportError:
    pass

def match_text(pattern):
    _l_(383006)

    line = (yield)
    _l_(382998)
    if _n_(382999, "pattern", lambda: pattern) in _n_(383000, "line", lambda: line):
        _l_(383005)

        _c_(383003, _n_(383001, "print", lambda: print), _n_(383002, "line", lambda: line))
        _l_(383004)

x = _c_(383008, _n_(383007, "match_text", lambda: match_text), 'apple')
_l_(383009)
_c_(383012, _a_(383011, _n_(383010, "x", lambda: x), "next"))
_l_(383013)

for line in _c_(383015, _n_(383014, "input", lambda: input), '>>>> '):
    _l_(383025)

    if _c_(383019, _a_(383017, _n_(383016, "x", lambda: x), "send"), _n_(383018, "line", lambda: line)):
        _l_(383024)

        _c_(383022, _n_(383020, "print", lambda: print), _n_(383021, "line", lambda: line))
        _l_(383023)

_c_(383028, _a_(383027, _n_(383026, "x", lambda: x), "close"))
_l_(383029)