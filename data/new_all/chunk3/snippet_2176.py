# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58891720/how-to-fix-this-error-in-selenium-attributeerror-list-object-has-no-attribut
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for s in _n_(576485, "site", lambda: site):
    _l_(576519)

    _c_(576488, _a_(576487, _n_(576486, "time", lambda: time), "sleep"), 3)
    _l_(576489)
    URL = 'https://www.bing.com/search?q=site%3a' + _c_(576492, _n_(576490, "str", lambda: str), _n_(576491, "site", lambda: site)) + '&qs=n&sp=-1&pq=site%3a' + _c_(576495, _n_(576493, "str", lambda: str), _n_(576494, "site", lambda: site)) + '&sc=0-22&sk=&cvid=D38F613A00C64A88B2C0F87BD653088A&first=' + _c_(576498, _n_(576496, "str", lambda: str), _n_(576497, "url_p", lambda: url_p))     
    _l_(576499)     
    _c_(576503, _a_(576501, _n_(576500, "driver", lambda: driver), "get"), _n_(576502, "URL", lambda: URL))
    _l_(576504)

    title = _c_(576507, _a_(576506, _n_(576505, "driver", lambda: driver), "find_elements_by_tag_name"), 'h2')
    _l_(576508)
    link = _c_(576511, _a_(576510, _n_(576509, "driver", lambda: driver), "find_elements_by_tag_name"), 'h2')
    _l_(576512)
    _c_(576517, _a_(576516, _c_(576515, _a_(576514, _n_(576513, "link", lambda: link), "find_elements_by_css_selector"), 'a'), "get_attribute"), 'href')
    _l_(576518)