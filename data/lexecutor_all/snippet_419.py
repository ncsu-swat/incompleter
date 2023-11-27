# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
# extract numbers from garbage string:
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s = '12//n,_@#$%3.14kjlw0xdadfackvj1.6e-19&*ghn334'
_l_(1539381)
newstr = _c_(1539386, _a_(1539382, '', "join"), ((_n_(1539383, "ch", lambda: ch) if _n_(1539384, "ch", lambda: ch) in '0123456789.-e' else ' ') for ch in _n_(1539385, "s", lambda: s)))
_l_(1539387)
listOfNumbers = [_c_(1539390, _n_(1539388, "float", lambda: float), _n_(1539389, "i", lambda: i)) for i in _c_(1539393, _a_(1539392, _n_(1539391, "newstr", lambda: newstr), "split"))]
_l_(1539394)
_c_(1539397, _n_(1539395, "print", lambda: print), _n_(1539396, "listOfNumbers", lambda: listOfNumbers))
_l_(1539398)
[12.0, 3.14, 0.0, 1.6e-19, 334.0]
_l_(1539399)

