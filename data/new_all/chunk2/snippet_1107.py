# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50895680/typeerror-firefoxwebelement-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(453543)

except ImportError:
    pass
try:
    from selenium.webdriver import FirefoxOptions
    _l_(453545)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(453547)

except ImportError:
    pass
try:
    from selenium.webdriver.support.ui import WebDriverWait
    _l_(453549)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(453551)

except ImportError:
    pass
try:
    from selenium.common.exceptions import TimeoutException
    _l_(453553)

except ImportError:
    pass

test_url = 'https://www.airbnb.jp/s/%E6%97%A5%E6%9C%AC%E6%B2%96%E7%B8%84%E7%9C%8C/homes?refinement_paths%5B%5D=%2Fhomes&query=%E6%97%A5%E6%9C%AC%E6%B2%96%E7%B8%84%E7%9C%8C&price_min=15000&allow_override%5B%5D=&checkin=2018-07-07&checkout=2018-07-08&place_id=ChIJ51ur7mJw9TQR79H9hnJhuzU&s_tag=z4scstF7'
_l_(453554)

opts = _c_(453556, _n_(453555, "FirefoxOptions", lambda: FirefoxOptions))
_l_(453557)
_c_(453560, _a_(453559, _n_(453558, "opts", lambda: opts), "add_argument"), "--headless")
_l_(453561)
driver = _c_(453565, _a_(453563, _n_(453562, "webdriver", lambda: webdriver), "Firefox"), firefox_options=_n_(453564, "opts", lambda: opts))
_l_(453566)
_c_(453570, _a_(453568, _n_(453567, "driver", lambda: driver), "get"), _n_(453569, "test_url", lambda: test_url))
_l_(453571)
_c_(453574, _a_(453573, _n_(453572, "driver", lambda: driver), "implicitly_wait"), 30)
_l_(453575)

for links in _c_(453578, _a_(453577, _n_(453576, "driver", lambda: driver), "find_element_by_xpath"), '//div[contains(@id, "listing-")]//a[contains(@href, "rooms")]'):
    _l_(453587)

    listing_url = _c_(453581, _a_(453580, _n_(453579, "links", lambda: links), "get_attribute"), 'href')
    _l_(453582)
    _c_(453585, _n_(453583, "print", lambda: print), _n_(453584, "listing_url", lambda: listing_url))
    _l_(453586)

_c_(453590, _a_(453589, _n_(453588, "driver", lambda: driver), "quit"))
_l_(453591)