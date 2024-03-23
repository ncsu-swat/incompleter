# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def letter_combinations(digits):
    _l_(62962)

    if _n_(62941, "digits", lambda: digits) == '':
        _l_(62943)

        aux = []
        _l_(62942)
        return aux
    string_maps = {'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', '7': 'tuv', '8': 'wxy', '9': 'z'}
    _l_(62944)
    result = ['']
    _l_(62945)
    for num in _n_(62946, "digits", lambda: digits):
        _l_(62959)

        temp = []
        _l_(62947)
        for an in _n_(62948, "result", lambda: result):
            _l_(62958)

            for char in _n_(62949, "string_maps", lambda: string_maps)[_n_(62950, "num", lambda: num)]:
                _l_(62957)

                _c_(62955, _a_(62952, _n_(62951, "temp", lambda: temp), "append"), _n_(62953, "an", lambda: an) + _n_(62954, "char", lambda: char))
                _l_(62956)
    aux = _n_(62960, "result", lambda: result)
    _l_(62961)
    return aux
digit_string = '47'
_l_(62963)
_c_(62968, _n_(62964, "print", lambda: print), _c_(62967, _n_(62965, "letter_combinations", lambda: letter_combinations), _n_(62966, "digit_string", lambda: digit_string)))
_l_(62969)
digit_string = '29'
_l_(62970)
_c_(62975, _n_(62971, "print", lambda: print), _c_(62974, _n_(62972, "letter_combinations", lambda: letter_combinations), _n_(62973, "digit_string", lambda: digit_string)))
_l_(62976)