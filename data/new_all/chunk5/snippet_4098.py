# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62907338/filenotfounderror-with-selenium-python-3-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from time import sleep
    _l_(663424)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(663426)

except ImportError:
    pass
driver = _c_(663429, _a_(663428, _n_(663427, "webdriver", lambda: webdriver), "Firefox"), executable_path='/opt/geckoDriver/geckodriver.exe')
_l_(663430)
_c_(663433, _a_(663432, _n_(663431, "driver", lambda: driver), "get"), 'https://instagram.com/')
_l_(663434)
_c_(663436, _n_(663435, "sleep", lambda: sleep), 5)
_l_(663437)
_c_(663440, _a_(663439, _n_(663438, "driver", lambda: driver), "close"))
_l_(663441)