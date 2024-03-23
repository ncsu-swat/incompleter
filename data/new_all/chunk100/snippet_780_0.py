# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78755)

except ImportError:
    pass
try:
    import re as re
    _l_(78757)

except ImportError:
    pass
_c_(78760, _a_(78759, _n_(78758, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(78761)
_c_(78763, _n_(78762, "print", lambda: print), 'Original DataFrame:')
_l_(78764)
_c_(78767, _n_(78765, "print", lambda: print), _n_(78766, "df", lambda: df))
_l_(78768)

def find_punctuations(text):
    _l_(78782)

    result = _c_(78772, _a_(78770, _n_(78769, "re", lambda: re), "findall"), '[!"\\$%&\\\'()*+,\\-.\\/:;=#@?\\[\\\\\\]^_`{|}~]*', _n_(78771, "text", lambda: text))
    _l_(78773)
    string = _c_(78776, _a_(78774, '', "join"), _n_(78775, "result", lambda: result))
    _l_(78777)
    aux = _c_(78780, _n_(78778, "list", lambda: list), _n_(78779, "string", lambda: string))
    _l_(78781)
    return aux
_n_(78783, "df", lambda: df)['nonalpha'] = _c_(78789, _a_(78785, _n_(78784, "df", lambda: df)['company_code'], "apply"), lambda x: _c_(78788, _n_(78786, "find_punctuations", lambda: find_punctuations), _n_(78787, "x", lambda: x)))
_l_(78790)
_c_(78792, _n_(78791, "print", lambda: print), '\nExtracting punctuation:')
_l_(78793)
_c_(78796, _n_(78794, "print", lambda: print), _n_(78795, "df", lambda: df))
_l_(78797)