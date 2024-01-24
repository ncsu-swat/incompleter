# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58090214/im-receiving-a-typeerror-can-only-concatenate-str-not-int-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def play():
        _l_(473123)

        grid,grid_height,grid_width,p1_name,p1_char,p2_name,p2_char=_c_(473087, _n_(473086, "getGameSettings", lambda: getGameSettings))
        _l_(473088)
        _c_(473093, _n_(473089, "displayGrid", lambda: displayGrid), _n_(473090, "grid", lambda: grid),_n_(473091, "grid_height", lambda: grid_height),_n_(473092, "grid_width", lambda: grid_width))
        _l_(473094)
        _c_(473101, _n_(473095, "updateGrid", lambda: updateGrid), _n_(473096, "grid", lambda: grid),_n_(473097, "grid_height", lambda: grid_height),_n_(473098, "grid_width", lambda: grid_width),_n_(473099, "p1_char", lambda: p1_char),_n_(473100, "p2_char", lambda: p2_char))
        _l_(473102)
        _c_(473107, _n_(473103, "displayGrid", lambda: displayGrid), _n_(473104, "grid", lambda: grid),_n_(473105, "grid_height", lambda: grid_height),_n_(473106, "grid_width", lambda: grid_width))
        _l_(473108)
        _c_(473115, _n_(473109, "updateGrid", lambda: updateGrid), _n_(473110, "grid", lambda: grid),_n_(473111, "grid_height", lambda: grid_height),_n_(473112, "grid_width", lambda: grid_width),_n_(473113, "p1_char", lambda: p1_char),_n_(473114, "p2_char", lambda: p2_char))
        _l_(473116)
        _c_(473121, _n_(473117, "displayGrid", lambda: displayGrid), _n_(473118, "grid", lambda: grid),_n_(473119, "grid_height", lambda: grid_height),_n_(473120, "grid_width", lambda: grid_width))
        _l_(473122)


