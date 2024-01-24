# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56070136/typeerror-running-tic-tac-toe-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import turtle
    _l_(527619)

except ImportError:
    pass
try:
    import time
    _l_(527621)

except ImportError:
    pass
try:
    import random
    _l_(527623)

except ImportError:
    pass

pieces = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
_l_(527624)
turn = "X"
_l_(527625)
def drawgame(brd):
    _l_(527804)

    # draw board
    _c_(527628, _a_(527627, _n_(527626, "turtle", lambda: turtle), "setup"), 600, 600)
    _l_(527629)
    _c_(527632, _a_(527631, _n_(527630, "turtle", lambda: turtle), "bgcolor"), "silver")
    _l_(527633)
    _c_(527636, _a_(527635, _n_(527634, "turtle", lambda: turtle), "color"), "white")
    _l_(527637)
    _c_(527640, _a_(527639, _n_(527638, "turtle", lambda: turtle), "width"), 10)
    _l_(527641)
    _c_(527644, _a_(527643, _n_(527642, "turtle", lambda: turtle), "up"))
    _l_(527645)

    # Horizontal bars
    _c_(527648, _a_(527647, _n_(527646, "turtle", lambda: turtle), "goto"), -300, 100)
    _l_(527649)
    _c_(527652, _a_(527651, _n_(527650, "turtle", lambda: turtle), "down"))
    _l_(527653)
    _c_(527656, _a_(527655, _n_(527654, "turtle", lambda: turtle), "forward"), 600)
    _l_(527657)
    _c_(527660, _a_(527659, _n_(527658, "turtle", lambda: turtle), "up"))
    _l_(527661)
    _c_(527664, _a_(527663, _n_(527662, "turtle", lambda: turtle), "goto"), -300, -100)
    _l_(527665)
    _c_(527668, _a_(527667, _n_(527666, "turtle", lambda: turtle), "down"))
    _l_(527669)
    _c_(527672, _a_(527671, _n_(527670, "turtle", lambda: turtle), "forward"), 600)
    _l_(527673)
    _c_(527676, _a_(527675, _n_(527674, "turtle", lambda: turtle), "up"))
    _l_(527677)

    # Vertical bars
    _c_(527680, _a_(527679, _n_(527678, "turtle", lambda: turtle), "goto"), -100, 300)
    _l_(527681)
    _c_(527684, _a_(527683, _n_(527682, "turtle", lambda: turtle), "setheading"), -90)
    _l_(527685)
    _c_(527688, _a_(527687, _n_(527686, "turtle", lambda: turtle), "down"))
    _l_(527689)
    _c_(527692, _a_(527691, _n_(527690, "turtle", lambda: turtle), "forward"), 600)
    _l_(527693)
    _c_(527696, _a_(527695, _n_(527694, "turtle", lambda: turtle), "up"))
    _l_(527697)
    _c_(527700, _a_(527699, _n_(527698, "turtle", lambda: turtle), "goto"), 100, 300)
    _l_(527701)
    _c_(527704, _a_(527703, _n_(527702, "turtle", lambda: turtle), "down"))
    _l_(527705)
    _c_(527708, _a_(527707, _n_(527706, "turtle", lambda: turtle), "forward"), 600)
    _l_(527709)
    _c_(527712, _a_(527711, _n_(527710, "turtle", lambda: turtle), "up"))
    _l_(527713)
    _c_(527716, _a_(527715, _n_(527714, "turtle", lambda: turtle), "color"), "blue")
    _l_(527717)
    x, y = -300, 300
    _l_(527718)
    for pos in _n_(527719, "pieces", lambda: pieces):
        _l_(527803)

        if _n_(527720, "pos", lambda: pos) == "X":
            _l_(527797)

            # Draw X
            _c_(527723, _a_(527722, _n_(527721, "turtle", lambda: turtle), "up"))
            _l_(527724)
            _c_(527729, _a_(527726, _n_(527725, "turtle", lambda: turtle), "goto"), _n_(527727, "x", lambda: x) + 20, _n_(527728, "y", lambda: y) - 20)
            _l_(527730)
            _c_(527733, _a_(527732, _n_(527731, "turtle", lambda: turtle), "setheading"), -45)
            _l_(527734)
            _c_(527737, _a_(527736, _n_(527735, "turtle", lambda: turtle), "down"))
            _l_(527738)
            _c_(527741, _a_(527740, _n_(527739, "turtle", lambda: turtle), "forward"), 226)
            _l_(527742)
            _c_(527745, _a_(527744, _n_(527743, "turtle", lambda: turtle), "up"))
            _l_(527746)
            _c_(527751, _a_(527748, _n_(527747, "turtle", lambda: turtle), "goto"), _n_(527749, "x", lambda: x) + 180, _n_(527750, "y", lambda: y) - 20)
            _l_(527752)
            _c_(527755, _a_(527754, _n_(527753, "turtle", lambda: turtle), "setheading"), -135)
            _l_(527756)
            _c_(527759, _a_(527758, _n_(527757, "turtle", lambda: turtle), "down"))
            _l_(527760)
            _c_(527763, _a_(527762, _n_(527761, "turtle", lambda: turtle), "forward"), 226)
            _l_(527764)
            _c_(527767, _a_(527766, _n_(527765, "turtle", lambda: turtle), "up"))
            _l_(527768)

        elif _n_(527769, "pos", lambda: pos) == "O":
            _l_(527796)

            #Draw O
            _c_(527772, _a_(527771, _n_(527770, "turtle", lambda: turtle), "up"))
            _l_(527773)
            _c_(527778, _a_(527775, _n_(527774, "turtle", lambda: turtle), "goto"), _n_(527776, "x", lambda: x) + 100, _n_(527777, "y", lambda: y) - 180)
            _l_(527779)
            _c_(527782, _a_(527781, _n_(527780, "turtle", lambda: turtle), "setheading"), 0)
            _l_(527783)
            _c_(527786, _a_(527785, _n_(527784, "turtle", lambda: turtle), "down"))
            _l_(527787)
            _c_(527790, _a_(527789, _n_(527788, "turtle", lambda: turtle), "circle"), 80)
            _l_(527791)
            _c_(527794, _a_(527793, _n_(527792, "turtle", lambda: turtle), "up"))
            _l_(527795)
        x += 200
        _l_(527798)
        if _n_(527799, "x", lambda: x) > 100:
            _l_(527802)

            x = -300
            _l_(527800)
            y -= 200
            _l_(527801)


