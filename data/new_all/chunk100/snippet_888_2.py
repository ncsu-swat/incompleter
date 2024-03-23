# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
str1 = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
_l_(87359)
_c_(87362, _n_(87360, "print", lambda: print), 'Original string: ', _n_(87361, "str1", lambda: str1))
_l_(87363)
lenght = _c_(87366, _n_(87364, "len", lambda: len), _n_(87365, "str_num", lambda: str_num))
_l_(87367)
numbers = _c_(87376, _n_(87368, "sorted", lambda: sorted), [_c_(87371, _n_(87369, "int", lambda: int), _n_(87370, "x", lambda: x)) for x in _n_(87372, "str_num", lambda: str_num) if _c_(87375, _a_(87374, _n_(87373, "x", lambda: x), "isdigit"))])
_l_(87377)
_c_(87379, _n_(87378, "print", lambda: print), 'Numbers in sorted form:')
_l_(87380)
for i in _c_(87385, _n_(87381, "filter", lambda: filter), lambda x: _n_(87382, "x", lambda: x) > _n_(87383, "lenght", lambda: lenght), _n_(87384, "numbers", lambda: numbers)):
    _l_(87390)

    _c_(87388, _n_(87386, "print", lambda: print), _n_(87387, "i", lambda: i), end=' ')
    _l_(87389)