# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65998183/python-dask-module-error-attributeerror-io-textiowrapper-object-has-no-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import dask.array as da
    _l_(626735)

except ImportError:
    pass
try:
    import dask.dataframe as ddf
    _l_(626737)

except ImportError:
    pass
'''Read .csv straight to list'''  
_l_(626738)  
with _c_(626743, _n_(626739, "open", lambda: open), _n_(626740, "wd", lambda: wd)+_n_(626741, "inputfilename", lambda: inputfilename)+_n_(626742, "extension_csv", lambda: extension_csv), 'r') as f:
    _l_(626754)

    reader = _c_(626747, _a_(626745, _n_(626744, "csv", lambda: csv), "reader"), _n_(626746, "f", lambda: f))
    _l_(626748)
    df = _c_(626752, _a_(626750, _n_(626749, "ddf", lambda: ddf), "read_csv"), _n_(626751, "f", lambda: f))   #data here is a dask pandas dataframe
    _l_(626753)   #data here is a dask pandas dataframe