# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64284524/typeerror-object-of-type-int-has-no-len-in-objective-function-nonlinear-opt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
m=_c_(386364, _n_(386363, "GEKKO", lambda: GEKKO))
_l_(386365)
x=_c_(386368, _a_(386367, _n_(386366, "m", lambda: m), "Var"), value=1,lb=0, ub=50)
_l_(386369)
y=_c_(386372, _a_(386371, _n_(386370, "m", lambda: m), "Var"), value=1, lb=0, ub=50)
_l_(386373)
_c_(386380, _a_(386375, _n_(386374, "m", lambda: m), "Equation"), _n_(386376, "puree", lambda: puree)*_n_(386377, "x", lambda: x)+_n_(386378, "cutlet", lambda: cutlet)*_n_(386379, "y", lambda: y)==1500)
_l_(386381)
_c_(386388, _a_(386383, _n_(386382, "m", lambda: m), "Obj"), -_c_(386387, _n_(386384, "min", lambda: min), _n_(386385, "x", lambda: x),_n_(386386, "y", lambda: y)))
_l_(386389)
_c_(386392, _a_(386391, _n_(386390, "m", lambda: m), "solve"), disp=False)
_l_(386393)
_a_(386395, _n_(386394, "x", lambda: x), "value")
_l_(386396)
_a_(386398, _n_(386397, "y", lambda: y), "value")
_l_(386399)