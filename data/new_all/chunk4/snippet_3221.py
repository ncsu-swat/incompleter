# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77195698/python3-typeerror-string-argument-expected-got-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import subprocess
    _l_(618294)

except ImportError:
    pass
try:
    from io import StringIO
    _l_(618296)

except ImportError:
    pass

image1, buffer1 = _c_(618307, _n_(618297, "captureTestImage", lambda: captureTestImage), _c_(618300, _n_(618298, "str", lambda: str), _n_(618299, "cameraSettings", lambda: cameraSettings)), _c_(618303, _n_(618301, "str", lambda: str), _n_(618302, "testWidth", lambda: testWidth)), _c_(618306, _n_(618304, "str", lambda: str), _n_(618305, "testHeight", lambda: testHeight)))
_l_(618308)

_c_(618315, _a_(618310, _n_(618309, "imageData", lambda: imageData), "write"), _c_(618314, _a_(618312, _n_(618311, "subprocess", lambda: subprocess), "check_output"), _n_(618313, "command", lambda: command), shell=True))
_l_(618316)