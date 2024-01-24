# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63823364/exception-has-occurred-typeerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(595136)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(595138)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(595140)

except ImportError:
    pass
try:
    import time
    _l_(595142)

except ImportError:
    pass

articlelist = []
_l_(595143)

def request(x):
    _l_(595162)

    url = f'https://www.seaporn.org/category/hevc/page/{_n_(595144, "x", lambda: x)}/'
    _l_(595145)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    _l_(595146)
    r = _c_(595151, _a_(595148, _n_(595147, 'requests', lambda: requests), 'get'), _n_(595149, 'url', lambda: url), headers=_n_(595150, 'headers', lambda: headers))
    _l_(595152)
    soup = _c_(595156, _n_(595153, 'BeautifulSoup', lambda: BeautifulSoup), _a_(595155, _n_(595154, 'r', lambda: r), 'content'), features='lxml')
    _l_(595157)
    aux = _c_(595160, _a_(595159, _n_(595158, 'soup', lambda: soup), 'find_all'), 'article', class_ = 'post-summary')
    _l_(595161)
    return aux

def parse(articles):
    _l_(595176)

    for item in _n_(595163, 'articles', lambda: articles):
        _l_(595175)

        link = _c_(595166, _a_(595165, _n_(595164, 'item', lambda: item), 'find'), {'a': 'entry-link'})
        _l_(595167)
        article = {
            'link': _n_(595168, 'link', lambda: link)['href']
        }
        _l_(595169)

        _c_(595173, _a_(595171, _n_(595170, 'articlelist', lambda: articlelist), 'append'), _n_(595172, 'article', lambda: article))
        _l_(595174)

def output():
    _l_(595189)

    df = _c_(595180, _a_(595178, _n_(595177, 'pd', lambda: pd), 'DataFrame'), _n_(595179, 'articlelist', lambda: articlelist))
    _l_(595181)
    _c_(595184, _a_(595183, _n_(595182, 'df', lambda: df), 'to_excel'), 'articlelist.xlsx', index=False)
    _l_(595185)
    _c_(595187, _n_(595186, 'print', lambda: print), 'Saved to xlsx.')
    _l_(595188)

x = 5000
_l_(595190)

while True:
    _l_(595214)

    _c_(595193, _n_(595191, 'print', lambda: print), f'Page {_n_(595192, "x", lambda: x)}')
    _l_(595194)
    articles = _c_(595197, _n_(595195, 'requests', lambda: requests), _n_(595196, 'x', lambda: x))
    _l_(595198)
    x = _n_(595199, 'x', lambda: x) + 1
    _l_(595200)
    _c_(595203, _a_(595202, _n_(595201, 'time', lambda: time), 'sleep'), 3)
    _l_(595204)
    if _c_(595207, _n_(595205, 'len', lambda: len), _n_(595206, 'articles', lambda: articles)) != 0:
        _l_(595213)

        _c_(595210, _n_(595208, 'parse', lambda: parse), _n_(595209, 'articles', lambda: articles))
        _l_(595211)
    else:
        break
        _l_(595212)

_c_(595219, _n_(595215, 'print', lambda: print), 'Completed, total articles is', _c_(595218, _n_(595216, 'len', lambda: len), _n_(595217, 'articlelist', lambda: articlelist)))
_l_(595220)
_c_(595222, _n_(595221, 'output', lambda: output))
_l_(595223)