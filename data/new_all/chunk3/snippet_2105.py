# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63660467/typeerror-unhashable-type-dict-unable-to-read-parquet-file-with-dask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyarrow
    _l_(534247)

except ImportError:
    pass
try:
    import dask.dataframe as dd
    _l_(534249)

except ImportError:
    pass

data = _c_(534252, _a_(534251, _n_(534250, "dd", lambda: dd), "read_parquet"), 'myfile.parquet', engine = 'pyarrow')
_l_(534253)