# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47056068/python-3-6-typeerror-a-bytes-like-object-is-required-not-str-when-trying-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_next_target(page):
    _l_(411327)

    start_link=_c_(411305, _a_(411304, _n_(411303, "page", lambda: page), "find"), '<a href=')
    _l_(411306)
    if _n_(411307, "start_link", lambda: start_link)==-1:
        _l_(411309)

        aux = None,0
        _l_(411308)
        return aux
    start_quote=_c_(411313, _a_(411311, _n_(411310, "page", lambda: page), "find"), '"',_n_(411312, "start_link", lambda: start_link))
    _l_(411314)
    end_quote=_c_(411318, _a_(411316, _n_(411315, "page", lambda: page), "find"), '"',_n_(411317, "start_quote", lambda: start_quote)+1)
    _l_(411319)
    url=_n_(411320, "page", lambda: page)[_n_(411321, "start_quote", lambda: start_quote)+1,_n_(411322, "end_quote", lambda: end_quote)]
    _l_(411323)
    aux = _n_(411324, "url", lambda: url),_n_(411325, "end_quote", lambda: end_quote)
    _l_(411326)
    return aux

def print_all_links(page):
    _l_(411343)

    while True:
        _l_(411342)

        url,endpos=_c_(411330, _n_(411328, "get_next_target", lambda: get_next_target), _n_(411329, "page", lambda: page))
        _l_(411331)
        if _n_(411332, "url", lambda: url):
            _l_(411341)

            _c_(411335, _n_(411333, "print", lambda: print), _n_(411334, "url", lambda: url))
            _l_(411336)
            page=_n_(411337, "page", lambda: page)[_n_(411338, "endpos", lambda: endpos):]
            _l_(411339)
        else:
            break
            _l_(411340)

def get_page(url):
    _l_(411353)

    try:
        import urllib.request
        _l_(411345)

    except ImportError:
        pass
    aux = _c_(411351, _a_(411350, _c_(411349, _a_(411347, _a_(411346, urllib, "request"), "urlopen"), _n_(411348, "url", lambda: url)), "read"))
    _l_(411352)
    return aux

_c_(411357, _n_(411354, "print_all_links", lambda: print_all_links), _c_(411356, _n_(411355, "get_page", lambda: get_page), 'https://youtube.com'))
_l_(411358)