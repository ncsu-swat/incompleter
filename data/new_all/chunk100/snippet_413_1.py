# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def amicable_numbers_sum(limit):
    _l_(40644)

    if not _c_(40599, _n_(40596, "isinstance", lambda: isinstance), _n_(40597, "limit", lambda: limit), _n_(40598, "int", lambda: int)):
        _l_(40601)

        aux = 'Input is not an integer!'
        _l_(40600)
        return aux
    if _n_(40602, "limit", lambda: limit) < 1:
        _l_(40604)

        aux = 'Input must be bigger than 0!'
        _l_(40603)
        return aux
    amicables = _c_(40606, _n_(40605, "set", lambda: set))
    _l_(40607)
    for num in _c_(40610, _n_(40608, "range", lambda: range), 2, _n_(40609, "limit", lambda: limit) + 1):
        _l_(40639)

        if _n_(40611, "num", lambda: num) in _n_(40612, "amicables", lambda: amicables):
            _l_(40614)

            continue
            _l_(40613)
        sum_fact2 = _c_(40622, _n_(40615, "sum", lambda: sum), [_n_(40616, "fact", lambda: fact) for fact in _c_(40619, _n_(40617, "range", lambda: range), 1, _n_(40618, "sum_fact", lambda: sum_fact)) if _n_(40620, "sum_fact", lambda: sum_fact) % _n_(40621, "fact", lambda: fact) == 0])
        _l_(40623)
        if _n_(40624, "num", lambda: num) == _n_(40625, "sum_fact2", lambda: sum_fact2) and _n_(40626, "num", lambda: num) != _n_(40627, "sum_fact", lambda: sum_fact):
            _l_(40638)

            _c_(40631, _a_(40629, _n_(40628, "amicables", lambda: amicables), "add"), _n_(40630, "num", lambda: num))
            _l_(40632)
            _c_(40636, _a_(40634, _n_(40633, "amicables", lambda: amicables), "add"), _n_(40635, "sum_fact2", lambda: sum_fact2))
            _l_(40637)
    aux = _c_(40642, _n_(40640, "sum", lambda: sum), _n_(40641, "amicables", lambda: amicables))
    _l_(40643)
    return aux
_c_(40648, _n_(40645, "print", lambda: print), _c_(40647, _n_(40646, "amicable_numbers_sum", lambda: amicable_numbers_sum), 9999))
_l_(40649)
_c_(40653, _n_(40650, "print", lambda: print), _c_(40652, _n_(40651, "amicable_numbers_sum", lambda: amicable_numbers_sum), 999))
_l_(40654)
_c_(40658, _n_(40655, "print", lambda: print), _c_(40657, _n_(40656, "amicable_numbers_sum", lambda: amicable_numbers_sum), 99))
_l_(40659)