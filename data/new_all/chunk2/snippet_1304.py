# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50799363/when-i-run-my-test-suite-i-am-getting-a-typeerror-i-am-not-able-to-understand-wh
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from unittest import TestLoader, TestSuite
    _l_(450129)

except ImportError:
    pass
try:
    from HtmlTestRunner import HTMLTestRunner
    _l_(450131)

except ImportError:
    pass
try:
    from tests.Home import category_test
    _l_(450133)

except ImportError:
    pass

example_tests = _c_(450138, _a_(450136, _c_(450135, _n_(450134, "TestLoader", lambda: TestLoader)), "loadTestsFromTestCase"), _n_(450137, "category_test", lambda: category_test))
_l_(450139)
suite = _c_(450142, _n_(450140, "TestSuite", lambda: TestSuite), _n_(450141, "example_tests", lambda: example_tests))
_l_(450143)
runner = _c_(450145, _n_(450144, "HTMLTestRunner", lambda: HTMLTestRunner), output='example_suite', template='path/to/template', report_title='My Report')
_l_(450146)
_c_(450150, _a_(450148, _n_(450147, "runner", lambda: runner), "run"), _n_(450149, "suite", lambda: suite))
_l_(450151)