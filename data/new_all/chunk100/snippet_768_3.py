# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def shift_first_last(lst):
    _l_(78044)

    x = _c_(78023, _a_(78022, _n_(78021, "lst", lambda: lst), "pop"), 0)
    _l_(78024)
    y = _c_(78027, _a_(78026, _n_(78025, "lst", lambda: lst), "pop"))
    _l_(78028)
    _c_(78032, _a_(78030, _n_(78029, "lst", lambda: lst), "insert"), 0, _n_(78031, "y", lambda: y))
    _l_(78033)
    _c_(78040, _a_(78035, _n_(78034, "lst", lambda: lst), "insert"), _c_(78038, _n_(78036, "len", lambda: len), _n_(78037, "lst", lambda: lst)), _n_(78039, "x", lambda: x))
    _l_(78041)
    aux = _n_(78042, "lst", lambda: lst)
    _l_(78043)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(78045)
_c_(78047, _n_(78046, "print", lambda: print), 'Original list:')
_l_(78048)
_c_(78051, _n_(78049, "print", lambda: print), _n_(78050, "nums", lambda: nums))
_l_(78052)
_c_(78054, _n_(78053, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(78055)
_c_(78060, _n_(78056, "print", lambda: print), _c_(78059, _n_(78057, "shift_first_last", lambda: shift_first_last), _n_(78058, "nums", lambda: nums)))
_l_(78061)
_c_(78063, _n_(78062, "print", lambda: print), '\nOriginal list:')
_l_(78064)
_c_(78067, _n_(78065, "print", lambda: print), _n_(78066, "chars", lambda: chars))
_l_(78068)
_c_(78070, _n_(78069, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(78071)
_c_(78076, _n_(78072, "print", lambda: print), _c_(78075, _n_(78073, "shift_first_last", lambda: shift_first_last), _n_(78074, "chars", lambda: chars)))
_l_(78077)