# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63881917/typeerror-module-object-is-not-callable-using-seleniumthrough-python-in-pycha
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(595229)

except ImportError:
    pass

driver=_c_(595232, _a_(595231, _n_(595230, "webdriver", lambda: webdriver), "firefox"), "D:\Pycharm_automation\geckodriver-v0.27.0-win64\geckodriver.exe")
_l_(595233)
_c_(595236, _a_(595235, _n_(595234, "driver", lambda: driver), "get"), "google.com")
_l_(595237)