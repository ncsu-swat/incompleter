# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57788626/typeerror-object-of-type-type-has-no-len-linear-search-on-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def linearSearch(list, targetValue):
    _l_(367281)

    for i in _c_(367272, _n_(367268, "range", lambda: range), 0, _c_(367271, _n_(367269, "len", lambda: len), _n_(367270, "list", lambda: list))):
        _l_(367279)

        if _n_(367273, "list", lambda: list)[_n_(367274, "i", lambda: i)] == _n_(367275, "targetValue", lambda: targetValue):
            _l_(367278)

            aux = _n_(367276, "i", lambda: i) #function stops
            _l_(367277) #function stops
            return aux #function stops
    aux = -1
    _l_(367280)

    return aux

# MAIN

myList = [3, 2, 8, 1, 10]
_l_(367282)

location = _c_(367285, _n_(367283, "linearSearch", lambda: linearSearch), _n_(367284, "list", lambda: list), 3)
_l_(367286)
_c_(367289, _n_(367287, "print", lambda: print), _n_(367288, "location", lambda: location))
_l_(367290)