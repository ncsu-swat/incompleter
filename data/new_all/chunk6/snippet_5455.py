# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from locators import Locators
    _l_(370531)

except ImportError:
    pass

class BasePage(_n_(370532, "object", lambda: object)):
    _l_(370537)

    def __init__(self, driver):
        _l_(370536)

        _n_(370533, "self", lambda: self).driver = _n_(370534, "driver", lambda: driver)
        _l_(370535)

class MainPage(_n_(370538, "BasePage", lambda: BasePage)):
    _l_(370553)


    def click_Login_Button(self):
        _l_(370552)

        element = _c_(370546, _a_(370541, _a_(370540, _n_(370539, "self", lambda: self), "driver"), "find_element"), *_a_(370545, _c_(370544, _a_(370543, _n_(370542, "Locators", lambda: Locators), "setLocators")), "ACEPTAR_LOGIN_BTN"))
        _l_(370547)
        _c_(370550, _a_(370549, _n_(370548, "element", lambda: element), "click"))
        _l_(370551)