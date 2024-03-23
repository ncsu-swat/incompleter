# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(61617, _n_(61616, "open", lambda: open), "foo.txt") as file:
    _l_(61622)

    data = _c_(61620, _a_(61619, _n_(61618, "file", lambda: file), "read"))
    _l_(61621)

