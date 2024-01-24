# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44786828/typeerror-unbound-method-getdriver-must-be-called-with-driver-instance-as-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from appium import webdriver
    _l_(372692)

except ImportError:
    pass

class Driver(_n_(372693, "object", lambda: object)):
    _l_(372743)


    def setUp(self):
        _l_(372702)

        _n_(372694, "self", lambda: self).browser = 'iOS'
        _l_(372695)
        _c_(372700, _a_(372697, _n_(372696, "self", lambda: self), "getDriver"), _a_(372699, _n_(372698, "self", lambda: self), "platform"))
        _l_(372701)

    def getDriver(self, platform):
        _l_(372736)

        desired_caps = {}
        _l_(372703)
        urlLink = "XXXXXXXX"
        _l_(372704)
        if _n_(372705, "platform", lambda: platform) == 'android':
            _l_(372732)

            _n_(372706, "self", lambda: self).driver = _c_(372711, _a_(372708, _n_(372707, "webdriver", lambda: webdriver), "Remote"), _n_(372709, "urlLink", lambda: urlLink), _n_(372710, "desired_caps", lambda: desired_caps))
            _l_(372712)
        elif _n_(372713, "platform", lambda: platform) == 'iOS':
            _l_(372731)

            _n_(372714, "desired_caps", lambda: desired_caps)['platformName'] = 'iOS'
            _l_(372715)
            _n_(372716, "desired_caps", lambda: desired_caps)['platformVersion'] = '10.0'
            _l_(372717)
            _n_(372718, "desired_caps", lambda: desired_caps)['deviceName'] = 'XXXXXXX'
            _l_(372719)
            _c_(372722, _n_(372720, "print", lambda: print), _n_(372721, "desired_caps", lambda: desired_caps))
            _l_(372723)
            _n_(372724, "self", lambda: self).driver = _c_(372729, _a_(372726, _n_(372725, "webdriver", lambda: webdriver), "Remote"), _n_(372727, "urlLink", lambda: urlLink), _n_(372728, "desired_caps", lambda: desired_caps))
            _l_(372730)
        aux = _a_(372734, _n_(372733, "self", lambda: self), "driver")
        _l_(372735)
        return aux

    def tearDown(self):
        _l_(372742)

        _c_(372740, _a_(372739, _a_(372738, _n_(372737, "self", lambda: self), "driver"), "quit"))
        _l_(372741)