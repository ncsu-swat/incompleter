# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56956782/getting-typeerror-argument-should-be-integer-or-bytes-like-object-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
req = _c_(565932, _a_(565927, _n_(565926, "urllib2", lambda: urllib2), "Request"), _a_(565929, _n_(565928, "article", lambda: article), "path"), headers=_a_(565931, _n_(565930, "settings", lambda: settings), "HDR"))
_l_(565933)
html = _c_(565941, _a_(565940, _c_(565939, _a_(565935, _n_(565934, "urllib2", lambda: urllib2), "urlopen"), _n_(565936, "req", lambda: req), timeout=_a_(565938, _n_(565937, "settings", lambda: settings), "SOCKET_TIMEOUT_IN_SECONDS")), "read"))
_l_(565942)
is_present = _c_(565946, _a_(565944, _n_(565943, "html", lambda: html), "find"), _n_(565945, "token_str", lambda: token_str)) >= 0
_l_(565947)