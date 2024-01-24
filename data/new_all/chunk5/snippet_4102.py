# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59872286/typeerror-unsupported-operand-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cel_to_fahr(c):
    _l_(704191)

    f = _n_(704187, "c", lambda: c) * 9/5 + 32
    _l_(704188)
    aux = _n_(704189, "f", lambda: f)
    _l_(704190)
    return aux

c = _c_(704193, _n_(704192, "input", lambda: input), "enter the temperature in celcius:")
_l_(704194)
_c_(704199, _n_(704195, "print", lambda: print), _c_(704198, _n_(704196, "cel_to_fahr", lambda: cel_to_fahr), _n_(704197, "c", lambda: c)))
_l_(704200)