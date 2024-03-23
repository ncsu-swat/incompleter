# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import islice
    _l_(96136)

except ImportError:
    pass

def split_list(lst, n):
    _l_(96154)

    lst = _c_(96139, _n_(96137, "iter", lambda: iter), _n_(96138, "lst", lambda: lst))
    _l_(96140)
    result = _c_(96148, _n_(96141, "iter", lambda: iter), lambda : _c_(96147, _n_(96142, "tuple", lambda: tuple), _c_(96146, _n_(96143, "islice", lambda: islice), _n_(96144, "lst", lambda: lst), _n_(96145, "n", lambda: n))), ())
    _l_(96149)
    aux = _c_(96152, _n_(96150, "list", lambda: list), _n_(96151, "result", lambda: result))
    _l_(96153)
    return aux
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
_l_(96155)
_c_(96157, _n_(96156, "print", lambda: print), 'Original list:')
_l_(96158)
_c_(96161, _n_(96159, "print", lambda: print), _n_(96160, "nums", lambda: nums))
_l_(96162)
n = 3
_l_(96163)
_c_(96166, _n_(96164, "print", lambda: print), '\nSplit the said list into equal size', _n_(96165, "n", lambda: n))
_l_(96167)
_c_(96173, _n_(96168, "print", lambda: print), _c_(96172, _n_(96169, "split_list", lambda: split_list), _n_(96170, "nums", lambda: nums), _n_(96171, "n", lambda: n)))
_l_(96174)
_c_(96177, _n_(96175, "print", lambda: print), '\nSplit the said list into equal size', _n_(96176, "n", lambda: n))
_l_(96178)
_c_(96184, _n_(96179, "print", lambda: print), _c_(96183, _n_(96180, "split_list", lambda: split_list), _n_(96181, "nums", lambda: nums), _n_(96182, "n", lambda: n)))
_l_(96185)
n = 5
_l_(96186)
_c_(96189, _n_(96187, "print", lambda: print), '\nSplit the said list into equal size', _n_(96188, "n", lambda: n))
_l_(96190)
_c_(96196, _n_(96191, "print", lambda: print), _c_(96195, _n_(96192, "split_list", lambda: split_list), _n_(96193, "nums", lambda: nums), _n_(96194, "n", lambda: n)))
_l_(96197)