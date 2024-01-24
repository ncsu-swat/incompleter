# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61825038/typeerror-list-indices-must-be-integers-or-slices-not-str-it-is-showing-in-if
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lst = ['abc', 'Bcd', 'abf', 'bbc', 'Anv']
_l_(706226)

w = 0
_l_(706227)

for i in _n_(706228, "lst", lambda: lst):
    _l_(706237)


    if _c_(706234, _n_(706229, "int", lambda: int), _c_(706233, _a_(706232, _n_(706230, "lst", lambda: lst)[_n_(706231, "i", lambda: i)][0], "isupper"))) != 0:
        _l_(706236)


        w += 1
        _l_(706235)
_c_(706240, _n_(706238, "print", lambda: print), _n_(706239, "w", lambda: w))
_l_(706241)