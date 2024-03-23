# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def delete_all_occurrences(str1, ch):
    _l_(67298)

    result = _c_(67294, _a_(67292, _n_(67291, "str1", lambda: str1), "replace"), _n_(67293, "ch", lambda: ch), '')
    _l_(67295)
    aux = _n_(67296, "result", lambda: result)
    _l_(67297)
    return aux
_c_(67300, _n_(67299, "print", lambda: print), 'Original string:')
_l_(67301)
_c_(67304, _n_(67302, "print", lambda: print), _n_(67303, "str_text", lambda: str_text))
_l_(67305)
_c_(67307, _n_(67306, "print", lambda: print), '\nModified string:')
_l_(67308)
ch = 'a'
_l_(67309)
_c_(67315, _n_(67310, "print", lambda: print), _c_(67314, _n_(67311, "delete_all_occurrences", lambda: delete_all_occurrences), _n_(67312, "str_text", lambda: str_text), _n_(67313, "ch", lambda: ch)))
_l_(67316)