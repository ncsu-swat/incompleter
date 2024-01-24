# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62903409/typeerror-string-argument-expected-got-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = "2a2b2c2a2b2c2a2b2c2a2b2cb1"
_l_(398596)
buf = _c_(398599, _a_(398598, _n_(398597, "io", lambda: io), "StringIO"))    
_l_(398600)    
for line in _c_(398603, _a_(398602, _n_(398601, "data", lambda: data), "splitlines")):
    _l_(398623)

    line = _c_(398608, _a_(398607, _c_(398606, _a_(398605, _n_(398604, "line", lambda: line), "strip")), "replace"), " ", "")
    _l_(398609)
    if not _n_(398610, "line", lambda: line):
        _l_(398612)

        continue
        _l_(398611)
    bytez = _c_(398616, _a_(398614, _n_(398613, "binascii", lambda: binascii), "unhexlify"), _n_(398615, "line", lambda: line))
    _l_(398617)
    _c_(398621, _a_(398619, _n_(398618, "buf", lambda: buf), "write"), _n_(398620, "bytez", lambda: bytez))
    _l_(398622)

with _c_(398625, _n_(398624, "open", lambda: open), "image.jpg", "wb") as f:
    _l_(398633)

    _c_(398631, _a_(398627, _n_(398626, "f", lambda: f), "write"), _c_(398630, _a_(398629, _n_(398628, "buf", lambda: buf), "getvalue"))) 
    _l_(398632) 