# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67847906/typeerror-when-dividing-two-integers-and-printing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
num1=_c_(645151, _n_(645150, "input", lambda: input), "Enter a number: ")
_l_(645152)
num2=_c_(645154, _n_(645153, "input", lambda: input), "Enter the divisor: ")
_l_(645155)
result = 0
_l_(645156)
def findRemainder(x, y):
    _l_(645166)

    result = (_n_(645157, "x", lambda: x)%_n_(645158, "y", lambda: y))
    _l_(645159)
    _c_(645164, _n_(645160, "print", lambda: print), _c_(645163, _n_(645161, "str", lambda: str), _n_(645162, "result", lambda: result)))
    _l_(645165)
_c_(645170, _n_(645167, "findRemainder", lambda: findRemainder), _n_(645168, "num1", lambda: num1), _n_(645169, "num2", lambda: num2))
_l_(645171)