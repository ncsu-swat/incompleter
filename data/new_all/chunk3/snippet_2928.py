# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58096497/im-getting-a-typeerror-unsupported-operand-types-for-str-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
PLAYING = "PLAYING"
_l_(527253)
WAITING = "WAITING"
_l_(527254)

class User:
    _l_(527276)

    state = ""
    _l_(527255)
    name = ""
    _l_(527256)
    def __init__(self,name, stateParam):
        _l_(527263)

        _n_(527257, "self", lambda: self).name = _n_(527258, "name", lambda: name)
        _l_(527259)
        _n_(527260, "self", lambda: self).state = _n_(527261, "stateParam", lambda: stateParam)
        _l_(527262)

    def userInfo(self):
        _l_(527267)

        aux = _a_(527265, _n_(527264, "self", lambda: self), "name")
        _l_(527266)
        return aux

    def getState(self):
        _l_(527271)

        aux = _a_(527269, _n_(527268, "self", lambda: self), "state")
        _l_(527270)
        return aux
    def setState(self, stateParam):
        _l_(527275)

        _n_(527272, "self", lambda: self).state = _n_(527273, "stateParam", lambda: stateParam)
        _l_(527274)

def play():
    _l_(527380)

    grid,grid_height,grid_width,p1_name,p1_char,p2_name,p2_char=_c_(527278, _n_(527277, "getGameSettings", lambda: getGameSettings))
    _l_(527279)
    _c_(527284, _n_(527280, "displayGrid", lambda: displayGrid), _n_(527281, "grid", lambda: grid),_n_(527282, "grid_height", lambda: grid_height),_n_(527283, "grid_width", lambda: grid_width))
    _l_(527285)
    _c_(527292, _n_(527286, "updateGrid", lambda: updateGrid), _n_(527287, "grid", lambda: grid),_n_(527288, "grid_height", lambda: grid_height),_n_(527289, "grid_width", lambda: grid_width),_n_(527290, "p1_char", lambda: p1_char),_n_(527291, "p2_char", lambda: p2_char))
    _l_(527293)
   # while True:
        #count=0
        #if count < 5:
            #displayGrid(grid,grid_height,grid_width)
            #updateGrid(grid,grid_height,grid_width,p1_char,p2_char)
            #count =+1
    userA = _c_(527297, _n_(527294, "User", lambda: User), _n_(527295, "p1_name", lambda: p1_name), _n_(527296, "PLAYING", lambda: PLAYING))
    _l_(527298)
    userB = _c_(527302, _n_(527299, "User", lambda: User), _n_(527300, "p2_name", lambda: p2_name), _n_(527301, "WAITING", lambda: WAITING))  
    _l_(527303)  

    turn = 0
    _l_(527304)
    while True:
        _l_(527379)

        user = _n_(527305, "userA", lambda: userA)
        _l_(527306)
        if _n_(527307, "turn", lambda: turn) % 2 == 0 :
            _l_(527334)

            p_char= _n_(527308, "p1_char", lambda: p1_char)
            _l_(527309)
            user = _n_(527310, "userA", lambda: userA)
            _l_(527311)
            _c_(527315, _a_(527313, _n_(527312, "userA", lambda: userA), "setState"), _n_(527314, "PLAYING", lambda: PLAYING))
            _l_(527316)
            _c_(527320, _a_(527318, _n_(527317, "userB", lambda: userB), "setState"), _n_(527319, "WAITING", lambda: WAITING))
            _l_(527321)
        else :
            user = _n_(527322, "userB", lambda: userB)
            _l_(527323)
            _c_(527327, _a_(527325, _n_(527324, "userB", lambda: userB), "setState"), _n_(527326, "PLAYING", lambda: PLAYING))
            _l_(527328)
            _c_(527332, _a_(527330, _n_(527329, "userA", lambda: userA), "setState"), _n_(527331, "WAITING", lambda: WAITING))
            _l_(527333)

        _c_(527336, _n_(527335, "print", lambda: print), ".................................................. ")
        _l_(527337)
        _c_(527345, _n_(527338, "print", lambda: print), "User to play : ", _c_(527341, _a_(527340, _n_(527339, "user", lambda: user), "userInfo")) , " SEQ : ", _c_(527344, _n_(527342, "str", lambda: str), _n_(527343, "turn", lambda: turn) + 1))
        _l_(527346)
        _c_(527348, _n_(527347, "print", lambda: print), ".................................................. ")
        _l_(527349)

        try:
            _l_(527360)

            move= _c_(527353, _n_(527350, "int", lambda: int), _c_(527352, _n_(527351, "input", lambda: input), 'Enter your move: '))
            _l_(527354)
        except _n_(527355, "ValueError", lambda: ValueError):
            _l_(527359)

            _c_(527357, _n_(527356, "print", lambda: print), 'Plese enter a valid  input.')
            _l_(527358)
        if _n_(527361, "move", lambda: move) < 1 or _n_(527362, "move", lambda: move) > _n_(527363, "grid_width", lambda: grid_width):
            _l_(527368)

            _c_(527365, _n_(527364, "print", lambda: print), 'Please  enter a valid input.')
            _l_(527366)
            continue
            _l_(527367)
        break
        _l_(527369)

        _c_(527376, _n_(527370, "updateGrid", lambda: updateGrid), _n_(527371, "grid", lambda: grid),_n_(527372, "move", lambda: move),_n_(527373, "p_char", lambda: p_char),_n_(527374, "grid_height", lambda: grid_height),_n_(527375, "grid_width", lambda: grid_width))
        _l_(527377)
        turn += 1
        _l_(527378)


