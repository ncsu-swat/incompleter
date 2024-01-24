# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63823364/exception-has-occurred-typeerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(642061)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(642063)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(642065)

except ImportError:
    pass
try:
    import time
    _l_(642067)

except ImportError:
    pass

articlelist = []
_l_(642068)

def request(x):
    _l_(642087)

    url = f'https://www.seaporn.org/category/hevc/page/{_n_(642069, "x", lambda: x)}/'
    _l_(642070)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    _l_(642071)
    r = _c_(642076, _a_(642073, _n_(642072, 'requests', lambda: requests), 'get'), _n_(642074, 'url', lambda: url), headers=_n_(642075, 'headers', lambda: headers))
    _l_(642077)
    soup = _c_(642081, _n_(642078, 'BeautifulSoup', lambda: BeautifulSoup), _a_(642080, _n_(642079, 'r', lambda: r), 'content'), features='lxml')
    _l_(642082)
    aux = _c_(642085, _a_(642084, _n_(642083, 'soup', lambda: soup), 'find_all'), 'article', class_ = 'post-summary')
    _l_(642086)
    return aux

def parse(articles):
    _l_(642101)

    for item in _n_(642088, 'articles', lambda: articles):
        _l_(642100)

        link = _c_(642091, _a_(642090, _n_(642089, 'item', lambda: item), 'find'), {'a': 'entry-link'})
        _l_(642092)
        article = {
            'link': _n_(642093, 'link', lambda: link)['href']
        }
        _l_(642094)

        _c_(642098, _a_(642096, _n_(642095, 'articlelist', lambda: articlelist), 'append'), _n_(642097, 'article', lambda: article))
        _l_(642099)

def output():
    _l_(642114)

    df = _c_(642105, _a_(642103, _n_(642102, 'pd', lambda: pd), 'DataFrame'), _n_(642104, 'articlelist', lambda: articlelist))
    _l_(642106)
    _c_(642109, _a_(642108, _n_(642107, 'df', lambda: df), 'to_excel'), 'articlelist.xlsx', index=False)
    _l_(642110)
    _c_(642112, _n_(642111, 'print', lambda: print), 'Saved to xlsx.')
    _l_(642113)

x = 5000
_l_(642115)

while True:
    _l_(642139)

    _c_(642118, _n_(642116, 'print', lambda: print), f'Page {_n_(642117, "x", lambda: x)}')
    _l_(642119)
    articles = _c_(642122, _n_(642120, 'requests', lambda: requests), _n_(642121, 'x', lambda: x))
    _l_(642123)
    x = _n_(642124, 'x', lambda: x) + 1
    _l_(642125)
    _c_(642128, _a_(642127, _n_(642126, 'time', lambda: time), 'sleep'), 3)
    _l_(642129)
    if _c_(642132, _n_(642130, 'len', lambda: len), _n_(642131, 'articles', lambda: articles)) != 0:
        _l_(642138)

        _c_(642135, _n_(642133, 'parse', lambda: parse), _n_(642134, 'articles', lambda: articles))
        _l_(642136)
    else:
        break
        _l_(642137)

_c_(642144, _n_(642140, 'print', lambda: print), 'Completed, total articles is', _c_(642143, _n_(642141, 'len', lambda: len), _n_(642142, 'articlelist', lambda: articlelist)))
_l_(642145)
_c_(642147, _n_(642146, 'output', lambda: output))
_l_(642148)