# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from appium import webdriver
    _l_(353478)

except ImportError:
    pass

class Driver(_n_(353479, "object", lambda: object)):
    _l_(353529)


    def setUp(self):
        _l_(353488)

        _n_(353480, "self", lambda: self).browser = 'iOS'
        _l_(353481)
        _c_(353486, _a_(353483, _n_(353482, "self", lambda: self), "getDriver"), _a_(353485, _n_(353484, "self", lambda: self), "platform"))
        _l_(353487)

    def getDriver(self, platform):
        _l_(353522)

        desired_caps = {}
        _l_(353489)
        urlLink = "XXXXXXXX"
        _l_(353490)
        if _n_(353491, "platform", lambda: platform) == 'android':
            _l_(353518)

            _n_(353492, "self", lambda: self).driver = _c_(353497, _a_(353494, _n_(353493, "webdriver", lambda: webdriver), "Remote"), _n_(353495, "urlLink", lambda: urlLink), _n_(353496, "desired_caps", lambda: desired_caps))
            _l_(353498)
        elif _n_(353499, "platform", lambda: platform) == 'iOS':
            _l_(353517)

            _n_(353500, "desired_caps", lambda: desired_caps)['platformName'] = 'iOS'
            _l_(353501)
            _n_(353502, "desired_caps", lambda: desired_caps)['platformVersion'] = '10.0'
            _l_(353503)
            _n_(353504, "desired_caps", lambda: desired_caps)['deviceName'] = 'XXXXXXX'
            _l_(353505)
            _c_(353508, _n_(353506, "print", lambda: print), _n_(353507, "desired_caps", lambda: desired_caps))
            _l_(353509)
            _n_(353510, "self", lambda: self).driver = _c_(353515, _a_(353512, _n_(353511, "webdriver", lambda: webdriver), "Remote"), _n_(353513, "urlLink", lambda: urlLink), _n_(353514, "desired_caps", lambda: desired_caps))
            _l_(353516)
        aux = _a_(353520, _n_(353519, "self", lambda: self), "driver")
        _l_(353521)
        return aux

    def tearDown(self):
        _l_(353528)

        _c_(353526, _a_(353525, _a_(353524, _n_(353523, "self", lambda: self), "driver"), "quit"))
        _l_(353527)