def getGameSettings():
    _l_(527528)


    #PLAYER 1 NAME
    while True:
        _l_(527396)

        p1_name=_c_(527382, _n_(527381, "input", lambda: input), "Enter p1_name: ")
        _l_(527383)
        if _c_(527386, _n_(527384, "len", lambda: len), _n_(527385, "p1_name", lambda: p1_name)) > 15 or _n_(527387, "p1_name", lambda: p1_name) == '':
            _l_(527395)

            _c_(527389, _n_(527388, "print", lambda: print), "Input a valid name. Max of 15 characters only.")
            _l_(527390)
            p1_name=_c_(527392, _n_(527391, "input", lambda: input), "Enter p1_name: ")
            _l_(527393)
        else:
            break
            _l_(527394)

    #PLAYER 1 CHARACTER
    while True:
        _l_(527414)

        p1_char=_c_(527400, _n_(527397, "str", lambda: str), _c_(527399, _n_(527398, "input", lambda: input), "Enter p1_character: "))
        _l_(527401)
        if _c_(527404, _n_(527402, "len", lambda: len), _n_(527403, "p1_char", lambda: p1_char)) != 1 or _n_(527405, "p1_char", lambda: p1_char)=='' :
            _l_(527413)

            _c_(527407, _n_(527406, "print", lambda: print), "1 character only.")
            _l_(527408)
            p1_char=_c_(527410, _n_(527409, "input", lambda: input), "Enter p1_character: ")
            _l_(527411)
        else:
            break
            _l_(527412)

    #PLAYER 2 NAME
    while True:
        _l_(527434)

        p2_name=_c_(527418, _n_(527415, "str", lambda: str), _c_(527417, _n_(527416, "input", lambda: input), "Enter p2_name: "))
        _l_(527419)
        if _c_(527422, _n_(527420, "len", lambda: len), _n_(527421, "p2_name", lambda: p2_name)) > 15 or _n_(527423, "p2_name", lambda: p2_name) == _n_(527424, "p1_name", lambda: p1_name) or _n_(527425, "p2_name", lambda: p2_name) == '':
            _l_(527433)

            _c_(527427, _n_(527426, "print", lambda: print), "Max of 15 characters only or choose a different name.")
            _l_(527428)
            p2_name=_c_(527430, _n_(527429, "input", lambda: input), "Enter p2_name: ")
            _l_(527431)
        else:
            break
            _l_(527432)

    #PLAYER 2 CHARACTER
    while  True:
        _l_(527456)

        p2_char=_c_(527438, _n_(527435, "str", lambda: str), _c_(527437, _n_(527436, "input", lambda: input), "Enter p2_character: "))
        _l_(527439)
        if _c_(527442, _n_(527440, "len", lambda: len), _n_(527441, "p2_char", lambda: p2_char)) != 1 or _n_(527443, "p2_char", lambda: p2_char) == _n_(527444, "p1_char", lambda: p1_char) or _n_(527445, "p2_char", lambda: p2_char) == '':
            _l_(527455)

            _c_(527447, _n_(527446, "print", lambda: print), "1 character only or choose a different character from player 1")
            _l_(527448)
            p2_char=_c_(527452, _n_(527449, "str", lambda: str), _c_(527451, _n_(527450, "input", lambda: input), "Enter p2_character: "))
            _l_(527453)
        else:
            break
            _l_(527454)

    while True:
        _l_(527478)

        try:
            _l_(527469)

            global grid_height
            _l_(527457)
            grid_height=_c_(527461, _n_(527458, "int", lambda: int), _c_(527460, _n_(527459, "input", lambda: input), "Enter grid_height(6-10): "))
            _l_(527462)
        except _n_(527463, "ValueError", lambda: ValueError):
            _l_(527468)

            _c_(527465, _n_(527464, "print", lambda: print), 'Ivalid input type. Enter an integer')
            _l_(527466)
            continue
            _l_(527467)
        if _n_(527470, "grid_height", lambda: grid_height) > 10 or _n_(527471, "grid_height", lambda: grid_height) < 6:
            _l_(527476)

            _c_(527473, _n_(527472, "print", lambda: print), 'Height must be less than 11 and greater than 5.')
            _l_(527474)
            continue  
            _l_(527475)  
        break
        _l_(527477)


    while True:
        _l_(527500)

        try:
            _l_(527491)

            global grid_width
            _l_(527479)
            grid_width=_c_(527483, _n_(527480, "int", lambda: int), _c_(527482, _n_(527481, "input", lambda: input), "Enter grid_width: "))
            _l_(527484)
        except _n_(527485, "ValueError", lambda: ValueError):
            _l_(527490)

            _c_(527487, _n_(527486, "print", lambda: print), 'Ivalid input type. Enter an integer')
            _l_(527488)
            continue
            _l_(527489)
        if _n_(527492, "grid_width", lambda: grid_width) > 9 or _n_(527493, "grid_width", lambda: grid_width) < 7:
            _l_(527498)

            _c_(527495, _n_(527494, "print", lambda: print), 'Width must be less than 10 and greater than 6.')
            _l_(527496)
            continue  
            _l_(527497)  
        break
        _l_(527499)

    #SETTING UP THE GRID
    grid=[]
    _l_(527501)
    for row in _c_(527504, _n_(527502, "range", lambda: range), _n_(527503, "grid_height", lambda: grid_height)):
        _l_(527519)

        z =[]
        _l_(527505)
        for col in _c_(527508, _n_(527506, "range", lambda: range), _n_(527507, "grid_width", lambda: grid_width)):
            _l_(527513)

            _c_(527511, _a_(527510, _n_(527509, "z", lambda: z), "append"), " ")
            _l_(527512)
        _c_(527517, _a_(527515, _n_(527514, "grid", lambda: grid), "append"), _n_(527516, "z", lambda: z))
        _l_(527518)
    aux = _n_(527520, "grid", lambda: grid),_n_(527521, "grid_width", lambda: grid_width),_n_(527522, "grid_width", lambda: grid_width),_n_(527523, "p1_name", lambda: p1_name),_n_(527524, "p1_char", lambda: p1_char),_n_(527525, "p2_name", lambda: p2_name),_n_(527526, "p2_char", lambda: p2_char)
    _l_(527527)

    return aux


