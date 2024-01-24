# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71437991/typeerror-unsupported-operand-types-for-str-and-str-in-robot-framework
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a=5
_l_(594817)
b=6
_l_(594818)
def Addition(a,b):
    _l_(594833)

    s=_n_(594819, "a", lambda: a)+_n_(594820, "b", lambda: b)
    _l_(594821)
    c = 3
    _l_(594822)
    d = 2
    _l_(594823)
    _c_(594827, _n_(594824, "Sub", lambda: Sub), _n_(594825, "c", lambda: c),_n_(594826, "d", lambda: d))
    _l_(594828)
    _c_(594831, _n_(594829, "print", lambda: print), _n_(594830, "s", lambda: s))
    _l_(594832)
def Sub(c,d):
    _l_(594841)

    e=_n_(594834, "c", lambda: c)-_n_(594835, "d", lambda: d)
    _l_(594836)
    _c_(594839, _n_(594837, "print", lambda: print), _n_(594838, "e", lambda: e))
    _l_(594840)
_c_(594845, _n_(594842, "Addition", lambda: Addition), _n_(594843, "a", lambda: a),_n_(594844, "b", lambda: b))
_l_(594846)