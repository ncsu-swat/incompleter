# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77556031/getting-typeerror-expected-str-bytes-or-os-pathlike-object-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Testcase_DDT_Login:
    _l_(343931)

    baseURL = _c_(343837, _a_(343836, ReadProperties, "application_url"))
    _l_(343838)
    Path = ".//TestData/test-data.xlsx"
    _l_(343839)
    logger = _c_(343841, _a_(343840, ReadLog, "loggen"))
    _l_(343842)

    # Verifying Multiple Login Credential

    def test_multiple_login(self, setup):
        _l_(343930)

        _c_(343846, _a_(343845, _a_(343844, _n_(343843, "self", lambda: self), "logger"), "info"), "[TestCase_002] : Verify multiple login credential form testdata file ")
        _l_(343847)
        _n_(343848, "self", lambda: self).driver = _n_(343849, "setup", lambda: setup)
        _l_(343850)
        _c_(343856, _a_(343853, _a_(343852, _n_(343851, "self", lambda: self), "driver"), "get"), _a_(343855, _n_(343854, "self", lambda: self), "baseURL"))
        _l_(343857)
        _n_(343858, "self", lambda: self).lp = _c_(343862, _n_(343859, "Login", lambda: Login), _a_(343861, _n_(343860, "self", lambda: self), "driver"))
        _l_(343863)
        _n_(343864, "self", lambda: self).rows = _c_(343869, _a_(343866, _n_(343865, "XLUtils", lambda: XLUtils), "getRowCount"), _a_(343868, _n_(343867, "self", lambda: self), "Path"), 'Sheet1')
        _l_(343870)
        lst_status = []
        _l_(343871)

        for r in _c_(343875, _n_(343872, "range", lambda: range), 2, _a_(343874, _n_(343873, "self", lambda: self), "rows") + 1):
            _l_(343929)

            _n_(343876, "self", lambda: self).user = _c_(343882, _a_(343878, _n_(343877, "XLUtils", lambda: XLUtils), "readData"), _a_(343880, _n_(343879, "self", lambda: self), "Path"), 'Sheet1', _n_(343881, "r", lambda: r), 1)
            _l_(343883)
            _n_(343884, "self", lambda: self).password = _c_(343890, _a_(343886, _n_(343885, "XLUtils", lambda: XLUtils), "readData"), _a_(343888, _n_(343887, "self", lambda: self), "rows"), 'Sheet1', _n_(343889, "r", lambda: r), 2)
            _l_(343891)
            _n_(343892, "self", lambda: self).exp_result = _c_(343898, _a_(343894, _n_(343893, "XLUtils", lambda: XLUtils), "readData"), _a_(343896, _n_(343895, "self", lambda: self), "rows"), 'Sheet1', _n_(343897, "r", lambda: r), 3)
            _l_(343899)
            _c_(343905, _a_(343902, _a_(343901, _n_(343900, "self", lambda: self), "lp"), "setUserName"), _a_(343904, _n_(343903, "self", lambda: self), "user"))
            _l_(343906)
            _c_(343912, _a_(343909, _a_(343908, _n_(343907, "self", lambda: self), "lp"), "setPassword"), _a_(343911, _n_(343910, "self", lambda: self), "password"))
            _l_(343913)
            _c_(343917, _a_(343916, _a_(343915, _n_(343914, "self", lambda: self), "lp"), "clicklogin"))
            _l_(343918)
            _c_(343921, _a_(343920, _n_(343919, "time", lambda: time), "sleep"), 10)
            _l_(343922)
            act_result = "Order Info"
            _l_(343923)
            exp_result_hp = _c_(343927, _a_(343926, _a_(343925, _n_(343924, "self", lambda: self), "lp"), "orderinfo"))
            _l_(343928)