# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62610636/django-typeerror-not-enough-arguments-for-format-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Summary = _c_(466901, _a_(466900, _a_(466899, _n_(466898, "myTable", lambda: myTable), "objects"), "raw"), "SELECT FROM_UNIXTIME (unixtime, '%Y/%m/%d') AS ndate, count(id) AS query_count FROM myTable GROUP BY ndate ORDER BY query_count DESC")
_l_(466902)