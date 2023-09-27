# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def somefunction(p):
    _l_(1547571)

    a=_n_(1547561, "p", lambda: p)+1
    _l_(1547562)
    b=_n_(1547563, "p", lambda: p)+2
    _l_(1547564)
    c=-_n_(1547565, "p", lambda: p)
    _l_(1547566)
    aux = _n_(1547567, "a", lambda: a), _n_(1547568, "b", lambda: b), _n_(1547569, "c", lambda: c)
    _l_(1547570)
    return aux

x, y, z = _c_(1547574, _n_(1547572, "somefunction", lambda: somefunction), _n_(1547573, "w", lambda: w))
_l_(1547575)

def somefunction(a, b, c):
    _l_(1547589)

    a = _n_(1547576, "a", lambda: a) * 2
    _l_(1547577)
    b = _n_(1547578, "b", lambda: b) + _n_(1547579, "a", lambda: a)
    _l_(1547580)
    c = _n_(1547581, "a", lambda: a) * _n_(1547582, "b", lambda: b) * _n_(1547583, "c", lambda: c)
    _l_(1547584)
    aux = _n_(1547585, "a", lambda: a), _n_(1547586, "b", lambda: b), _n_(1547587, "c", lambda: c)
    _l_(1547588)
    return aux

x = 3
_l_(1547590)
y = 5
_l_(1547591)
z = 10
_l_(1547592)
_c_(1547597, _n_(1547593, "print", lambda: print), F"Before : {_n_(1547594, "x", lambda: x)}, {_n_(1547595, "y", lambda: y)}, {_n_(1547596, "z", lambda: z)}")
_l_(1547598)

x, y, z = _c_(1547603, _n_(1547599, "somefunction", lambda: somefunction), _n_(1547600, "x", lambda: x), _n_(1547601, "y", lambda: y), _n_(1547602, "z", lambda: z))
_l_(1547604)

_c_(1547609, _n_(1547605, "print", lambda: print), F"After  : {_n_(1547606, "x", lambda: x)}, {_n_(1547607, "y", lambda: y)}, {_n_(1547608, "z", lambda: z)}")
_l_(1547610)

