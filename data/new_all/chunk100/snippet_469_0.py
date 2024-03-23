# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def catalan_number(num):
    _l_(49410)

    if _n_(49393, "num", lambda: num) <= 1:
        _l_(49395)

        aux = 1
        _l_(49394)
        return aux
    for i in _c_(49398, _n_(49396, "range", lambda: range), _n_(49397, "num", lambda: num)):
        _l_(49407)

        res_num += _c_(49401, _n_(49399, "catalan_number", lambda: catalan_number), _n_(49400, "i", lambda: i)) * _c_(49405, _n_(49402, "catalan_number", lambda: catalan_number), _n_(49403, "num", lambda: num) - _n_(49404, "i", lambda: i) - 1)
        _l_(49406)
    aux = _n_(49408, "res_num", lambda: res_num)
    _l_(49409)
    return aux
for n in _c_(49412, _n_(49411, "range", lambda: range), 10):
    _l_(49419)

    _c_(49417, _n_(49413, "print", lambda: print), _c_(49416, _n_(49414, "catalan_number", lambda: catalan_number), _n_(49415, "n", lambda: n)))
    _l_(49418)