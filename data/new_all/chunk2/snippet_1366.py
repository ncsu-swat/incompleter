# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68968383/attributeerror-while-attempting-to-grab-table-from-a-website-in-python-bs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(447990)

except ImportError:
    pass
try:
    import requests
    _l_(447992)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(447994)

except ImportError:
    pass

browser = _c_(447997, _a_(447996, _n_(447995, "webdriver", lambda: webdriver), "Chrome"), 'C://Python38/chromedriver')
_l_(447998)
_c_(448001, _a_(448000, _n_(447999, "browser", lambda: browser), "get"), "https://poocoin.app/rugcheck/0xe56842ed550ff2794f010738554db45e60730371/top-holders")
_l_(448002)
url = "https://poocoin.app/rugcheck/0xe56842ed550ff2794f010738554db45e60730371/top-holders"
_l_(448003)

r = _c_(448007, _a_(448005, _n_(448004, "requests", lambda: requests), "get"), _n_(448006, "url", lambda: url))
_l_(448008)
soup = _c_(448012, _n_(448009, "BeautifulSoup", lambda: BeautifulSoup), _a_(448011, _n_(448010, "r", lambda: r), "text"), 'lxml')
_l_(448013)
t = _c_(448016, _a_(448015, _n_(448014, "soup", lambda: soup), "find"), 'table', class_='table table-bordered table-condensed text-small')
_l_(448017)
trs = _c_(448022, _a_(448021, _c_(448020, _a_(448019, _n_(448018, "t", lambda: t), "find"), 'tbody'), "find_all"), 'tr')
_l_(448023)
for tr in _n_(448024, "trs", lambda: trs)[:10]:
    _l_(448032)

    _c_(448030, _n_(448025, "print", lambda: print), _c_(448029, _n_(448026, "list", lambda: list), _a_(448028, _n_(448027, "tr", lambda: tr), "stripped_strings")))
    _l_(448031)
_c_(448035, _a_(448034, _n_(448033, "browser", lambda: browser), "quit"))
_l_(448036)