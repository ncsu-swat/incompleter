# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30712020/typeerror-encoding-or-errors-without-a-string-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(381303, _n_(381302, "open", lambda: open), r"E:\Avinash\Python\extracting-drug-data\out.csv", "wb") as w:
    _l_(381316)

    writer = _c_(381307, _a_(381305, _n_(381304, "csv", lambda: csv), "writer"), _n_(381306, "w", lambda: w))
    _l_(381308)
    _c_(381314, _a_(381310, _n_(381309, "writer", lambda: writer), "writerows"), _c_(381313, _n_(381311, "bytes", lambda: bytes), _n_(381312, "datas", lambda: datas), 'UTF-8'))
    _l_(381315)