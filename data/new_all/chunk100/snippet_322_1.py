# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cocktail_shaker_sort(nums):
    _l_(31145)

    for i in _c_(31100, _n_(31096, "range", lambda: range), _c_(31099, _n_(31097, "len", lambda: len), _n_(31098, "nums", lambda: nums)) - 1, 0, -1):
        _l_(31144)

        is_swapped = False
        _l_(31101)
        for j in _c_(31104, _n_(31102, "range", lambda: range), _n_(31103, "i", lambda: i), 0, -1):
            _l_(31120)

            if _n_(31105, "nums", lambda: nums)[_n_(31106, "j", lambda: j)] < _n_(31107, "nums", lambda: nums)[_n_(31108, "j", lambda: j) - 1]:
                _l_(31119)

                (_n_(31109, "nums", lambda: nums)[_n_(31110, "j", lambda: j)], _n_(31111, "nums", lambda: nums)[_n_(31112, "j", lambda: j) - 1]) = (_n_(31113, "nums", lambda: nums)[_n_(31114, "j", lambda: j) - 1], _n_(31115, "nums", lambda: nums)[_n_(31116, "j", lambda: j)])
                _l_(31117)
                is_swapped = True
                _l_(31118)
        for j in _c_(31123, _n_(31121, "range", lambda: range), _n_(31122, "i", lambda: i)):
            _l_(31139)

            if _n_(31124, "nums", lambda: nums)[_n_(31125, "j", lambda: j)] > _n_(31126, "nums", lambda: nums)[_n_(31127, "j", lambda: j) + 1]:
                _l_(31138)

                (_n_(31128, "nums", lambda: nums)[_n_(31129, "j", lambda: j)], _n_(31130, "nums", lambda: nums)[_n_(31131, "j", lambda: j) + 1]) = (_n_(31132, "nums", lambda: nums)[_n_(31133, "j", lambda: j) + 1], _n_(31134, "nums", lambda: nums)[_n_(31135, "j", lambda: j)])
                _l_(31136)
                is_swapped = True
                _l_(31137)
        if not _n_(31140, "is_swapped", lambda: is_swapped):
            _l_(31143)

            aux = _n_(31141, "nums", lambda: nums)
            _l_(31142)
            return aux
nums = [_c_(31148, _n_(31146, "int", lambda: int), _n_(31147, "item", lambda: item)) for item in _c_(31151, _a_(31150, _n_(31149, "num1", lambda: num1), "split"), ',')]
_l_(31152)
_c_(31157, _n_(31153, "print", lambda: print), _c_(31156, _n_(31154, "cocktail_shaker_sort", lambda: cocktail_shaker_sort), _n_(31155, "nums", lambda: nums)))
_l_(31158)