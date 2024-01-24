# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55819002/attributeerror-classname-object-has-no-attribute-driver-on-appium-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(694739)

except ImportError:
    pass
try:
    from appium import webdriver
    _l_(694741)

except ImportError:
    pass
try:
    import time
    _l_(694743)

except ImportError:
    pass
try:
    import tracemalloc
    _l_(694745)

except ImportError:
    pass
_c_(694748, _a_(694747, _n_(694746, "tracemalloc", lambda: tracemalloc), "start"))
_l_(694749)
try:
    from config import desired_caps
    _l_(694751)

except ImportError:
    pass
# self = webdriver
# self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


class BaseTest(_a_(694753, _n_(694752, "unittest", lambda: unittest), "TestCase")):
    _l_(694786)


    def test_testcase1(self):
        _l_(694760)

        _n_(694754, "self", lambda: self).driver = _c_(694758, _a_(694756, _n_(694755, "webdriver", lambda: webdriver), "Remote"), 'http://127.0.0.1:4723/wd/hub', _n_(694757, "desired_caps", lambda: desired_caps))
        _l_(694759)

    def test_credentials(self):
        _l_(694779)

        email = _c_(694764, _a_(694763, _a_(694762, _n_(694761, "self", lambda: self), "driver"), "find_element_by_xpath"), "proper Xpath")
        _l_(694765)
        _c_(694768, _a_(694767, _n_(694766, "email", lambda: email), "send_keys"), "Test")
        _l_(694769)

        save = _c_(694773, _a_(694772, _a_(694771, _n_(694770, "self", lambda: self), "driver"), "find_element_by_link_text"), "Log In")
        _l_(694774)
        _c_(694777, _a_(694776, _n_(694775, "save", lambda: save), "click"))
        _l_(694778)

    def tearDown(self):
        _l_(694785)

        _c_(694783, _a_(694782, _a_(694781, _n_(694780, "self", lambda: self), "driver"), "quit"))
        _l_(694784)


if _n_(694787, "__name__", lambda: __name__) == '__main__':
    _l_(694802)


    suite = _c_(694793, _a_(694791, _c_(694790, _a_(694789, _n_(694788, "unittest", lambda: unittest), "TestLoader")), "loadTestsFromTestCase"), _n_(694792, "BaseTest", lambda: BaseTest))
    _l_(694794)
    _c_(694800, _a_(694798, _c_(694797, _a_(694796, _n_(694795, "unittest", lambda: unittest), "TextTestRunner"), verbosity=3), "run"), _n_(694799, "suite", lambda: suite))
    _l_(694801)