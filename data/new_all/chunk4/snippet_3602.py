# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71450772/flask-pytest-failed-tests-test-data-response-pytest-post-data-response-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(642618, "dataclass", lambda: dataclass)
class SeleniumElements:
    _l_(642723)

    search_page: _n_(642619, "str", lambda: str)
    _l_(642620)
    response_page: _n_(642621, "str", lambda: str)
    _l_(642622)
    selenium_id: _n_(642623, "str", lambda: str)
    _l_(642624)
    selenium_class: _n_(642625, "str", lambda: str)
    _l_(642626)
    search_data: _n_(642627, "str", lambda: str)
    _l_(642628)
    driver: _n_(642629, "str", lambda: str)
    _l_(642630)
    
    def element_search_max_time(self,sec):
        _l_(642637)

        aux = _c_(642635, _a_(642633, _a_(642632, _n_(642631, "self", lambda: self), "driver"), "implicitly_wait"), _n_(642634, "sec", lambda: sec))
        _l_(642636)
        return aux
  
    def get_data(self):
        _l_(642722)

        _c_(642643, _a_(642640, _a_(642639, _n_(642638, "self", lambda: self), "driver"), "get"), _a_(642642, _n_(642641, "self", lambda: self), "search_page"))
        _l_(642644)
        _c_(642647, _a_(642646, _n_(642645, "self", lambda: self), "element_search_max_time"), 30)
        _l_(642648)
        to_search = _c_(642656, _a_(642651, _a_(642650, _n_(642649, "self", lambda: self), "driver"), "find_element"), _a_(642653, _n_(642652, "By", lambda: By), "ID"), _a_(642655, _n_(642654, "self", lambda: self), "selenium_id"))
        _l_(642657)
        _c_(642660, _a_(642659, _n_(642658, "to_search", lambda: to_search), "click"))
        _l_(642661)
        _c_(642666, _a_(642663, _n_(642662, "to_search", lambda: to_search), "send_keys"), _a_(642665, _n_(642664, "self", lambda: self), "search_data"))
        _l_(642667)
        submit = _c_(642675, _a_(642670, _a_(642669, _n_(642668, "self", lambda: self), "driver"), "find_element"), _a_(642672, _n_(642671, "By", lambda: By), "CLASS_NAME"),_a_(642674, _n_(642673, "self", lambda: self), "selenium_class"))
        _l_(642676)
        _c_(642679, _a_(642678, _n_(642677, "submit", lambda: submit), "click"))
        _l_(642680)
        _c_(642683, _a_(642682, _n_(642681, "self", lambda: self), "element_search_max_time"), 30)
        _l_(642684)
        fund_response = _c_(642689, _a_(642686, _n_(642685, "requests", lambda: requests), "get"), _a_(642688, _n_(642687, "self", lambda: self), "search_page"))
        _l_(642690)
        assert _a_(642692, _n_(642691, "fund_response", lambda: fund_response), "status_code") == 200
        _l_(642693)
        _c_(642696, _a_(642695, _n_(642694, "self", lambda: self), "element_search_max_time"), 30)
        _l_(642697)
        round_store_href_link = _c_(642703, _a_(642700, _a_(642699, _n_(642698, "self", lambda: self), "driver"), "find_element"), _a_(642702, _n_(642701, "By", lambda: By), "XPATH"), '//*[@id="main-content"]/div[4]/div/h1/a')
        _l_(642704)
        _c_(642707, _a_(642706, _n_(642705, "round_store_href_link", lambda: round_store_href_link), "click"))
        _l_(642708)
        _c_(642711, _a_(642710, _n_(642709, "self", lambda: self), "element_search_max_time"), 30)
        _l_(642712)
        rounds_response = _c_(642717, _a_(642714, _n_(642713, "requests", lambda: requests), "get"), _a_(642716, _n_(642715, "self", lambda: self), "response_page"))
        _l_(642718)
        assert _a_(642720, _n_(642719, "rounds_response", lambda: rounds_response), "status_code") == 200
        _l_(642721)