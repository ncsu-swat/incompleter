# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_string(str_list1, l):
    _l_(119462)

    result = _c_(119458, _n_(119450, "list", lambda: list), _c_(119457, _n_(119451, "filter", lambda: filter), lambda e: _c_(119454, _n_(119452, "len", lambda: len), _n_(119453, "e", lambda: e)) == _n_(119455, "l", lambda: l), _n_(119456, "str_list1", lambda: str_list1)))
    _l_(119459)
    aux = _n_(119460, "result", lambda: result)
    _l_(119461)
    return aux
_c_(119464, _n_(119463, "print", lambda: print), 'Original list:')
_l_(119465)
_c_(119468, _n_(119466, "print", lambda: print), _n_(119467, "str_list1", lambda: str_list1))
_l_(119469)
l = 8
_l_(119470)
_c_(119472, _n_(119471, "print", lambda: print), '\nlength of the string to extract:')
_l_(119473)
_c_(119476, _n_(119474, "print", lambda: print), _n_(119475, "l", lambda: l))
_l_(119477)
_c_(119479, _n_(119478, "print", lambda: print), '\nAfter extracting strings of specified length from the said list:')
_l_(119480)
_c_(119486, _n_(119481, "print", lambda: print), _c_(119485, _n_(119482, "extract_string", lambda: extract_string), _n_(119483, "str_list1", lambda: str_list1), _n_(119484, "l", lambda: l)))
_l_(119487)