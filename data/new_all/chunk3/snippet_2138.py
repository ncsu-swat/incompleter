# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61876429/why-python-is-throwing-attribute-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from utilities.teststatus import TestStatus as ts
    _l_(556959)

except ImportError:
    pass
try:
    import unittest
    _l_(556961)

except ImportError:
    pass
try:
    import pytest
    _l_(556963)

except ImportError:
    pass

@_c_(556967, _a_(556966, _a_(556965, _n_(556964, "pytest", lambda: pytest), "mark"), "usefixtures"), "oneTimeSetup", "setUp")
class testLogin(_a_(556969, _n_(556968, "unittest", lambda: unittest), "TestCase")):
    _l_(557006)


    @_c_(556972, _a_(556971, _n_(556970, "pytest", lambda: pytest), "fixture"), autouse=True)
    def classSetup(self,oneTimeSetup):
        _l_(556979)

        _n_(556973, "self", lambda: self).lp = _c_(556977, _n_(556974, "LoginPage", lambda: LoginPage), _a_(556976, _n_(556975, "self", lambda: self), "driver"))
        _l_(556978)
    @_a_(556982, _a_(556981, _n_(556980, "pytest", lambda: pytest), "mark"), "order1")
    def test_validLogin(self):
        _l_(557005)

        _c_(556986, _a_(556985, _a_(556984, _n_(556983, "self", lambda: self), "lp"), "login"), "test@email.com", "abcabc")
        _l_(556987)
        userIcon = _c_(556991, _a_(556990, _a_(556989, _n_(556988, "self", lambda: self), "lp"), "verifyLoginSuccessful"))
        _l_(556992)
        title = _c_(556996, _a_(556995, _a_(556994, _n_(556993, "self", lambda: self), "lp"), "verifyPageTitle"))
        _l_(556997)
        _c_(557001, _a_(556999, _n_(556998, "ts", lambda: ts), "markFinal"), _n_(557000, "title", lambda: title),"Login not successful")
        _l_(557002)
        assert _n_(557003, "userIcon", lambda: userIcon) == True
        _l_(557004)