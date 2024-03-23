# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def letter_combinations(digits):
    _l_(62926)

    if _n_(62904, "digits", lambda: digits) == '':
        _l_(62906)

        aux = []
        _l_(62905)
        return aux
    result = ['']
    _l_(62907)
    for num in _n_(62908, "digits", lambda: digits):
        _l_(62923)

        temp = []
        _l_(62909)
        for an in _n_(62910, "result", lambda: result):
            _l_(62920)

            for char in _n_(62911, "string_maps", lambda: string_maps)[_n_(62912, "num", lambda: num)]:
                _l_(62919)

                _c_(62917, _a_(62914, _n_(62913, "temp", lambda: temp), "append"), _n_(62915, "an", lambda: an) + _n_(62916, "char", lambda: char))
                _l_(62918)
        result = _n_(62921, "temp", lambda: temp)
        _l_(62922)
    aux = _n_(62924, "result", lambda: result)
    _l_(62925)
    return aux
digit_string = '47'
_l_(62927)
_c_(62932, _n_(62928, "print", lambda: print), _c_(62931, _n_(62929, "letter_combinations", lambda: letter_combinations), _n_(62930, "digit_string", lambda: digit_string)))
_l_(62933)
digit_string = '29'
_l_(62934)
_c_(62939, _n_(62935, "print", lambda: print), _c_(62938, _n_(62936, "letter_combinations", lambda: letter_combinations), _n_(62937, "digit_string", lambda: digit_string)))
_l_(62940)