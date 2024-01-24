# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69457805/i-am-taking-data-from-an-api-but-i-get-the-error-message-typeerror-list-indic
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(366519)

except ImportError:
    pass
try:
    import json
    _l_(366521)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(366523)

except ImportError:
    pass
link = _c_(366526, _a_(366525, _n_(366524, "requests", lambda: requests), "get"), 'https://api.hypixel.net/skyblock/bazaar')
_l_(366527)
data = _a_(366529, _n_(366528, "link", lambda: link), "text")
_l_(366530)
dictionary = _c_(366534, _a_(366532, _n_(366531, "json", lambda: json), "loads"), _n_(366533, "data", lambda: data))
_l_(366535)
_c_(366540, _n_(366536, "print", lambda: print), _c_(366539, _n_(366537, "str", lambda: str), _n_(366538, "dictionary", lambda: dictionary)['products']['BROWN_MUSHROOM']['sell_summary']['sellPrice']))
_l_(366541)