# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2502833/store-output-of-subprocess-popen-call-in-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(1547232)

except ImportError:
    pass

p = _c_(1547235, _a_(1547234, _n_(1547233, "subprocess", lambda: subprocess), "run"), ["echo", "hello world!"], capture_output=True, text=True)
_l_(1547236)
assert _a_(1547238, _n_(1547237, "p", lambda: p), "stdout") == 'hello world!\n'
_l_(1547239)

