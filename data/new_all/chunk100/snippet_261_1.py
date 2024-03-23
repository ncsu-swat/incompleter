# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_substring(str1, sub_str):
    _l_(21249)

    result = _c_(21245, _n_(21239, "list", lambda: list), _c_(21244, _n_(21240, "filter", lambda: filter), lambda x: _n_(21241, "sub_str", lambda: sub_str) in _n_(21242, "x", lambda: x), _n_(21243, "str1", lambda: str1)))
    _l_(21246)
    aux = _n_(21247, "result", lambda: result)
    _l_(21248)
    return aux
colors = ['red', 'black', 'white', 'green', 'orange']
_l_(21250)
_c_(21252, _n_(21251, "print", lambda: print), 'Original list:')
_l_(21253)
_c_(21256, _n_(21254, "print", lambda: print), _n_(21255, "colors", lambda: colors))
_l_(21257)
_c_(21259, _n_(21258, "print", lambda: print), '\nSubstring to search:')
_l_(21260)
_c_(21263, _n_(21261, "print", lambda: print), _n_(21262, "sub_str", lambda: sub_str))
_l_(21264)
_c_(21266, _n_(21265, "print", lambda: print), 'Elements of the said list that contain specific substring:')
_l_(21267)
_c_(21273, _n_(21268, "print", lambda: print), _c_(21272, _n_(21269, "find_substring", lambda: find_substring), _n_(21270, "colors", lambda: colors), _n_(21271, "sub_str", lambda: sub_str)))
_l_(21274)
sub_str = 'abc'
_l_(21275)
_c_(21277, _n_(21276, "print", lambda: print), '\nSubstring to search:')
_l_(21278)
_c_(21281, _n_(21279, "print", lambda: print), _n_(21280, "sub_str", lambda: sub_str))
_l_(21282)
_c_(21284, _n_(21283, "print", lambda: print), 'Elements of the said list that contain specific substring:')
_l_(21285)
_c_(21291, _n_(21286, "print", lambda: print), _c_(21290, _n_(21287, "find_substring", lambda: find_substring), _n_(21288, "colors", lambda: colors), _n_(21289, "sub_str", lambda: sub_str)))
_l_(21292)