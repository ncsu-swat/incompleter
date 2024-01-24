# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60574127/typeerror-nonetype-object-is-not-callable-selenium
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium import webdriver
    _l_(532382)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(532384)

except ImportError:
    pass

driver=_c_(532387, _a_(532386, _n_(532385, "webdriver", lambda: webdriver), "Chrome"), 'H:\datascience-python\selinium\chromedriver.exe')
_l_(532388)

_c_(532391, _a_(532390, _n_(532389, "driver", lambda: driver), "get"), 'https://www.aljazeera.com/news/')
_l_(532392)

button = _c_(532395, _a_(532394, _n_(532393, "driver", lambda: driver), "find_element_by_id"), 'btn_showmore_b1_418')
_l_(532396)

_c_(532400, _a_(532398, _n_(532397, "driver", lambda: driver), "execute_script"), "arguments[0].click();", _n_(532399, "button", lambda: button))
_l_(532401)

content = _a_(532403, _n_(532402, "driver", lambda: driver), "page_source")
_l_(532404)

soup = _c_(532407, _n_(532405, "BeautifulSoup", lambda: BeautifulSoup), _n_(532406, "content", lambda: content), 'html.parser')
_l_(532408)

container = _c_(532411, _a_(532410, _n_(532409, "soup", lambda: soup), "select"), 'div.topics-sec-item-cont')
_l_(532412)

titlelist = []
_l_(532413)

urllist = []
_l_(532414)

for items in  _n_(532415, "container", lambda: container):
    _l_(532451)


    if _n_(532416, "items", lambda: items) is not None:
        _l_(532450)


        title = _a_(532420, _c_(532419, _a_(532418, _n_(532417, "items", lambda: items), "find_element_by_xpath"), '//div[@class="col-sm-7 topics-sec-item-cont"]/a/h2'), "text")
        _l_(532421)

        url = _c_(532424, _a_(532423, _n_(532422, "items", lambda: items), "find_element_by_xpath"), '//div[@class="col-sm-7 topics-sec-item-cont"]/a')
        _l_(532425)

        _c_(532429, _a_(532427, _n_(532426, "titlelist", lambda: titlelist), "append"), _n_(532428, "title", lambda: title))
        _l_(532430)

        _c_(532436, _a_(532432, _n_(532431, "urllist", lambda: urllist), "append"), _c_(532435, _a_(532434, _n_(532433, "url", lambda: url), "get_attribute"), 'href'))
        _l_(532437)

        _c_(532442, _n_(532438, "print", lambda: print), _c_(532441, _n_(532439, "str", lambda: str), _n_(532440, "titlelist", lambda: titlelist)) + '\n')
        _l_(532443)

        _c_(532448, _n_(532444, "print", lambda: print), _c_(532447, _n_(532445, "str", lambda: str), _n_(532446, "urllist", lambda: urllist)) + '\n')
        _l_(532449)