# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def shift_first_last(lst):
    _l_(77932)

    x = _c_(77915, _a_(77914, _n_(77913, "lst", lambda: lst), "pop"), 0)
    _l_(77916)
    _c_(77920, _a_(77918, _n_(77917, "lst", lambda: lst), "insert"), 0, _n_(77919, "y", lambda: y))
    _l_(77921)
    _c_(77928, _a_(77923, _n_(77922, "lst", lambda: lst), "insert"), _c_(77926, _n_(77924, "len", lambda: len), _n_(77925, "lst", lambda: lst)), _n_(77927, "x", lambda: x))
    _l_(77929)
    aux = _n_(77930, "lst", lambda: lst)
    _l_(77931)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(77933)
_c_(77935, _n_(77934, "print", lambda: print), 'Original list:')
_l_(77936)
_c_(77939, _n_(77937, "print", lambda: print), _n_(77938, "nums", lambda: nums))
_l_(77940)
_c_(77942, _n_(77941, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(77943)
_c_(77948, _n_(77944, "print", lambda: print), _c_(77947, _n_(77945, "shift_first_last", lambda: shift_first_last), _n_(77946, "nums", lambda: nums)))
_l_(77949)
chars = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
_l_(77950)
_c_(77952, _n_(77951, "print", lambda: print), '\nOriginal list:')
_l_(77953)
_c_(77956, _n_(77954, "print", lambda: print), _n_(77955, "chars", lambda: chars))
_l_(77957)
_c_(77959, _n_(77958, "print", lambda: print), 'Shift last element to first position and first element to last position of the said list:')
_l_(77960)
_c_(77965, _n_(77961, "print", lambda: print), _c_(77964, _n_(77962, "shift_first_last", lambda: shift_first_last), _n_(77963, "chars", lambda: chars)))
_l_(77966)