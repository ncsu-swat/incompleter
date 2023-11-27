# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1538364)

except ImportError:
    pass
_c_(1538368, _a_(1538367, _a_(1538366, _n_(1538365, "os", lambda: os), "path"), "abspath"), "mydir/myfile.txt")
_l_(1538369)
'C:/example/cwd/mydir/myfile.txt'
_l_(1538370)
try:
    import os
    _l_(1538372)

except ImportError:
    pass
_c_(1538376, _a_(1538375, _a_(1538374, _n_(1538373, "os", lambda: os), "path"), "abspath"), "C:/example/cwd/mydir/myfile.txt")
_l_(1538377)
'C:/example/cwd/mydir/myfile.txt'
_l_(1538378)

