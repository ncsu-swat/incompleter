# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46622020/attributeerror-nonetype-object-has-no-attribute-div
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(687460)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(687462)

except ImportError:
    pass
try:
    import urllib.request
    _l_(687464)

except ImportError:
    pass
try:
    import requests
    _l_(687466)

except ImportError:
    pass
try:
    from urllib.parse import quote
    _l_(687468)

except ImportError:
    pass
try:
    import os
    _l_(687470)

except ImportError:
    pass
try:
    import xlwt
    _l_(687472)

except ImportError:
    pass
try:
    import re
    _l_(687474)

except ImportError:
    pass
try:
    import time
    _l_(687476)

except ImportError:
    pass
try:
    import random
    _l_(687478)

except ImportError:
    pass
try:
    import re, requests, csv
    _l_(687480)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(687482)

except ImportError:
    pass
try:
    from time import sleep
    _l_(687484)

except ImportError:
    pass

# CMD chcp 65001


def reviews_info(div):
    _l_(687500)

    review_text = _a_(687489, _a_(687488, _c_(687487, _a_(687486, _n_(687485, "div", lambda: div), "find"), "div", "review-content"), "div"), "text") 
    _l_(687490) 
    review_stars = _a_(687495, _a_(687494, _c_(687493, _a_(687492, _n_(687491, "div", lambda: div), "find"), "div", "i-stars i-stars--regular-1 rating-large"), "a"), "text")
    _l_(687496)
    aux = {
        "review_text" : _n_(687497, "review_text", lambda: review_text),
        "review_stars" : _n_(687498, "review_stars", lambda: review_stars),
    }
    _l_(687499)
    return aux

base_url = "https://www.yelp.com/biz/founding-farmers-d-c-washington-2?start="
_l_(687501)
reviews = []
_l_(687502)
NUM_PAGES = 36
_l_(687503)

for page_num in _c_(687506, _n_(687504, "range", lambda: range), 1, _n_(687505, "NUM_PAGES", lambda: NUM_PAGES) + 20):
    _l_(687540)

    _c_(687512, _n_(687507, "print", lambda: print), "souping page", _n_(687508, "page_num", lambda: page_num), ",", _c_(687511, _n_(687509, "len", lambda: len), _n_(687510, "reviews", lambda: reviews)), "data")
    _l_(687513)
    url = _n_(687514, "base_url", lambda: base_url) + _c_(687517, _n_(687515, "str", lambda: str), _n_(687516, "page_num", lambda: page_num))
    _l_(687518)
    soup = _c_(687525, _n_(687519, "BeautifulSoup", lambda: BeautifulSoup), _a_(687524, _c_(687523, _a_(687521, _n_(687520, "requests", lambda: requests), "get"), _n_(687522, "url", lambda: url)), "text"), 'lxml') 
    _l_(687526) 

    for div in _c_(687528, _n_(687527, "soup", lambda: soup), 'div', 'review-content'):
        _l_(687536)

        _c_(687534, _a_(687530, _n_(687529, "reviews", lambda: reviews), "append"), _c_(687533, _n_(687531, "reviews_info", lambda: reviews_info), _n_(687532, "div", lambda: div)))
        _l_(687535)
    _c_(687538, _n_(687537, "sleep", lambda: sleep), 5)#############################################
    _l_(687539)#############################################
keys = _c_(687543, _a_(687542, _n_(687541, "reviews", lambda: reviews)[0], "keys"))
_l_(687544)
with _c_(687546, _n_(687545, "open", lambda: open), 'testtest.csv', 'w', encoding="utf-8") as f:
    _l_(687562)

    dict_writer = _c_(687551, _a_(687548, _n_(687547, "csv", lambda: csv), "DictWriter"), _n_(687549, "f", lambda: f), delimiter=',', lineterminator='\n', fieldnames=_n_(687550, "keys", lambda: keys))
    _l_(687552)
    _c_(687555, _a_(687554, _n_(687553, "dict_writer", lambda: dict_writer), "writeheader"))
    _l_(687556)
    _c_(687560, _a_(687558, _n_(687557, "dict_writer", lambda: dict_writer), "writerows"), _n_(687559, "reviews", lambda: reviews))
    _l_(687561)