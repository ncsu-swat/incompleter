# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40505484/typeerror-int-object-is-not-subscriptable-adding-to-a-tuple-in-a-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
GeneratedX = []
_l_(674700)
x = (200,1)
_l_(674701)
y = (168,1)
_l_(674702)
_c_(674706, _a_(674704, _n_(674703, "GeneratedX", lambda: GeneratedX), "append"), _n_(674705, "x", lambda: x))
_l_(674707)
_c_(674711, _a_(674709, _n_(674708, "GeneratedX", lambda: GeneratedX), "append"), _n_(674710, "y", lambda: y))
_l_(674712)
i = True
_l_(674713)
while _n_(674714, "i", lambda: i) == True:
    _l_(674724)

    for current in _n_(674715, "GeneratedX", lambda: GeneratedX):
        _l_(674723)

        GeneratedX = (_n_(674716, "current", lambda: current)[0],_n_(674717, "current", lambda: current)[1] + 1)
        _l_(674718)
        _c_(674721, _n_(674719, "print", lambda: print), _n_(674720, "GeneratedX", lambda: GeneratedX))
        _l_(674722)