def displayGrid(grid,grid_height,grid_width):
    _l_(527564)

    for row in _c_(527531, _n_(527529, "range", lambda: range), 1,_n_(527530, "grid_height", lambda: grid_height)):
        _l_(527550)

        #print(row) #for checking
        for col in _c_(527534, _n_(527532, "range", lambda: range), _n_(527533, "grid_width", lambda: grid_width)):
            _l_(527546)

            _c_(527536, _n_(527535, "print", lambda: print), "|", end="")
            _l_(527537)
            _c_(527544, _n_(527538, "print", lambda: print), _c_(527543, _n_(527539, "str", lambda: str), _n_(527540, "grid", lambda: grid)[_n_(527541, "row", lambda: row)-1][_n_(527542, "col", lambda: col)-1]),end = "")
            _l_(527545)
        _c_(527548, _n_(527547, "print", lambda: print), "|")
        _l_(527549)
    _c_(527560, _n_(527551, "print", lambda: print), " "+_c_(527559, _a_(527552, " ", "join"), [_c_(527555, _n_(527553, "str", lambda: str), _n_(527554, "i", lambda: i)) for i in _c_(527558, _n_(527556, "range", lambda: range), 1, _n_(527557, "grid_width", lambda: grid_width)+1)]))
    _l_(527561)
    aux = _n_(527562, "grid", lambda: grid)
    _l_(527563)
    return aux

def updateGrid(grid,move,p_char,grid_height,grid_width):
    _l_(527595)

    for i in _c_(527567, _n_(527565, "range", lambda: range), 1, _n_(527566, "grid_height", lambda: grid_height)-1):
        _l_(527592)

        if _n_(527568, "grid", lambda: grid)[_n_(527569, "grid_height", lambda: grid_height)-_n_(527570, "i", lambda: i)][_n_(527571, "move", lambda: move)-2] == " ":
            _l_(527590)

            _n_(527572, "grid", lambda: grid)[_n_(527573, "grid_height", lambda: grid_height)-_n_(527574, "i", lambda: i)][_n_(527575, "move", lambda: move)-2]= _n_(527576, "p_char", lambda: p_char)
            _l_(527577)
        else:
            if _n_(527578, "grid", lambda: grid)[0][_n_(527579, "move", lambda: move)-1] != " ":
                _l_(527589)

                _c_(527586, _n_(527580, "updateGrid", lambda: updateGrid), _n_(527581, "grid", lambda: grid),_n_(527582, "move", lambda: move),_n_(527583, "p_char", lambda: p_char),_n_(527584, "grid_height", lambda: grid_height),_n_(527585, "grid_width", lambda: grid_width))
                _l_(527587)
            else:
                continue
                _l_(527588)
        break
        _l_(527591)
    aux = _n_(527593, "grid", lambda: grid)
    _l_(527594)

    return aux


#def isWin():

#def isDraw():


if _n_(527596, "__name__", lambda: __name__) == '__main__':
    _l_(527600)

    _c_(527598, _n_(527597, "play", lambda: play))
    _l_(527599)