# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73790830/typeerror-int-object-is-not-iterable-apperars-when-i-try-to-add-a-string-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def calculate(string: _n_(557222, "str", lambda: str)):
    _l_(557266)

    allowed_symboles = "1234567890+-*$"
    _l_(557223)
    symbole_sum = _c_(557226, _n_(557224, "len", lambda: len), _n_(557225, "string", lambda: string))
    _l_(557227)
    symbole_sum0 = 0
    _l_(557228)

    for symbole in _n_(557229, "string", lambda: string):
        _l_(557236)

        for lol in _n_(557230, "allowed_symboles", lambda: allowed_symboles):
            _l_(557235)

            if _n_(557231, "symbole", lambda: symbole) == _n_(557232, "lol", lambda: lol):
                _l_(557234)

                symbole_sum0 += 1
                _l_(557233)

    if _n_(557237, "symbole_sum", lambda: symbole_sum) != _n_(557238, "symbole_sum0", lambda: symbole_sum0):
        _l_(557240)

        aux = "400: Bad request"
        _l_(557239)
        return aux

    all_numbers = []
    _l_(557241)
    pos_of_operators = []
    _l_(557242)

    for x, num in _c_(557250, _n_(557243, "zip", lambda: zip), _n_(557244, "string", lambda: string), _c_(557249, _n_(557245, "range", lambda: range), 0, _c_(557248, _n_(557246, "len", lambda: len), _n_(557247, "string", lambda: string)))):
        _l_(557260)

        if _n_(557251, "x", lambda: x) != "+" and _n_(557252, "x", lambda: x) != "-" and _n_(557253, "x", lambda: x) != "*" and _n_(557254, "x", lambda: x) != "$":
            _l_(557259)

            all_numbers += _n_(557255, "x", lambda: x)
            _l_(557256)
        else:
            pos_of_operators += _n_(557257, "num", lambda: num)
            _l_(557258)

    _c_(557264, _n_(557261, "print", lambda: print), _n_(557262, "all_numbers", lambda: all_numbers), _n_(557263, "pos_of_operators", lambda: pos_of_operators))
    _l_(557265)

_c_(557268, _n_(557267, "calculate", lambda: calculate), "1231241+4234")
_l_(557269)