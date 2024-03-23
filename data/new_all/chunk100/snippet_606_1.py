# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unfold(fn, seed):
    _l_(63475)


    def fn_generator(val):
        _l_(63469)

        while True:
            _l_(63468)

            val = _c_(63461, _n_(63459, "fn", lambda: fn), _n_(63460, "val", lambda: val)[1])
            _l_(63462)
            if _n_(63463, "val", lambda: val) == False:
                _l_(63465)

                break
                _l_(63464)
            yield _n_(63466, "val", lambda: val)[0]
            _l_(63467)
    aux = [_n_(63470, "i", lambda: i) for i in _c_(63473, _n_(63471, "fn_generator", lambda: fn_generator), [None, _n_(63472, "seed", lambda: seed)])]
    _l_(63474)
    return aux
_c_(63480, _n_(63476, "print", lambda: print), _c_(63479, _n_(63477, "unfold", lambda: unfold), _n_(63478, "f", lambda: f), 10))
_l_(63481)