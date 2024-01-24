# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67154104/exception-has-occurred-attributeerror-webdriver-object-has-no-attribute-link
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(459147)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(459149)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(459151)

except ImportError:
    pass
try:
    from selenium.webdriver.chrome.options import Options
    _l_(459153)

except ImportError:
    pass
try:
    from selenium.webdriver.support.ui import WebDriverWait
    _l_(459155)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(459157)

except ImportError:
    pass
try:
    import webbrowser
    _l_(459159)

except ImportError:
    pass
try:
    import time
    _l_(459161)

except ImportError:
    pass
try:
    import os
    _l_(459163)

except ImportError:
    pass

urls = [
    "URL 1",
    "URL 2"
]
_l_(459164)

PATH = "C:\Program Files (x86)\chromedriver.exe"
_l_(459165)

options = _c_(459167, _n_(459166, "Options", lambda: Options))
_l_(459168)
_c_(459171, _a_(459170, _n_(459169, "options", lambda: options), "add_argument"), '--headless')
_l_(459172)
_c_(459175, _a_(459174, _n_(459173, "options", lambda: options), "add_argument"), '--disable-gpu')
_l_(459176)
driver = _c_(459181, _a_(459178, _n_(459177, "webdriver", lambda: webdriver), "Chrome"), _n_(459179, "PATH", lambda: PATH), chrome_options=_n_(459180, "options", lambda: options))
_l_(459182)

def main():
    _l_(459233)

    
    # stuff
    while True:
        _l_(459232)

        for i in _c_(459187, _n_(459183, "range", lambda: range), 0, _c_(459186, _n_(459184, "len", lambda: len), _n_(459185, "urls", lambda: urls))):
            _l_(459231)

            url = _n_(459188, "urls", lambda: urls)[_n_(459189, "i", lambda: i)]
            _l_(459190)
            _c_(459193, _a_(459192, _n_(459191, "time", lambda: time), "sleep"), 2)
            _l_(459194)
            _c_(459197, _n_(459195, "print", lambda: print), _n_(459196, "url", lambda: url))
            _l_(459198)
            wait = _c_(459201, _n_(459199, "WebDriverWait", lambda: WebDriverWait), _n_(459200, "driver", lambda: driver), 10)
            _l_(459202)
            _c_(459206, _a_(459204, _n_(459203, "driver", lambda: driver), "link"), _n_(459205, "url", lambda: url))
            _l_(459207)
            _c_(459215, _a_(459209, _n_(459208, "wait", lambda: wait), "until"), _c_(459214, _a_(459211, _n_(459210, "EC", lambda: EC), "element_to_be_clickable"), (_a_(459213, _n_(459212, "By", lambda: By), "XPATH"), '//*[@id="availability"]/span')))
            _l_(459216)
            _c_(459220, _n_(459217, "print", lambda: print), _a_(459219, _n_(459218, "driver", lambda: driver), "title"))
            _l_(459221)
            availablility = _c_(459224, _a_(459223, _n_(459222, "driver", lambda: driver), "find_element_by_xpath"), '//*[@id="availability"]/span')
            _l_(459225)
            _c_(459229, _n_(459226, "print", lambda: print), _a_(459228, _n_(459227, "availablility", lambda: availablility), "text"))
            _l_(459230)

_c_(459235, _n_(459234, "main", lambda: main))
_l_(459236)