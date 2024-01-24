# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63442808/typeerror-list-indices-must-be-integers-or-slices-not-nonetype-on-a-connect-4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(340080)

    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]
    _l_(340009)

    board_list = []
    _l_(340010)
    while _c_(340013, _n_(340011, "len", lambda: len), _n_(340012, "board", lambda: board)[0]) > _c_(340016, _n_(340014, "len", lambda: len), _n_(340015, "board_list", lambda: board_list)):
        _l_(340026)

        _c_(340024, _a_(340018, _n_(340017, "board_list", lambda: board_list), "append"), _c_(340023, _n_(340019, "str", lambda: str), _c_(340022, _n_(340020, "len", lambda: len), _n_(340021, "board_list", lambda: board_list)) + 1))
        _l_(340025)

    _c_(340028, _n_(340027, "header", lambda: header))
    _l_(340029)

    active_player_index = 0
    _l_(340030)
    players = ["Vasco", "PC"]
    _l_(340031)
    symbols = ["O", "X"]
    _l_(340032)
    player = _n_(340033, "players", lambda: players)[_n_(340034, "active_player_index", lambda: active_player_index)]
    _l_(340035)

    while not _c_(340038, _n_(340036, "find_winner", lambda: find_winner), _n_(340037, "board", lambda: board)):
        _l_(340076)

        # show the board
        player = _n_(340039, "players", lambda: players)[_n_(340040, "active_player_index", lambda: active_player_index)]
        _l_(340041)
        symbol = _n_(340042, "symbols", lambda: symbols)[_n_(340043, "active_player_index", lambda: active_player_index)]
        _l_(340044)

        _c_(340047, _n_(340045, "announce_turn", lambda: announce_turn), _n_(340046, "player", lambda: player))
        _l_(340048)
        _c_(340051, _n_(340049, "show_board", lambda: show_board), _n_(340050, "board", lambda: board))
        _l_(340052)
        if not _c_(340056, _n_(340053, "choose_location", lambda: choose_location), _n_(340054, "board", lambda: board), _n_(340055, "symbol", lambda: symbol)):
            _l_(340070)

            _c_(340058, _n_(340057, "print", lambda: print))
            _l_(340059)
            _c_(340061, _n_(340060, "print", lambda: print), "You're an UBER IDIOT!")
            _l_(340062)
            _c_(340064, _n_(340063, "print", lambda: print), "That spot was already used!")
            _l_(340065)
            _c_(340067, _n_(340066, "print", lambda: print))
            _l_(340068)
            continue
            _l_(340069)

        #   toggle active player
        active_player_index = (_n_(340071, "active_player_index", lambda: active_player_index) + 1) % _c_(340074, _n_(340072, "len", lambda: len), _n_(340073, "player", lambda: player))
        _l_(340075)

    _c_(340078, _n_(340077, "footer", lambda: footer))
    _l_(340079)


def header():
    _l_(340099)

    _c_(340082, _n_(340081, "print", lambda: print))
    _l_(340083)
    _c_(340085, _n_(340084, "print", lambda: print), "-----------------------------")
    _l_(340086)
    _c_(340088, _n_(340087, "print", lambda: print), "----------WHALECUM-----------")
    _l_(340089)
    _c_(340091, _n_(340090, "print", lambda: print), "-----------------------------")
    _l_(340092)
    _c_(340094, _n_(340093, "print", lambda: print), "----------CONNECT 4----------")
    _l_(340095)
    _c_(340097, _n_(340096, "print", lambda: print), "-----------------------------")
    _l_(340098)


def footer():
    _l_(340112)

    _c_(340101, _n_(340100, "print", lambda: print))
    _l_(340102)
    _c_(340104, _n_(340103, "print", lambda: print), "-----------------------------")
    _l_(340105)
    _c_(340107, _n_(340106, "print", lambda: print), "-----------THE END-----------")
    _l_(340108)
    _c_(340110, _n_(340109, "print", lambda: print), "-----------------------------")
    _l_(340111)


def show_board(board):
    _l_(340144)

    _c_(340114, _n_(340113, "print", lambda: print))
    _l_(340115)
    for row in _n_(340116, "board", lambda: board):
        _l_(340132)

        _c_(340118, _n_(340117, "print", lambda: print), "| ", end='')
        _l_(340119)
        for cell in _n_(340120, "row", lambda: row):
            _l_(340128)

            symbol = _n_(340121, "cell", lambda: cell) if _n_(340122, "cell", lambda: cell) is not None else " "
            _l_(340123)
            _c_(340126, _n_(340124, "print", lambda: print), _n_(340125, "symbol", lambda: symbol), end=" | ")
            _l_(340127)
        _c_(340130, _n_(340129, "print", lambda: print))
        _l_(340131)
    for index, r in _c_(340135, _n_(340133, "enumerate", lambda: enumerate), _n_(340134, "board", lambda: board)[0], start=1):
        _l_(340140)

        _c_(340138, _n_(340136, "print", lambda: print), f"  {_n_(340137, 'index', lambda: index)} ", end="")
        _l_(340139)
    _c_(340142, _n_(340141, "print", lambda: print))
    _l_(340143)


