# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from appium.webdriver.common.mobileby import MobileBy
    _l_(337884)

except ImportError:
    pass

class Locators(_n_(337885, "object", lambda: object)):
    _l_(337914)

    def setLocators(self):
        _l_(337913)

        if (_a_(337887, _n_(337886, "self", lambda: self), "platform")=='android'):
            _l_(337912)

            ACEPTAR_PERMISO_BTN = (_a_(337889, _n_(337888, "MobileBy", lambda: MobileBy), "ID"),"com.android.packageinstaller:id/permission_allow_button")
            _l_(337890)
            ACEPTAR_LOGIN_BTN = (_a_(337892, _n_(337891, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/btnLogin")
            _l_(337893)
            ACEPTAR_MENSAJE_ERROR_BTN = (_a_(337895, _n_(337894, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/btnPositive")
            _l_(337896)
            INGRESAR_NUMERO_TXT = (_a_(337898, _n_(337897, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/etNumber")
            _l_(337899)
            INGRESAR_PASSWORD_TXT = (_a_(337901, _n_(337900, "MobileBy", lambda: MobileBy), "ID"),"com.entel.movil:id/etPassword")
            _l_(337902)
        elif (_a_(337904, _n_(337903, "self", lambda: self), "platform")=='iOS'):
            _l_(337911)

            INGRESAR_PASSWORD_TXT= (_a_(337906, _n_(337905, "MobileBy", lambda: MobileBy), "ID"),"//XCUIElementTypeSecureTextField[1]")
            _l_(337907)
            ACEPTAR_LOGIN_BTN = (_a_(337909, _n_(337908, "MobileBy", lambda: MobileBy), "ID"),"INGRESAR")
            _l_(337910)