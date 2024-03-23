# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unfold(fn, seed):
    _l_(63448)


    def fn_generator(val):
        _l_(63442)

        while True:
            _l_(63441)

            if _n_(63436, "val", lambda: val) == False:
                _l_(63438)

                break
                _l_(63437)
            yield _n_(63439, "val", lambda: val)[0]
            _l_(63440)
    aux = [_n_(63443, "i", lambda: i) for i in _c_(63446, _n_(63444, "fn_generator", lambda: fn_generator), [None, _n_(63445, "seed", lambda: seed)])]
    _l_(63447)
    return aux
f = lambda n: False if _n_(63449, "n", lambda: n) > 40 else [-_n_(63450, "n", lambda: n), _n_(63451, "n", lambda: n) + 10]
_l_(63452)
_c_(63457, _n_(63453, "print", lambda: print), _c_(63456, _n_(63454, "unfold", lambda: unfold), _n_(63455, "f", lambda: f), 10))
_l_(63458)