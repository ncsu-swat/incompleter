# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
word_list = _c_(48365, _a_(48364, _n_(48363, "string_words", lambda: string_words), "split"))
_l_(48366)
word_freq = [_c_(48370, _a_(48368, _n_(48367, "word_list", lambda: word_list), "count"), _n_(48369, "n", lambda: n)) for n in _n_(48371, "word_list", lambda: word_list)]
_l_(48372)
_c_(48377, _n_(48373, "print", lambda: print), _c_(48376, _a_(48374, 'String:\n {} \n', "format"), _n_(48375, "string_words", lambda: string_words)))
_l_(48378)
_c_(48385, _n_(48379, "print", lambda: print), _c_(48384, _a_(48380, 'List:\n {} \n', "format"), _c_(48383, _n_(48381, "str", lambda: str), _n_(48382, "word_list", lambda: word_list))))
_l_(48386)
_c_(48398, _n_(48387, "print", lambda: print), _c_(48397, _a_(48388, 'Pairs (Words and Frequencies:\n {}', "format"), _c_(48396, _n_(48389, "str", lambda: str), _c_(48395, _n_(48390, "list", lambda: list), _c_(48394, _n_(48391, "zip", lambda: zip), _n_(48392, "word_list", lambda: word_list), _n_(48393, "word_freq", lambda: word_freq))))))
_l_(48399)