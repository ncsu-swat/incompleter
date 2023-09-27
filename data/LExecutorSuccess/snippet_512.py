# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26886653/create-new-column-based-on-values-from-other-columns-apply-a-function-of-multi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(1542860)

except ImportError:
    pass

# make a simple dataframe
df = _c_(1542863, _a_(1542862, _n_(1542861, "pd", lambda: pd), "DataFrame"), {'a':[1,2], 'b':[3,4]})
_l_(1542864)
_n_(1542865, "df", lambda: df)
_l_(1542866)
#    a  b
# 0  1  3
# 1  2  4

# create an unattached column with an index
_c_(1542873, _a_(1542868, _n_(1542867, "df", lambda: df), "apply"), lambda row: _a_(1542870, _n_(1542869, "row", lambda: row), "a") + _a_(1542872, _n_(1542871, "row", lambda: row), "b"), axis=1)
_l_(1542874)
# 0    4
# 1    6

# do same but attach it to the dataframe
_n_(1542875, "df", lambda: df)['c'] = _c_(1542882, _a_(1542877, _n_(1542876, "df", lambda: df), "apply"), lambda row: _a_(1542879, _n_(1542878, "row", lambda: row), "a") + _a_(1542881, _n_(1542880, "row", lambda: row), "b"), axis=1)
_l_(1542883)
_n_(1542884, "df", lambda: df)
_l_(1542885)
#    a  b  c
# 0  1  3  4
# 1  2  4  6

fn = lambda row: _a_(1542887, _n_(1542886, "row", lambda: row), "a") + _a_(1542889, _n_(1542888, "row", lambda: row), "b") # define a function for the new column
_l_(1542890) # define a function for the new column
col = _c_(1542894, _a_(1542892, _n_(1542891, "df", lambda: df), "apply"), _n_(1542893, "fn", lambda: fn), axis=1) # get column data with an index
_l_(1542895) # get column data with an index
df = _c_(1542900, _a_(1542897, _n_(1542896, "df", lambda: df), "assign"), c=_a_(1542899, _n_(1542898, "col", lambda: col), "values")) # assign values to column 'c'
_l_(1542901) # assign values to column 'c'

df = _c_(1542906, _a_(1542903, _n_(1542902, "df", lambda: df), "assign"), **{'some column name': _a_(1542905, _n_(1542904, "col", lambda: col), "values")})
_l_(1542907)

