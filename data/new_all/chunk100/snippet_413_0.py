# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def amicable_numbers_sum(limit):
    _l_(40580)

    if not _c_(40535, _n_(40532, "isinstance", lambda: isinstance), _n_(40533, "limit", lambda: limit), _n_(40534, "int", lambda: int)):
        _l_(40537)

        aux = 'Input is not an integer!'
        _l_(40536)
        return aux
    if _n_(40538, "limit", lambda: limit) < 1:
        _l_(40540)

        aux = 'Input must be bigger than 0!'
        _l_(40539)
        return aux
    amicables = _c_(40542, _n_(40541, "set", lambda: set))
    _l_(40543)
    for num in _c_(40546, _n_(40544, "range", lambda: range), 2, _n_(40545, "limit", lambda: limit) + 1):
        _l_(40575)

        if _n_(40547, "num", lambda: num) in _n_(40548, "amicables", lambda: amicables):
            _l_(40550)

            continue
            _l_(40549)
        sum_fact = _c_(40558, _n_(40551, "sum", lambda: sum), [_n_(40552, "fact", lambda: fact) for fact in _c_(40555, _n_(40553, "range", lambda: range), 1, _n_(40554, "num", lambda: num)) if _n_(40556, "num", lambda: num) % _n_(40557, "fact", lambda: fact) == 0])
        _l_(40559)
        if _n_(40560, "num", lambda: num) == _n_(40561, "sum_fact2", lambda: sum_fact2) and _n_(40562, "num", lambda: num) != _n_(40563, "sum_fact", lambda: sum_fact):
            _l_(40574)

            _c_(40567, _a_(40565, _n_(40564, "amicables", lambda: amicables), "add"), _n_(40566, "num", lambda: num))
            _l_(40568)
            _c_(40572, _a_(40570, _n_(40569, "amicables", lambda: amicables), "add"), _n_(40571, "sum_fact2", lambda: sum_fact2))
            _l_(40573)
    aux = _c_(40578, _n_(40576, "sum", lambda: sum), _n_(40577, "amicables", lambda: amicables))
    _l_(40579)
    return aux
_c_(40584, _n_(40581, "print", lambda: print), _c_(40583, _n_(40582, "amicable_numbers_sum", lambda: amicable_numbers_sum), 9999))
_l_(40585)
_c_(40589, _n_(40586, "print", lambda: print), _c_(40588, _n_(40587, "amicable_numbers_sum", lambda: amicable_numbers_sum), 999))
_l_(40590)
_c_(40594, _n_(40591, "print", lambda: print), _c_(40593, _n_(40592, "amicable_numbers_sum", lambda: amicable_numbers_sum), 99))
_l_(40595)