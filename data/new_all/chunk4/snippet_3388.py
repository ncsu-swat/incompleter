# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74989743/how-can-i-choose-a-specific-intersection-element-in-a-list-typeerror-unhashed
#x = []
#x.append([[hockeymatch], [number1], [number2]])
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = [[[('Dallas-Arizona', 'NHL', '15:00')], [1.75], [87.5]],
     [('Seattle-Minnesota', 'NHL', '18:00')], [2.5], [125.0]]
_l_(637734)

#y = []
#y.append([[hockeymatch], [number1], [number2]])
y = [[[('Seattle-Minnesota', 'NHL', '18:00')], [1.33], [62.0]],
       [('Vancouver-Vegas', 'NHL', '20:00')], [0.50], [43.0]]
_l_(637735)

test = _c_(637743, _n_(637736, "list", lambda: list), _c_(637742, _a_(637740, _c_(637739, _n_(637737, "set", lambda: set), _n_(637738, "x", lambda: x)[0]), "intersection"), _n_(637741, "y", lambda: y)[0]))
_l_(637744)
_c_(637747, _n_(637745, "print", lambda: print), _n_(637746, "test", lambda: test))
_l_(637748)