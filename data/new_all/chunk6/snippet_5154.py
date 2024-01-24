# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73433600/selenium-python-typeerror-str-object-is-not-callable-whenever-trying-to-prin
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from cgitb import text
    _l_(348328)

except ImportError:
    pass
try:
    from http import server
    _l_(348330)

except ImportError:
    pass
try:
    from re import search
    _l_(348332)

except ImportError:
    pass
try:
    import selenium
    _l_(348334)

except ImportError:
    pass
try:
    import time
    _l_(348336)

except ImportError:
    pass
try:
    import sys
    _l_(348338)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(348340)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(348342)

except ImportError:
    pass
try:
    from selenium.webdriver.support.ui import WebDriverWait
    _l_(348344)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(348346)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(348348)

except ImportError:
    pass
PATH = "/usr/local/bin/chromedriver"
_l_(348349)
driver = _c_(348353, _a_(348351, _n_(348350, "webdriver", lambda: webdriver), "Chrome"), _n_(348352, "PATH", lambda: PATH))
_l_(348354)

_c_(348357, _a_(348356, _n_(348355, "driver", lambda: driver), "get"), "https://t.me/s/klfjezlkjfzlek")
_l_(348358)
test = _c_(348364, _a_(348360, _n_(348359, "driver", lambda: driver), "find_element"), _c_(348363, _a_(348362, _n_(348361, "By", lambda: By), "XPATH"), "//html//body//main//div//section//div//div//div//div[@class='tgme_widget_message_text js-message_text before_footer'][last()]"))
_l_(348365)
source_code = _a_(348367, _n_(348366, "test", lambda: test), "text")
_l_(348368)
_c_(348371, _n_(348369, "print", lambda: print), _n_(348370, "source_code", lambda: source_code))
_l_(348372)