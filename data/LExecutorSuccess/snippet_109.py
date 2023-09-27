# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(1548462)

except ImportError:
    pass
data = [1,2,3,4,5]
_l_(1548463)
with _c_(1548465, _n_(1548464, "open", lambda: open), 'no.txt', 'w') as txtfile:
    _l_(1548472)

    _c_(1548470, _a_(1548467, _n_(1548466, "json", lambda: json), "dump"), _n_(1548468, "data", lambda: data), _n_(1548469, "txtfile", lambda: txtfile))
    _l_(1548471)

