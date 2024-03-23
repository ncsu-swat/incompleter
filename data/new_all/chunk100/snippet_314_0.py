# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(29527)

except ImportError:
    pass

def plusMinus(nums):
    _l_(29555)

    n = _c_(29530, _n_(29528, "len", lambda: len), _n_(29529, "nums", lambda: nums))
    _l_(29531)
    n1 = n2 = n3 = 0
    _l_(29532)
    for x in _n_(29533, "nums", lambda: nums):
        _l_(29541)

        if _n_(29534, "x", lambda: x) > 0:
            _l_(29540)

            n1 += 1
            _l_(29535)
        elif _n_(29536, "x", lambda: x) < 0:
            _l_(29539)

            n2 += 1
            _l_(29537)
        else:
            n3 += 1
            _l_(29538)
    aux = (_c_(29545, _n_(29542, "round", lambda: round), _n_(29543, "n1", lambda: n1) / _n_(29544, "n", lambda: n), 2), _c_(29549, _n_(29546, "round", lambda: round), _n_(29547, "n2", lambda: n2) / _n_(29548, "n", lambda: n), 2), _c_(29553, _n_(29550, "round", lambda: round), _n_(29551, "n3", lambda: n3) / _n_(29552, "n", lambda: n), 2))
    _l_(29554)
    return aux
_c_(29558, _n_(29556, "print", lambda: print), 'Original array:', _n_(29557, "nums", lambda: nums))
_l_(29559)
nums_arr = _c_(29565, _n_(29560, "list", lambda: list), _c_(29564, _n_(29561, "map", lambda: map), _n_(29562, "int", lambda: int), _n_(29563, "nums", lambda: nums)))
_l_(29566)
result = _c_(29569, _n_(29567, "plusMinus", lambda: plusMinus), _n_(29568, "nums_arr", lambda: nums_arr))
_l_(29570)
_c_(29572, _n_(29571, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29573)
_c_(29576, _n_(29574, "print", lambda: print), _n_(29575, "result", lambda: result))
_l_(29577)
nums = _c_(29579, _n_(29578, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(29580)
_c_(29583, _n_(29581, "print", lambda: print), '\nOriginal array:', _n_(29582, "nums", lambda: nums))
_l_(29584)
nums_arr = _c_(29590, _n_(29585, "list", lambda: list), _c_(29589, _n_(29586, "map", lambda: map), _n_(29587, "int", lambda: int), _n_(29588, "nums", lambda: nums)))
_l_(29591)
result = _c_(29594, _n_(29592, "plusMinus", lambda: plusMinus), _n_(29593, "nums_arr", lambda: nums_arr))
_l_(29595)
_c_(29597, _n_(29596, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29598)
_c_(29601, _n_(29599, "print", lambda: print), _n_(29600, "result", lambda: result))
_l_(29602)