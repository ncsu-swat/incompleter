# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69839628/attributeerror-nonetype-object-has-no-attribute-dropna
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(622001)

except ImportError:
    pass
try:
    from src.numeric import NumericColumn
    _l_(622003)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(622005)

except ImportError:
    pass

class TestNumeric(_a_(622007, _n_(622006, "unittest", lambda: unittest), "TestCase")):
    _l_(622035)

    def test_numeric(self):
        _l_(622034)

        ### test on dummy data ###
        # create series of data
        dc1 = _c_(622009, _n_(622008, "NumericColumn", lambda: NumericColumn))
        _l_(622010)
        _n_(622011, "dc1", lambda: dc1).col_name = "my_test"
        _l_(622012)

        # test methods
        _c_(622018, _a_(622014, _n_(622013, "self", lambda: self), "assertEqual"), _c_(622017, _a_(622016, _n_(622015, "dc1", lambda: dc1), "get_name")),"my_test")
        _l_(622019)
        _c_(622025, _a_(622021, _n_(622020, "self", lambda: self), "assertEqual"), _c_(622024, _a_(622023, _n_(622022, "dc1", lambda: dc1), "get_unique")),7)
        _l_(622026)
        _c_(622032, _a_(622028, _n_(622027, "self", lambda: self), "assertEqual"), _c_(622031, _a_(622030, _n_(622029, "dc1", lambda: dc1), "get_missing")),1)
        _l_(622033)