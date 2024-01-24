# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38626868/in-python-using-amazon-bottlenose-api-i-have-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bottlenose
    _l_(671186)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(671188)

except ImportError:
    pass


def item_search(keywords, search_index="Toys", item_page= 1):
    _l_(671204)

    response = _c_(671194, _a_(671190, _n_(671189, "amazon", lambda: amazon), "ItemSearch"), SearchIndex=_n_(671191, "search_index", lambda: search_index), Keywords=_n_(671192, "keywords", lambda: keywords), ItemPage=_n_(671193, "item_page", lambda: item_page), ResponseGroup="Large")
    _l_(671195)
    soup = _c_(671198, _n_(671196, "BeautifulSoup", lambda: BeautifulSoup), _n_(671197, "response", lambda: response), 'lxml')
    _l_(671199)
    aux = _c_(671202, _a_(671201, _n_(671200, "soup", lambda: soup), "find"), 'item')
    _l_(671203)
    return aux

def item_Lookup(item_id):
    _l_(671218)

    response = _c_(671208, _a_(671206, _n_(671205, "amazon", lambda: amazon), "ItemLookup"), ItemId= _n_(671207, "item_id", lambda: item_id),  ResponseGroup="Images")
    _l_(671209)
    soup = _c_(671212, _n_(671210, "BeautifulSoup", lambda: BeautifulSoup), _n_(671211, "response", lambda: response), 'lxml')
    _l_(671213)
    aux = _c_(671216, _a_(671215, _n_(671214, "soup", lambda: soup), "find"), 'largeimage')
    _l_(671217)
    return aux

def amazon_api():
    _l_(671249)

    api_id = 'your api_id'
    _l_(671219)
    api_key = 'your api_key'
    _l_(671220)
    tag_id = 'your tag_id'
    _l_(671221)

    amazon = _c_(671227, _a_(671223, _n_(671222, "bottlenose", lambda: bottlenose), "Amazon"), _n_(671224, "api_id", lambda: api_id),_n_(671225, "api_key", lambda: api_key),_n_(671226, "tag_id", lambda: tag_id))    
    _l_(671228)    
    item = _c_(671230, _n_(671229, "item_search", lambda: item_search), 'nike', search_index="All", item_page= 1)
    _l_(671231)
    asin = _a_(671235, _c_(671234, _a_(671233, _n_(671232, "item", lambda: item), "find"), 'asin'), "text")
    _l_(671236)

    _c_(671239, _n_(671237, "print", lambda: print), _n_(671238, "asin", lambda: asin))
    _l_(671240)
    img = _c_(671243, _n_(671241, "item_Lookup", lambda: item_Lookup), _n_(671242, "asin", lambda: asin))
    _l_(671244)
    _c_(671247, _n_(671245, "print", lambda: print), _n_(671246, "img", lambda: img))
    _l_(671248)

_c_(671251, _n_(671250, "amazon_api", lambda: amazon_api))
_l_(671252)