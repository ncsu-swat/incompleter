# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67453146/typeerror-in-tic-tac-toe-game-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(608202)

except ImportError:
    pass
try:
    from player import HumanPlayer, RandomComputerPlayer
    _l_(608204)

except ImportError:
    pass

class TicTacToe:
    _l_(608339)

    def __init__(self):
        _l_(608211)

        _n_(608205, "self", lambda: self).board = [' ' for _ in _c_(608207, _n_(608206, "range", lambda: range), 9)]
        _l_(608208)
        _n_(608209, "self", lambda: self).current_winner = None
        _l_(608210)
    
    def print_board(self):
        _l_(608225)

        for row in [_a_(608213, _n_(608212, "self", lambda: self), "board")[_n_(608214, "i", lambda: i)*3:(_n_(608215, "i", lambda: i)+1)*3] for i in _c_(608217, _n_(608216, "range", lambda: range), 3)]:
            _l_(608224)

            _c_(608222, _n_(608218, "print", lambda: print), '| ' + _c_(608221, _a_(608219, ' | ', "join"), _n_(608220, "row", lambda: row)) + ' |')
            _l_(608223)

    @_n_(608226, "staticmethod", lambda: staticmethod)
    def print_board_nums():
        _l_(608245)

        number_board = [[_c_(608229, _n_(608227, "str", lambda: str), _n_(608228, "i", lambda: i)) for i in _c_(608233, _n_(608230, "range", lambda: range), _n_(608231, "j", lambda: j)*3, (_n_(608232, "j", lambda: j)+1)*3)] for j in _c_(608235, _n_(608234, "range", lambda: range), 3)]
        _l_(608236)
        for row in _n_(608237, "number_board", lambda: number_board):
            _l_(608244)

            _c_(608242, _n_(608238, "print", lambda: print), '| ' + _c_(608241, _a_(608239, ' | ', "join"), _n_(608240, "row", lambda: row)) + ' |')
            _l_(608243)

    def available_moves(self):
        _l_(608253)

        aux = [_n_(608246, "i", lambda: i) for i, spot in _c_(608250, _n_(608247, "enumerate", lambda: enumerate), _a_(608249, _n_(608248, "self", lambda: self), "board")) if _n_(608251, "spot", lambda: spot) == ' ']
        _l_(608252)
        return aux

    def empty_squares(self):
        _l_(608257)

        aux = ' ' in _a_(608255, _n_(608254, "self", lambda: self), "board")
        _l_(608256)
        return aux

    def num_empty_squares(self):
        _l_(608263)

        aux = _c_(608261, _a_(608260, _a_(608259, _n_(608258, "self", lambda: self), "board"), "count"), ' ')
        _l_(608262)
        return aux

    def make_move(self, square, letter):
        _l_(608284)

        if _a_(608265, _n_(608264, "self", lambda: self), "board")[_n_(608266, "square", lambda: square)] == ' ':
            _l_(608282)

            _a_(608268, _n_(608267, "self", lambda: self), "board")[_n_(608269, "square", lambda: square)] = _n_(608270, "letter", lambda: letter)
            _l_(608271)
            if _c_(608276, _a_(608273, _n_(608272, "self", lambda: self), "winner"), _n_(608274, "square", lambda: square), _n_(608275, "letter", lambda: letter)):
                _l_(608280)

                _n_(608277, "self", lambda: self).current_winner = _n_(608278, "letter", lambda: letter)
                _l_(608279)
            aux = True
            _l_(608281)
            return aux
        aux = False
        _l_(608283)
        return aux

    def winner(self, square, letter):
        _l_(608338)

        row_ind = _n_(608285, "square", lambda: square) // 3
        _l_(608286)
        row = _a_(608288, _n_(608287, "self", lambda: self), "board")[_n_(608289, "row_ind", lambda: row_ind)*3:(_n_(608290, "row_ind", lambda: row_ind)+1)*3]
        _l_(608291)
        if _c_(608296, _n_(608292, "all", lambda: all), [_n_(608293, "spot", lambda: spot) == _n_(608294, "letter", lambda: letter) for spot in _n_(608295, "row", lambda: row)]):
            _l_(608298)

            aux = True
            _l_(608297)
            return aux

        col_ind = _n_(608299, "square", lambda: square) % 3
        _l_(608300)
        column = _a_(608302, _n_(608301, "self", lambda: self), "board")[_n_(608303, "col_ind", lambda: col_ind)*3:(_n_(608304, "col_ind", lambda: col_ind)+1)*3]
        _l_(608305)
        if _c_(608310, _n_(608306, "all", lambda: all), [_n_(608307, "spot", lambda: spot) == _n_(608308, "letter", lambda: letter) for spot in _n_(608309, "column", lambda: column)]):
            _l_(608312)

            aux = True
            _l_(608311)
            return aux

        if _n_(608313, "square", lambda: square) % 2 == 0:
            _l_(608336)

            diag1 = [_a_(608315, _n_(608314, "self", lambda: self), "board")[_n_(608316, "i", lambda: i)] for i in [0, 4, 8]]
            _l_(608317)
            if _c_(608322, _n_(608318, "all", lambda: all), [_n_(608319, "spot", lambda: spot) == _n_(608320, "letter", lambda: letter) for spot in _n_(608321, "diag1", lambda: diag1)]):
                _l_(608324)

                aux = True
                _l_(608323)
                return aux
            diag2 = [_a_(608326, _n_(608325, "self", lambda: self), "board")[_n_(608327, "i", lambda: i)] for i in [2, 4, 6]]
            _l_(608328)
            if _c_(608333, _n_(608329, "all", lambda: all), [_n_(608330, "spot", lambda: spot) == _n_(608331, "letter", lambda: letter) for spot in _n_(608332, "diag2", lambda: diag2)]):
                _l_(608335)

                aux = True
                _l_(608334)
                return aux
        aux = False
        _l_(608337)

        return aux



