# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_Product(arr):
    _l_(9452)

    arr_len = _c_(9418, _n_(9416, "len", lambda: len), _n_(9417, "arr", lambda: arr))
    _l_(9419)
    if _n_(9420, "arr_len", lambda: arr_len) < 2:
        _l_(9425)

        _c_(9422, _n_(9421, "print", lambda: print), 'No pairs exists')
        _l_(9423)
        aux = ""
        _l_(9424)
        return aux
    x = _n_(9426, "arr", lambda: arr)[0]
    _l_(9427)
    y = _n_(9428, "arr", lambda: arr)[1]
    _l_(9429)
    for i in _c_(9432, _n_(9430, "range", lambda: range), 0, _n_(9431, "arr_len", lambda: arr_len)):
        _l_(9448)

        for j in _c_(9436, _n_(9433, "range", lambda: range), _n_(9434, "i", lambda: i) + 1, _n_(9435, "arr_len", lambda: arr_len)):
            _l_(9447)

            if _n_(9437, "arr", lambda: arr)[_n_(9438, "i", lambda: i)] * _n_(9439, "arr", lambda: arr)[_n_(9440, "j", lambda: j)] > _n_(9441, "x", lambda: x) * _n_(9442, "y", lambda: y):
                _l_(9446)

                y = _n_(9443, "arr", lambda: arr)[_n_(9444, "j", lambda: j)]
                _l_(9445)
    aux = (_n_(9449, "x", lambda: x), _n_(9450, "y", lambda: y))
    _l_(9451)
    return aux
nums = [1, 2, 3, 4, 7, 0, 8, 4]
_l_(9453)
_c_(9456, _n_(9454, "print", lambda: print), 'Original array:', _n_(9455, "nums", lambda: nums))
_l_(9457)
_c_(9462, _n_(9458, "print", lambda: print), 'Maximum product pair is:', _c_(9461, _n_(9459, "max_Product", lambda: max_Product), _n_(9460, "nums", lambda: nums)))
_l_(9463)
nums = [0, -1, -2, -4, 5, 0, -6]
_l_(9464)
_c_(9467, _n_(9465, "print", lambda: print), '\nOriginal array:', _n_(9466, "nums", lambda: nums))
_l_(9468)
_c_(9473, _n_(9469, "print", lambda: print), 'Maximum product pair is:', _c_(9472, _n_(9470, "max_Product", lambda: max_Product), _n_(9471, "nums", lambda: nums)))
_l_(9474)