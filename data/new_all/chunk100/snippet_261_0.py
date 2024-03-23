# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_substring(str1, sub_str):
    _l_(21195)

    result = _c_(21191, _n_(21185, "list", lambda: list), _c_(21190, _n_(21186, "filter", lambda: filter), lambda x: _n_(21187, "sub_str", lambda: sub_str) in _n_(21188, "x", lambda: x), _n_(21189, "str1", lambda: str1)))
    _l_(21192)
    aux = _n_(21193, "result", lambda: result)
    _l_(21194)
    return aux
colors = ['red', 'black', 'white', 'green', 'orange']
_l_(21196)
_c_(21198, _n_(21197, "print", lambda: print), 'Original list:')
_l_(21199)
_c_(21202, _n_(21200, "print", lambda: print), _n_(21201, "colors", lambda: colors))
_l_(21203)
sub_str = 'ack'
_l_(21204)
_c_(21206, _n_(21205, "print", lambda: print), '\nSubstring to search:')
_l_(21207)
_c_(21210, _n_(21208, "print", lambda: print), _n_(21209, "sub_str", lambda: sub_str))
_l_(21211)
_c_(21213, _n_(21212, "print", lambda: print), 'Elements of the said list that contain specific substring:')
_l_(21214)
_c_(21220, _n_(21215, "print", lambda: print), _c_(21219, _n_(21216, "find_substring", lambda: find_substring), _n_(21217, "colors", lambda: colors), _n_(21218, "sub_str", lambda: sub_str)))
_l_(21221)
_c_(21223, _n_(21222, "print", lambda: print), '\nSubstring to search:')
_l_(21224)
_c_(21227, _n_(21225, "print", lambda: print), _n_(21226, "sub_str", lambda: sub_str))
_l_(21228)
_c_(21230, _n_(21229, "print", lambda: print), 'Elements of the said list that contain specific substring:')
_l_(21231)
_c_(21237, _n_(21232, "print", lambda: print), _c_(21236, _n_(21233, "find_substring", lambda: find_substring), _n_(21234, "colors", lambda: colors), _n_(21235, "sub_str", lambda: sub_str)))
_l_(21238)