# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from appium.webdriver.common.mobileby import MobileBy
    _l_(340269)

except ImportError:
    pass

class Locators(_n_(340270, "object", lambda: object)):
    _l_(340299)

    def setLocators(self):
        _l_(340298)

        if (_a_(340272, _n_(340271, "self", lambda: self), "platform")=='android'):
            _l_(340297)

            ACEPTAR_PERMISO_BTN = (_a_(340274, _n_(340273, "MobileBy", lambda: MobileBy), "ID"),"com.android.packageinstaller:id/permission_allow_button")
            _l_(340275)
            ACEPTAR_LOGIN_BTN = (_a_(340277, _n_(340276, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/btnLogin")
            _l_(340278)
            ACEPTAR_MENSAJE_ERROR_BTN = (_a_(340280, _n_(340279, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/btnPositive")
            _l_(340281)
            INGRESAR_NUMERO_TXT = (_a_(340283, _n_(340282, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/etNumber")
            _l_(340284)
            INGRESAR_PASSWORD_TXT = (_a_(340286, _n_(340285, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/etPassword")
            _l_(340287)
        elif (_a_(340289, _n_(340288, "self", lambda: self), "platform")=='iOS'):
            _l_(340296)

            INGRESAR_PASSWORD_TXT= (_a_(340291, _n_(340290, "MobileBy", lambda: MobileBy), "ID"),"//XCUIElementTypeSecureTextField[1]")
            _l_(340292)
            ACEPTAR_LOGIN_BTN = (_a_(340294, _n_(340293, "MobileBy", lambda: MobileBy), "ID"),"INGRESAR")
            _l_(340295)