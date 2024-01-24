# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76550506/typeerror-webdriver-init-got-an-unexpected-keyword-argument-executable-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(419235)

except ImportError:
    pass
try:
    from selenium.webdriver.chrome.options import Options
    _l_(419237)

except ImportError:
    pass

option = _c_(419240, _a_(419239, _n_(419238, "webdriver", lambda: webdriver), "ChromeOptions"))
_l_(419241)
driver = _c_(419245, _a_(419243, _n_(419242, "webdriver", lambda: webdriver), "Chrome"), executable_path='./chromedriver.exe', options=_n_(419244, "option", lambda: option))
_l_(419246)

_c_(419249, _a_(419248, _n_(419247, "driver", lambda: driver), "get"), 'https://www.google.com/')
_l_(419250)