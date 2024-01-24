# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58800137/rpy2-typeerror-parameter-categories-must-be-list-like
# Convert R Dataframe to python Dataframe
# !pip install tzlocal
# type(data)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rpy2.robjects import pandas2ri
    _l_(523631)

except ImportError:
    pass
pd_df = _c_(523635, _a_(523633, _n_(523632, "pandas2ri", lambda: pandas2ri), "ri2py_dataframe"), _n_(523634, "data", lambda: data))
_l_(523636)
_n_(523637, "pd_df", lambda: pd_df)
_l_(523638)