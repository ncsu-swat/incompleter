# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(110330)

except ImportError:
    pass

def test(*dicts):
    _l_(110350)

    result = _c_(110333, _n_(110331, "defaultdict", lambda: defaultdict), _n_(110332, "list", lambda: list))
    _l_(110334)
    for el in _n_(110335, "dicts", lambda: dicts):
        _l_(110345)

        for key in _n_(110336, "el", lambda: el):
            _l_(110344)

            _c_(110342, _a_(110339, _n_(110337, "result", lambda: result)[_n_(110338, "key", lambda: key)], "append"), _n_(110340, "el", lambda: el)[_n_(110341, "key", lambda: key)])
            _l_(110343)
    aux = _c_(110348, _n_(110346, "dict", lambda: dict), _n_(110347, "result", lambda: result))
    _l_(110349)
    return aux
d2 = {'x': 300, 'y': 'Red', 'z': 600}
_l_(110351)
_c_(110353, _n_(110352, "print", lambda: print), 'Original dictionaries:')
_l_(110354)
_c_(110357, _n_(110355, "print", lambda: print), _n_(110356, "d1", lambda: d1))
_l_(110358)
_c_(110361, _n_(110359, "print", lambda: print), _n_(110360, "d2", lambda: d2))
_l_(110362)
_c_(110364, _n_(110363, "print", lambda: print), '\nCombined dictionaries, creating a list of values for each key:')
_l_(110365)
_c_(110371, _n_(110366, "print", lambda: print), _c_(110370, _n_(110367, "test", lambda: test), _n_(110368, "d1", lambda: d1), _n_(110369, "d2", lambda: d2)))
_l_(110372)