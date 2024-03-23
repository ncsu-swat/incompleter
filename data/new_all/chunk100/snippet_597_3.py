# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def letter_combinations(digits):
    _l_(63000)

    if _n_(62977, "digits", lambda: digits) == '':
        _l_(62979)

        aux = []
        _l_(62978)
        return aux
    string_maps = {'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', '7': 'tuv', '8': 'wxy', '9': 'z'}
    _l_(62980)
    result = ['']
    _l_(62981)
    for num in _n_(62982, "digits", lambda: digits):
        _l_(62997)

        temp = []
        _l_(62983)
        for an in _n_(62984, "result", lambda: result):
            _l_(62994)

            for char in _n_(62985, "string_maps", lambda: string_maps)[_n_(62986, "num", lambda: num)]:
                _l_(62993)

                _c_(62991, _a_(62988, _n_(62987, "temp", lambda: temp), "append"), _n_(62989, "an", lambda: an) + _n_(62990, "char", lambda: char))
                _l_(62992)
        result = _n_(62995, "temp", lambda: temp)
        _l_(62996)
    aux = _n_(62998, "result", lambda: result)
    _l_(62999)
    return aux
digit_string = '47'
_l_(63001)
_c_(63006, _n_(63002, "print", lambda: print), _c_(63005, _n_(63003, "letter_combinations", lambda: letter_combinations), _n_(63004, "digit_string", lambda: digit_string)))
_l_(63007)
_c_(63012, _n_(63008, "print", lambda: print), _c_(63011, _n_(63009, "letter_combinations", lambda: letter_combinations), _n_(63010, "digit_string", lambda: digit_string)))
_l_(63013)