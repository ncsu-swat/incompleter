# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(64675)

except ImportError:
    pass

url = 'https://www.python.org/static/img/python-logo.png'
_l_(64676)
fileName = 'D:\Python\dwnldPythonLogo.png'
_l_(64677)
req = _c_(64681, _a_(64679, _n_(64678, "requests", lambda: requests), "get"), _n_(64680, "url", lambda: url))
_l_(64682)
file = _c_(64685, _n_(64683, "open", lambda: open), _n_(64684, "fileName", lambda: fileName), 'wb')
_l_(64686)
for chunk in _c_(64689, _a_(64688, _n_(64687, "req", lambda: req), "iter_content"), 100000):
    _l_(64695)

    _c_(64693, _a_(64691, _n_(64690, "file", lambda: file), "write"), _n_(64692, "chunk", lambda: chunk))
    _l_(64694)
_c_(64698, _a_(64697, _n_(64696, "file", lambda: file), "close"))
_l_(64699)

