# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cocktail_shaker_sort(nums):
    _l_(110551)

    for i in _c_(110506, _n_(110502, "range", lambda: range), _c_(110505, _n_(110503, "len", lambda: len), _n_(110504, "nums", lambda: nums)) - 1, 0, -1):
        _l_(110550)

        is_swapped = False
        _l_(110507)
        for j in _c_(110510, _n_(110508, "range", lambda: range), _n_(110509, "i", lambda: i), 0, -1):
            _l_(110526)

            if _n_(110511, "nums", lambda: nums)[_n_(110512, "j", lambda: j)] < _n_(110513, "nums", lambda: nums)[_n_(110514, "j", lambda: j) - 1]:
                _l_(110525)

                _n_(110515, "nums", lambda: nums)[_n_(110516, "j", lambda: j)], _n_(110517, "nums", lambda: nums)[_n_(110518, "j", lambda: j) - 1] = (_n_(110519, "nums", lambda: nums)[_n_(110520, "j", lambda: j) - 1], _n_(110521, "nums", lambda: nums)[_n_(110522, "j", lambda: j)])
                _l_(110523)
                is_swapped = True
                _l_(110524)
        for j in _c_(110529, _n_(110527, "range", lambda: range), _n_(110528, "i", lambda: i)):
            _l_(110545)

            if _n_(110530, "nums", lambda: nums)[_n_(110531, "j", lambda: j)] > _n_(110532, "nums", lambda: nums)[_n_(110533, "j", lambda: j) + 1]:
                _l_(110544)

                _n_(110534, "nums", lambda: nums)[_n_(110535, "j", lambda: j)], _n_(110536, "nums", lambda: nums)[_n_(110537, "j", lambda: j) + 1] = (_n_(110538, "nums", lambda: nums)[_n_(110539, "j", lambda: j) + 1], _n_(110540, "nums", lambda: nums)[_n_(110541, "j", lambda: j)])
                _l_(110542)
                is_swapped = True
                _l_(110543)
        if not _n_(110546, "is_swapped", lambda: is_swapped):
            _l_(110549)

            aux = _n_(110547, "nums", lambda: nums)
            _l_(110548)
            return aux
nums = [_c_(110554, _n_(110552, "int", lambda: int), _n_(110553, "item", lambda: item)) for item in _c_(110557, _a_(110556, _n_(110555, "num1", lambda: num1), "split"), ',')]
_l_(110558)
_c_(110563, _n_(110559, "print", lambda: print), _c_(110562, _n_(110560, "cocktail_shaker_sort", lambda: cocktail_shaker_sort), _n_(110561, "nums", lambda: nums)))
_l_(110564)