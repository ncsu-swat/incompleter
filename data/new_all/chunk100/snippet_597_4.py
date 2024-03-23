# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def letter_combinations(digits):
    _l_(63036)

    if _n_(63014, "digits", lambda: digits) == '':
        _l_(63016)

        aux = []
        _l_(63015)
        return aux
    string_maps = {'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', '7': 'tuv', '8': 'wxy', '9': 'z'}
    _l_(63017)
    for num in _n_(63018, "digits", lambda: digits):
        _l_(63033)

        temp = []
        _l_(63019)
        for an in _n_(63020, "result", lambda: result):
            _l_(63030)

            for char in _n_(63021, "string_maps", lambda: string_maps)[_n_(63022, "num", lambda: num)]:
                _l_(63029)

                _c_(63027, _a_(63024, _n_(63023, "temp", lambda: temp), "append"), _n_(63025, "an", lambda: an) + _n_(63026, "char", lambda: char))
                _l_(63028)
        result = _n_(63031, "temp", lambda: temp)
        _l_(63032)
    aux = _n_(63034, "result", lambda: result)
    _l_(63035)
    return aux
digit_string = '47'
_l_(63037)
_c_(63042, _n_(63038, "print", lambda: print), _c_(63041, _n_(63039, "letter_combinations", lambda: letter_combinations), _n_(63040, "digit_string", lambda: digit_string)))
_l_(63043)
digit_string = '29'
_l_(63044)
_c_(63049, _n_(63045, "print", lambda: print), _c_(63048, _n_(63046, "letter_combinations", lambda: letter_combinations), _n_(63047, "digit_string", lambda: digit_string)))
_l_(63050)