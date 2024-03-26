# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def filter_data(students):
    _l_(110929)

    result = {_n_(110919, "k", lambda: k): _n_(110920, "s", lambda: s) for k, s in _c_(110923, _a_(110922, _n_(110921, "students", lambda: students), "items")) if _n_(110924, "s", lambda: s)[0] >= 6.0 and _n_(110925, "s", lambda: s)[1] >= 70}
    _l_(110926)
    aux = _n_(110927, "result", lambda: result)
    _l_(110928)
    return aux
_c_(110931, _n_(110930, "print", lambda: print), 'Original Dictionary:')
_l_(110932)
_c_(110935, _n_(110933, "print", lambda: print), _n_(110934, "students", lambda: students))
_l_(110936)
_c_(110938, _n_(110937, "print", lambda: print), '\nHeight > 6ft and Weight> 70kg:')
_l_(110939)
_c_(110944, _n_(110940, "print", lambda: print), _c_(110943, _n_(110941, "filter_data", lambda: filter_data), _n_(110942, "students", lambda: students)))
_l_(110945)