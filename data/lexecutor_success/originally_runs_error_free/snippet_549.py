# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request
    _l_(1541483)

except ImportError:
    pass
url = "http://www.google.com/"
_l_(1541484)
request = _c_(1541488, _a_(1541486, _a_(1541485, urllib, "request"), "Request"), _n_(1541487, "url", lambda: url))
_l_(1541489)
response = _c_(1541493, _a_(1541491, _a_(1541490, urllib, "request"), "urlopen"), _n_(1541492, "request", lambda: request))
_l_(1541494)
_c_(1541501, _n_(1541495, "print", lambda: print), _c_(1541500, _a_(1541499, _c_(1541498, _a_(1541497, _n_(1541496, "response", lambda: response), "read")), "decode"), 'utf-8'))
_l_(1541502)

