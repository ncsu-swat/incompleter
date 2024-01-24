# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61550473/why-does-calling-reversed-upon-a-tuple-throw-an-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = (1, 2, 3, 4)
_l_(390901)
_c_(390904, _a_(390903, _n_(390902, "x", lambda: x), "__reversed__"))
_l_(390905)
#causes an attribute error