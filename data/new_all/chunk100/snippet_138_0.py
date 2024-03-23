# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(9334)

    arr_len = _c_(9297, _n_(9295, "len", lambda: len), _n_(9296, "arr", lambda: arr))
    _l_(9298)
    if _n_(9299, "arr_len", lambda: arr_len) < 2:
        _l_(9304)

        _c_(9301, _n_(9300, "print", lambda: print), 'No pairs exists')
        _l_(9302)
        aux = ""
        _l_(9303)
        return aux
    x = _n_(9305, "arr", lambda: arr)[0]
    _l_(9306)
    y = _n_(9307, "arr", lambda: arr)[1]
    _l_(9308)
    for i in _c_(9311, _n_(9309, "range", lambda: range), 0, _n_(9310, "arr_len", lambda: arr_len)):
        _l_(9330)

        for j in _c_(9315, _n_(9312, "range", lambda: range), _n_(9313, "i", lambda: i) + 1, _n_(9314, "arr_len", lambda: arr_len)):
            _l_(9329)

            if _n_(9316, "arr", lambda: arr)[_n_(9317, "i", lambda: i)] * _n_(9318, "arr", lambda: arr)[_n_(9319, "j", lambda: j)] > _n_(9320, "x", lambda: x) * _n_(9321, "y", lambda: y):
                _l_(9328)

                x = _n_(9322, "arr", lambda: arr)[_n_(9323, "i", lambda: i)]
                _l_(9324)
                y = _n_(9325, "arr", lambda: arr)[_n_(9326, "j", lambda: j)]
                _l_(9327)
    aux = (_n_(9331, "x", lambda: x), _n_(9332, "y", lambda: y))
    _l_(9333)
    return aux
nums = [1, 2, 3, 4, 7, 0, 8, 4]
_l_(9335)
_c_(9338, _n_(9336, "print", lambda: print), 'Original array:', _n_(9337, "nums", lambda: nums))
_l_(9339)
_c_(9344, _n_(9340, "print", lambda: print), 'Maximum product pair is:', _c_(9343, _n_(9341, "max_Product", lambda: max_Product), _n_(9342, "nums", lambda: nums)))
_l_(9345)
_c_(9348, _n_(9346, "print", lambda: print), '\nOriginal array:', _n_(9347, "nums", lambda: nums))
_l_(9349)
_c_(9354, _n_(9350, "print", lambda: print), 'Maximum product pair is:', _c_(9353, _n_(9351, "max_Product", lambda: max_Product), _n_(9352, "nums", lambda: nums)))
_l_(9355)