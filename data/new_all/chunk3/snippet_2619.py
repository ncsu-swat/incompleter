# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68656775/attributeerror-set-object-has-no-attribute-items-python-product-in-stock-ch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(572335)

except ImportError:
    pass
try:
    import requests
    _l_(572337)

except ImportError:
    pass
try:
    import time
    _l_(572339)

except ImportError:
    pass

def get_page_html(URL):
    _l_(572355)

    headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    _l_(572340)
    page = _c_(572345, _a_(572342, _n_(572341, "requests", lambda: requests), "get"), _n_(572343, "url", lambda: url), headers=_n_(572344, "headers", lambda: headers))
    _l_(572346)
    _c_(572350, _n_(572347, "print", lambda: print), _a_(572349, _n_(572348, "page", lambda: page), "status_code"))
    _l_(572351)
    aux = _a_(572353, _n_(572352, "page", lambda: page), "content")
    _l_(572354)
    return aux


def check_item_in_stock(page_html):
    _l_(572367)

    soup = _c_(572358, _n_(572356, "BeautifulSoup", lambda: BeautifulSoup), _n_(572357, "page_html", lambda: page_html), 'html.parser')
    _l_(572359)
    out_of_stock_div = _c_(572362, _a_(572361, _n_(572360, "soup", lambda: soup), "find"), "div", {"id": "sold_out_text"})
    _l_(572363)
    aux = _a_(572365, _n_(572364, "out_of_stock_div", lambda: out_of_stock_div), "text") == "In stock."
    _l_(572366)
    return aux

def check_inventory():
    _l_(572383)

    url = "https://www.boots.com/dyson-v10-cyclone-animal-10267801" 
    _l_(572368) 
    page_html = _c_(572371, _n_(572369, "get_page_html", lambda: get_page_html), _n_(572370, "URL", lambda: URL))
    _l_(572372)
    if _c_(572375, _n_(572373, "check_item_in_stock", lambda: check_item_in_stock), _n_(572374, "page_html", lambda: page_html)):
        _l_(572382)

        _c_(572377, _n_(572376, "print", lambda: print), "In stock")
        _l_(572378)
    else:
        _c_(572380, _n_(572379, "print", lambda: print), "Out of stock")
        _l_(572381)

while True:
    _l_(572391)

    _c_(572385, _n_(572384, "check_inventory", lambda: check_inventory))
    _l_(572386)
    _c_(572389, _a_(572388, _n_(572387, "time", lambda: time), "sleep"), 60)
    _l_(572390)