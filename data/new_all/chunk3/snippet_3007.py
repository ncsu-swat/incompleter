# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54915685/attributeerror-nonetype-object-has-no-attribute-lower-while-trying-to-con
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(551011)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup as bs
    _l_(551013)

except ImportError:
    pass
try:
    import operator
    _l_(551015)

except ImportError:
    pass

def webpage(url):
    _l_(551037)

    word_list = []
    _l_(551016)
    soup = _c_(551023, _n_(551017, "bs", lambda: bs), _a_(551022, _c_(551021, _a_(551019, _n_(551018, "requests", lambda: requests), "get"), _n_(551020, "url", lambda: url)), "text"), 'html.parser')
    _l_(551024)
    for text in _c_(551026, _n_(551025, "soup", lambda: soup), 'p', {'class': 'PE7lZb'}):
        _l_(551036)

        content = _a_(551028, _n_(551027, "text", lambda: text), "string")
        _l_(551029)
        words = _c_(551034, _a_(551033, _c_(551032, _a_(551031, _n_(551030, "content", lambda: content), "lower")), "split"))
        _l_(551035)

_c_(551039, _n_(551038, "webpage", lambda: webpage), "https://godan.business.site/")
_l_(551040)