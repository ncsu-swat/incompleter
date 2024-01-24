# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64906323/typeerror-get-missing-1-required-positional-argument-url-using-chromedrive
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(636602)

except ImportError:
    pass

driver = _a_(636604, _n_(636603, "webdriver", lambda: webdriver), "Chrome")
_l_(636605)

_c_(636608, _a_(636607, _n_(636606, "driver", lambda: driver), "get"), 'https://www.walmart.com/')
_l_(636609)