# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49868595/nameerror-name-data-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(356715)

except ImportError:
    pass
try:
    from io import BytesIO
    _l_(356717)

except ImportError:
    pass
try:
    import base64
    _l_(356719)

except ImportError:
    pass

_n_(356720, "data", lambda: data)['img'] = '''R0lGODlhDwAPAKECAAAAzMzM/////wAAACwAAAAADwAPAAACIISPeQHsrZ5ModrLlN48CXF8m2iQ3YmmKqVlRtW4MLwWACH+H09wdGltaXplZCBieSBVbGVhZCBTbWFydFNhdmVyIQAAOw==''' 
_l_(356721) 

im = _c_(356730, _a_(356723, _n_(356722, "Image", lambda: Image), "open"), _c_(356729, _n_(356724, "BytesIO", lambda: BytesIO), _c_(356728, _a_(356726, _n_(356725, "base64", lambda: base64), "b64decode"), _n_(356727, "data", lambda: data))))
_l_(356731)