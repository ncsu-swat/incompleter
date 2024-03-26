# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_last_n(nums, N):
    _l_(102793)

    result = _n_(102785, "nums", lambda: nums)[:_c_(102788, _n_(102786, "len", lambda: len), _n_(102787, "nums", lambda: nums)) - _n_(102789, "N", lambda: N)]
    _l_(102790)
    aux = _n_(102791, "result", lambda: result)
    _l_(102792)
    return aux
_c_(102795, _n_(102794, "print", lambda: print), 'Original lists:')
_l_(102796)
_c_(102799, _n_(102797, "print", lambda: print), _n_(102798, "nums", lambda: nums))
_l_(102800)
N = 3
_l_(102801)
_c_(102804, _n_(102802, "print", lambda: print), '\nRemove the last', _n_(102803, "N", lambda: N), 'elements from the said list:')
_l_(102805)
_c_(102811, _n_(102806, "print", lambda: print), _c_(102810, _n_(102807, "remove_last_n", lambda: remove_last_n), _n_(102808, "nums", lambda: nums), _n_(102809, "N", lambda: N)))
_l_(102812)
N = 5
_l_(102813)
_c_(102816, _n_(102814, "print", lambda: print), '\nRemove the last', _n_(102815, "N", lambda: N), 'elements from the said list:')
_l_(102817)
_c_(102823, _n_(102818, "print", lambda: print), _c_(102822, _n_(102819, "remove_last_n", lambda: remove_last_n), _n_(102820, "nums", lambda: nums), _n_(102821, "N", lambda: N)))
_l_(102824)
N = 1
_l_(102825)
_c_(102828, _n_(102826, "print", lambda: print), '\nRemove the last', _n_(102827, "N", lambda: N), 'element from the said list:')
_l_(102829)
_c_(102835, _n_(102830, "print", lambda: print), _c_(102834, _n_(102831, "remove_last_n", lambda: remove_last_n), _n_(102832, "nums", lambda: nums), _n_(102833, "N", lambda: N)))
_l_(102836)