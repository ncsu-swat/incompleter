# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67847906/typeerror-when-dividing-two-integers-and-printing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
num1=_c_(630335, _n_(630334, "input", lambda: input), "Enter a number: ")
_l_(630336)
num2=_c_(630338, _n_(630337, "input", lambda: input), "Enter the divisor: ")
_l_(630339)
result = 0
_l_(630340)
def findRemainder(x, y):
    _l_(630350)

    result = (_n_(630341, "x", lambda: x)%_n_(630342, "y", lambda: y))
    _l_(630343)
    _c_(630348, _n_(630344, "print", lambda: print), _c_(630347, _n_(630345, "str", lambda: str), _n_(630346, "result", lambda: result)))
    _l_(630349)
_c_(630354, _n_(630351, "findRemainder", lambda: findRemainder), _n_(630352, "num1", lambda: num1), _n_(630353, "num2", lambda: num2))
_l_(630355)