# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39957316/typeerror-init-takes-2-positional-arguments-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from termcolor import colored
    _l_(606823)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(606825)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(606827)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(606829)

except ImportError:
    pass
try:
    from selenium.webdriver.support.ui import WebDriverWait
    _l_(606831)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(606833)

except ImportError:
    pass
try:
    from selenium.common.exceptions import TimeoutException
    _l_(606835)

except ImportError:
    pass


myfile = [_c_(606838, _a_(606837, _n_(606836, "p", lambda: p), "rstrip")) for p in _c_(606840, _n_(606839, "open", lambda: open), 'test.txt')]
_l_(606841)

for ip in _n_(606842, "myfile", lambda: myfile):
    _l_(606883)


    driver = _c_(606845, _a_(606844, _n_(606843, "webdriver", lambda: webdriver), "Chrome"), './lib/chromedriver.exe')
    _l_(606846)
    _c_(606850, _a_(606848, _n_(606847, "driver", lambda: driver), "get"), "http://admin:password@" + _n_(606849, "ip", lambda: ip))
    _l_(606851)
    try:
        _l_(606882)

        element = _c_(606861, _a_(606855, _c_(606854, _n_(606852, "WebDriverWait", lambda: WebDriverWait), _n_(606853, "driver", lambda: driver), 20), "until"), _c_(606860, _a_(606857, _n_(606856, "EC", lambda: EC), "presence_of_element_located"), _a_(606859, _n_(606858, "By", lambda: By), "XPATH"), ".//*/tbody/tr/td/table/tbody/tr[2]/td[2]")
        )
        _l_(606862)
    except _n_(606863, "TimeoutException", lambda: TimeoutException):
        _l_(606870)

        _c_(606868, _n_(606864, "print", lambda: print), _c_(606867, _n_(606865, "colored", lambda: colored), _n_(606866, "ip", lambda: ip) + " except timeout error", "red"))
        _l_(606869)

    else:
        _c_(606875, _n_(606871, "print", lambda: print), _c_(606874, _n_(606872, "colored", lambda: colored), _n_(606873, "ip", lambda: ip) + " is OK", "green"))
        _l_(606876)
    finally:
        _l_(606881)

        _c_(606879, _a_(606878, _n_(606877, "driver", lambda: driver), "quit"))
        _l_(606880)