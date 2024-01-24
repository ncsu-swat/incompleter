# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75953316/python3-attributeerror-nonetype-object-has-no-attribute-find-all
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(365606)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(365608)

except ImportError:
    pass

url = 'https://otakudesu.lol/genre-list/'
_l_(365609)

response = _c_(365613, _a_(365611, _n_(365610, "requests", lambda: requests), "get"), _n_(365612, "url", lambda: url))
_l_(365614)
soup = _c_(365618, _n_(365615, "BeautifulSoup", lambda: BeautifulSoup), _a_(365617, _n_(365616, "response", lambda: response), "text"), 'html.parser')
_l_(365619)

genres_div = _c_(365622, _a_(365621, _n_(365620, "soup", lambda: soup), "find"), 'div', class_='genres')
_l_(365623)
genre_links = _c_(365626, _a_(365625, _n_(365624, "genres_div", lambda: genres_div), "find_all"), 'a')
_l_(365627)

path = []
_l_(365628)
text = []
_l_(365629)

for link in _n_(365630, "genre_links", lambda: genre_links):
    _l_(365642)

    _c_(365634, _a_(365632, _n_(365631, "path", lambda: path), "append"), _n_(365633, "link", lambda: link)['href'])
    _l_(365635)
    _c_(365640, _a_(365637, _n_(365636, "text", lambda: text), "append"), _a_(365639, _n_(365638, "link", lambda: link), "text"))
    _l_(365641)

_c_(365645, _n_(365643, "print", lambda: print), _n_(365644, "path", lambda: path))
_l_(365646)
_c_(365649, _n_(365647, "print", lambda: print), _n_(365648, "text", lambda: text))
_l_(365650)