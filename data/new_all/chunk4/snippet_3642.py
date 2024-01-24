# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70837963/name-error-in-class-when-importing-my-script-file-to-another-from
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from script import*
    _l_(631307)

except ImportError:
    pass

Jp = _c_(631309, _n_(631308, "Operators", lambda: Operators), ['Jp'])
_l_(631310)
Jm = _c_(631312, _n_(631311, "Operators", lambda: Operators), ['Jm'])
_l_(631313)
    
ket_1 = _c_(631317, _n_(631314, "Single_Ket", lambda: Single_Ket), (1, 1), 1, [_n_(631315, "Jp", lambda: Jp) @ _n_(631316, "Jm", lambda: Jm)])
_l_(631318)

_c_(631321, _n_(631319, "print", lambda: print), _n_(631320, "ket_1", lambda: ket_1))
_l_(631322)