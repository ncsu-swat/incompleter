# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65250730/typeerror-str-object-is-not-callable-in-driver-title
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(692307)

except ImportError:
    pass
path = "C:\Program Files\chromedriver.exe"
_l_(692308)
driver = _c_(692312, _a_(692310, _n_(692309, "webdriver", lambda: webdriver), "Chrome"), _n_(692311, "path", lambda: path))
_l_(692313)
_c_(692316, _a_(692315, _n_(692314, "driver", lambda: driver), "get")) # in the parentheses is a link like https://link.com/
_l_(692317) # in the parentheses is a link like https://link.com/
_c_(692322, _n_(692318, "print", lambda: print), _c_(692321, _a_(692320, _n_(692319, "driver", lambda: driver), "title")))
_l_(692323)
_c_(692326, _a_(692325, _n_(692324, "driver", lambda: driver), "quit"))
_l_(692327)