# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from locators import Locators
    _l_(350405)

except ImportError:
    pass

class BasePage(_n_(350406, "object", lambda: object)):
    _l_(350411)

    def __init__(self, driver):
        _l_(350410)

        _n_(350407, "self", lambda: self).driver = _n_(350408, "driver", lambda: driver)
        _l_(350409)

class MainPage(_n_(350412, "BasePage", lambda: BasePage)):
    _l_(350427)


    def click_Login_Button(self):
        _l_(350426)

        element = _c_(350420, _a_(350415, _a_(350414, _n_(350413, "self", lambda: self), "driver"), "find_element"), *_a_(350419, _c_(350418, _a_(350417, _n_(350416, "Locators", lambda: Locators), "setLocators")), "ACEPTAR_LOGIN_BTN"))
        _l_(350421)
        _c_(350424, _a_(350423, _n_(350422, "element", lambda: element), "click"))
        _l_(350425)