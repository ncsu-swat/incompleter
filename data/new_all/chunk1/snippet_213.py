# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70125758/attributeerror-options-object-has-no-attribute-set-headless
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from webbrowser import Chrome
    _l_(415697)

except ImportError:
    pass
try:
    from dolphin.common.commonlogger import CommonLogger
    _l_(415699)

except ImportError:
    pass
try:
    from selenium.webdriver import chrome
    _l_(415701)

except ImportError:
    pass
try:
    from selenium.webdriver.chrome.options import Options
    _l_(415703)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(415705)

except ImportError:
    pass


class FetchMusic:
    _l_(415710)


    def __init__(self):
        _l_(415709)

        _c_(415707, _n_(415706, "print", lambda: print), "fetch...")
        _l_(415708)


if _n_(415711, "__name__", lambda: __name__) == '__main__':
    _l_(415745)

    opts = _c_(415713, _n_(415712, "Options", lambda: Options))
    _l_(415714)
    _c_(415717, _a_(415716, _n_(415715, "opts", lambda: opts), "set_headless"))
    _l_(415718)
    assert _a_(415720, _n_(415719, "opts", lambda: opts), "headless")  # Operating in headless mode
    _l_(415721)  # Operating in headless mode
    browser = _c_(415724, _n_(415722, "Chrome", lambda: Chrome), executable_path=r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                     options=_n_(415723, "opts", lambda: opts))
    _l_(415725)
    _c_(415728, _a_(415727, _n_(415726, "browser", lambda: browser), "implicitly_wait"), 3)
    _l_(415729)
    _c_(415732, _a_(415731, _n_(415730, "browser", lambda: browser), "get"), 'https://ca.finance.yahoo.com/quote/AMZN/profile?p=AMZN')
    _l_(415733)
    results = _c_(415736, _a_(415735, _n_(415734, "browser", lambda: browser), "find_elements_by_xpath"), '//*[@id="quote-header-info"]/div[3]/div/div/span[1]')
    _l_(415737)
    for result in _n_(415738, "results", lambda: results):
        _l_(415744)

        _c_(415742, _n_(415739, "print", lambda: print), _a_(415741, _n_(415740, "result", lambda: result), "text"))
        _l_(415743)