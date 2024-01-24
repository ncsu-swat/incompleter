# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40554805/attributeerror-module-selenium-webdriver-has-no-attribute-firefox
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(562515)

except ImportError:
    pass
try:
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    _l_(562517)

except ImportError:
    pass

binary = _c_(562519, _n_(562518, "FirefoxBinary", lambda: FirefoxBinary), 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
_l_(562520)
browser = _c_(562524, _a_(562522, _n_(562521, "webdriver", lambda: webdriver), "Firefox"), firefox_binary=_n_(562523, "binary", lambda: binary))
_l_(562525)