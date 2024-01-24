# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40499916/htmltestrunner-error-raise-typeerror-is-not-callable-formatreprtest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pymysql
    _l_(649570)

except ImportError:
    pass
try:
    import pymysql
    _l_(649572)

except ImportError:
    pass
try:
    import unittest
    _l_(649574)

except ImportError:
    pass
try:
    import time
    _l_(649576)

except ImportError:
    pass
try:
    import unittest.suite
    _l_(649578)

except ImportError:
    pass
try:
    import HTMLTestRunner
    _l_(649580)

except ImportError:
    pass
try:
    import sys
    _l_(649582)

except ImportError:
    pass
def hell(a):
    _l_(649589)

    _c_(649585, _n_(649583, "print", lambda: print), _n_(649584, "a", lambda: a))
    _l_(649586)
    aux = _n_(649587, "a", lambda: a)
    _l_(649588)
    return aux
testunit = _c_(649592, _a_(649591, _n_(649590, "unittest", lambda: unittest), "TestSuite"))
_l_(649593)
_c_(649598, _a_(649595, _n_(649594, "testunit", lambda: testunit), "addTest"), _c_(649597, _n_(649596, "hell", lambda: hell), 'ad'))
_l_(649599)
filename = '/Users/vivi/Downloads/aa.html'
_l_(649600)
fp = _c_(649603, _n_(649601, "open", lambda: open), _n_(649602, "filename", lambda: filename), 'wb')  
_l_(649604)  
runner = _c_(649608, _a_(649606, _n_(649605, "HTMLTestRunner", lambda: HTMLTestRunner), "HTMLTestRunner"), stream=_n_(649607, "fp", lambda: fp), title=u'print', description=u'简单')
_l_(649609)
_c_(649613, _a_(649611, _n_(649610, "runner", lambda: runner), "run"), _n_(649612, "testunit", lambda: testunit))
_l_(649614)