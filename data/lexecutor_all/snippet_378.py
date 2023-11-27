# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from six.moves.urllib.parse import urlencode, quote
    _l_(1544646)

except ImportError:
    pass
data = {'some': 'query', 'for': 'encoding'}
_l_(1544647)
_c_(1544650, _n_(1544648, "urlencode", lambda: urlencode), _n_(1544649, "data", lambda: data))
_l_(1544651)
'some=query&for=encoding'
_l_(1544652)
url = '/some/url/with spaces and %;!<>&'
_l_(1544653)
_c_(1544656, _n_(1544654, "quote", lambda: quote), _n_(1544655, "url", lambda: url))
_l_(1544657)
'/some/url/with%20spaces%20and%20%25%3B%21%3C%3E%26'
_l_(1544658)

