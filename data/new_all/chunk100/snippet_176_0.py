# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from re import sub
    _l_(12679)

except ImportError:
    pass

def camel_case(s):
    _l_(12687)

    aux = _c_(12685, _a_(12680, '', "join"), [_c_(12683, _a_(12682, _n_(12681, "s", lambda: s)[0], "lower")), _n_(12684, "s", lambda: s)[1:]])
    _l_(12686)
    return aux
_c_(12691, _n_(12688, "print", lambda: print), _c_(12690, _n_(12689, "camel_case", lambda: camel_case), 'JavaScript'))
_l_(12692)
_c_(12696, _n_(12693, "print", lambda: print), _c_(12695, _n_(12694, "camel_case", lambda: camel_case), 'Foo-Bar'))
_l_(12697)
_c_(12701, _n_(12698, "print", lambda: print), _c_(12700, _n_(12699, "camel_case", lambda: camel_case), 'foo_bar'))
_l_(12702)
_c_(12706, _n_(12703, "print", lambda: print), _c_(12705, _n_(12704, "camel_case", lambda: camel_case), '--foo.bar'))
_l_(12707)
_c_(12711, _n_(12708, "print", lambda: print), _c_(12710, _n_(12709, "camel_case", lambda: camel_case), 'Foo-BAR'))
_l_(12712)
_c_(12716, _n_(12713, "print", lambda: print), _c_(12715, _n_(12714, "camel_case", lambda: camel_case), 'fooBAR'))
_l_(12717)
_c_(12721, _n_(12718, "print", lambda: print), _c_(12720, _n_(12719, "camel_case", lambda: camel_case), 'foo bar'))
_l_(12722)