def getGameSettings():
        _l_(473263)


        #PLAYER 1 NAME
        while True:
                _l_(473139)

                p1_name=_c_(473125, _n_(473124, "input", lambda: input), "Enter p1_name: ")
                _l_(473126)
                if _c_(473129, _n_(473127, "len", lambda: len), _n_(473128, "p1_name", lambda: p1_name)) > 15 or _n_(473130, "p1_name", lambda: p1_name) == '':
                        _l_(473138)

                        _c_(473132, _n_(473131, "print", lambda: print), "Input a valid name. Max of 15 characters only.")
                        _l_(473133)
                        p1_name=_c_(473135, _n_(473134, "input", lambda: input), "Enter p1_name: ")
                        _l_(473136)
                else:
                    break
                    _l_(473137)

        #PLAYER 1 CHARACTER
        while True:
                _l_(473155)

                p1_char=_c_(473141, _n_(473140, "input", lambda: input), "Enter p1_character: ")
                _l_(473142)
                if _c_(473145, _n_(473143, "len", lambda: len), _n_(473144, "p1_char", lambda: p1_char)) != 1 or _n_(473146, "p1_char", lambda: p1_char)=='' :
                        _l_(473154)

                        _c_(473148, _n_(473147, "print", lambda: print), "1 character only.")
                        _l_(473149)
                        p1_char=_c_(473151, _n_(473150, "input", lambda: input), "Enter p1_character: ")
                        _l_(473152)
                else:
                    break
                    _l_(473153)

        #PLAYER 2 NAME
        while True:
                _l_(473173)

                p2_name=_c_(473157, _n_(473156, "input", lambda: input), "Enter p2_name: ")
                _l_(473158)
                if _c_(473161, _n_(473159, "len", lambda: len), _n_(473160, "p2_name", lambda: p2_name)) > 15 or _n_(473162, "p2_name", lambda: p2_name) == _n_(473163, "p1_name", lambda: p1_name) or _n_(473164, "p2_name", lambda: p2_name) == '':
                        _l_(473172)

                        _c_(473166, _n_(473165, "print", lambda: print), "Max of 15 characters only or choose a different name.")
                        _l_(473167)
                        p2_name=_c_(473169, _n_(473168, "input", lambda: input), "Enter p2_name: ")
                        _l_(473170)
                else:
                    break
                    _l_(473171)

        #PLAYER 2 CHARACTER
        while  True:
                _l_(473191)

                p2_char=_c_(473175, _n_(473174, "input", lambda: input), "Enter p2_character: ")
                _l_(473176)
                if _c_(473179, _n_(473177, "len", lambda: len), _n_(473178, "p2_char", lambda: p2_char)) != 1 or _n_(473180, "p2_char", lambda: p2_char) == _n_(473181, "p1_char", lambda: p1_char) or _n_(473182, "p2_char", lambda: p2_char) == '':
                        _l_(473190)

                        _c_(473184, _n_(473183, "print", lambda: print), "1 character only or choose a different character from player 1")
                        _l_(473185)
                        p2_char=_c_(473187, _n_(473186, "input", lambda: input), "Enter p2_character: ")
                        _l_(473188)
                else:
                    break
                    _l_(473189)

        while True:
                _l_(473213)

                try:
                        _l_(473204)

                        global grid_height
                        _l_(473192)
                        grid_height=_c_(473196, _n_(473193, "int", lambda: int), _c_(473195, _n_(473194, "input", lambda: input), "Enter grid_height(6-10): "))
                        _l_(473197)
                except _n_(473198, "ValueError", lambda: ValueError):
                        _l_(473203)

                        _c_(473200, _n_(473199, "print", lambda: print), 'Ivalid input type. Enter an integer')
                        _l_(473201)
                        continue
                        _l_(473202)
                if _n_(473205, "grid_height", lambda: grid_height) > 10 or _n_(473206, "grid_height", lambda: grid_height) < 6:
                        _l_(473211)

                        _c_(473208, _n_(473207, "print", lambda: print), 'Height must be less than 11 and greater than 5.')
                        _l_(473209)
                        continue  
                        _l_(473210)  
                break
                _l_(473212)


        while True:
                _l_(473235)

                try:
                        _l_(473226)

                        global grid_width
                        _l_(473214)
                        grid_width=_c_(473218, _n_(473215, "int", lambda: int), _c_(473217, _n_(473216, "input", lambda: input), "Enter grid_width: "))
                        _l_(473219)
                except _n_(473220, "ValueError", lambda: ValueError):
                        _l_(473225)

                        _c_(473222, _n_(473221, "print", lambda: print), 'Ivalid input type. Enter an integer')
                        _l_(473223)
                        continue
                        _l_(473224)
                if _n_(473227, "grid_width", lambda: grid_width) > 9 or _n_(473228, "grid_width", lambda: grid_width) < 7:
                        _l_(473233)

                        _c_(473230, _n_(473229, "print", lambda: print), 'Width must be less than 10 and greater than 6.')
                        _l_(473231)
                        continue  
                        _l_(473232)  
                break
                _l_(473234)

        #SETTING UP THE GRID
        grid=[]
        _l_(473236)
        for row in _c_(473239, _n_(473237, "range", lambda: range), _n_(473238, "grid_height", lambda: grid_height)):
                _l_(473254)

                z =[]
                _l_(473240)
                for col in _c_(473243, _n_(473241, "range", lambda: range), _n_(473242, "grid_width", lambda: grid_width)):
                        _l_(473248)

                        _c_(473246, _a_(473245, _n_(473244, "z", lambda: z), "append"), " ")
                        _l_(473247)
                _c_(473252, _a_(473250, _n_(473249, "grid", lambda: grid), "append"), _n_(473251, "z", lambda: z))
                _l_(473253)
        aux = _n_(473255, "grid", lambda: grid),_n_(473256, "grid_width", lambda: grid_width),_n_(473257, "grid_width", lambda: grid_width),_n_(473258, "p1_name", lambda: p1_name),_n_(473259, "p1_char", lambda: p1_char),_n_(473260, "p2_name", lambda: p2_name),_n_(473261, "p2_char", lambda: p2_char)
        _l_(473262)

        return aux


