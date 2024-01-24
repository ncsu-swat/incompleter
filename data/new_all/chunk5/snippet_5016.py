# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65250730/typeerror-str-object-is-not-callable-in-driver-title
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(687687)

except ImportError:
    pass
path = "C:\Program Files\chromedriver.exe"
_l_(687688)
driver = _c_(687692, _a_(687690, _n_(687689, "webdriver", lambda: webdriver), "Chrome"), _n_(687691, "path", lambda: path))
_l_(687693)
_c_(687696, _a_(687695, _n_(687694, "driver", lambda: driver), "get")) # in the parentheses is a link like https://link.com/
_l_(687697) # in the parentheses is a link like https://link.com/
_c_(687702, _n_(687698, "print", lambda: print), _c_(687701, _a_(687700, _n_(687699, "driver", lambda: driver), "title")))
_l_(687703)
_c_(687706, _a_(687705, _n_(687704, "driver", lambda: driver), "quit"))
_l_(687707)