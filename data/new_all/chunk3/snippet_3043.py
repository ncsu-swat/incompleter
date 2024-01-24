# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52000635/typeerror-nonetype-object-is-not-callable-but-object-is-not-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def winner(board):
    _l_(562464)

    WAYS_TOWIN = ((0, 1, 2),
                  (3, 4, 5),
                  (6, 7, 8),
                  (0, 4, 8),
                  (2, 4, 6),
                  (0, 3, 6),
                  (1, 4, 7),
                  (2, 5, 8))
    _l_(562444)
    for row in _n_(562445, "WAYS_TOWIN", lambda: WAYS_TOWIN):
        _l_(562458)

        if _n_(562446, "board", lambda: board)[_n_(562447, "row", lambda: row)[0]] == _n_(562448, "board", lambda: board)[_n_(562449, "row", lambda: row)[1]] == _n_(562450, "board", lambda: board)[_n_(562451, "row", lambda: row)[2]] != " ":
            _l_(562457)

            winner = _n_(562452, "board", lambda: board)[_n_(562453, "row", lambda: row)[0]]
            _l_(562454)
            aux = _n_(562455, "winner", lambda: winner)
            _l_(562456)
            return aux
    if " " not in _n_(562459, "board", lambda: board):
        _l_(562463)

        aux = _n_(562460, "TIE", lambda: TIE)
        _l_(562461)
        return aux
    else:
        aux = None
        _l_(562462)
        return aux



#Main
_c_(562466, _n_(562465, "instructions", lambda: instructions))
_l_(562467)
human = _c_(562469, _n_(562468, "input", lambda: input), "Enter your name: "); _c_(562471, _n_(562470, "print", lambda: print), "\n")
_l_(562472)
pieces = _c_(562476, _n_(562473, "who_first", lambda: who_first), _n_(562474, "human", lambda: human), _n_(562475, "computer", lambda: computer)); _c_(562478, _n_(562477, "print", lambda: print), "\n")#pieces becomes a list with human piece first and computer piece second
_l_(562479)#pieces becomes a list with human piece first and computer piece second
board = _c_(562481, _n_(562480, "new_board", lambda: new_board)); _c_(562483, _n_(562482, "print", lambda: print), "\n")
_l_(562484)
winner = _c_(562487, _n_(562485, "winner", lambda: winner), _n_(562486, "board", lambda: board))
_l_(562488)



while _n_(562489, "winner", lambda: winner) == None and _n_(562490, "winner", lambda: winner) != _n_(562491, "TIE", lambda: TIE):
    _l_(562499)

    if _n_(562492, "turn", lambda: turn) == _n_(562493, "pieces", lambda: pieces)[0]:
        _l_(562498)

        winner = _c_(562496, _n_(562494, "winner", lambda: winner), _n_(562495, "board", lambda: board))
        _l_(562497)