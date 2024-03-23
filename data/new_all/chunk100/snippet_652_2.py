# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def delete_all_occurrences(str1, ch):
    _l_(67346)

    result = _c_(67342, _a_(67340, _n_(67339, "str1", lambda: str1), "replace"), _n_(67341, "ch", lambda: ch), '')
    _l_(67343)
    aux = _n_(67344, "result", lambda: result)
    _l_(67345)
    return aux
str_text = 'Delete all occurrences of a specified character in a given string'
_l_(67347)
_c_(67349, _n_(67348, "print", lambda: print), 'Original string:')
_l_(67350)
_c_(67353, _n_(67351, "print", lambda: print), _n_(67352, "str_text", lambda: str_text))
_l_(67354)
_c_(67356, _n_(67355, "print", lambda: print), '\nModified string:')
_l_(67357)
_c_(67363, _n_(67358, "print", lambda: print), _c_(67362, _n_(67359, "delete_all_occurrences", lambda: delete_all_occurrences), _n_(67360, "str_text", lambda: str_text), _n_(67361, "ch", lambda: ch)))
_l_(67364)