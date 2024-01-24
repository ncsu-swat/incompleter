# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58558412/typeerror-type-tuple-cannot-be-instantiated-use-tuple-instead
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(398948)

except ImportError:
    pass
try:
    import numpy as np
    _l_(398950)

except ImportError:
    pass
try:
    from typing import Tuple
    _l_(398952)

except ImportError:
    pass

def split_data(self, df: _a_(398954, _n_(398953, "pd", lambda: pd), "DataFrame"), split_quantile: _n_(398955, "float", lambda: float)) -> _c_(398961, _n_(398956, "Tuple", lambda: Tuple), _a_(398958, _n_(398957, "pd", lambda: pd), "DataFrame"), _a_(398960, _n_(398959, "pd", lambda: pd), "DataFrame")):
    _l_(398991)

    '''Split data sets into two parts - train and test data sets.'''
    _l_(398962)
    df = _c_(398967, _a_(398966, _c_(398965, _a_(398964, _n_(398963, "df", lambda: df), "sort_values"), by='datein'), "reset_index"), drop=True)
    _l_(398968)
    quantile = _c_(398976, _n_(398969, "int", lambda: int), _c_(398975, _a_(398971, _n_(398970, "np", lambda: np), "quantile"), _a_(398973, _n_(398972, "df", lambda: df), "index"), _n_(398974, "split_quantile", lambda: split_quantile)))
    _l_(398977)
    aux = (
        _c_(398983, _a_(398982, _n_(398978, "df", lambda: df)[_a_(398980, _n_(398979, "df", lambda: df), "index") <= _n_(398981, "quantile", lambda: quantile)], "reset_index"), drop=True),
        _c_(398989, _a_(398988, _n_(398984, "df", lambda: df)[_a_(398986, _n_(398985, "df", lambda: df), "index") > _n_(398987, "quantile", lambda: quantile)], "reset_index"), drop=True)
    )
    _l_(398990)
    return aux