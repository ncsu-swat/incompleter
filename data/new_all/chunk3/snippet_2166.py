# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60541782/attributeerror-when-patching-class-variable-when-mocking
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(579040)

except ImportError:
    pass
try:
    from unittest.mock import patch
    _l_(579042)

except ImportError:
    pass
try:
    from unittest.mock import Mock
    _l_(579044)

except ImportError:
    pass
try:
    from mocking_module import class_util
    _l_(579046)

except ImportError:
    pass


class TestSomething(_a_(579048, _n_(579047, "unittest", lambda: unittest), "TestCase")):
    _l_(579061)


    @_c_(579051, _a_(579050, _n_(579049, "patch", lambda: patch), "object"), "mocking_module.class_util.SampleClass", "base_url", "http://override.com")
    def test_class_variable_override(self):
        _l_(579060)


        _c_(579058, _n_(579052, "print", lambda: print), _c_(579057, _a_(579053, "url = {}", "format"), _c_(579056, _a_(579055, _n_(579054, "class_util", lambda: class_util), "do_something"))))
        _l_(579059)