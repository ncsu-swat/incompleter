# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48946999/django-and-selenium-typeerror-setupclass-missing-1-required-positional-argume
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.staticfiles.testing import StaticLiveServerTestCase
    _l_(442103)

except ImportError:
    pass
try:
    from selenium.webdriver.firefox.webdriver import WebDriver
    _l_(442105)

except ImportError:
    pass


class LevelListViewTest(_n_(442106, "StaticLiveServerTestCase", lambda: StaticLiveServerTestCase)):
    _l_(442142)


    @_n_(442107, "staticmethod", lambda: staticmethod)
    def setUpClass(cls):
        _l_(442121)

        _c_(442110, _a_(442109, _n_(442108, "super", lambda: super)(), "setUpClass"))
        _l_(442111)
        _n_(442112, "cls", lambda: cls).selenium = _c_(442114, _n_(442113, "WebDriver", lambda: WebDriver))
        _l_(442115)
        _c_(442119, _a_(442118, _a_(442117, _n_(442116, "cls", lambda: cls), "selenium"), "implicitly_wait"), 10)
        _l_(442120)

    @_n_(442122, "staticmethod", lambda: staticmethod)
    def tearDownClass(cls):
        _l_(442133)

        _c_(442126, _a_(442125, _a_(442124, _n_(442123, "cls", lambda: cls), "selenium"), "quit"))
        _l_(442127)
        _c_(442131, _a_(442130, _a_(442129, _n_(442128, "cls", lambda: cls), "selenium"), "tearDownClass"))
        _l_(442132)

    def test_level_is_in_admin_panel(self):
        _l_(442141)

        _c_(442139, _a_(442136, _a_(442135, _n_(442134, "self", lambda: self), "selenium"), "get"), '%s%s' % (_a_(442138, _n_(442137, "self", lambda: self), "live_server_url"), '/admin/login/?next=/admin/'))
        _l_(442140)