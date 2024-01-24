# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63343056/how-to-solve-nameerror-name-urllib2-is-not-defined-in-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib2.request
    _l_(617717)

except ImportError:
    pass

response = _c_(617720, _a_(617719, _n_(617718, "urllib2", lambda: urllib2), "urlopen"), "http://www.google.com")
_l_(617721)
html = _c_(617724, _a_(617723, _n_(617722, "response", lambda: response), "read"))
_l_(617725)
_c_(617728, _n_(617726, "print", lambda: print), _n_(617727, "html", lambda: html))
_l_(617729)