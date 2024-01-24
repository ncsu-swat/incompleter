# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50799363/when-i-run-my-test-suite-i-am-getting-a-typeerror-i-am-not-able-to-understand-wh
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pages.Home.category_page import CategoryPage
    _l_(447693)

except ImportError:
    pass
try:
    from utilites.testStatus import TestStatus
    _l_(447695)

except ImportError:
    pass
try:
    import pytest
    _l_(447697)

except ImportError:
    pass
try:
    import unittest
    _l_(447699)

except ImportError:
    pass
try:
    import time
    _l_(447701)

except ImportError:
    pass

@_c_(447705, _a_(447704, _a_(447703, _n_(447702, "pytest", lambda: pytest), "mark"), "usefixture"), "oneTimeSetUp","setUp")
class CategoryTest(_a_(447707, _n_(447706, "unittest", lambda: unittest), "TestCase")):
    _l_(447804)

    @_c_(447710, _a_(447709, _n_(447708, "pytest", lambda: pytest), "fixture"), autouse=True)
    def classSetup(self,oneTimeSetUp):
        _l_(447723)

        _n_(447711, "self", lambda: self).ca = _c_(447715, _n_(447712, "CategoryPage", lambda: CategoryPage), _a_(447714, _n_(447713, "self", lambda: self), "driver"))
        _l_(447716)
        _n_(447717, "self", lambda: self).ts = _c_(447721, _n_(447718, "TestStatus", lambda: TestStatus), _a_(447720, _n_(447719, "self", lambda: self), "driver"))
        _l_(447722)

    @_c_(447727, _a_(447726, _a_(447725, _n_(447724, "pytest", lambda: pytest), "mark"), "run"), order=1)
    def test_Announcements_link_WAF001(self):
        _l_(447743)

        result = _c_(447731, _a_(447730, _a_(447729, _n_(447728, "self", lambda: self), "ca"), "find_announcements_link"))
        _l_(447732)
        _c_(447737, _a_(447735, _a_(447734, _n_(447733, "self", lambda: self), "ts"), "markFinal"), "Announcements link", _n_(447736, "result", lambda: result),"To find announcements link")
        _l_(447738)
        _c_(447741, _a_(447740, _n_(447739, "time", lambda: time), "sleep"), 2)
        _l_(447742)

    @_c_(447747, _a_(447746, _a_(447745, _n_(447744, "pytest", lambda: pytest), "mark"), "run"), order=2)
    def test_FirstLinkInAnnouncements_WAF002(self):
        _l_(447763)

        result=_c_(447751, _a_(447750, _a_(447749, _n_(447748, "self", lambda: self), "ca"), "find_first_announcement_link"))
        _l_(447752)
        _c_(447757, _a_(447755, _a_(447754, _n_(447753, "self", lambda: self), "ts"), "markFinal"), "Latest link in announcements",_n_(447756, "result", lambda: result),"To click on latest announcements link")
        _l_(447758)
        _c_(447761, _a_(447760, _n_(447759, "time", lambda: time), "sleep"), 2)
        _l_(447762)

    @_c_(447767, _a_(447766, _a_(447765, _n_(447764, "pytest", lambda: pytest), "mark"), "run"), order=3)
    def test_Products_Link_WAF003(self):
        _l_(447783)

        result=_c_(447771, _a_(447770, _a_(447769, _n_(447768, "self", lambda: self), "ca"), "find_products"))
        _l_(447772)
        _c_(447777, _a_(447775, _a_(447774, _n_(447773, "self", lambda: self), "ts"), "markFinal"), "Products link",_n_(447776, "result", lambda: result),"To find products link")
        _l_(447778)
        _c_(447781, _a_(447780, _n_(447779, "time", lambda: time), "sleep"), 2)
        _l_(447782)

    @_c_(447787, _a_(447786, _a_(447785, _n_(447784, "pytest", lambda: pytest), "mark"), "run"), order=4)
    def test_FirstLinkInProducts_WAF004(self):
        _l_(447803)

        result=_c_(447791, _a_(447790, _a_(447789, _n_(447788, "self", lambda: self), "ca"), "find_first_products_link"))
        _l_(447792)
        _c_(447797, _a_(447795, _a_(447794, _n_(447793, "self", lambda: self), "ts"), "markFinal"), "Latest link in products",_n_(447796, "result", lambda: result),"To click on latest products link")
        _l_(447798)
        _c_(447801, _a_(447800, _n_(447799, "time", lambda: time), "sleep"), 2)
        _l_(447802)