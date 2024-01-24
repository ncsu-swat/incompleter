# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52020762/beautifulsoup-attributeerror-navigablestring-object-has-no-attribute-find
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(463310)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(463312)

except ImportError:
    pass
try:
    import requests
    _l_(463314)

except ImportError:
    pass
try:
    import lxml.html as lh
    _l_(463316)

except ImportError:
    pass


with _c_(463318, _n_(463317, "open", lambda: open), "htmltabletest.html", encoding="utf-8") as f:
    _l_(463369)

    data = _c_(463321, _a_(463320, _n_(463319, "f", lambda: f), "read"))
    _l_(463322)
    soup = _c_(463325, _n_(463323, "BeautifulSoup", lambda: BeautifulSoup), _n_(463324, "data", lambda: data), 'lxml')
    _l_(463326)
    for table in _c_(463329, _a_(463328, _n_(463327, "soup", lambda: soup), "find"), 'table', attrs={'id': 'eventSearchTable'}):
        _l_(463368)

        for rows in _c_(463332, _a_(463331, _n_(463330, "table", lambda: table), "find_all"), 'tr'):
            _l_(463367)

            cols = _c_(463335, _a_(463334, _n_(463333, "table", lambda: table), "find_all"), 'td')
            _l_(463336)

            empty = _c_(463339, _a_(463338, _n_(463337, "cols", lambda: cols)[0], "get_text"))
            _l_(463340)
            eventdate = _c_(463343, _a_(463342, _n_(463341, "cols", lambda: cols)[1], "get_text"))
            _l_(463344)
            eventname = _c_(463347, _a_(463346, _n_(463345, "cols", lambda: cols)[2], "get_text"))
            _l_(463348)
            tickslisted = _c_(463351, _a_(463350, _n_(463349, "cols", lambda: cols)[3], "get_text"))
            _l_(463352)
            pricerange = _c_(463355, _a_(463354, _n_(463353, "cols", lambda: cols)[4], "get_text"))
            _l_(463356)

            entry = (_n_(463357, "empty", lambda: empty), _n_(463358, "eventdate", lambda: eventdate), _n_(463359, "eventname", lambda: eventname), _n_(463360, "tickslisted", lambda: tickslisted), _n_(463361, "pricerange", lambda: pricerange))
            _l_(463362)

            _c_(463365, _n_(463363, "print", lambda: print), _n_(463364, "entry", lambda: entry))
            _l_(463366)