def play(game, x_player, o_player, print_game=True):
    _l_(608405)

    if _n_(608340, "print_game", lambda: print_game):
        _l_(608345)

        _c_(608343, _a_(608342, _n_(608341, "game", lambda: game), "print_board_nums"))
        _l_(608344)
    
    letter = 'X'
    _l_(608346)
    
    while _c_(608349, _a_(608348, _n_(608347, "game", lambda: game), "empty_squares")):
        _l_(608399)

        if _n_(608350, "letter", lambda: letter) == 'O':
            _l_(608361)

            square = _c_(608354, _a_(608352, _n_(608351, "o_player", lambda: o_player), "get_move"), _n_(608353, "game", lambda: game))
            _l_(608355)
        else:
            square = _c_(608359, _a_(608357, _n_(608356, "x_player", lambda: x_player), "get_move"), _n_(608358, "game", lambda: game))
            _l_(608360)
        
        if _c_(608366, _a_(608363, _n_(608362, "game", lambda: game), "make_move"), _n_(608364, "square", lambda: square), _n_(608365, "letter", lambda: letter)):
            _l_(608394)

            if _n_(608367, "print_game", lambda: print_game):
                _l_(608380)

                _c_(608371, _n_(608368, "print", lambda: print), _n_(608369, "letter", lambda: letter) + f' makes a move to a square {_n_(608370, "square", lambda: square)}')
                _l_(608372)
                _c_(608375, _a_(608374, _n_(608373, 'game', lambda: game), 'print_board'))
                _l_(608376)
                _c_(608378, _n_(608377, 'print', lambda: print), '')
                _l_(608379)

            if _a_(608382, _n_(608381, 'game', lambda: game), 'current_winner'):
                _l_(608391)

                if _n_(608383, 'print_game', lambda: print_game):
                    _l_(608388)

                    _c_(608386, _n_(608384, 'print', lambda: print), _n_(608385, 'letter', lambda: letter) + ' wins!')
                    _l_(608387)
                aux = _n_(608389, 'letter', lambda: letter)
                _l_(608390)
                return aux
            
            letter = 'O' if _n_(608392, 'letter', lambda: letter) == 'X' else 'X'
            _l_(608393)

        _c_(608397, _a_(608396, _n_(608395, 'time', lambda: time), 'sleep'), 0.8)
        _l_(608398)

    if _n_(608400, 'print_game', lambda: print_game):
        _l_(608404)

        _c_(608402, _n_(608401, 'print', lambda: print), 'It\'s a tie')
        _l_(608403)

if _n_(608406, '__name__', lambda: __name__) == '__main__':
    _l_(608422)

    x_player = _c_(608408, _n_(608407, 'HumanPlayer', lambda: HumanPlayer), 'X')
    _l_(608409)
    o_player = _c_(608411, _n_(608410, 'RandomComputerPlayer', lambda: RandomComputerPlayer), 'O')
    _l_(608412)
    t = _c_(608414, _n_(608413, 'TicTacToe', lambda: TicTacToe))
    _l_(608415)
    _c_(608420, _n_(608416, 'play', lambda: play), _n_(608417, 't', lambda: t), _n_(608418, 'x_player', lambda: x_player), _n_(608419, 'o_player', lambda: o_player), print_game=True)
    _l_(608421)