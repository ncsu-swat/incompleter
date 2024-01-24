# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76077843/why-is-my-code-giving-me-an-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(446475)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(446477)

except ImportError:
    pass

url = 'https://www.ilga.gov/legislation/default.asp'
_l_(446478)
response = _c_(446482, _a_(446480, _n_(446479, "requests", lambda: requests), "get"), _n_(446481, "url", lambda: url))
_l_(446483)
soup = _c_(446487, _n_(446484, "BeautifulSoup", lambda: BeautifulSoup), _a_(446486, _n_(446485, "response", lambda: response), "text"), 'html.parser')
_l_(446488)

# Find the House Bills section
house_bills = _a_(446492, _c_(446491, _a_(446490, _n_(446489, "soup", lambda: soup), "find"), 'a', {"name": "h_bills"}), "parent")
_l_(446493)

# Iterate through all links in the House Bills section
for link in _c_(446496, _a_(446495, _n_(446494, "house_bills", lambda: house_bills), "find_all"), 'a'):
    _l_(446531)

    href = _c_(446499, _a_(446498, _n_(446497, "link", lambda: link), "get"), 'href')
    _l_(446500)
    if _c_(446503, _a_(446502, _n_(446501, "href", lambda: href), "startswith"), '/legislation/BillStatus.asp?'):
        _l_(446530)

        bill_url = _n_(446504, "url", lambda: url) + _n_(446505, "href", lambda: href)
        _l_(446506)
        bill_response = _c_(446510, _a_(446508, _n_(446507, "requests", lambda: requests), "get"), _n_(446509, "bill_url", lambda: bill_url))
        _l_(446511)
        bill_soup = _c_(446515, _n_(446512, "BeautifulSoup", lambda: BeautifulSoup), _a_(446514, _n_(446513, "bill_response", lambda: bill_response), "content"), 'html.parser')
        _l_(446516)

        # Find the table cell with width
        td = _c_(446519, _a_(446518, _n_(446517, "bill_soup", lambda: bill_soup), "find"), 'td', {'width': '100%'})
        _l_(446520)
        
        # Iterate through all the <li> elements in table
        for li in _c_(446523, _a_(446522, _n_(446521, "td", lambda: td), "find_all"), 'li'):
            _l_(446529)

            _c_(446527, _n_(446524, "print", lambda: print), _a_(446526, _n_(446525, "li", lambda: li), "text"))   
            _l_(446528)   