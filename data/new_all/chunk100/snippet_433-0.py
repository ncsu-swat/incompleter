# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(116130)

except ImportError:
    pass
try:
    import re as re
    _l_(116132)

except ImportError:
    pass
_c_(116135, _a_(116134, _n_(116133, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(116136)
_c_(116138, _n_(116137, "print", lambda: print), 'Original DataFrame:')
_l_(116139)
_c_(116142, _n_(116140, "print", lambda: print), _n_(116141, "df", lambda: df))
_l_(116143)

def test_and_cond(text):
    _l_(116153)

    result = _c_(116147, _a_(116145, _n_(116144, "re", lambda: re), "findall"), '(?=.*Ave.)(?=.*9910).*', _n_(116146, "text", lambda: text))
    _l_(116148)
    aux = _c_(116151, _a_(116149, ' ', "join"), _n_(116150, "result", lambda: result))
    _l_(116152)
    return aux
_n_(116154, "df", lambda: df)['check_two_words'] = _c_(116160, _a_(116156, _n_(116155, "df", lambda: df)['address'], "apply"), lambda x: _c_(116159, _n_(116157, "test_and_cond", lambda: test_and_cond), _n_(116158, "x", lambda: x)))
_l_(116161)
_c_(116163, _n_(116162, "print", lambda: print), '\nPresent two words!')
_l_(116164)
_c_(116167, _n_(116165, "print", lambda: print), _n_(116166, "df", lambda: df))
_l_(116168)