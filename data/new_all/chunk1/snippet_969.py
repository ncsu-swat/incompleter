# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61723726/dask-apply-function-to-return-dataframe-attributeerror-dataframe-object-has
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(417978)

except ImportError:
    pass
try:
    from dask import dataframe as dd
    _l_(417980)

except ImportError:
    pass

dummy_df = _c_(417983, _a_(417982, _n_(417981, "pd", lambda: pd), "DataFrame"), {'a' : [1,2,3,4,5]})
_l_(417984)

dd_dummy = _c_(417988, _a_(417986, _n_(417985, "dd", lambda: dd), "from_pandas"), _n_(417987, "dummy_df", lambda: dummy_df), npartitions = 1)
_l_(417989)

"""Arbitrary function that returns dataframe, taking keyword argument from apply"""
def test(x, bleh):
    _l_(417995)

    aux = _c_(417993, _a_(417991, _n_(417990, "pd", lambda: pd), "DataFrame"), {'test' : 7 * [_n_(417992, "bleh", lambda: bleh)]})
    _l_(417994)
    return aux

ok = _c_(418001, _a_(418000, _c_(417999, _a_(417997, _n_(417996, "dd_dummy", lambda: dd_dummy), "apply"), _n_(417998, "test", lambda: test), axis = 1
                , bleh = 'fish'
                , meta = {'test' : 'str'}), "compute"))
_l_(418002)