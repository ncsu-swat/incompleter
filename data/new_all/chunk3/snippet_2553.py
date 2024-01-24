# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71764549/python-error-attributeerror-enter-using-selenium
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from asyncio import selector_events
    _l_(539620)

except ImportError:
    pass
try:
    from lib2to3.pgen2 import driver
    _l_(539622)

except ImportError:
    pass
try:
    import booking.constants as const
    _l_(539624)

except ImportError:
    pass
try:
    import os
    _l_(539626)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(539628)

except ImportError:
    pass
try:
    from webdriver_manager.chrome import ChromeDriverManager
    _l_(539630)

except ImportError:
    pass
try:
    from selenium.webdriver.chrome.service import Service
    _l_(539632)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(539634)

except ImportError:
    pass

class Booking:
    _l_(539695)

    def __init__(self, teardown = False):
        _l_(539664)

        s = _c_(539640, _n_(539635, "Service", lambda: Service), _c_(539639, _a_(539638, _c_(539637, _n_(539636, "ChromeDriverManager", lambda: ChromeDriverManager)), "install")))
        _l_(539641)
        _n_(539642, "self", lambda: self).driver = _c_(539646, _a_(539644, _n_(539643, "webdriver", lambda: webdriver), "Chrome"), service=_n_(539645, "s", lambda: s))
        _l_(539647)
        _c_(539653, _a_(539650, _a_(539649, _n_(539648, "self", lambda: self), "driver"), "get"), _a_(539652, _n_(539651, "const", lambda: const), "BASE_URL"))
        _l_(539654)
        _a_(539656, _n_(539655, "self", lambda: self), "driver").teardown = _n_(539657, "teardown", lambda: teardown)
        _l_(539658)
        _c_(539662, _a_(539661, _a_(539660, _n_(539659, "self", lambda: self), "driver"), "implicitly_wait"), 15)
        _l_(539663)

    def __exit__(self, exc_type, exc_val, exc_tb):
        _l_(539674)

        if _a_(539667, _a_(539666, _n_(539665, "self", lambda: self), "driver"), "teardown"):
            _l_(539673)

            _c_(539671, _a_(539670, _a_(539669, _n_(539668, "self", lambda: self), "driver"), "quit"))
            _l_(539672)

    def cookies(self):
        _l_(539684)

        _c_(539682, _a_(539681, _c_(539680, _a_(539677, _a_(539676, _n_(539675, "self", lambda: self), "driver"), "find_element"), _a_(539679, _n_(539678, "By", lambda: By), "ID"), 'onetrust-accept-btn-handler'), "click"))
        _l_(539683)

    def select_place_to_go(self):
        _l_(539694)

        _c_(539692, _a_(539691, _c_(539690, _a_(539687, _a_(539686, _n_(539685, "self", lambda: self), "driver"), "find_element"), _a_(539689, _n_(539688, "By", lambda: By), "ID"), "ss"), "click"))
        _l_(539693)