# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76429200/attributeerror-nonetype-object-has-no-attribute-send-keys-plz-rply
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(361681)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(361683)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(361685)

except ImportError:
    pass

driver = _c_(361688, _a_(361687, _n_(361686, "webdriver", lambda: webdriver), "Chrome"), r"C:\Users\ram.sn\Desktop\New folder\chromedriver_win32 (2)\chromedriver.exe")
_l_(361689)

_c_(361692, _a_(361691, _n_(361690, "driver", lambda: driver), "get"), "https://www.nopcommerce.com/en/login")
_l_(361693)

_c_(361698, _a_(361697, _c_(361696, _a_(361695, _n_(361694, "driver", lambda: driver), "find_element_by_id"), "Username"), "send_keys"), "test")
_l_(361699)