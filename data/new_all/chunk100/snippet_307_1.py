# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test_dsc(n):
    _l_(26325)

    aux = _c_(26323, _n_(26315, "int", lambda: int), _c_(26322, _a_(26316, '', "join"), _c_(26321, _n_(26317, "sorted", lambda: sorted), _c_(26320, _n_(26318, "str", lambda: str), _n_(26319, "n", lambda: n)), reverse=True)))
    _l_(26324)
    return aux

def test_asc(n):
    _l_(26338)

    aux = _c_(26336, _n_(26326, "int", lambda: int), _c_(26335, _a_(26327, '', "join"), _c_(26334, _n_(26328, "sorted", lambda: sorted), _c_(26333, _n_(26329, "list", lambda: list), _c_(26332, _n_(26330, "str", lambda: str), _n_(26331, "n", lambda: n)))))[::1])
    _l_(26337)
    return aux
_c_(26341, _n_(26339, "print", lambda: print), 'Original Number: ', _n_(26340, "n", lambda: n))
_l_(26342)
_c_(26347, _n_(26343, "print", lambda: print), 'Descending order of the said number: ', _c_(26346, _n_(26344, "test_dsc", lambda: test_dsc), _n_(26345, "n", lambda: n)))
_l_(26348)
_c_(26353, _n_(26349, "print", lambda: print), 'Ascending order of the said number: ', _c_(26352, _n_(26350, "test_asc", lambda: test_asc), _n_(26351, "n", lambda: n)))
_l_(26354)
n = 43750973
_l_(26355)
_c_(26358, _n_(26356, "print", lambda: print), '\nOriginal Number: ', _n_(26357, "n", lambda: n))
_l_(26359)
_c_(26364, _n_(26360, "print", lambda: print), 'Descending order of the said number: ', _c_(26363, _n_(26361, "test_dsc", lambda: test_dsc), _n_(26362, "n", lambda: n)))
_l_(26365)
_c_(26370, _n_(26366, "print", lambda: print), 'Ascending order of the said number: ', _c_(26369, _n_(26367, "test_asc", lambda: test_asc), _n_(26368, "n", lambda: n)))
_l_(26371)