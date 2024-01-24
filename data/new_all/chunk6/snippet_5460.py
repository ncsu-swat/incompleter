# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(372120)

except ImportError:
    pass
try:
    from core import Driver
    _l_(372122)

except ImportError:
    pass
try:
    import page
    _l_(372124)

except ImportError:
    pass

class testLoginOK(_a_(372126, _n_(372125, "unittest", lambda: unittest), "TestCase")):
    _l_(372150)


    def setUp(self):
        _l_(372132)

        _n_(372127, "self", lambda: self).driver = _c_(372130, _a_(372129, _n_(372128, "Driver", lambda: Driver), "getDriver"), 'iOS')
        _l_(372131)

    def test_login_error_message(self):
        _l_(372143)


        main_page = _c_(372137, _a_(372134, _n_(372133, "page", lambda: page), "MainPage"), _a_(372136, _n_(372135, "self", lambda: self), "driver"))
        _l_(372138)
        _c_(372141, _a_(372140, _n_(372139, "main_page", lambda: main_page), "click_Login_Button"))
        _l_(372142)

    def tearDown(self):
        _l_(372149)

        _c_(372147, _a_(372146, _a_(372145, _n_(372144, "self", lambda: self), "driver"), "close"))
        _l_(372148)

if _n_(372151, "__name__", lambda: __name__) == "__main__":
    _l_(372156)

    _c_(372154, _a_(372153, _n_(372152, "unittest", lambda: unittest), "main"))
    _l_(372155)