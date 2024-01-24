# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62907338/filenotfounderror-with-selenium-python-3-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from time import sleep
    _l_(692230)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(692232)

except ImportError:
    pass
driver = _c_(692235, _a_(692234, _n_(692233, "webdriver", lambda: webdriver), "Firefox"), executable_path='/opt/geckoDriver/geckodriver.exe')
_l_(692236)
_c_(692239, _a_(692238, _n_(692237, "driver", lambda: driver), "get"), 'https://instagram.com/')
_l_(692240)
_c_(692242, _n_(692241, "sleep", lambda: sleep), 5)
_l_(692243)
_c_(692246, _a_(692245, _n_(692244, "driver", lambda: driver), "close"))
_l_(692247)