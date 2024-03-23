# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(8947)

except ImportError:
    pass
try:
    import re as re
    _l_(8949)

except ImportError:
    pass
_c_(8951, _n_(8950, "print", lambda: print), 'Original DataFrame:')
_l_(8952)
_c_(8955, _n_(8953, "print", lambda: print), _n_(8954, "df", lambda: df))
_l_(8956)

def find_unique_sentence(str1):
    _l_(8964)

    result = _c_(8960, _a_(8958, _n_(8957, "re", lambda: re), "findall"), '(?sm)(^[^\\r\\n]+$)(?!.*^\\1$)', _n_(8959, "str1", lambda: str1))
    _l_(8961)
    aux = _n_(8962, "result", lambda: result)
    _l_(8963)
    return aux
_n_(8965, "df", lambda: df)['unique_sentence'] = _c_(8971, _a_(8967, _n_(8966, "df", lambda: df)['address'], "apply"), lambda st: _c_(8970, _n_(8968, "find_unique_sentence", lambda: find_unique_sentence), _n_(8969, "st", lambda: st)))
_l_(8972)
_c_(8974, _n_(8973, "print", lambda: print), '\nExtract unique sentences :')
_l_(8975)
_c_(8978, _n_(8976, "print", lambda: print), _n_(8977, "df", lambda: df))
_l_(8979)