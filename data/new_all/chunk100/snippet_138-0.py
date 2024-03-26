# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(102140)

    arr_len = _c_(102103, _n_(102101, "len", lambda: len), _n_(102102, "arr", lambda: arr))
    _l_(102104)
    if _n_(102105, "arr_len", lambda: arr_len) < 2:
        _l_(102110)

        _c_(102107, _n_(102106, "print", lambda: print), 'No pairs exists')
        _l_(102108)
        aux = ""
        _l_(102109)
        return aux
    x = _n_(102111, "arr", lambda: arr)[0]
    _l_(102112)
    y = _n_(102113, "arr", lambda: arr)[1]
    _l_(102114)
    for i in _c_(102117, _n_(102115, "range", lambda: range), 0, _n_(102116, "arr_len", lambda: arr_len)):
        _l_(102136)

        for j in _c_(102121, _n_(102118, "range", lambda: range), _n_(102119, "i", lambda: i) + 1, _n_(102120, "arr_len", lambda: arr_len)):
            _l_(102135)

            if _n_(102122, "arr", lambda: arr)[_n_(102123, "i", lambda: i)] * _n_(102124, "arr", lambda: arr)[_n_(102125, "j", lambda: j)] > _n_(102126, "x", lambda: x) * _n_(102127, "y", lambda: y):
                _l_(102134)

                x = _n_(102128, "arr", lambda: arr)[_n_(102129, "i", lambda: i)]
                _l_(102130)
                y = _n_(102131, "arr", lambda: arr)[_n_(102132, "j", lambda: j)]
                _l_(102133)
    aux = (_n_(102137, "x", lambda: x), _n_(102138, "y", lambda: y))
    _l_(102139)
    return aux
_c_(102143, _n_(102141, "print", lambda: print), 'Original array:', _n_(102142, "nums", lambda: nums))
_l_(102144)
_c_(102149, _n_(102145, "print", lambda: print), 'Maximum product pair is:', _c_(102148, _n_(102146, "max_Product", lambda: max_Product), _n_(102147, "nums", lambda: nums)))
_l_(102150)
nums = [0, -1, -2, -4, 5, 0, -6]
_l_(102151)
_c_(102154, _n_(102152, "print", lambda: print), '\nOriginal array:', _n_(102153, "nums", lambda: nums))
_l_(102155)
_c_(102160, _n_(102156, "print", lambda: print), 'Maximum product pair is:', _c_(102159, _n_(102157, "max_Product", lambda: max_Product), _n_(102158, "nums", lambda: nums)))
_l_(102161)