def displayGrid(grid,grid_height,grid_width):
        _l_(473294)

        for row in _c_(473266, _n_(473264, "range", lambda: range), _n_(473265, "grid_height", lambda: grid_height)):
                _l_(473280)

                for col in _c_(473269, _n_(473267, "range", lambda: range), _n_(473268, "grid_width", lambda: grid_width)+1):
                        _l_(473276)

                        _c_(473274, _n_(473270, "print", lambda: print), "|" + _n_(473271, "grid", lambda: grid)[_n_(473272, "row", lambda: row)-1][_n_(473273, "col", lambda: col)-1],end = "")
                        _l_(473275)
                _c_(473278, _n_(473277, "print", lambda: print))
                _l_(473279)
        _c_(473290, _n_(473281, "print", lambda: print), " "+_c_(473289, _a_(473282, " ", "join"), [_c_(473285, _n_(473283, "str", lambda: str), _n_(473284, "i", lambda: i)) for i in _c_(473288, _n_(473286, "range", lambda: range), 1, _n_(473287, "grid_width", lambda: grid_width)+1)]))
        _l_(473291)
        aux = _n_(473292, "grid", lambda: grid)
        _l_(473293)
        return aux

def updateGrid(grid,p1_char,p2_char,p1_name,p2_name):
        _l_(473344)

        while True:
                _l_(473313)

                try:
                        _l_(473305)

                        move= _c_(473298, _n_(473295, "int", lambda: int), _c_(473297, _n_(473296, "input", lambda: input), 'Enter your move: '))
                        _l_(473299)
                except _n_(473300, "ValueError", lambda: ValueError):
                        _l_(473304)

                        _c_(473302, _n_(473301, "print", lambda: print), 'Plese enter a valid  input.')
                        _l_(473303)
                if _n_(473306, "move", lambda: move) < 1:
                        _l_(473311)

                        _c_(473308, _n_(473307, "print", lambda: print), 'Please  enter a valid input.')
                        _l_(473309)
                        continue
                        _l_(473310)
                break
                _l_(473312)

        for i in _c_(473316, _n_(473314, "range", lambda: range), 1,_n_(473315, "grid_height", lambda: grid_height)+1):
                _l_(473341)

                if _n_(473317, "grid", lambda: grid)[_n_(473318, "grid_height", lambda: grid_height)-_n_(473319, "i", lambda: i)][_n_(473320, "move", lambda: move)-2]== " ":
                        _l_(473339)

                        _n_(473321, "grid", lambda: grid)[_n_(473322, "grid_height", lambda: grid_height)-_n_(473323, "i", lambda: i)][_n_(473324, "move", lambda: move)-2]= _n_(473325, "p1_char", lambda: p1_char)
                        _l_(473326)
                else:
                    if _n_(473327, "grid", lambda: grid)[0][_n_(473328, "move", lambda: move)-2] != " ":
                            _l_(473338)

                            _c_(473335, _n_(473329, "updateGrid", lambda: updateGrid), _n_(473330, "grid", lambda: grid),_n_(473331, "grid_height", lambda: grid_height),_n_(473332, "grid_width", lambda: grid_width),_n_(473333, "p1_char", lambda: p1_char),_n_(473334, "p2_char", lambda: p2_char))
                            _l_(473336)
                    else:
                        continue
                        _l_(473337)
                break
                _l_(473340)
        aux = _n_(473342, "grid", lambda: grid)
        _l_(473343)

        return aux


#def get_input(player, grids, )
#def isWin():

#def isDraw():

#def play():
#displayGrid()
#updateGrid(grid)

if _n_(473345, "__name__", lambda: __name__) == '__main__':
        _l_(473349)

        _c_(473347, _n_(473346, "play", lambda: play))
        _l_(473348)