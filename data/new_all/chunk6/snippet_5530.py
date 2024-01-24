# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66767714/typeerror-int-object-is-not-iterable-in-a-for-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(371861)

except ImportError:
    pass

def compte(l,v):
    _l_(371872)

    nbreOccurences = 0
    _l_(371862)
    for i in _n_(371863, "l", lambda: l):
        _l_(371869)

        if (_n_(371864, "i", lambda: i) == _n_(371865, "v", lambda: v)):
            _l_(371868)

            nbreOccurences = _n_(371866, "nbreOccurences", lambda: nbreOccurences) + 1
            _l_(371867)
    aux = _n_(371870, "nbreOccurences", lambda: nbreOccurences)
    _l_(371871)
    return aux

N = 100
_l_(371873)
            
l3 = []
_l_(371874)
for i in _c_(371877, _n_(371875, "range", lambda: range), _n_(371876, "N", lambda: N)):
    _l_(371888)

    v = _c_(371881, _a_(371879, _n_(371878, "random", lambda: random), "randrange"), 1,_n_(371880, "N", lambda: N)+1)
    _l_(371882)
    _c_(371886, _a_(371884, _n_(371883, "l3", lambda: l3), "append"), _n_(371885, "v", lambda: v))
    _l_(371887)

_c_(371891, _n_(371889, "print", lambda: print), _n_(371890, "l3", lambda: l3))
_l_(371892)
_c_(371896, _n_(371893, "print", lambda: print), _c_(371895, _n_(371894, "compte", lambda: compte), 13,3))            
_l_(371897)            