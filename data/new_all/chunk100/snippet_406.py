# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6591931/getting-file-size-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(61463)

except ImportError:
    pass
_c_(61467, _a_(61466, _a_(61465, _n_(61464, "os", lambda: os), "path"), "getsize"), 'C:\\Python27\\Lib\\genericpath.py')
_l_(61468)
try:
    import os
    _l_(61470)

except ImportError:
    pass
_a_(61474, _c_(61473, _a_(61472, _n_(61471, "os", lambda: os), "stat"), 'C:\\Python27\\Lib\\genericpath.py'), "st_size") 
_l_(61475) 
try:
    from pathlib import Path
    _l_(61477)

except ImportError:
    pass
_a_(61482, _c_(61481, _a_(61480, _c_(61479, _n_(61478, "Path", lambda: Path), 'C:\\Python27\\Lib\\genericpath.py'), "stat")), "st_size")
_l_(61483)

