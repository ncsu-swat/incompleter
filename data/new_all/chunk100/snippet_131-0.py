# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_difference(l1, l2):
    _l_(101742)

    result = _c_(101731, _n_(101729, "list", lambda: list), _n_(101730, "l1", lambda: l1))
    _l_(101732)
    for el in _n_(101733, "l2", lambda: l2):
        _l_(101739)

        _c_(101737, _a_(101735, _n_(101734, "result", lambda: result), "remove"), _n_(101736, "el", lambda: el))
        _l_(101738)
    aux = _n_(101740, "result", lambda: result)
    _l_(101741)
    return aux
l2 = [1, 1, 2, 4, 5, 6]
_l_(101743)
_c_(101745, _n_(101744, "print", lambda: print), 'Original lists:')
_l_(101746)
_c_(101749, _n_(101747, "print", lambda: print), _n_(101748, "l1", lambda: l1))
_l_(101750)
_c_(101753, _n_(101751, "print", lambda: print), _n_(101752, "l2", lambda: l2))
_l_(101754)
_c_(101756, _n_(101755, "print", lambda: print), '\nDifference between two said list including duplicate elements):')
_l_(101757)
_c_(101763, _n_(101758, "print", lambda: print), _c_(101762, _n_(101759, "list_difference", lambda: list_difference), _n_(101760, "l1", lambda: l1), _n_(101761, "l2", lambda: l2)))
_l_(101764)