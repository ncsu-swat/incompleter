# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def letter_combinations(digits):
    _l_(62890)

    if _n_(62867, "digits", lambda: digits) == '':
        _l_(62869)

        aux = []
        _l_(62868)
        return aux
    string_maps = {'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', '7': 'tuv', '8': 'wxy', '9': 'z'}
    _l_(62870)
    result = ['']
    _l_(62871)
    for num in _n_(62872, "digits", lambda: digits):
        _l_(62887)

        temp = []
        _l_(62873)
        for an in _n_(62874, "result", lambda: result):
            _l_(62884)

            for char in _n_(62875, "string_maps", lambda: string_maps)[_n_(62876, "num", lambda: num)]:
                _l_(62883)

                _c_(62881, _a_(62878, _n_(62877, "temp", lambda: temp), "append"), _n_(62879, "an", lambda: an) + _n_(62880, "char", lambda: char))
                _l_(62882)
        result = _n_(62885, "temp", lambda: temp)
        _l_(62886)
    aux = _n_(62888, "result", lambda: result)
    _l_(62889)
    return aux
_c_(62895, _n_(62891, "print", lambda: print), _c_(62894, _n_(62892, "letter_combinations", lambda: letter_combinations), _n_(62893, "digit_string", lambda: digit_string)))
_l_(62896)
digit_string = '29'
_l_(62897)
_c_(62902, _n_(62898, "print", lambda: print), _c_(62901, _n_(62899, "letter_combinations", lambda: letter_combinations), _n_(62900, "digit_string", lambda: digit_string)))
_l_(62903)