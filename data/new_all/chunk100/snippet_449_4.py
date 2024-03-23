# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, value):
    _l_(48116)

    result = [_n_(48107, "i", lambda: i) for (i, val) in _c_(48110, _n_(48108, "enumerate", lambda: enumerate), _n_(48109, "lst", lambda: lst)) if _n_(48111, "val", lambda: val) > _n_(48112, "value", lambda: value)]
    _l_(48113)
    aux = _n_(48114, "result", lambda: result)
    _l_(48115)
    return aux
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
_l_(48117)
_c_(48119, _n_(48118, "print", lambda: print), '\nOriginal list:')
_l_(48120)
_c_(48123, _n_(48121, "print", lambda: print), _n_(48122, "nums", lambda: nums))
_l_(48124)
val = 3000
_l_(48125)
_c_(48128, _n_(48126, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(48127, "val", lambda: val))
_l_(48129)
_c_(48135, _n_(48130, "print", lambda: print), _c_(48134, _n_(48131, "test", lambda: test), _n_(48132, "nums", lambda: nums), _n_(48133, "val", lambda: val)))
_l_(48136)
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
_l_(48137)
_c_(48139, _n_(48138, "print", lambda: print), '\nOriginal list:')
_l_(48140)
_c_(48143, _n_(48141, "print", lambda: print), _n_(48142, "nums", lambda: nums))
_l_(48144)
_c_(48147, _n_(48145, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(48146, "val", lambda: val))
_l_(48148)
_c_(48154, _n_(48149, "print", lambda: print), _c_(48153, _n_(48150, "test", lambda: test), _n_(48151, "nums", lambda: nums), _n_(48152, "val", lambda: val)))
_l_(48155)