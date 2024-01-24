# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69005427/typeerror-list-indices-must-be-integers-or-slices-not-str-even-after-following
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(347922)

except ImportError:
    pass
try:
    import random
    _l_(347924)

except ImportError:
    pass
try:
    import string
    _l_(347926)

except ImportError:
    pass
try:
    import json
    _l_(347928)

except ImportError:
    pass

url = 'https://www.1secmail.com/api/v1/?action=getMessages&login=Demo&domain=1secmail.com'
_l_(347929)
r = _c_(347933, _a_(347931, _n_(347930, "requests", lambda: requests), "get"), _n_(347932, "url", lambda: url))
_l_(347934)
raw = _c_(347937, _a_(347936, _n_(347935, "r", lambda: r), "json"))
_l_(347938)
_c_(347941, _n_(347939, "print", lambda: print), _n_(347940, "raw", lambda: raw)["id"])
_l_(347942)