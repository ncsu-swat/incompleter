# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61208342/attributeerror-trying-to-automate-whatsapp-using-selenium-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(370048)

except ImportError:
    pass
try:
    from selenium.webdriver.support.ui  import WebDriverWait
    _l_(370050)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(370052)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(370054)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(370056)

except ImportError:
    pass
try:
    import time
    _l_(370058)

except ImportError:
    pass

driver = _c_(370061, _a_(370060, _n_(370059, "webdriver", lambda: webdriver), "Edge"), r"C:\Users\Manan\Downloads\edgedriver_win64\msedgedriver") 
_l_(370062) 
_c_(370065, _a_(370064, _n_(370063, "driver", lambda: driver), "get"), "https://web.whatsapp.com/")
_l_(370066)
wait = _c_(370069, _n_(370067, "WebDriverWait", lambda: WebDriverWait), _n_(370068, "driver", lambda: driver),600)
_l_(370070)
target = "Dad"
_l_(370071)
string = "message send from manan!!"
_l_(370072)
x_arg ='//span[contains(@title,'+ _n_(370073, "target", lambda: target) + ')]'
_l_(370074)
target = _c_(370083, _a_(370076, _n_(370075, "wait", lambda: wait), "until"), _c_(370082, _a_(370078, _n_(370077, "EC", lambda: EC), "presence_of_all_elements_located"), (_a_(370080, _n_(370079, "By", lambda: By), "XPATH"), _n_(370081, "x_arg", lambda: x_arg))))
_l_(370084)
_c_(370087, _a_(370086, _n_(370085, "target", lambda: target), "click"))
_l_(370088)