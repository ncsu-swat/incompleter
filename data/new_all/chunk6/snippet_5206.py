# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61208342/attributeerror-trying-to-automate-whatsapp-using-selenium-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(351239)

except ImportError:
    pass
try:
    from selenium.webdriver.support.ui  import WebDriverWait
    _l_(351241)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(351243)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(351245)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(351247)

except ImportError:
    pass
try:
    import time
    _l_(351249)

except ImportError:
    pass

driver = _c_(351252, _a_(351251, _n_(351250, "webdriver", lambda: webdriver), "Edge"), r"C:\Users\Manan\Downloads\edgedriver_win64\msedgedriver") 
_l_(351253) 
_c_(351256, _a_(351255, _n_(351254, "driver", lambda: driver), "get"), "https://web.whatsapp.com/")
_l_(351257)
wait = _c_(351260, _n_(351258, "WebDriverWait", lambda: WebDriverWait), _n_(351259, "driver", lambda: driver),600)
_l_(351261)
target = "Dad"
_l_(351262)
string = "message send from manan!!"
_l_(351263)
x_arg ='//span[contains(@title,'+ _n_(351264, "target", lambda: target) + ')]'
_l_(351265)
target = _c_(351274, _a_(351267, _n_(351266, "wait", lambda: wait), "until"), _c_(351273, _a_(351269, _n_(351268, "EC", lambda: EC), "presence_of_all_elements_located"), (_a_(351271, _n_(351270, "By", lambda: By), "XPATH"), _n_(351272, "x_arg", lambda: x_arg))))
_l_(351275)
_c_(351278, _a_(351277, _n_(351276, "target", lambda: target), "click"))
_l_(351279)