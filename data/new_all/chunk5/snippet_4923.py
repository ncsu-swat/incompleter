# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40505484/typeerror-int-object-is-not-subscriptable-adding-to-a-tuple-in-a-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
GeneratedX = []
_l_(662023)
x = (200,1)
_l_(662024)
y = (168,1)
_l_(662025)
_c_(662029, _a_(662027, _n_(662026, "GeneratedX", lambda: GeneratedX), "append"), _n_(662028, "x", lambda: x))
_l_(662030)
_c_(662034, _a_(662032, _n_(662031, "GeneratedX", lambda: GeneratedX), "append"), _n_(662033, "y", lambda: y))
_l_(662035)
i = True
_l_(662036)
while _n_(662037, "i", lambda: i) == True:
    _l_(662047)

    for current in _n_(662038, "GeneratedX", lambda: GeneratedX):
        _l_(662046)

        GeneratedX = (_n_(662039, "current", lambda: current)[0],_n_(662040, "current", lambda: current)[1] + 1)
        _l_(662041)
        _c_(662044, _n_(662042, "print", lambda: print), _n_(662043, "GeneratedX", lambda: GeneratedX))
        _l_(662045)