def clicked(board, x, y):
    _l_(527852)

    #sig: list(str), int, int -> bool 
    #THIS FUNCTION MUST RETURN A BOOL, true if operation is successful, false otherwise
    global turn, pieces
    _l_(527805)

    done = True
    _l_(527806)

    _c_(527809, _a_(527808, _n_(527807, "turtle", lambda: turtle), "onscreenclick"), None)  # disabling handler when inside handler
    _l_(527810)  # disabling handler when inside handler
    column = (_n_(527811, "x", lambda: x) + 300) // 200
    _l_(527812)
    row = (_n_(527813, "y", lambda: y) - 300) // -200
    _l_(527814)
    square = _c_(527818, _n_(527815, "int", lambda: int), _n_(527816, "row", lambda: row) * 3 + _n_(527817, "column", lambda: column))
    _l_(527819)
    _c_(527824, _n_(527820, "print", lambda: print), "User clicked ", _n_(527821, "x", lambda: x), ",", _n_(527822, "y", lambda: y), " at square ", _n_(527823, "square", lambda: square))
    _l_(527825)

    if _n_(527826, "pieces", lambda: pieces)[_n_(527827, "square", lambda: square)] == "_":
        _l_(527844)

        _n_(527828, "pieces", lambda: pieces)[_n_(527829, "square", lambda: square)] = _n_(527830, "turn", lambda: turn)
        _l_(527831)
        if _n_(527832, "turn", lambda: turn) == "X":
            _l_(527835)

            turn = "O"
            _l_(527833)
        else:
            turn = "X"
            _l_(527834)
        _c_(527838, _n_(527836, "drawgame", lambda: drawgame), _n_(527837, "pieces", lambda: pieces))
        _l_(527839)
    else:
        _c_(527841, _n_(527840, "print", lambda: print), "That square is already taken")
        _l_(527842)
        done = False
        _l_(527843)
    _c_(527848, _a_(527846, _n_(527845, "turtle", lambda: turtle), "onscreenclick"), _n_(527847, "clicked", lambda: clicked))
    _l_(527849)
    aux = _n_(527850, "done", lambda: done)
    _l_(527851)

    return aux


