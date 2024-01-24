# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63715326/functional-logger-raises-filenotfounderror-in-pytest
# test_code.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(399716)

except ImportError:
    pass
try:
    from workers.code import Worker
    _l_(399718)

except ImportError:
    pass


class CodeTest(_a_(399720, _n_(399719, "unittest", lambda: unittest), "TestCase")):
    _l_(399737)

    def test__init__(self):
        _l_(399728)

        worker = _c_(399722, _n_(399721, "Worker", lambda: Worker))
        _l_(399723)
        assert _a_(399726, _a_(399725, _n_(399724, "worker", lambda: worker), "logger"), "handlers")  # this fails with FileNotFound Error
        _l_(399727)  # this fails with FileNotFound Error

    def test_do_something(self):
        _l_(399736)

        worker = _c_(399730, _n_(399729, "Worker", lambda: Worker))  # this also fails even when delay=True on FileHandler
        _l_(399731)  # this also fails even when delay=True on FileHandler
        assert _c_(399734, _a_(399733, _n_(399732, "worker", lambda: worker), "do_something"))
        _l_(399735)