# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67916291/pd-dataframe-resulting-in-typeerror-when-a-metaclass-is-defined-before-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Test(_n_(437603, "Mapping", lambda: Mapping)):
    _l_(437607)

    x = 1
    _l_(437604)
    y = 2
    _l_(437605)
    z = 3
    _l_(437606)

'x' in _n_(437608, "Test", lambda: Test)           # True
_l_(437609)           # True
_c_(437614, _n_(437610, "list", lambda: list), _c_(437613, _a_(437612, _n_(437611, "Test", lambda: Test), "items")))    # [('x', 1), ('y', 2), ('z', 3)]
_l_(437615)    # [('x', 1), ('y', 2), ('z', 3)]
{**_n_(437616, "Test", lambda: Test)}              # {'x': 1, 'y': 2, 'z': 3}
_l_(437617)              # {'x': 1, 'y': 2, 'z': 3}