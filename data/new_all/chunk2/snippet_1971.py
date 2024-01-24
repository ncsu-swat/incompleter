# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74348377/python-selenium-by-raises-attributeerror-type-object-by-has-no-attribute-xpa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main_test():
    _l_(460690)

    chrome_options = _c_(460642, _n_(460641, "Options", lambda: Options))
    _l_(460643)
    prefs = {"download.default_directory": f"{_c_(460646, _a_(460645, _n_(460644, 'os', lambda: os), 'getcwd'))}/Music"}
    _l_(460647)
    _c_(460650, _a_(460649, _n_(460648, "chrome_options", lambda: chrome_options), "add_argument"), "user-data-dir=selenium")
    _l_(460651)
    _c_(460655, _a_(460653, _n_(460652, "chrome_options", lambda: chrome_options), "add_experimental_option"), "prefs", _n_(460654, "prefs", lambda: prefs))
    _l_(460656)
    dr = _c_(460666, _a_(460658, _n_(460657, "webdriver", lambda: webdriver), "Chrome"), options=_n_(460659, "chrome_options", lambda: chrome_options), service=_c_(460665, _n_(460660, "Service", lambda: Service), _c_(460664, _a_(460663, _c_(460662, _n_(460661, "ChromeDriverManager", lambda: ChromeDriverManager)), "install"))))
    _l_(460667)
    _c_(460671, _a_(460669, _n_(460668, "dr", lambda: dr), "get"), _n_(460670, "URL", lambda: URL))
    _l_(460672)
    _c_(460676, _n_(460673, "print", lambda: print), f"{_a_(460675, _n_(460674, 'selenium', lambda: selenium), '__version__')=}")
    _l_(460677)
    _c_(460684, _a_(460683, _c_(460682, _a_(460679, _n_(460678, "dr", lambda: dr), "find_element"), _a_(460681, _n_(460680, "By", lambda: By), "XPATH"), "/html/body/div[1]/div[1]/div/div[1]/ul/li[2]/a"), "click"))
    _l_(460685)
    _c_(460688, _a_(460687, _n_(460686, "dr", lambda: dr), "quit"))
    _l_(460689)


if _n_(460691, "__name__", lambda: __name__) == '__main__':
    _l_(460695)

    _c_(460693, _n_(460692, "main_test", lambda: main_test))
    _l_(460694)