def announce_turn(player):
    _l_(340167)

    _c_(340146, _n_(340145, "print", lambda: print))
    _l_(340147)
    _c_(340150, _n_(340148, "print", lambda: print), f"It's {_n_(340149, 'player', lambda: player)} turn!")
    _l_(340151)
    _c_(340153, _n_(340152, "print", lambda: print))
    _l_(340154)
    _c_(340156, _n_(340155, "print", lambda: print), "Pick your column...")
    _l_(340157)
    _c_(340159, _n_(340158, "print", lambda: print))
    _l_(340160)
    _c_(340162, _n_(340161, "print", lambda: print), "Here's the Board:")
    _l_(340163)
    _c_(340165, _n_(340164, "print", lambda: print))
    _l_(340166)


def choose_location(board, symbol, board_list):
    _l_(340206)

    column = _c_(340169, _n_(340168, "input", lambda: input), "Choose a column: ")
    _l_(340170)
    while _n_(340171, "column", lambda: column) not in _n_(340172, "board_list", lambda: board_list):
        _l_(340180)

        _c_(340175, _n_(340173, "print", lambda: print), f"{_n_(340174, 'column', lambda: column)} is not an option, try again")
        _l_(340176)
        column = _c_(340178, _n_(340177, "input", lambda: input), "Choose a column: ")
        _l_(340179)
    column = _c_(340183, _n_(340181, "int", lambda: int), _n_(340182, "column", lambda: column)) - 1
    _l_(340184)
    row = None
    _l_(340185)

    while _n_(340186, "board", lambda: board)[_n_(340187, "row", lambda: row)][_n_(340188, "column", lambda: column)] is None:
        _l_(340190)

        row += 1
        _l_(340189)
    row = _n_(340191, "row", lambda: row) - 1
    _l_(340192)
    cell = _n_(340193, "board", lambda: board)[_n_(340194, "row", lambda: row)][_n_(340195, "column", lambda: column)]
    _l_(340196)
    if _n_(340197, "cell", lambda: cell) is not None:
        _l_(340199)

        aux = False
        _l_(340198)
        return aux

    _n_(340200, "board", lambda: board)[_n_(340201, "row", lambda: row)][_n_(340202, "column", lambda: column)] = _n_(340203, "symbol", lambda: symbol)
    _l_(340204)
    aux = True
    _l_(340205)
    return aux


def find_winner(board):
    _l_(340224)

    sequences = _c_(340209, _n_(340207, "get_winning_sequences", lambda: get_winning_sequences), _n_(340208, "board", lambda: board))
    _l_(340210)

    for cells in _n_(340211, "sequences", lambda: sequences):
        _l_(340222)

        symbol1 = _n_(340212, "cells", lambda: cells)[0]
        _l_(340213)
        if _n_(340214, "symbol1", lambda: symbol1) and _c_(340219, _n_(340215, "all", lambda: all), (_n_(340216, "symbol1", lambda: symbol1) == _n_(340217, "cell", lambda: cell) for cell in _n_(340218, "cells", lambda: cells))):
            _l_(340221)

            aux = True
            _l_(340220)
            return aux
    aux = False
    _l_(340223)

    return aux


def get_winning_sequences(board):
    _l_(340262)

    sequences = []
    _l_(340225)

    # win by row
    rows = _n_(340226, "board", lambda: board)
    _l_(340227)
    _c_(340231, _a_(340229, _n_(340228, "sequences", lambda: sequences), "extend"), _n_(340230, "rows", lambda: rows))
    _l_(340232)

    # win by columns
    for col_idx in _c_(340234, _n_(340233, "range", lambda: range), 0, 3):
        _l_(340247)

        col = [
            _n_(340235, "board", lambda: board)[0][_n_(340236, "col_idx", lambda: col_idx)],
            _n_(340237, "board", lambda: board)[1][_n_(340238, "col_idx", lambda: col_idx)],
            _n_(340239, "board", lambda: board)[2][_n_(340240, "col_idx", lambda: col_idx)],
        ]
        _l_(340241)
        _c_(340245, _a_(340243, _n_(340242, "sequences", lambda: sequences), "append"), _n_(340244, "col", lambda: col))
        _l_(340246)

    # win by diagonals
    diagonals = [
        [_n_(340248, "board", lambda: board)[0][0], _n_(340249, "board", lambda: board)[1][1], _n_(340250, "board", lambda: board)[2][2]],
        [_n_(340251, "board", lambda: board)[0][2], _n_(340252, "board", lambda: board)[1][1], _n_(340253, "board", lambda: board)[2][0]],
    ]
    _l_(340254)
    _c_(340258, _a_(340256, _n_(340255, "sequences", lambda: sequences), "extend"), _n_(340257, "diagonals", lambda: diagonals))
    _l_(340259)
    aux = _n_(340260, "sequences", lambda: sequences)
    _l_(340261)

    return aux


if _n_(340263, "__name__", lambda: __name__) == '__main__':
    _l_(340267)

    _c_(340265, _n_(340264, "main", lambda: main))
    _l_(340266)