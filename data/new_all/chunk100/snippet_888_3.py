# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
str1 = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
_l_(87391)
_c_(87394, _n_(87392, "print", lambda: print), 'Original string: ', _n_(87393, "str1", lambda: str1))
_l_(87395)
str_num = [_n_(87396, "i", lambda: i) for i in _c_(87399, _a_(87398, _n_(87397, "str1", lambda: str1), "split"), ' ')]
_l_(87400)
lenght = _c_(87403, _n_(87401, "len", lambda: len), _n_(87402, "str_num", lambda: str_num))
_l_(87404)
_c_(87406, _n_(87405, "print", lambda: print), 'Numbers in sorted form:')
_l_(87407)
for i in _c_(87412, _n_(87408, "filter", lambda: filter), lambda x: _n_(87409, "x", lambda: x) > _n_(87410, "lenght", lambda: lenght), _n_(87411, "numbers", lambda: numbers)):
    _l_(87417)

    _c_(87415, _n_(87413, "print", lambda: print), _n_(87414, "i", lambda: i), end=' ')
    _l_(87416)