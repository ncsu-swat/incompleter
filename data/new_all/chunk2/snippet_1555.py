# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/22961897/why-do-i-get-and-error-when-my-loop-runs-the-2nd-time-typeerror-int-object-h
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy
    _l_(467039)

except ImportError:
    pass

board = _c_(467042, _a_(467041, _n_(467040, "numpy", lambda: numpy), "array"), [[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 2, 0, 0, 0],
                     [0, 0, 0, 2, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])
_l_(467043)



boardlist0 = [_n_(467044, "board", lambda: board)]*2
_l_(467045)

boardlist1 = []
_l_(467046)
ind = 0
_l_(467047)
move = [[0,0], [7,4]]
_l_(467048)


for k in _n_(467049, "move", lambda: move):
    _l_(467064)

    move = _n_(467050, "move", lambda: move)[_n_(467051, "ind", lambda: ind)]
    _l_(467052)

    _n_(467053, "boardlist0", lambda: boardlist0)[_n_(467054, "ind", lambda: ind)][_n_(467055, "move", lambda: move)[0]][_n_(467056, "move", lambda: move)[1]] = 1
    _l_(467057)

    _c_(467061, _a_(467059, _n_(467058, "boardlist1", lambda: boardlist1), "append"), _n_(467060, "boardlist0", lambda: boardlist0))
    _l_(467062)
    ind += 1
    _l_(467063)