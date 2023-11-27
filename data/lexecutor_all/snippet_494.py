# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1541416)

except ImportError:
    pass
try:
    import inspect
    _l_(1541418)

except ImportError:
    pass
currentdir = _c_(1541432, _a_(1541421, _a_(1541420, _n_(1541419, "os", lambda: os), "path"), "dirname"), _c_(1541431, _a_(1541424, _a_(1541423, _n_(1541422, "os", lambda: os), "path"), "abspath"), _c_(1541430, _a_(1541426, _n_(1541425, "inspect", lambda: inspect), "getfile"), _c_(1541429, _a_(1541428, _n_(1541427, "inspect", lambda: inspect), "currentframe")))))
_l_(1541433)
parentdir = _c_(1541438, _a_(1541436, _a_(1541435, _n_(1541434, "os", lambda: os), "path"), "dirname"), _n_(1541437, "currentdir", lambda: currentdir))
_l_(1541439)
_c_(1541445, _a_(1541443, _a_(1541442, _a_(1541441, _n_(1541440, "os", lambda: os), "sys"), "path"), "insert"), 1, _n_(1541444, "parentdir", lambda: parentdir))
_l_(1541446)
# print("currentdir = ", currentdir)
# print("parentdir=", parentdir)

