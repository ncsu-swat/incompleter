# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55468914/how-to-fix-filenotfounderror-winerror-2-the-system-cannot-find-the-file-speci
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(428913)

except ImportError:
    pass
_c_(428917, _a_(428915, _n_(428914, "os", lambda: os), "chdir"), _n_(428916, "directory", lambda: directory))
_l_(428918)
for f in _c_(428921, _a_(428920, _n_(428919, "os", lambda: os), "listdir")):
    _l_(428939)

    f_name, f_ext = _c_(428926, _a_(428924, _a_(428923, _n_(428922, "os", lambda: os), "path"), "splitext"), _n_(428925, "f", lambda: f))
    _l_(428927)
    _c_(428937, _a_(428929, _n_(428928, "os", lambda: os), "rename"), _n_(428930, "f_name", lambda: f_name),_c_(428936, _a_(428932, _n_(428931, "f_name", lambda: f_name), "translate"), _c_(428935, _a_(428934, _n_(428933, "str", lambda: str), "maketrans"), "","","ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")))
    _l_(428938)