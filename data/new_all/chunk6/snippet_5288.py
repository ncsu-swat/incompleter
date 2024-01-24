# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73066850/getting-attributeerror-nonetype-object-has-no-attribute-get-using-pytest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from self import self
    _l_(367068)

except ImportError:
    pass
try:
    from pageObjects.LoginPage import LoginPage
    _l_(367070)

except ImportError:
    pass
try:
    from utilities.readProperties import ReadConfig
    _l_(367072)

except ImportError:
    pass
try:
    from utilities.customLogger import LogGen
    _l_(367074)

except ImportError:
    pass


class Test_001_Login:
    _l_(367091)

    baseURL = _c_(367077, _a_(367076, _n_(367075, "ReadConfig", lambda: ReadConfig), "getApplicationURL"))
    _l_(367078)
    username = _c_(367081, _a_(367080, _n_(367079, "ReadConfig", lambda: ReadConfig), "getUseremail"))
    _l_(367082)
    password = _c_(367085, _a_(367084, _n_(367083, "ReadConfig", lambda: ReadConfig), "getPassword"))
    _l_(367086)
    logger = _c_(367089, _a_(367088, _n_(367087, "LogGen", lambda: LogGen), "loggen"))
    _l_(367090)

def test_login(self, setup):
    _l_(367157)

    _n_(367092, "self", lambda: self).driver = _n_(367093, "setup", lambda: setup)
    _l_(367094)
    _c_(367100, _a_(367097, _a_(367096, _n_(367095, "self", lambda: self), "driver"), "get"), _a_(367099, _n_(367098, "self", lambda: self), "baseURL"))
    _l_(367101)
    _c_(367105, _a_(367104, _a_(367103, _n_(367102, "self", lambda: self), "logger"), "info"), "URL iS loaded successfully")
    _l_(367106)
    _c_(367110, _a_(367109, _a_(367108, _n_(367107, "self", lambda: self), "driver"), "maximize_window"))
    _l_(367111)

    _n_(367112, "self", lambda: self).lp = _c_(367116, _n_(367113, "LoginPage", lambda: LoginPage), _a_(367115, _n_(367114, "self", lambda: self), "driver"))
    _l_(367117)

    _c_(367123, _a_(367120, _a_(367119, _n_(367118, "self", lambda: self), "lp"), "setUserName"), _a_(367122, _n_(367121, "self", lambda: self), "username"))
    _l_(367124)
    _c_(367128, _a_(367127, _a_(367126, _n_(367125, "self", lambda: self), "logger"), "info"), "username   entered successfully")
    _l_(367129)
    _c_(367135, _a_(367132, _a_(367131, _n_(367130, "self", lambda: self), "lp"), "setPassword"), _a_(367134, _n_(367133, "self", lambda: self), "password"))
    _l_(367136)
    _c_(367140, _a_(367139, _a_(367138, _n_(367137, "self", lambda: self), "logger"), "info"), "password   entered successfully")
    _l_(367141)
    _c_(367145, _a_(367144, _a_(367143, _n_(367142, "self", lambda: self), "lp"), "clickLogin"))
    _l_(367146)
    _c_(367150, _a_(367149, _a_(367148, _n_(367147, "self", lambda: self), "logger"), "info"), "clicked on login button")
    _l_(367151)
    _c_(367155, _a_(367154, _a_(367153, _n_(367152, "self", lambda: self), "driver"), "close"))
    _l_(367156)