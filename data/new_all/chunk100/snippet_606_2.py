# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unfold(fn, seed):
    _l_(63494)


    def fn_generator(val):
        _l_(63488)

        while True:
            _l_(63487)

            if _n_(63482, "val", lambda: val) == False:
                _l_(63484)

                break
                _l_(63483)
            yield _n_(63485, "val", lambda: val)[0]
            _l_(63486)
    aux = [_n_(63489, "i", lambda: i) for i in _c_(63492, _n_(63490, "fn_generator", lambda: fn_generator), [None, _n_(63491, "seed", lambda: seed)])]
    _l_(63493)
    return aux
f = lambda n: False if _n_(63495, "n", lambda: n) > 40 else [-_n_(63496, "n", lambda: n), _n_(63497, "n", lambda: n) + 10]
_l_(63498)
_c_(63503, _n_(63499, "print", lambda: print), _c_(63502, _n_(63500, "unfold", lambda: unfold), _n_(63501, "f", lambda: f), 10))
_l_(63504)