# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_sublists(input_list):
    _l_(106399)

    result = [_c_(106394, _n_(106391, "sorted", lambda: sorted), _n_(106392, "x", lambda: x), key=lambda x: _n_(106393, "x", lambda: x)[0]) for x in _n_(106395, "input_list", lambda: input_list)]
    _l_(106396)
    aux = _n_(106397, "result", lambda: result)
    _l_(106398)
    return aux
_c_(106401, _n_(106400, "print", lambda: print), '\nOriginal list:')
_l_(106402)
_c_(106405, _n_(106403, "print", lambda: print), _n_(106404, "color1", lambda: color1))
_l_(106406)
_c_(106408, _n_(106407, "print", lambda: print), '\nAfter sorting each sublist of the said list of lists:')
_l_(106409)
_c_(106414, _n_(106410, "print", lambda: print), _c_(106413, _n_(106411, "sort_sublists", lambda: sort_sublists), _n_(106412, "color1", lambda: color1)))
_l_(106415)