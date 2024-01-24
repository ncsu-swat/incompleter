# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57224598/attributeerror-module-matlab-has-no-attribute-engine
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matlab
    _l_(392330)

except ImportError:
    pass
try:
    from numpy import *
    _l_(392332)

except ImportError:
    pass
try:
    import sys
    _l_(392334)

except ImportError:
    pass
if _n_(392335, "__name__", lambda: __name__) == '__main__':
    _l_(392385)

    _c_(392339, _n_(392336, "print", lambda: print), _a_(392338, _n_(392337, "sys", lambda: sys), "maxsize") > 2 ** 32)
    _l_(392340)
    eng = _c_(392344, _a_(392343, _a_(392342, _n_(392341, "matlab", lambda: matlab), "engine"), "connect_matlab"))
    _l_(392345)
    names = _c_(392349, _a_(392348, _a_(392347, _n_(392346, "matlab", lambda: matlab), "engine"), "find_matlab"))
    _l_(392350)
    _c_(392353, _n_(392351, "print", lambda: print), _n_(392352, "names", lambda: names))
    _l_(392354)

    eng = _c_(392358, _a_(392357, _a_(392356, _n_(392355, "matlab", lambda: matlab), "engine"), "start_matlab"))
    _l_(392359)
    A = _c_(392362, _a_(392361, _n_(392360, "matlab", lambda: matlab), "double"), [[1,2],[5,6]])
    _l_(392363)
    _c_(392371, _n_(392364, "print", lambda: print), _c_(392367, _n_(392365, "type", lambda: type), _n_(392366, "A", lambda: A)),_a_(392369, _n_(392368, "A", lambda: A), "size"),_n_(392370, "A", lambda: A))
    _l_(392372)
    _c_(392378, _n_(392373, "print", lambda: print), _c_(392377, _a_(392375, _n_(392374, "eng", lambda: eng), "eig"), _n_(392376, "A", lambda: A)))
    _l_(392379)
    _c_(392382, _a_(392381, _n_(392380, "eng", lambda: eng), "quit"))
    _l_(392383)
    pass
    _l_(392384)