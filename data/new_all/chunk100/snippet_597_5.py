# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def letter_combinations(digits):
    _l_(63073)

    if _n_(63051, "digits", lambda: digits) == '':
        _l_(63053)

        aux = []
        _l_(63052)
        return aux
    string_maps = {'1': 'abc', '2': 'def', '3': 'ghi', '4': 'jkl', '5': 'mno', '6': 'pqrs', '7': 'tuv', '8': 'wxy', '9': 'z'}
    _l_(63054)
    result = ['']
    _l_(63055)
    for num in _n_(63056, "digits", lambda: digits):
        _l_(63070)

        for an in _n_(63057, "result", lambda: result):
            _l_(63067)

            for char in _n_(63058, "string_maps", lambda: string_maps)[_n_(63059, "num", lambda: num)]:
                _l_(63066)

                _c_(63064, _a_(63061, _n_(63060, "temp", lambda: temp), "append"), _n_(63062, "an", lambda: an) + _n_(63063, "char", lambda: char))
                _l_(63065)
        result = _n_(63068, "temp", lambda: temp)
        _l_(63069)
    aux = _n_(63071, "result", lambda: result)
    _l_(63072)
    return aux
digit_string = '47'
_l_(63074)
_c_(63079, _n_(63075, "print", lambda: print), _c_(63078, _n_(63076, "letter_combinations", lambda: letter_combinations), _n_(63077, "digit_string", lambda: digit_string)))
_l_(63080)
digit_string = '29'
_l_(63081)
_c_(63086, _n_(63082, "print", lambda: print), _c_(63085, _n_(63083, "letter_combinations", lambda: letter_combinations), _n_(63084, "digit_string", lambda: digit_string)))
_l_(63087)