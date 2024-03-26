# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_substring(str1, sub_str):
    _l_(107553)

    result = _c_(107549, _n_(107543, "list", lambda: list), _c_(107548, _n_(107544, "filter", lambda: filter), lambda x: _n_(107545, "sub_str", lambda: sub_str) in _n_(107546, "x", lambda: x), _n_(107547, "str1", lambda: str1)))
    _l_(107550)
    aux = _n_(107551, "result", lambda: result)
    _l_(107552)
    return aux
_c_(107555, _n_(107554, "print", lambda: print), 'Original list:')
_l_(107556)
_c_(107559, _n_(107557, "print", lambda: print), _n_(107558, "colors", lambda: colors))
_l_(107560)
sub_str = 'ack'
_l_(107561)
_c_(107563, _n_(107562, "print", lambda: print), '\nSubstring to search:')
_l_(107564)
_c_(107567, _n_(107565, "print", lambda: print), _n_(107566, "sub_str", lambda: sub_str))
_l_(107568)
_c_(107570, _n_(107569, "print", lambda: print), 'Elements of the said list that contain specific substring:')
_l_(107571)
_c_(107577, _n_(107572, "print", lambda: print), _c_(107576, _n_(107573, "find_substring", lambda: find_substring), _n_(107574, "colors", lambda: colors), _n_(107575, "sub_str", lambda: sub_str)))
_l_(107578)
sub_str = 'abc'
_l_(107579)
_c_(107581, _n_(107580, "print", lambda: print), '\nSubstring to search:')
_l_(107582)
_c_(107585, _n_(107583, "print", lambda: print), _n_(107584, "sub_str", lambda: sub_str))
_l_(107586)
_c_(107588, _n_(107587, "print", lambda: print), 'Elements of the said list that contain specific substring:')
_l_(107589)
_c_(107595, _n_(107590, "print", lambda: print), _c_(107594, _n_(107591, "find_substring", lambda: find_substring), _n_(107592, "colors", lambda: colors), _n_(107593, "sub_str", lambda: sub_str)))
_l_(107596)