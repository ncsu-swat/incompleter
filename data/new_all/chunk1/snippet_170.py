# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/13175253/python-error-type-error-post-data-should-be-bytes-also-user-agent-issue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.parse
    _l_(413592)

except ImportError:
    pass
try:
    import urllib.request
    _l_(413594)

except ImportError:
    pass

url = 'http://getliberty.org/contact-us/'
_l_(413595)
user_agent = 'Mozilla/5.0 (compatible; Chrome/22.0.1229.94; Windows NT)'
_l_(413596)
values = {'Your Name' : 'Horatio',
          'Your Email' : '6765Minus4181@gmail.com',
          'Subject' : 'Hello',
          'Your Message' : 'Cheers'}
_l_(413597)

headers = {'User-Agent': _n_(413598, "user_agent", lambda: user_agent) }
_l_(413599)

data = _c_(413603, _a_(413601, _a_(413600, urllib, "parse"), "urlencode"), _n_(413602, "values", lambda: values))
_l_(413604)
req = _c_(413609, _a_(413606, _a_(413605, urllib, "request"), "Request"), _n_(413607, "url", lambda: url), _n_(413608, "data", lambda: data))
_l_(413610)
response = _c_(413614, _a_(413612, _a_(413611, urllib, "request"), "urlopen"), _n_(413613, "req", lambda: req))
_l_(413615)
the_page = _c_(413618, _a_(413617, _n_(413616, "response", lambda: response), "read"))
_l_(413619)