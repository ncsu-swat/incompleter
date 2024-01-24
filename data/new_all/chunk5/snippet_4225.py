# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61125518/is-there-a-way-to-get-the-sum-of-non-zero-elements-in-numpy-array-i-keep-gettin
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
result=[]
_l_(706160)
FracPos = _c_(706164, _a_(706162, _n_(706161, "np", lambda: np), "array"), _n_(706163, "result", lambda: result))
_l_(706165)
for x in _n_(706166, "lines", lambda: lines):
    _l_(706174)

    _c_(706172, _a_(706168, _n_(706167, "result", lambda: result), "append"), _c_(706171, _a_(706170, _n_(706169, "x", lambda: x), "split")))
    _l_(706173)
TotalCells = _c_(706178, _a_(706176, _n_(706175, "np", lambda: np), "array"), _n_(706177, "result", lambda: result))[:,2]
_l_(706179)
_c_(706184, _n_(706180, "print", lambda: print), _c_(706183, _n_(706181, "type", lambda: type), _n_(706182, "TotalCells", lambda: TotalCells)))
_l_(706185)
_c_(706190, _n_(706186, "print", lambda: print), _c_(706189, _n_(706187, "type", lambda: type), _n_(706188, "FracPos", lambda: FracPos)))
_l_(706191)
FracPos = _c_(706195, _a_(706193, _n_(706192, "np", lambda: np), "sum"), _n_(706194, "TotalCells", lambda: (TotalCells))>0)
_l_(706196)