# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76428561/typeerror-webdriver-init-got-multiple-values-for-argument-options
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
chrome_options = _c_(376837, _n_(376836, "Options", lambda: Options))
_l_(376838)
_c_(376841, _a_(376840, _n_(376839, "chrome_options", lambda: chrome_options), "add_argument"), '--headless')
_l_(376842)
_c_(376845, _a_(376844, _n_(376843, "chrome_options", lambda: chrome_options), "add_argument"), '--no-sandbox')
_l_(376846)
_c_(376849, _a_(376848, _n_(376847, "chrome_options", lambda: chrome_options), "add_argument"), '--disable-dev-shm-usage')
_l_(376850)

browser = _c_(376854, _a_(376852, _n_(376851, "webdriver", lambda: webdriver), "Chrome"), r'/usr/bin/chromedriver', options=_n_(376853, "chrome_options", lambda: chrome_options))
_l_(376855)