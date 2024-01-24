# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74023972/i-am-trying-to-run-this-code-and-getting-error-attributeerror-webdriver-objec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(596622, _a_(596621, _n_(596620, "driver", lambda: driver), "get"), "https://opensource-demo.orangehrmlive.com/")
_l_(596623)
_c_(596628, _a_(596627, _c_(596626, _a_(596625, _n_(596624, "driver", lambda: driver), "find_element_by_name"), "txtUsername"), "send_keys"), "Admin")
_l_(596629)
_c_(596634, _a_(596633, _c_(596632, _a_(596631, _n_(596630, "driver", lambda: driver), "find_element_by_id"), "txtPassword"), "send_keys"), "admin123")
_l_(596635)
_c_(596640, _a_(596639, _c_(596638, _a_(596637, _n_(596636, "driver", lambda: driver), "find_element_by_id"), "btnLogin"), "click"))
_l_(596641)

act_title=_a_(596643, _n_(596642, "driver", lambda: driver), "title")
_l_(596644)
exp_title="OrangeHRM"
_l_(596645)

if _n_(596646, "act_title", lambda: act_title)==_n_(596647, "exp_title", lambda: exp_title):
    _l_(596654)

    _c_(596649, _n_(596648, "print", lambda: print), "Login test pass")
    _l_(596650)
else:
    _c_(596652, _n_(596651, "print", lambda: print), "Login test fail")
    _l_(596653)

_c_(596657, _a_(596656, _n_(596655, "driver", lambda: driver), "close"))
_l_(596658)