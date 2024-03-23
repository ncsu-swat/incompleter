# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
str1 = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
_l_(87326)
_c_(87329, _n_(87327, "print", lambda: print), 'Original string: ', _n_(87328, "str1", lambda: str1))
_l_(87330)
str_num = [_n_(87331, "i", lambda: i) for i in _c_(87334, _a_(87333, _n_(87332, "str1", lambda: str1), "split"), ' ')]
_l_(87335)
numbers = _c_(87344, _n_(87336, "sorted", lambda: sorted), [_c_(87339, _n_(87337, "int", lambda: int), _n_(87338, "x", lambda: x)) for x in _n_(87340, "str_num", lambda: str_num) if _c_(87343, _a_(87342, _n_(87341, "x", lambda: x), "isdigit"))])
_l_(87345)
_c_(87347, _n_(87346, "print", lambda: print), 'Numbers in sorted form:')
_l_(87348)
for i in _c_(87353, _n_(87349, "filter", lambda: filter), lambda x: _n_(87350, "x", lambda: x) > _n_(87351, "lenght", lambda: lenght), _n_(87352, "numbers", lambda: numbers)):
    _l_(87358)

    _c_(87356, _n_(87354, "print", lambda: print), _n_(87355, "i", lambda: i), end=' ')
    _l_(87357)