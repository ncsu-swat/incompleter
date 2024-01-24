# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49196607/attributeerror-nonetype-object-has-no-attribute-jvm-when-passing-sql-funct
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql import functions as F
    _l_(609588)

except ImportError:
    pass

def apply_filter(df, group=_c_(609591, _a_(609590, _n_(609589, "F", lambda: F), "lit"), True)):
    _l_(609597)

    filtered_df = _c_(609595, _a_(609593, _n_(609592, "df", lambda: df), "filter"), _n_(609594, "group", lambda: group))
    _l_(609596)