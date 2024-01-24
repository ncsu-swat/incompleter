# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62907338/filenotfounderror-with-selenium-python-3-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from time import sleep
    _l_(657293)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(657295)

except ImportError:
    pass
driver = _c_(657298, _a_(657297, _n_(657296, "webdriver", lambda: webdriver), "Firefox"), executable_path='/opt/geckoDriver/geckodriver.exe')
_l_(657299)
_c_(657302, _a_(657301, _n_(657300, "driver", lambda: driver), "get"), 'https://instagram.com/')
_l_(657303)
_c_(657305, _n_(657304, "sleep", lambda: sleep), 5)
_l_(657306)
_c_(657309, _a_(657308, _n_(657307, "driver", lambda: driver), "close"))
_l_(657310)