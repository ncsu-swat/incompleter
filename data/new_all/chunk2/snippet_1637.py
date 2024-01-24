# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68421612/problem-with-udf-in-spark-typeerror-column-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql.functions import udf
    _l_(467262)

except ImportError:
    pass

punct_remove = _c_(467267, _n_(467263, "udf", lambda: udf), lambda s: _c_(467266, _n_(467264, "remove_punct", lambda: remove_punct), _n_(467265, "s", lambda: s)))
_l_(467268)

removeEmoji = _c_(467273, _n_(467269, "udf", lambda: udf), lambda s: _c_(467272, _n_(467270, "removeEmoji", lambda: removeEmoji), _n_(467271, "s", lambda: s)))
_l_(467274)