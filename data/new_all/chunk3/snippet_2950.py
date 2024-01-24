# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57262877/urllib-request-urlopen-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib import request
    _l_(561026)

except ImportError:
    pass

def get_page(page):
    _l_(561036)

    page = _c_(561032, _a_(561031, _c_(561030, _a_(561028, _n_(561027, "request", lambda: request), "urlopen"), _n_(561029, "page", lambda: page)), "read"))
    _l_(561033)
    aux = _n_(561034, "page", lambda: page)
    _l_(561035)
    return aux

def get_next_target(page):
    _l_(561065)

    start_link = _c_(561039, _a_(561038, _n_(561037, "page", lambda: page), "find"), "<a href=")
    _l_(561040)
    if(_n_(561041, "start_link", lambda: start_link) == -1):
        _l_(561043)

        aux = None
        _l_(561042)
        return aux
    start_quote = _c_(561047, _a_(561045, _n_(561044, "page", lambda: page), "find"), '"', _n_(561046, "start_link", lambda: start_link))
    _l_(561048)
    end_quote = _c_(561052, _a_(561050, _n_(561049, "page", lambda: page), "find"), '"', _n_(561051, "start_quote", lambda: start_quote)+1)
    _l_(561053)
    url = _n_(561054, "page", lambda: page)[_n_(561055, "start_quote", lambda: start_quote)+1:_n_(561056, "end_quote", lambda: end_quote)]
    _l_(561057)
    _c_(561060, _n_(561058, "print", lambda: print), _n_(561059, "url", lambda: url))
    _l_(561061)
    aux = (_n_(561062, "url", lambda: url),_n_(561063, "end_quote", lambda: end_quote))
    _l_(561064)
    return aux

def print_all_links(page):
    _l_(561081)

    while True:
        _l_(561080)

        url, endpos = _c_(561068, _n_(561066, "get_next_target", lambda: get_next_target), _n_(561067, "page", lambda: page))
        _l_(561069)
        if _n_(561070, "url", lambda: url):
            _l_(561079)

            _c_(561073, _n_(561071, "print", lambda: print), _n_(561072, "url", lambda: url))
            _l_(561074)
            page = _n_(561075, "page", lambda: page)[_n_(561076, "endpos", lambda: endpos):]
            _l_(561077)
        else:
            break
            _l_(561078)

page = _c_(561083, _n_(561082, "get_page", lambda: get_page), 'https://xkcd.com/')
_l_(561084)
_c_(561087, _n_(561085, "print", lambda: print), _n_(561086, "page", lambda: page))
_l_(561088)
_c_(561091, _n_(561089, "get_next_target", lambda: get_next_target), _n_(561090, "page", lambda: page))
_l_(561092)
#print_all_links(page)