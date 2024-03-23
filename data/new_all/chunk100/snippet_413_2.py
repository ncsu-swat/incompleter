# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def amicable_numbers_sum(limit):
    _l_(40714)

    if not _c_(40663, _n_(40660, "isinstance", lambda: isinstance), _n_(40661, "limit", lambda: limit), _n_(40662, "int", lambda: int)):
        _l_(40665)

        aux = 'Input is not an integer!'
        _l_(40664)
        return aux
    if _n_(40666, "limit", lambda: limit) < 1:
        _l_(40668)

        aux = 'Input must be bigger than 0!'
        _l_(40667)
        return aux
    for num in _c_(40671, _n_(40669, "range", lambda: range), 2, _n_(40670, "limit", lambda: limit) + 1):
        _l_(40709)

        if _n_(40672, "num", lambda: num) in _n_(40673, "amicables", lambda: amicables):
            _l_(40675)

            continue
            _l_(40674)
        sum_fact = _c_(40683, _n_(40676, "sum", lambda: sum), [_n_(40677, "fact", lambda: fact) for fact in _c_(40680, _n_(40678, "range", lambda: range), 1, _n_(40679, "num", lambda: num)) if _n_(40681, "num", lambda: num) % _n_(40682, "fact", lambda: fact) == 0])
        _l_(40684)
        sum_fact2 = _c_(40692, _n_(40685, "sum", lambda: sum), [_n_(40686, "fact", lambda: fact) for fact in _c_(40689, _n_(40687, "range", lambda: range), 1, _n_(40688, "sum_fact", lambda: sum_fact)) if _n_(40690, "sum_fact", lambda: sum_fact) % _n_(40691, "fact", lambda: fact) == 0])
        _l_(40693)
        if _n_(40694, "num", lambda: num) == _n_(40695, "sum_fact2", lambda: sum_fact2) and _n_(40696, "num", lambda: num) != _n_(40697, "sum_fact", lambda: sum_fact):
            _l_(40708)

            _c_(40701, _a_(40699, _n_(40698, "amicables", lambda: amicables), "add"), _n_(40700, "num", lambda: num))
            _l_(40702)
            _c_(40706, _a_(40704, _n_(40703, "amicables", lambda: amicables), "add"), _n_(40705, "sum_fact2", lambda: sum_fact2))
            _l_(40707)
    aux = _c_(40712, _n_(40710, "sum", lambda: sum), _n_(40711, "amicables", lambda: amicables))
    _l_(40713)
    return aux
_c_(40718, _n_(40715, "print", lambda: print), _c_(40717, _n_(40716, "amicable_numbers_sum", lambda: amicable_numbers_sum), 9999))
_l_(40719)
_c_(40723, _n_(40720, "print", lambda: print), _c_(40722, _n_(40721, "amicable_numbers_sum", lambda: amicable_numbers_sum), 999))
_l_(40724)
_c_(40728, _n_(40725, "print", lambda: print), _c_(40727, _n_(40726, "amicable_numbers_sum", lambda: amicable_numbers_sum), 99))
_l_(40729)