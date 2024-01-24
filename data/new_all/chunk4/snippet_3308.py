# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75889310/attributeerror-testorders-object-has-no-attribute-token
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(583744)

except ImportError:
    pass
try:
    import HtmlTestRunner
    _l_(583746)

except ImportError:
    pass
try:
    from API_project.Tests.test_orders import TestOrders
    _l_(583748)

except ImportError:
    pass


class MyTestSuite(_a_(583750, _n_(583749, "unittest", lambda: unittest), "TestCase")):
    _l_(583774)

   
    def test_suite(self):
        _l_(583773)

       
        test_to_run = _c_(583753, _a_(583752, _n_(583751, "unittest", lambda: unittest), "TestSuite"))
        _l_(583754)
        _c_(583762, _a_(583756, _n_(583755, "test_to_run", lambda: test_to_run), "addTests"), [
            _c_(583761, _a_(583759, _a_(583758, _n_(583757, "unittest", lambda: unittest), "defaultTestLoader"), "loadTestsFromTestCase"), _n_(583760, "TestOrders", lambda: TestOrders))
            ]
        )
        _l_(583763)
        runner = _c_(583766, _a_(583765, _n_(583764, "HtmlTestRunner", lambda: HtmlTestRunner), "HTMLTestRunner"), combine_reports=True,
            report_name='TestProject',
            report_title = 'TestProjectUnitTesting'
        )
        _l_(583767)
        _c_(583771, _a_(583769, _n_(583768, "runner", lambda: runner), "run"), _n_(583770, "test_to_run", lambda: test_to_run))
        _l_(583772)