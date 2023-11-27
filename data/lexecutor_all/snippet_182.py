# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(1543574)

except ImportError:
    pass

text = 'Mary had a little lamb'
_l_(1543575)
chars = _c_(1543578, _n_(1543576, "defaultdict", lambda: defaultdict), _n_(1543577, "int", lambda: int))
_l_(1543579)

for char in _n_(1543580, "text", lambda: text):
    _l_(1543584)

    _n_(1543581, "chars", lambda: chars)[_n_(1543582, "char", lambda: char)] += 1
    _l_(1543583)

_n_(1543585, "chars", lambda: chars)['a']
_l_(1543586)
4
_l_(1543587)
_n_(1543588, "chars", lambda: chars)['x']
_l_(1543589)
0
_l_(1543590)

class CICounter(_n_(1543591, "defaultdict", lambda: defaultdict)):
    _l_(1543609)

    def __getitem__(self, k):
        _l_(1543599)

        aux = _c_(1543597, _a_(1543593, _n_(1543592, "super", lambda: super)(), "__getitem__"), _c_(1543596, _a_(1543595, _n_(1543594, "k", lambda: k), "lower")))
        _l_(1543598)
        return aux

    def __setitem__(self, k, v):
        _l_(1543608)

        _c_(1543606, _a_(1543601, _n_(1543600, "super", lambda: super)(), "__setitem__"), _c_(1543604, _a_(1543603, _n_(1543602, "k", lambda: k), "lower")), _n_(1543605, "v", lambda: v))
        _l_(1543607)


chars = _c_(1543612, _n_(1543610, "CICounter", lambda: CICounter), _n_(1543611, "int", lambda: int))
_l_(1543613)

for char in _n_(1543614, "text", lambda: text):
    _l_(1543618)

    _n_(1543615, "chars", lambda: chars)[_n_(1543616, "char", lambda: char)] += 1
    _l_(1543617)

_n_(1543619, "chars", lambda: chars)['a']
_l_(1543620)
4
_l_(1543621)
_n_(1543622, "chars", lambda: chars)['M']
_l_(1543623)
2
_l_(1543624)
_n_(1543625, "chars", lambda: chars)['x']
_l_(1543626)
0
_l_(1543627)

