# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56406492/attributeerror-module-datetime-has-no-attribute-today-error-while-executing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver as wd
    _l_(442292)

except ImportError:
    pass

driver = _c_(442295, _a_(442294, _n_(442293, "wd", lambda: wd), "Firefox"), executable_path=r'C:\Users\User\Downloads\geckodriver-v0.24.0-win64')
_l_(442296)
_c_(442299, _a_(442298, _n_(442297, "driver", lambda: driver), "get"), 'https://youtube.com')
_l_(442300)