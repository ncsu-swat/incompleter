# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66296031/why-driver-find-elements-by-class-name-click-results-in-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from webdriver_manager.chrome import ChromeDriverManager
    _l_(534552)

except ImportError:
    pass
try:
    from selenium.webdriver.support.select import Select
    _l_(534554)

except ImportError:
    pass
try:
    import time
    _l_(534556)

except ImportError:
    pass

driver = _c_(534563, _a_(534558, _n_(534557, "webdriver", lambda: webdriver), "Chrome"), _c_(534562, _a_(534561, _c_(534560, _n_(534559, "ChromeDriverManager", lambda: ChromeDriverManager)), "install")))
_l_(534564)
_c_(534567, _a_(534566, _n_(534565, "driver", lambda: driver), "get"), 'https://website.com/signup')
_l_(534568)
_c_(534571, _a_(534570, _n_(534569, "time", lambda: time), "sleep"), 1)
_l_(534572)

button = _c_(534575, _a_(534574, _n_(534573, "driver", lambda: driver), "find_elements_by_class_name"), "continue")
_l_(534576)
_c_(534579, _a_(534578, _n_(534577, "button", lambda: button), "click"))
_l_(534580)
_c_(534583, _a_(534582, _n_(534581, "time", lambda: time), "sleep"), 1)
_l_(534584)