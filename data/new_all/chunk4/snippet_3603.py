# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71448341/typeerror-object-of-type-numpy-int64-has-no-len-selenium
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(627163)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(627165)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(627167)

except ImportError:
    pass

df = _c_(627170, _a_(627169, _n_(627168, "pd", lambda: pd), "read_excel"), 'data.xlsx')
_l_(627171)
_c_(627175, _n_(627172, "print", lambda: print), _a_(627174, _n_(627173, "df", lambda: df), "iloc")[1])
_l_(627176)

browser = _c_(627179, _a_(627178, _n_(627177, "webdriver", lambda: webdriver), "Chrome"))
_l_(627180)
_c_(627183, _a_(627182, _n_(627181, "browser", lambda: browser), "get"), 'https://my.web.site')
_l_(627184)

for i in _a_(627186, _n_(627185, "df", lambda: df), "index"):
    _l_(627221)

    entry = _a_(627188, _n_(627187, "df", lambda: df), "iloc")[_n_(627189, "i", lambda: i)]
    _l_(627190)
    _c_(627193, _n_(627191, "print", lambda: print), _n_(627192, "entry", lambda: entry)["CN"])
    _l_(627194)
    _c_(627197, _n_(627195, "print", lambda: print), _n_(627196, "entry", lambda: entry)["NIN"])
    _l_(627198)
    CarteNational = _c_(627203, _a_(627200, _n_(627199, "browser", lambda: browser), "find_element"), _a_(627202, _n_(627201, "By", lambda: By), "XPATH"), '/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div/input')
    _l_(627204)
    _c_(627208, _a_(627206, _n_(627205, "CarteNational", lambda: CarteNational), "send_keys"), _n_(627207, "entry", lambda: entry)["CN"])
    _l_(627209)
    NumeroIdentification = _c_(627214, _a_(627211, _n_(627210, "browser", lambda: browser), "find_element"), _a_(627213, _n_(627212, "By", lambda: By), "XPATH"), '/html/body/div/div[2]/div/div[2]/div[2]/div/form/div/div[5]/div/div/input')
    _l_(627215)
    _c_(627219, _a_(627217, _n_(627216, "NumeroIdentification", lambda: NumeroIdentification), "send_keys"), _n_(627218, "entry", lambda: entry)["NIN"])
    _l_(627220)