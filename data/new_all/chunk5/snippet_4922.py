# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40499916/htmltestrunner-error-raise-typeerror-is-not-callable-formatreprtest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pymysql
    _l_(676933)

except ImportError:
    pass
try:
    import pymysql
    _l_(676935)

except ImportError:
    pass
try:
    import unittest
    _l_(676937)

except ImportError:
    pass
try:
    import time
    _l_(676939)

except ImportError:
    pass
try:
    import unittest.suite
    _l_(676941)

except ImportError:
    pass
try:
    import HTMLTestRunner
    _l_(676943)

except ImportError:
    pass
try:
    import sys
    _l_(676945)

except ImportError:
    pass
def hell(a):
    _l_(676952)

    _c_(676948, _n_(676946, "print", lambda: print), _n_(676947, "a", lambda: a))
    _l_(676949)
    aux = _n_(676950, "a", lambda: a)
    _l_(676951)
    return aux
testunit = _c_(676955, _a_(676954, _n_(676953, "unittest", lambda: unittest), "TestSuite"))
_l_(676956)
_c_(676961, _a_(676958, _n_(676957, "testunit", lambda: testunit), "addTest"), _c_(676960, _n_(676959, "hell", lambda: hell), 'ad'))
_l_(676962)
filename = '/Users/vivi/Downloads/aa.html'
_l_(676963)
fp = _c_(676966, _n_(676964, "open", lambda: open), _n_(676965, "filename", lambda: filename), 'wb')  
_l_(676967)  
runner = _c_(676971, _a_(676969, _n_(676968, "HTMLTestRunner", lambda: HTMLTestRunner), "HTMLTestRunner"), stream=_n_(676970, "fp", lambda: fp), title=u'print', description=u'简单')
_l_(676972)
_c_(676976, _a_(676974, _n_(676973, "runner", lambda: runner), "run"), _n_(676975, "testunit", lambda: testunit))
_l_(676977)