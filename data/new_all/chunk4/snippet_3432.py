# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74287845/python-recursion-problem-typeerror-unsupported-operand-types-for-int-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum1(n):
    _l_(592841)

    if _n_(592833, "n", lambda: n)==0:
        _l_(592835)

        aux = 0
        _l_(592834)
        return aux
    _n_(592836, "n", lambda: n)+_c_(592839, _n_(592837, "sum1", lambda: sum1), _n_(592838, "n", lambda: n)-1)
    _l_(592840)



_c_(592845, _n_(592842, "print", lambda: print), _c_(592844, _n_(592843, "sum1", lambda: sum1), 5))
_l_(592846)