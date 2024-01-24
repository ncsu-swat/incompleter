# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77556031/getting-typeerror-expected-str-bytes-or-os-pathlike-object-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Testcase_DDT_Login:
    _l_(374948)

    baseURL = _c_(374854, _a_(374853, ReadProperties, "application_url"))
    _l_(374855)
    Path = ".//TestData/test-data.xlsx"
    _l_(374856)
    logger = _c_(374858, _a_(374857, ReadLog, "loggen"))
    _l_(374859)

    # Verifying Multiple Login Credential

    def test_multiple_login(self, setup):
        _l_(374947)

        _c_(374863, _a_(374862, _a_(374861, _n_(374860, "self", lambda: self), "logger"), "info"), "[TestCase_002] : Verify multiple login credential form testdata file ")
        _l_(374864)
        _n_(374865, "self", lambda: self).driver = _n_(374866, "setup", lambda: setup)
        _l_(374867)
        _c_(374873, _a_(374870, _a_(374869, _n_(374868, "self", lambda: self), "driver"), "get"), _a_(374872, _n_(374871, "self", lambda: self), "baseURL"))
        _l_(374874)
        _n_(374875, "self", lambda: self).lp = _c_(374879, _n_(374876, "Login", lambda: Login), _a_(374878, _n_(374877, "self", lambda: self), "driver"))
        _l_(374880)
        _n_(374881, "self", lambda: self).rows = _c_(374886, _a_(374883, _n_(374882, "XLUtils", lambda: XLUtils), "getRowCount"), _a_(374885, _n_(374884, "self", lambda: self), "Path"), 'Sheet1')
        _l_(374887)
        lst_status = []
        _l_(374888)

        for r in _c_(374892, _n_(374889, "range", lambda: range), 2, _a_(374891, _n_(374890, "self", lambda: self), "rows") + 1):
            _l_(374946)

            _n_(374893, "self", lambda: self).user = _c_(374899, _a_(374895, _n_(374894, "XLUtils", lambda: XLUtils), "readData"), _a_(374897, _n_(374896, "self", lambda: self), "Path"), 'Sheet1', _n_(374898, "r", lambda: r), 1)
            _l_(374900)
            _n_(374901, "self", lambda: self).password = _c_(374907, _a_(374903, _n_(374902, "XLUtils", lambda: XLUtils), "readData"), _a_(374905, _n_(374904, "self", lambda: self), "rows"), 'Sheet1', _n_(374906, "r", lambda: r), 2)
            _l_(374908)
            _n_(374909, "self", lambda: self).exp_result = _c_(374915, _a_(374911, _n_(374910, "XLUtils", lambda: XLUtils), "readData"), _a_(374913, _n_(374912, "self", lambda: self), "rows"), 'Sheet1', _n_(374914, "r", lambda: r), 3)
            _l_(374916)
            _c_(374922, _a_(374919, _a_(374918, _n_(374917, "self", lambda: self), "lp"), "setUserName"), _a_(374921, _n_(374920, "self", lambda: self), "user"))
            _l_(374923)
            _c_(374929, _a_(374926, _a_(374925, _n_(374924, "self", lambda: self), "lp"), "setPassword"), _a_(374928, _n_(374927, "self", lambda: self), "password"))
            _l_(374930)
            _c_(374934, _a_(374933, _a_(374932, _n_(374931, "self", lambda: self), "lp"), "clicklogin"))
            _l_(374935)
            _c_(374938, _a_(374937, _n_(374936, "time", lambda: time), "sleep"), 10)
            _l_(374939)
            act_result = "Order Info"
            _l_(374940)
            exp_result_hp = _c_(374944, _a_(374943, _a_(374942, _n_(374941, "self", lambda: self), "lp"), "orderinfo"))
            _l_(374945)