# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myfile = _c_(61435, _n_(61434, "open", lambda: open), "data.txt","r")
_l_(61436)
data = ""
_l_(61437)
lines = _c_(61440, _a_(61439, _n_(61438, "myfile", lambda: myfile), "readlines"))
_l_(61441)
for line in _n_(61442, "lines", lambda: lines):
    _l_(61448)

    data = _n_(61443, "data", lambda: data) + _c_(61446, _a_(61445, _n_(61444, "line", lambda: line), "strip"));
    _l_(61447)

