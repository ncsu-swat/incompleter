# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28354945/why-am-i-getting-typeerror-int-object-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
amx = []
_l_(447447)

def validamount(amount, limit):
    _l_(447454)

    if _n_(447448, "amount", lambda: amount) >= _n_(447449, "limit", lambda: limit):
        _l_(447453)

        aux = _n_(447450, "amount", lambda: amount)
        _l_(447451)
        return aux
    else:
        aux = 0
        _l_(447452)
        return aux

def main():
    _l_(447472)

    for i in 10:
        _l_(447463)

        _c_(447461, _a_(447456, _n_(447455, "amx", lambda: amx), "append"), _c_(447460, _n_(447457, "int", lambda: int), _c_(447459, _n_(447458, "input", lambda: input))))
        _l_(447462)
    for i in 10:
        _l_(447471)

        _c_(447469, _n_(447464, "print", lambda: print), _c_(447468, _n_(447465, "validamount", lambda: validamount), _n_(447466, "amx", lambda: amx)[_n_(447467, "i", lambda: i)], 5))
        _l_(447470)

_c_(447474, _n_(447473, "main", lambda: main))
_l_(447475)