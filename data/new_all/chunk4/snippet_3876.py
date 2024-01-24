# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66104884/unsupported-operand-type-error-when-trying-to-multiply-function-parameter-by-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def user_input(x):
    _l_(585960)

    _c_(585958, _n_(585956, "print", lambda: print), _n_(585957, "x", lambda: x))
    _l_(585959)


def repeat(y):
    _l_(585963)

    aux = 5*_n_(585961, "y", lambda: y)
    _l_(585962)
    return aux


_c_(585969, _n_(585964, "repeat", lambda: repeat), _c_(585968, _n_(585965, "user_input", lambda: user_input), _c_(585967, _n_(585966, "input", lambda: input), 'Get input ')))
_l_(585970)