# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(345771)

except ImportError:
    pass
try:
    from core import Driver
    _l_(345773)

except ImportError:
    pass
try:
    import page
    _l_(345775)

except ImportError:
    pass

class testLoginOK(_a_(345777, _n_(345776, "unittest", lambda: unittest), "TestCase")):
    _l_(345801)


    def setUp(self):
        _l_(345783)

        _n_(345778, "self", lambda: self).driver = _c_(345781, _a_(345780, _n_(345779, "Driver", lambda: Driver), "getDriver"), 'iOS')
        _l_(345782)

    def test_login_error_message(self):
        _l_(345794)


        main_page = _c_(345788, _a_(345785, _n_(345784, "page", lambda: page), "MainPage"), _a_(345787, _n_(345786, "self", lambda: self), "driver"))
        _l_(345789)
        _c_(345792, _a_(345791, _n_(345790, "main_page", lambda: main_page), "click_Login_Button"))
        _l_(345793)

    def tearDown(self):
        _l_(345800)

        _c_(345798, _a_(345797, _a_(345796, _n_(345795, "self", lambda: self), "driver"), "close"))
        _l_(345799)

if _n_(345802, "__name__", lambda: __name__) == "__main__":
    _l_(345807)

    _c_(345805, _a_(345804, _n_(345803, "unittest", lambda: unittest), "main"))
    _l_(345806)