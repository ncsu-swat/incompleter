# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29653129/update-to-django-1-8-attributeerror-django-test-testcase-has-no-attribute-cl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import django
    _l_(378956)

except ImportError:
    pass
try:
    import unittest
    _l_(378958)

except ImportError:
    pass
try:
    from django.test import TestCase
    _l_(378960)

except ImportError:
    pass
try:
    import logging
    _l_(378962)

except ImportError:
    pass
try:
    import sys
    _l_(378964)

except ImportError:
    pass
try:
    from builtins import classmethod, isinstance
    _l_(378966)

except ImportError:
    pass

class ATestTests(_n_(378967, "TestCase", lambda: TestCase)):
    _l_(378994)


    @_n_(378968, "classmethod", lambda: classmethod)
    def setUpClass(cls):
        _l_(378981)

        _c_(378971, _a_(378970, _n_(378969, "django", lambda: django), "setup"))
        _l_(378972)
        _c_(378979, _a_(378974, _n_(378973, "logging", lambda: logging), "basicConfig"), stream=_a_(378976, _n_(378975, "sys", lambda: sys), "stderr"), level=_a_(378978, _n_(378977, "logging", lambda: logging), "DEBUG"))
        _l_(378980)


    def setUp(self):
        _l_(378986)

        _n_(378982, "self", lambda: self)._app = _c_(378984, _n_(378983, "Application", lambda: Application), name="a")
        _l_(378985)


    def testtest(self):
        _l_(378993)


        _c_(378991, _a_(378988, _n_(378987, "self", lambda: self), "assertIsNotNone"), _a_(378990, _n_(378989, "self", lambda: self), "_app"))
        _l_(378992)