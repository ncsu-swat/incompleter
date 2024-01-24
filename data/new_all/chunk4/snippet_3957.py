# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64906323/typeerror-get-missing-1-required-positional-argument-url-using-chromedrive
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(581631)

except ImportError:
    pass

driver = _a_(581633, _n_(581632, "webdriver", lambda: webdriver), "Chrome")
_l_(581634)

_c_(581637, _a_(581636, _n_(581635, "driver", lambda: driver), "get"), 'https://www.walmart.com/')
_l_(581638)