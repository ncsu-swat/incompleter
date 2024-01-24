# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59872286/typeerror-unsupported-operand-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cel_to_fahr(c):
    _l_(652545)

    f = _n_(652541, "c", lambda: c) * 9/5 + 32
    _l_(652542)
    aux = _n_(652543, "f", lambda: f)
    _l_(652544)
    return aux

c = _c_(652547, _n_(652546, "input", lambda: input), "enter the temperature in celcius:")
_l_(652548)
_c_(652553, _n_(652549, "print", lambda: print), _c_(652552, _n_(652550, "cel_to_fahr", lambda: cel_to_fahr), _n_(652551, "c", lambda: c)))
_l_(652554)