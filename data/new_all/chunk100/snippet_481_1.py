# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def second_smallest(numbers):
    _l_(50389)

    if _c_(50357, _n_(50355, "len", lambda: len), _n_(50356, "numbers", lambda: numbers)) < 2:
        _l_(50359)

        aux = ""
        _l_(50358)
        return aux
    if _c_(50362, _n_(50360, "len", lambda: len), _n_(50361, "numbers", lambda: numbers)) == 2 and _n_(50363, "numbers", lambda: numbers)[0] == _n_(50364, "numbers", lambda: numbers)[1]:
        _l_(50366)

        aux = ""
        _l_(50365)
        return aux
    uniq_items = []
    _l_(50367)
    for x in _n_(50368, "numbers", lambda: numbers):
        _l_(50382)

        if _n_(50369, "x", lambda: x) not in _n_(50370, "dup_items", lambda: dup_items):
            _l_(50381)

            _c_(50374, _a_(50372, _n_(50371, "uniq_items", lambda: uniq_items), "append"), _n_(50373, "x", lambda: x))
            _l_(50375)
            _c_(50379, _a_(50377, _n_(50376, "dup_items", lambda: dup_items), "add"), _n_(50378, "x", lambda: x))
            _l_(50380)
    _c_(50385, _a_(50384, _n_(50383, "uniq_items", lambda: uniq_items), "sort"))
    _l_(50386)
    aux = _n_(50387, "uniq_items", lambda: uniq_items)[1]
    _l_(50388)
    return aux
_c_(50393, _n_(50390, "print", lambda: print), _c_(50392, _n_(50391, "second_smallest", lambda: second_smallest), [1, 2, -8, -2, 0, -2]))
_l_(50394)
_c_(50398, _n_(50395, "print", lambda: print), _c_(50397, _n_(50396, "second_smallest", lambda: second_smallest), [1, 1, 0, 0, 2, -2, -2]))
_l_(50399)
_c_(50403, _n_(50400, "print", lambda: print), _c_(50402, _n_(50401, "second_smallest", lambda: second_smallest), [1, 1, 1, 0, 0, 0, 2, -2, -2]))
_l_(50404)
_c_(50408, _n_(50405, "print", lambda: print), _c_(50407, _n_(50406, "second_smallest", lambda: second_smallest), [2, 2]))
_l_(50409)
_c_(50413, _n_(50410, "print", lambda: print), _c_(50412, _n_(50411, "second_smallest", lambda: second_smallest), [2]))
_l_(50414)