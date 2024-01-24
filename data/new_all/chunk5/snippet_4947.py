# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38626868/in-python-using-amazon-bottlenose-api-i-have-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bottlenose
    _l_(675228)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(675230)

except ImportError:
    pass


def item_search(keywords, search_index="Toys", item_page= 1):
    _l_(675246)

    response = _c_(675236, _a_(675232, _n_(675231, "amazon", lambda: amazon), "ItemSearch"), SearchIndex=_n_(675233, "search_index", lambda: search_index), Keywords=_n_(675234, "keywords", lambda: keywords), ItemPage=_n_(675235, "item_page", lambda: item_page), ResponseGroup="Large")
    _l_(675237)
    soup = _c_(675240, _n_(675238, "BeautifulSoup", lambda: BeautifulSoup), _n_(675239, "response", lambda: response), 'lxml')
    _l_(675241)
    aux = _c_(675244, _a_(675243, _n_(675242, "soup", lambda: soup), "find"), 'item')
    _l_(675245)
    return aux

def item_Lookup(item_id):
    _l_(675260)

    response = _c_(675250, _a_(675248, _n_(675247, "amazon", lambda: amazon), "ItemLookup"), ItemId= _n_(675249, "item_id", lambda: item_id),  ResponseGroup="Images")
    _l_(675251)
    soup = _c_(675254, _n_(675252, "BeautifulSoup", lambda: BeautifulSoup), _n_(675253, "response", lambda: response), 'lxml')
    _l_(675255)
    aux = _c_(675258, _a_(675257, _n_(675256, "soup", lambda: soup), "find"), 'largeimage')
    _l_(675259)
    return aux

def amazon_api():
    _l_(675291)

    api_id = 'your api_id'
    _l_(675261)
    api_key = 'your api_key'
    _l_(675262)
    tag_id = 'your tag_id'
    _l_(675263)

    amazon = _c_(675269, _a_(675265, _n_(675264, "bottlenose", lambda: bottlenose), "Amazon"), _n_(675266, "api_id", lambda: api_id),_n_(675267, "api_key", lambda: api_key),_n_(675268, "tag_id", lambda: tag_id))    
    _l_(675270)    
    item = _c_(675272, _n_(675271, "item_search", lambda: item_search), 'nike', search_index="All", item_page= 1)
    _l_(675273)
    asin = _a_(675277, _c_(675276, _a_(675275, _n_(675274, "item", lambda: item), "find"), 'asin'), "text")
    _l_(675278)

    _c_(675281, _n_(675279, "print", lambda: print), _n_(675280, "asin", lambda: asin))
    _l_(675282)
    img = _c_(675285, _n_(675283, "item_Lookup", lambda: item_Lookup), _n_(675284, "asin", lambda: asin))
    _l_(675286)
    _c_(675289, _n_(675287, "print", lambda: print), _n_(675288, "img", lambda: img))
    _l_(675290)

_c_(675293, _n_(675292, "amazon_api", lambda: amazon_api))
_l_(675294)