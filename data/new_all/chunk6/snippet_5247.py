# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41803669/typeerror-bad-operant-type-for-unary-type-while-extracting-keywords-form
#Loading Libraries
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib
    _l_(349006)

except ImportError:
    pass
try:
    import os
    _l_(349008)

except ImportError:
    pass
try:
    from urllib.parse import urlparse
    _l_(349010)

except ImportError:
    pass
try:
    from urllib.parse import urljoin
    _l_(349012)

except ImportError:
    pass
try:
    import urllib.request
    _l_(349014)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(349016)

except ImportError:
    pass
id= 1
_l_(349017)
url='http://scitechdaily.com/new-technique-reveals-internal-characteristics-of-photonic-crystals/'
_l_(349018)
def getKeywords(articletext):
    _l_(349058)

    common = _c_(349024, _a_(349023, _c_(349022, _a_(349021, _c_(349020, _n_(349019, "open", lambda: open), 'C:\\Users\\Hassan Raza\\Desktop\\Mozilla tech article\\common.txt'), "read")), "split"), '\n')
    _l_(349025)
    word_dict = {_n_(349026, "articletext", lambda: articletext):_n_(349027, "float", lambda: float)}
    _l_(349028)
    word_list = _c_(349033, _a_(349032, _c_(349031, _a_(349030, _n_(349029, "articletext", lambda: articletext), "lower")), "split"))
    _l_(349034)
    for word in _n_(349035, "word_list", lambda: word_list):
        _l_(349051)

        if _n_(349036, "word", lambda: word) not in _n_(349037, "common", lambda: common):
            _l_(349050)

            if _n_(349038, "word", lambda: word) not in _n_(349039, "word_dict", lambda: word_dict):
                _l_(349043)

                _n_(349040, "word_dict", lambda: word_dict)[_n_(349041, "word", lambda: word)] = 1
                _l_(349042)
            if _n_(349044, "word", lambda: word) in _n_(349045, "word_dict", lambda: word_dict):
                _l_(349049)

                _n_(349046, "word_dict", lambda: word_dict)[_n_(349047, "word", lambda: word)] +=1
                _l_(349048)

    sorteddata = _c_(349056, _a_(349055, _c_(349054, _n_(349052, "Counter", lambda: Counter), _n_(349053, "word_dict", lambda: word_dict)), "most_common"))
    _l_(349057)


def GetArticles(url,id):
    _l_(349108)

    file = _c_(349060, _n_(349059, "open", lambda: open), 'C:\\Users\\Hassan Raza\\Desktop\\Mozilla tech article\\Article'+'.txt', 'w')
    _l_(349061)
    req = _c_(349065, _a_(349063, _a_(349062, urllib, "request"), "Request"), _n_(349064, "url", lambda: url), headers={'User-Agent': 'Mozilla/5.0'})
    _l_(349066)
    html = _c_(349072, _a_(349071, _c_(349070, _a_(349068, _a_(349067, urllib, "request"), "urlopen"), _n_(349069, "req", lambda: req)), "read"))
    _l_(349073)

    soup = _c_(349076, _n_(349074, "BeautifulSoup", lambda: BeautifulSoup), _n_(349075, "html", lambda: html),"html.parser")
    _l_(349077)

    title= _c_(349080, _a_(349079, _n_(349078, "soup", lambda: soup), "find_all"), 'h1', {'class','title'})
    _l_(349081)
    for titles in _n_(349082, "title", lambda: title):
        _l_(349088)

        _c_(349086, _n_(349083, "print", lambda: print), _a_(349085, _n_(349084, "titles", lambda: titles), "text"))
        _l_(349087)
    text = _c_(349091, _a_(349090, _n_(349089, "soup", lambda: soup), "find_all"), 'div' , {'class', 'entry'})
    _l_(349092)
    for pg in _n_(349093, "text", lambda: text):
        _l_(349103)

        articletext=_c_(349097, _a_(349096, _a_(349095, _n_(349094, "pg", lambda: pg), "text"), "encode"), 'utf8')
        _l_(349098)
        _c_(349101, _n_(349099, "getKeywords", lambda: getKeywords), _n_(349100, "articletext", lambda: articletext))
        _l_(349102)

    _c_(349106, _a_(349105, _n_(349104, "file", lambda: file), "close"))
    _l_(349107)

_c_(349112, _n_(349109, "GetArticles", lambda: GetArticles), _n_(349110, "url", lambda: url),_n_(349111, "id", lambda: id))
_l_(349113)