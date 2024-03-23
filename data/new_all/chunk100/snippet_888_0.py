# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(87292, _n_(87290, "print", lambda: print), 'Original string: ', _n_(87291, "str1", lambda: str1))
_l_(87293)
str_num = [_n_(87294, "i", lambda: i) for i in _c_(87297, _a_(87296, _n_(87295, "str1", lambda: str1), "split"), ' ')]
_l_(87298)
lenght = _c_(87301, _n_(87299, "len", lambda: len), _n_(87300, "str_num", lambda: str_num))
_l_(87302)
numbers = _c_(87311, _n_(87303, "sorted", lambda: sorted), [_c_(87306, _n_(87304, "int", lambda: int), _n_(87305, "x", lambda: x)) for x in _n_(87307, "str_num", lambda: str_num) if _c_(87310, _a_(87309, _n_(87308, "x", lambda: x), "isdigit"))])
_l_(87312)
_c_(87314, _n_(87313, "print", lambda: print), 'Numbers in sorted form:')
_l_(87315)
for i in _c_(87320, _n_(87316, "filter", lambda: filter), lambda x: _n_(87317, "x", lambda: x) > _n_(87318, "lenght", lambda: lenght), _n_(87319, "numbers", lambda: numbers)):
    _l_(87325)

    _c_(87323, _n_(87321, "print", lambda: print), _n_(87322, "i", lambda: i), end=' ')
    _l_(87324)