# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from time import time, sleep
    _l_(396739)

except ImportError:
    pass
try:
    from selenium.webdriver import Chrome
    _l_(396741)

except ImportError:
    pass
try:
    from selenium.webdriver.chrome.options import Options
    _l_(396743)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(396745)

except ImportError:
    pass
try:
    from selenium.webdriver.remote.webelement import WebElement
    _l_(396747)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(396749)

except ImportError:
    pass
try:
    from selenium.webdriver.support.wait import WebDriverWait
    _l_(396751)

except ImportError:
    pass
try:
    from webdriver_manager.chrome import ChromeDriverManager
    _l_(396753)

except ImportError:
    pass
try:
    from selenium.webdriver.common.action_chains import ActionChains
    _l_(396755)

except ImportError:
    pass
try:
    from args_parser import ArgsParser
    _l_(396757)

except ImportError:
    pass
try:
    from downloader import download_file
    _l_(396759)

except ImportError:
    pass

args = _c_(396761, _n_(396760, "ArgsParser", lambda: ArgsParser))
_l_(396762)


def print_if_verbose(val):
    _l_(396770)

    if _a_(396764, _n_(396763, "args", lambda: args), "output_verbose"):
        _l_(396769)

        _c_(396767, _n_(396765, "print", lambda: print), _n_(396766, "val", lambda: val))
        _l_(396768)


WAITING_TIMEOUT = 180
_l_(396771)
chrome_options = _c_(396773, _n_(396772, "Options", lambda: Options))
_l_(396774)
driver_user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
_l_(396775)
_c_(396779, _a_(396777, _n_(396776, "chrome_options", lambda: chrome_options), "add_argument"), f'user-agent={_n_(396778, "driver_user_agent", lambda: driver_user_agent)}')
_l_(396780)
if not _a_(396782, _n_(396781, 'args', lambda: args), 'display_browser'):
    _l_(396787)

    _c_(396785, _a_(396784, _n_(396783, 'chrome_options', lambda: chrome_options), 'add_argument'), '--headless')
    _l_(396786)
try:
    _l_(396813)

    driver = _c_(396794, _n_(396788, 'Chrome', lambda: Chrome), _c_(396792, _a_(396791, _c_(396790, _n_(396789, 'ChromeDriverManager', lambda: ChromeDriverManager)), 'install')), options=_n_(396793, 'chrome_options', lambda: chrome_options))
    _l_(396795)
except _n_(396796, 'Exception', lambda: Exception) as e:
    _l_(396812)

    _c_(396799, _n_(396797, 'print', lambda: print), _n_(396798, 'e', lambda: e))
    _l_(396800)
    try:
        _l_(396811)

        driver = _c_(396803, _n_(396801, 'Chrome', lambda: Chrome), "./chromedriver", options=_n_(396802, 'chrome_options', lambda: chrome_options))
        _l_(396804)
    except _n_(396805, 'Exception', lambda: Exception):
        _l_(396810)

        driver = _c_(396808, _n_(396806, 'Chrome', lambda: Chrome), "chromedriver.exe", options=_n_(396807, 'chrome_options', lambda: chrome_options))
        _l_(396809)