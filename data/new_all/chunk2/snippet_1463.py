# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55722527/typeerror-cannot-use-a-bytes-pattern-on-a-string-like-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(434386)

except ImportError:
    pass
_WORD_SPLIT = _c_(434389, _a_(434388, _n_(434387, "re", lambda: re), "compile"), b"([.,!?\"':;)(])")
_l_(434390)

def basic_tokenizer(sentence):
    _l_(434410)

    words = []
    _l_(434391)
    for space_separated_fragment in _c_(434396, _a_(434395, _c_(434394, _a_(434393, _n_(434392, "sentence", lambda: sentence), "strip")), "split")):
        _l_(434405)

        _c_(434403, _a_(434398, _n_(434397, "words", lambda: words), "extend"), _c_(434402, _a_(434400, _n_(434399, "_WORD_SPLIT", lambda: _WORD_SPLIT), "split"), _n_(434401, "space_separated_fragment", lambda: space_separated_fragment)))
        _l_(434404)
    aux = [_n_(434406, "w", lambda: w) for w in _n_(434407, "words", lambda: words) if _n_(434408, "w", lambda: w)]
    _l_(434409)
    return aux

_c_(434412, _n_(434411, "basic_tokenizer", lambda: basic_tokenizer), "I live, in Mumbai.")
_l_(434413)