def computer_AI(board):
    _l_(527875)

    #sig: list(str) -> NoneType
    #construct an AI that competes against the user

    #Random AI selection
    AI_selection = _c_(527855, _a_(527854, _n_(527853, "random", lambda: random), "randint"), 0,8) 
    _l_(527856) 

    #check for an empty space
    while _n_(527857, "pieces", lambda: pieces)[_n_(527858, "AI_selection", lambda: AI_selection)] != "_":
        _l_(527863)

        AI_selection = _c_(527861, _a_(527860, _n_(527859, "random", lambda: random), "randint"), 0,8)
        _l_(527862)

    #Mark
    _n_(527864, "pieces", lambda: pieces)[_n_(527865, "AI_selection", lambda: AI_selection)] = "O"
    _l_(527866)

    _c_(527869, _n_(527867, "print", lambda: print), "Computer Mark at :",_n_(527868, "AI_selection", lambda: AI_selection))
    _l_(527870)

    _c_(527873, _n_(527871, "drawgame", lambda: drawgame), _n_(527872, "pieces", lambda: pieces))
    _l_(527874)

def check(P,table):
    _l_(527946)

    win = False
    _l_(527876)

    '''ROWS'''
    _l_(527877)
    #check 1 row
    if (_n_(527878, "table", lambda: table)[0] == _n_(527879, "P", lambda: P)) and (_n_(527880, "table", lambda: table)[1] == _n_(527881, "P", lambda: P)) and (_n_(527882, "table", lambda: table)[2] == _n_(527883, "P", lambda: P)):
        _l_(527885)

        win = True  
        _l_(527884)  
    #check 2 row
    if (_n_(527886, "table", lambda: table)[3] == _n_(527887, "P", lambda: P)) and (_n_(527888, "table", lambda: table)[4] == _n_(527889, "P", lambda: P)) and (_n_(527890, "table", lambda: table)[5] == _n_(527891, "P", lambda: P)):
        _l_(527893)

        win = True 
        _l_(527892) 
    #check3 row
    if (_n_(527894, "table", lambda: table)[6] == _n_(527895, "P", lambda: P)) and (_n_(527896, "table", lambda: table)[7] == _n_(527897, "P", lambda: P)) and (_n_(527898, "table", lambda: table)[8] == _n_(527899, "P", lambda: P)):
        _l_(527901)

        win = True
        _l_(527900)

    '''COLUMNS'''
    _l_(527902)
    #check 1 Col
    if (_n_(527903, "table", lambda: table)[0] == _n_(527904, "P", lambda: P)) and (_n_(527905, "table", lambda: table)[3] == _n_(527906, "P", lambda: P)) and (_n_(527907, "table", lambda: table)[6] == _n_(527908, "P", lambda: P)):
        _l_(527910)

        win = True
        _l_(527909)
    #check 2 Col
    if (_n_(527911, "table", lambda: table)[1] == _n_(527912, "P", lambda: P)) and (_n_(527913, "table", lambda: table)[4] == _n_(527914, "P", lambda: P)) and (_n_(527915, "table", lambda: table)[7] == _n_(527916, "P", lambda: P)):
        _l_(527918)

        win = True
        _l_(527917)
    #check 3 Col
    if (_n_(527919, "table", lambda: table)[2] == _n_(527920, "P", lambda: P)) and (_n_(527921, "table", lambda: table)[5] == _n_(527922, "P", lambda: P)) and (_n_(527923, "table", lambda: table)[8] == _n_(527924, "P", lambda: P)):
        _l_(527926)

        win = True
        _l_(527925)

    ''' Diag's '''
    _l_(527927)
    #check 1 Diag
    if (_n_(527928, "table", lambda: table)[0] == _n_(527929, "P", lambda: P)) and (_n_(527930, "table", lambda: table)[4] == _n_(527931, "P", lambda: P)) and (_n_(527932, "table", lambda: table)[8] == _n_(527933, "P", lambda: P)):
        _l_(527935)

        win = True
        _l_(527934)
    #check 2 diag
    if (_n_(527936, "table", lambda: table)[2] == _n_(527937, "P", lambda: P)) and (_n_(527938, "table", lambda: table)[4] == _n_(527939, "P", lambda: P)) and (_n_(527940, "table", lambda: table)[6] == _n_(527941, "P", lambda: P)):
        _l_(527943)

        win = True
        _l_(527942)
    aux = _n_(527944, "win", lambda: win)
    _l_(527945)

    return aux

