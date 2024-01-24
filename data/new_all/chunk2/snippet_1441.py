# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58389828/typeerror-unhashable-type-list-in-python-chess-program
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
king=(5,1)
_l_(475070)
opponentmoves={'ksknight': [(8, 3), (5, 2), (6, 3)],
 'ksbishop': [(3, 6), (4, 7), (5, 8), (1, 4), (1, 6), (3, 4), (4, 3), (5, 1), (6, 1)],
 'king': [(6, 1), (5, 2), (4, 1)],
 'queen': [(4, 5), (2, 4), (1, 3), (2, 6), (1, 7), (4, 4)],
 'qsknight': [(3, 3), (1, 3)]}
_l_(475071)
opponentposition={'ksknight': (1, 3), 
 'ksbishop': (1, 6), 
 'king': (6, 1), 
 'queen': (4, 5), 
 'qsknight': (3, 3)}
_l_(475072)
if _n_(475073, "king", lambda: king) in [_n_(475074, "z", lambda: z) for v in _c_(475077, _a_(475076, _n_(475075, "opponentmoves", lambda: opponentmoves), "values")) for z in _n_(475078, "v", lambda: v)]:
    _l_(475094)

    piece=[_n_(475079, "key", lambda: key) for key in _n_(475080, "opponentmoves", lambda: opponentmoves) if _n_(475081, "king", lambda: king) in _n_(475082, "opponentmoves", lambda: opponentmoves)[_n_(475083, "key", lambda: key)]]
    _l_(475084)
    opponentpieceposition=_c_(475088, _a_(475086, _n_(475085, "opponentposition", lambda: opponentposition), "get"), _n_(475087, "piece", lambda: piece))
    _l_(475089)
    _c_(475092, _n_(475090, "print", lambda: print), _n_(475091, "opponentpieceposition", lambda: opponentpieceposition))
    _l_(475093)