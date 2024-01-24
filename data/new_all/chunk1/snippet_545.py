# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55679929/how-to-fix-attributeerror-dict-object-has-no-attribute-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(395762)

except ImportError:
    pass
try:
    import pprint
    _l_(395764)

except ImportError:
    pass

URL = 'https://github.com/timeline.json'
_l_(395765)

def get_github_json(URL):
    _l_(395775)

    response = _c_(395771, _a_(395770, _c_(395769, _a_(395767, _n_(395766, "requests", lambda: requests), "get"), _n_(395768, "URL", lambda: URL)), "json"))
    _l_(395772)
    aux = _n_(395773, "response", lambda: response)
    _l_(395774)
    return aux

assert _a_(395779, _c_(395778, _n_(395776, "get_github_json", lambda: get_github_json), _n_(395777, "URL", lambda: URL)), "documentation_url") == 'https://developer.github.com/v3/activity/events/#list-public-events'
_l_(395780)