def gameover(board):
    _l_(527995)

    #sig: list(str) -> bool
    #checks gameover on board if there is a three in a row pattern or not, check who wins

    game_over = False
    _l_(527947)
    #change font size here
    font_size = 30
    _l_(527948)

    if "_" not in _n_(527949, "pieces", lambda: pieces):
        _l_(527951)

        game_over = True
        _l_(527950)

    #when game over == true
    if_n_(527952, "game_over", lambda: (game_over)):
        _l_(527992)

        player_wins = _c_(527955, _n_(527953, "check", lambda: check), "X",_n_(527954, "pieces", lambda: pieces))
        _l_(527956)
        computer_wins = _c_(527959, _n_(527957, "check", lambda: check), "O",_n_(527958, "pieces", lambda: pieces))
        _l_(527960)

        if_n_(527961, "player_wins", lambda: (player_wins)):
            _l_(527991)

            _c_(527963, _n_(527962, "print", lambda: print), "Player Wins!")
            _l_(527964)
            _c_(527969, _a_(527966, _n_(527965, "turtle", lambda: turtle), "write"), "Player Wins!", align="center", font = ("Arial",_n_(527967, "font_size", lambda: font_size),_n_(527968, "bold", lambda: bold)) )
            _l_(527970)
        elif_n_(527971, "computer_wins", lambda: (computer_wins)):
            _l_(527990)

            _c_(527973, _n_(527972, "print", lambda: print), "Computer Wins!")
            _l_(527974)
            _c_(527979, _a_(527976, _n_(527975, "turtle", lambda: turtle), "write"), "Computer Wins!", align="center", font = ("Arial",_n_(527977, "font_size", lambda: font_size),_n_(527978, "bold", lambda: bold)) )
            _l_(527980)
        else:
            _c_(527982, _n_(527981, "print", lambda: print), "No Winner!")
            _l_(527983)
            _c_(527988, _a_(527985, _n_(527984, "turtle", lambda: turtle), "write"), "No Winner!", align="center", font = ("Arial",_n_(527986, "font_size", lambda: font_size),_n_(527987, "bold", lambda: bold)) )
            _l_(527989)
    aux = _n_(527993, "game_over", lambda: game_over)
    _l_(527994)


    return aux


def handler(x, y):
    _l_(528022)

    #sig: int, int -> NoneType
    if _c_(528000, _n_(527996, "clicked", lambda: clicked), _n_(527997, "pieces", lambda: pieces), _n_(527998, "x", lambda: x), _n_(527999, "y", lambda: y)):
        _l_(528021)

        _c_(528003, _n_(528001, "drawgame", lambda: drawgame), _n_(528002, "pieces", lambda: pieces))
        _l_(528004)
        if not _c_(528007, _n_(528005, "gameover", lambda: gameover), _n_(528006, "pieces", lambda: pieces)):
            _l_(528020)

            _c_(528010, _n_(528008, "computer_AI", lambda: computer_AI), _n_(528009, "pieces", lambda: pieces))
            _l_(528011)
            _c_(528014, _n_(528012, "drawgame", lambda: drawgame), _n_(528013, "pieces", lambda: pieces))
            _l_(528015)
            _c_(528018, _n_(528016, "gameover", lambda: gameover), _n_(528017, "pieces", lambda: pieces))
            _l_(528019)


def main():
    _l_(528044)

    #Runs the game 
    _c_(528025, _a_(528024, _n_(528023, "turtle", lambda: turtle), "tracer"), 0,0)
    _l_(528026)
    _c_(528029, _a_(528028, _n_(528027, "turtle", lambda: turtle), "hideturtle"))
    _l_(528030)
    _c_(528034, _a_(528032, _n_(528031, "turtle", lambda: turtle), "onscreenclick"), _n_(528033, "handler", lambda: handler))
    _l_(528035)
    _c_(528038, _n_(528036, "drawgame", lambda: drawgame), _n_(528037, "pieces", lambda: pieces))
    _l_(528039)
    _c_(528042, _a_(528041, _n_(528040, "turtle", lambda: turtle), "mainloop"))
    _l_(528043)

_c_(528046, _n_(528045, "main", lambda: main))
_l_(528047)