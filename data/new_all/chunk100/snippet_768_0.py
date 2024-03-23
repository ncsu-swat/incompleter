# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def shift_first_last(lst):
    _l_(77878)

    y = _c_(77861, _a_(77860, _n_(77859, "lst", lambda: lst), "pop"))
    _l_(77862)
    _c_(77866, _a_(77864, _n_(77863, "lst", lambda: lst), "insert"), 0, _n_(77865, "y", lambda: y))
    _l_(77867)
    _c_(77874, _a_(77869, _n_(77868, "lst", lambda: lst), "insert"), _c_(77872, _n_(77870, "len", lambda: len), _n_(77871, "lst", lambda: lst)), _n_(77873, "x", lambda: x))
    _l_(77875)
    aux = _n_(77876, "lst", lambda: lst)
    _l_(77877)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(77879)
_c_(77881, _n_(77880, "print", lambda: print), 'Original list:')
_l_(77882)
_c_(77885, _n_(77883, "print", lambda: print), _n_(77884, "nums", lambda: nums))
_l_(77886)
_c_(77888, _n_(77887, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(77889)
_c_(77894, _n_(77890, "print", lambda: print), _c_(77893, _n_(77891, "shift_first_last", lambda: shift_first_last), _n_(77892, "nums", lambda: nums)))
_l_(77895)
chars = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
_l_(77896)
_c_(77898, _n_(77897, "print", lambda: print), '\nOriginal list:')
_l_(77899)
_c_(77902, _n_(77900, "print", lambda: print), _n_(77901, "chars", lambda: chars))
_l_(77903)
_c_(77905, _n_(77904, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(77906)
_c_(77911, _n_(77907, "print", lambda: print), _c_(77910, _n_(77908, "shift_first_last", lambda: shift_first_last), _n_(77909, "chars", lambda: chars)))
_l_(77912)