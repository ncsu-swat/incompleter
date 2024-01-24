# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50895680/typeerror-firefoxwebelement-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(459058)

except ImportError:
    pass
try:
    from selenium.webdriver import FirefoxOptions
    _l_(459060)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(459062)

except ImportError:
    pass
try:
    from selenium.webdriver.support.ui import WebDriverWait
    _l_(459064)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(459066)

except ImportError:
    pass
try:
    from selenium.common.exceptions import TimeoutException
    _l_(459068)

except ImportError:
    pass

test_url = 'https://www.airbnb.jp/s/%E6%97%A5%E6%9C%AC%E6%B2%96%E7%B8%84%E7%9C%8C/homes?refinement_paths%5B%5D=%2Fhomes&query=%E6%97%A5%E6%9C%AC%E6%B2%96%E7%B8%84%E7%9C%8C&price_min=15000&allow_override%5B%5D=&checkin=2018-07-07&checkout=2018-07-08&place_id=ChIJ51ur7mJw9TQR79H9hnJhuzU&s_tag=z4scstF7'
_l_(459069)

opts = _c_(459071, _n_(459070, "FirefoxOptions", lambda: FirefoxOptions))
_l_(459072)
_c_(459075, _a_(459074, _n_(459073, "opts", lambda: opts), "add_argument"), "--headless")
_l_(459076)
driver = _c_(459080, _a_(459078, _n_(459077, "webdriver", lambda: webdriver), "Firefox"), firefox_options=_n_(459079, "opts", lambda: opts))
_l_(459081)
_c_(459085, _a_(459083, _n_(459082, "driver", lambda: driver), "get"), _n_(459084, "test_url", lambda: test_url))
_l_(459086)
_c_(459089, _a_(459088, _n_(459087, "driver", lambda: driver), "implicitly_wait"), 30)
_l_(459090)


links = _c_(459093, _a_(459092, _n_(459091, "driver", lambda: driver), "find_element_by_xpath"), '//a[contains(@href, "rooms")]')
_l_(459094)
for link in _n_(459095, "links", lambda: links):
    _l_(459104)

    listing_url = _c_(459098, _a_(459097, _n_(459096, "link", lambda: link), "get_attribute"), 'href')
    _l_(459099)
    _c_(459102, _n_(459100, "print", lambda: print), _n_(459101, "listing_url", lambda: listing_url))
    _l_(459103)

_c_(459107, _a_(459106, _n_(459105, "driver", lambda: driver), "quit"))
_l_(459108)