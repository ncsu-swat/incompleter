# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/22938809/attributeerror-oandx-object-has-no-attribute-run
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(440230)

except ImportError:
    pass
try:
    import sys
    _l_(440232)

except ImportError:
    pass
try:
    from pygame import *
    _l_(440234)

except ImportError:
    pass
try:
    from pygame.locals import *
    _l_(440236)

except ImportError:
    pass

# game classes

class OAndX:
    _l_(440262)

    def __init__(self):
        _l_(440261)

        # Initialize Pygame
        _c_(440239, _a_(440238, _n_(440237, "pygame", lambda: pygame), "init"))
        _l_(440240)
        # Create the clock to manage the game loop
        _n_(440241, "self", lambda: self).clock = _c_(440244, _a_(440243, _n_(440242, "time", lambda: time), "Clock"))
        _l_(440245)
        _c_(440248, _a_(440247, _n_(440246, "display", lambda: display), "set_caption"), "Noughts and Crosses")
        _l_(440249)
        # Create a windows with a resolution of 640 x 480
        _n_(440250, "self", lambda: self).displaySize=(640,480)
        _l_(440251)
        _n_(440252, "self", lambda: self).screen=_c_(440257, _a_(440254, _n_(440253, "display", lambda: display), "set_mode"), _a_(440256, _n_(440255, "self", lambda: self), "displaySize"))
        _l_(440258)
        # will either be 0 or X
        _n_(440259, "self", lambda: self).player="0"
        _l_(440260)

# The background class

class Background:
    _l_(440313)

    def __init__(self,displaySize):
        _l_(440305)

        _n_(440263, "self", lambda: self).image=_c_(440266, _n_(440264, "Surface", lambda: Surface), _n_(440265, "displaySize", lambda: displaySize))
        _l_(440267)
    # Draw a title
    # Create the font we'll use
        _n_(440268, "self", lambda: self).font=_c_(440272, _a_(440270, _n_(440269, "font", lambda: font), "Font"), None,(_n_(440271, "displaySize", lambda: displaySize)[0]/12))
        _l_(440273)
        _n_(440274, "self", lambda: self).text = _c_(440280, _a_(440277, _a_(440276, _n_(440275, "self", lambda: self), "font"), "render"), "Noughts and crosses",True,_c_(440279, _n_(440278, "Color", lambda: Color), "White"))
        _l_(440281)
        # Work out where to place the text
        _n_(440282, "self", lambda: self).textRect = _c_(440286, _a_(440285, _a_(440284, _n_(440283, "self", lambda: self), "text"), "get_rect"))
        _l_(440287)
        _a_(440289, _n_(440288, "self", lambda: self), "textRect").centerx=_n_(440290, "displaySize", lambda: displaySize)[0] / 2
        _l_(440291)
        # Add a little margin
        _a_(440293, _n_(440292, "self", lambda: self), "textRect").top = _n_(440294, "displaySize", lambda: displaySize)[1] * 0.02
        _l_(440295)
        # Blit the text to the background image
        _c_(440303, _a_(440298, _a_(440297, _n_(440296, "self", lambda: self), "image"), "blit"), _a_(440300, _n_(440299, "self", lambda: self), "text"), _a_(440302, _n_(440301, "self", lambda: self), "textRect"))
        _l_(440304)
    def draw(self, display):
        _l_(440312)

        _c_(440310, _a_(440307, _n_(440306, "display", lambda: display), "blit"), _a_(440309, _n_(440308, "self", lambda: self), "image"), (0, 0))
        _l_(440311)

# A class for an individual grid square
class GridSquare(_a_(440315, _n_(440314, "sprite", lambda: sprite), "Sprite")):
    _l_(440413)

    def __init__(self, position, gridSize):
        _l_(440412)

        # Initialise the sprite base class
        _c_(440320, _a_(440319, _n_(440316, "super", lambda: super)(_n_(440317, "GridSquare", lambda: GridSquare), _n_(440318, "self", lambda: self)), "__init__"))
        _l_(440321)
        # We want to know which row and column we are in
        _n_(440322, "self", lambda: self).position = _n_(440323, "position", lambda: position)
        _l_(440324)
        # State can be “X”, “O” or “”
        _n_(440325, "self", lambda: self).state = ""
        _l_(440326)
        _n_(440327, "self", lambda: self).permanentState = False
        _l_(440328)
        _n_(440329, "self", lambda: self).newState = ""
        _l_(440330)
        # Work out the position and size of the square
        width = _n_(440331, "gridSize", lambda: gridSize)[0] / 3
        _l_(440332)
        height = _n_(440333, "gridSize", lambda: gridSize)[1] / 3
        _l_(440334)
        # Get the x and y co ordinate of the top left corner
        x = (_n_(440335, "position", lambda: position)[0] * _n_(440336, "width", lambda: width)) - _n_(440337, "width", lambda: width)
        _l_(440338)
        y = (_n_(440339, "position", lambda: position)[1] * _n_(440340, "height", lambda: height)) - _n_(440341, "height", lambda: height)
        _l_(440342)
        # Create the image, the rect and then position the rect
        _n_(440343, "self", lambda: self).image = _c_(440347, _n_(440344, "Surface", lambda: Surface), (_n_(440345, "width", lambda: width),_n_(440346, "height", lambda: height)))
        _l_(440348)
        _c_(440354, _a_(440351, _a_(440350, _n_(440349, "self", lambda: self), "image"), "fill"), _c_(440353, _n_(440352, "Color", lambda: Color), "white"))
        _l_(440355)
        _n_(440356, "self", lambda: self).rect = _c_(440360, _a_(440359, _a_(440358, _n_(440357, "self", lambda: self), "image"), "get_rect"))
        _l_(440361)
        _a_(440363, _n_(440362, "self", lambda: self), "rect").topleft = (_n_(440364, "x", lambda: x), _n_(440365, "y", lambda: y))
        _l_(440366)
        # The rect we have is white, which is the parent rect
        # We will draw another rect in the middle so that we have
        # a white border but a blue center
        _n_(440367, "self", lambda: self).childImage = _c_(440375, _n_(440368, "Surface", lambda: Surface), ((_a_(440371, _a_(440370, _n_(440369, "self", lambda: self), "rect"), "w") * 0.9), (_a_(440374, _a_(440373, _n_(440372, "self", lambda: self), "rect"), "h") * 0.9)))
        _l_(440376)
        _c_(440382, _a_(440379, _a_(440378, _n_(440377, "self", lambda: self), "childImage"), "fill"), _c_(440381, _n_(440380, "Color", lambda: Color), "blue"))
        _l_(440383)
        _n_(440384, "self", lambda: self).childRect = _c_(440388, _a_(440387, _a_(440386, _n_(440385, "self", lambda: self), "childImage"), "get_rect"))
        _l_(440389)
        _a_(440391, _n_(440390, "self", lambda: self), "childRect").center = ((_n_(440392, "width", lambda: width) /2), (_n_(440393, "height", lambda: height) / 2))
        _l_(440394)
        _c_(440402, _a_(440397, _a_(440396, _n_(440395, "self", lambda: self), "image"), "blit"), _a_(440399, _n_(440398, "self", lambda: self), "childImage"),_a_(440401, _n_(440400, "self", lambda: self), "childRect"))
        _l_(440403)
        # Create the font we’ll use to display O and X
        _n_(440404, "self", lambda: self).font = _c_(440410, _a_(440406, _n_(440405, "font", lambda: font), "Font"), None, _a_(440409, _a_(440408, _n_(440407, "self", lambda: self), "childRect"), "w"))
        _l_(440411)

class Grid:
    _l_(440540)

    def __init__(self, displaySize):
        _l_(440462)

        _n_(440414, "self", lambda: self).image=_c_(440417, _n_(440415, "Surface", lambda: Surface), _n_(440416, "displaySize", lambda: displaySize))
        _l_(440418)
        # Make a number of grid squares
        gridSize = (_n_(440419, "displaySize", lambda: displaySize)[0] * 0.75,_n_(440420, "displaySize", lambda: displaySize)[1] * 0.75)
        _l_(440421)
        # Work out the co-ordinate of the top left corner of the grid so that it can be centered on the screen
        _n_(440422, "self", lambda: self).position = ((_n_(440423, "displaySize", lambda: displaySize)[0] /2) - (_n_(440424, "gridSize", lambda: gridSize)[0] / 2),(_n_(440425, "displaySize", lambda: displaySize)[1] / 2) - (_n_(440426, "gridSize", lambda: gridSize)[1] / 2))
        _l_(440427)
        # An empty array to hold our grid squares in
        _n_(440428, "self", lambda: self).squares = []
        _l_(440429)
        for row in _c_(440431, _n_(440430, "range", lambda: range), 1,4):
            _l_(440461)

            # Loop to make 3 rows
            for column in _c_(440433, _n_(440432, "range", lambda: range), 1,4):
                _l_(440460)

            # Loop to make 3 columns
                squarePosition = (_n_(440434, "column", lambda: column),_n_(440435, "row", lambda: row))
                _l_(440436)
                _c_(440444, _a_(440439, _a_(440438, _n_(440437, "self", lambda: self), "squares"), "append"), _c_(440443, _n_(440440, "GridSquare", lambda: GridSquare), _n_(440441, "squarePosition", lambda: squarePosition), _n_(440442, "gridSize", lambda: gridSize)))
                _l_(440445)
                # Get the squares in a sprite group
                _n_(440446, "self", lambda: self).sprites = _c_(440449, _a_(440448, _n_(440447, "sprite", lambda: sprite), "Group"))
                _l_(440450)
                for square in _a_(440452, _n_(440451, "self", lambda: self), "squares"):
                    _l_(440459)

                    _c_(440457, _a_(440455, _a_(440454, _n_(440453, "self", lambda: self), "sprites"), "add"), _n_(440456, "square", lambda: square))
                    _l_(440458)

    def draw(self, display):
        _l_(440483)

        _c_(440466, _a_(440465, _a_(440464, _n_(440463, "self", lambda: self), "sprites"), "update"))
        _l_(440467)
        _c_(440473, _a_(440470, _a_(440469, _n_(440468, "self", lambda: self), "sprites"), "draw"), _a_(440472, _n_(440471, "self", lambda: self), "image"))
        _l_(440474)
        _c_(440481, _a_(440476, _n_(440475, "display", lambda: display), "blit"), _a_(440478, _n_(440477, "self", lambda: self), "image"), _a_(440480, _n_(440479, "self", lambda: self), "position"))
        _l_(440482)

    def update(self):
        _l_(440539)

        # Need to update if we need to set a new state
        if (_a_(440485, _n_(440484, "self", lambda: self), "state") != _a_(440487, _n_(440486, "self", lambda: self), "newState")):
            _l_(440538)

            # Refill the childImage blue
            _c_(440493, _a_(440490, _a_(440489, _n_(440488, "self", lambda: self), "childImage"), "fill"), _c_(440492, _n_(440491, "Color", lambda: Color), "blue"))
            _l_(440494)
            text = _c_(440502, _a_(440497, _a_(440496, _n_(440495, "self", lambda: self), "font"), "render"), _a_(440499, _n_(440498, "self", lambda: self), "newState"), True, _c_(440501, _n_(440500, "Color", lambda: Color), "white"))
            _l_(440503)
            textRect = _c_(440506, _a_(440505, _n_(440504, "text", lambda: text), "get_rect"))
            _l_(440507)
            _n_(440508, "textRect", lambda: textRect).center = ((_a_(440511, _a_(440510, _n_(440509, "self", lambda: self), "childRect"), "w") / 2),(_a_(440514, _a_(440513, _n_(440512, "self", lambda: self), "childRect"), "h") / 2))
            _l_(440515)
            # We need to blit twice because the new child image needs to be blitted to the parent image
            _c_(440521, _a_(440518, _a_(440517, _n_(440516, "self", lambda: self), "childImage"), "blit"), _n_(440519, "text", lambda: text),_n_(440520, "textRect", lambda: textRect))
            _l_(440522)
            _c_(440530, _a_(440525, _a_(440524, _n_(440523, "self", lambda: self), "image"), "blit"), _a_(440527, _n_(440526, "self", lambda: self), "childImage"), _a_(440529, _n_(440528, "self", lambda: self), "childRect"))
            _l_(440531)
            # Reset the newState variable
            _n_(440532, "self", lambda: self).state = _a_(440534, _n_(440533, "self", lambda: self), "newState")
            _l_(440535)
            _n_(440536, "self", lambda: self).newState = ""
            _l_(440537)
def setState(self, newState,permanent=False):
    _l_(440551)

    if not _a_(440542, _n_(440541, "self", lambda: self), "permanentState"):
        _l_(440550)

        _n_(440543, "self", lambda: self).newState = _n_(440544, "newState", lambda: newState)
        _l_(440545)
        if _n_(440546, "permanent", lambda: permanent):
            _l_(440549)

            _n_(440547, "self", lambda: self).permanentState = True
            _l_(440548)

def reset(self):
    _l_(440564)

    # Create an instance of our background and grid class
    _n_(440552, "self", lambda: self).background =_c_(440556, _n_(440553, "Background", lambda: Background), _a_(440555, _n_(440554, "self", lambda: self), "displaySize"))
    _l_(440557)
    _n_(440558, "self", lambda: self).grid = _c_(440562, _n_(440559, "Grid", lambda: Grid), _a_(440561, _n_(440560, "self", lambda: self), "displaySize"))
    _l_(440563)

def getSquareState(self, column, row):
    _l_(440576)

    # Get the square with the requested position
    for square in _a_(440566, _n_(440565, "self", lambda: self), "squares"):
        _l_(440575)

        if _a_(440568, _n_(440567, "square", lambda: square), "position") == (_n_(440569, "column", lambda: column),_n_(440570, "row", lambda: row)):
            _l_(440574)

            aux = _a_(440572, _n_(440571, "square", lambda: square), "state")
            _l_(440573)
            return aux

def full(self):
    _l_(440589)

    # Finds out if the grid is full
    count = 0
    _l_(440577)
    for square in _a_(440579, _n_(440578, "self", lambda: self), "squares"):
        _l_(440588)

        if _a_(440581, _n_(440580, "square", lambda: square), "permanentState") ==True:
            _l_(440587)

            count += 1
            _l_(440582)
            if _n_(440583, "count", lambda: count) == 9:
                _l_(440586)

                aux = True
                _l_(440584)
                return aux
            else:
                aux = False
                _l_(440585)
                return aux

def getWinner(self):
    _l_(440743)

    players = ["X", "O"]
    _l_(440590)
    for player in _n_(440591, "players", lambda: players):
        _l_(440742)

        # check horizontal spaces
        for column in _c_(440593, _n_(440592, "range", lambda: range), 1, 4):
            _l_(440741)

            for row in _c_(440595, _n_(440594, "range", lambda: range), 1, 4):
                _l_(440740)

                square1 = _c_(440601, _a_(440598, _a_(440597, _n_(440596, "self", lambda: self), "grid"), "getSquareState"), _n_(440599, "column", lambda: column), _n_(440600, "row", lambda: row))
                _l_(440602)
                square2 = _c_(440608, _a_(440605, _a_(440604, _n_(440603, "self", lambda: self), "grid"), "getSquareState"), (_n_(440606, "column", lambda: column) + 1),_n_(440607, "row", lambda: row))
                _l_(440609)
                square3 = _c_(440615, _a_(440612, _a_(440611, _n_(440610, "self", lambda: self), "grid"), "getSquareState"), (_n_(440613, "column", lambda: column) + 2), _n_(440614, "row", lambda: row))
                _l_(440616)
                # Get the player of the square (either O or X)
                if (_n_(440617, "square1", lambda: square1) == _n_(440618, "player", lambda: player)) and (_n_(440619, "square2", lambda: square2) == _n_(440620, "player", lambda: player)) and (_n_(440621, "square3", lambda: square3) == _n_(440622, "player", lambda: player)):
                    _l_(440739)

                    aux = _n_(440623, "player", lambda: player)
                    _l_(440624)
                    return aux
                    # check vertical spaces
                    for column in _c_(440626, _n_(440625, "range", lambda: range), 1, 4):
                        _l_(440738)

                        for row in _c_(440628, _n_(440627, "range", lambda: range), 1, 4):
                            _l_(440737)

                            square1 = _c_(440634, _a_(440631, _a_(440630, _n_(440629, "self", lambda: self), "grid"), "getSquareState"), _n_(440632, "column", lambda: column), _n_(440633, "row", lambda: row))
                            _l_(440635)
                            square2 = _c_(440641, _a_(440638, _a_(440637, _n_(440636, "self", lambda: self), "grid"), "getSquareState"), _n_(440639, "column", lambda: column), (_n_(440640, "row", lambda: row) + 1))
                            _l_(440642)
                            square3 = _c_(440648, _a_(440645, _a_(440644, _n_(440643, "self", lambda: self), "grid"), "getSquareState"), _n_(440646, "column", lambda: column), (_n_(440647, "row", lambda: row) + 2))
                            _l_(440649)
                            # Get the player of the square (either O or X)
                            if (_n_(440650, "square1", lambda: square1) == _n_(440651, "player", lambda: player)) and (_n_(440652, "square2", lambda: square2) == _n_(440653, "player", lambda: player)) and (_n_(440654, "square3", lambda: square3) == _n_(440655, "player", lambda: player)):
                                _l_(440736)

                                aux = _n_(440656, "player", lambda: player)
                                _l_(440657)
                                return aux
                                # check forwards diagonal spaces
                                for column in _c_(440659, _n_(440658, "range", lambda: range), 1, 4):
                                    _l_(440735)

                                    for row in _c_(440661, _n_(440660, "range", lambda: range), 1, 4):
                                        _l_(440734)

                                        square1 = _c_(440667, _a_(440664, _a_(440663, _n_(440662, "self", lambda: self), "grid"), "getSquareState"), _n_(440665, "column", lambda: column), _n_(440666, "row", lambda: row))
                                        _l_(440668)
                                        square2 = _c_(440674, _a_(440671, _a_(440670, _n_(440669, "self", lambda: self), "grid"), "getSquareState"), (_n_(440672, "column", lambda: column) + 1), (_n_(440673, "row", lambda: row) - 1))
                                        _l_(440675)
                                        square3 = _c_(440681, _a_(440678, _a_(440677, _n_(440676, "self", lambda: self), "grid"), "getSquareState"), (_n_(440679, "column", lambda: column) + 2), (_n_(440680, "row", lambda: row) - 2))
                                        _l_(440682)
                                        # Get the player of the square (either O or X)
                                        if (_n_(440683, "square1", lambda: square1) == _n_(440684, "player", lambda: player)) and (_n_(440685, "square2", lambda: square2) == _n_(440686, "player", lambda: player)) and (_n_(440687, "square3", lambda: square3) == _n_(440688, "player", lambda: player)):
                                            _l_(440733)

                                            aux = _n_(440689, "player", lambda: player)
                                            _l_(440690)
                                            return aux
                                            # check backwards diagonal spaces
                                            for column in _c_(440692, _n_(440691, "range", lambda: range), 1, 4):
                                                _l_(440732)

                                                for row in _c_(440694, _n_(440693, "range", lambda: range), 1, 4):
                                                    _l_(440731)

                                                    square1 = _c_(440700, _a_(440697, _a_(440696, _n_(440695, "self", lambda: self), "grid"), "getSquareState"), _n_(440698, "column", lambda: column), _n_(440699, "row", lambda: row))
                                                    _l_(440701)
                                                    square2 = _c_(440707, _a_(440704, _a_(440703, _n_(440702, "self", lambda: self), "grid"), "getSquareState"), (_n_(440705, "column", lambda: column) + 1), (_n_(440706, "row", lambda: row) + 1))
                                                    _l_(440708)
                                                    square3 = _c_(440714, _a_(440711, _a_(440710, _n_(440709, "self", lambda: self), "grid"), "getSquareState"), (_n_(440712, "column", lambda: column) + 2), (_n_(440713, "row", lambda: row) + 2))
                                                    _l_(440715)
                                                    # Get the player of the square (either O or X)
                                                    if (_n_(440716, "square1", lambda: square1) == _n_(440717, "player", lambda: player)) and (_n_(440718, "square2", lambda: square2) == _n_(440719, "player", lambda: player)) and (_n_(440720, "square3", lambda: square3) == _n_(440721, "player", lambda: player)):
                                                        _l_(440730)

                                                        aux = _n_(440722, "player", lambda: player)
                                                        _l_(440723)
                                                        return aux

                                                        # Check if grid is full if someone hasn’t won already
                                                        if _c_(440727, _a_(440726, _a_(440725, _n_(440724, "self", lambda: self), "grid"), "full")):
                                                            _l_(440729)

                                                            aux = "draw"
                                                            _l_(440728)
                                                            return aux

def winMessage(self, winner):
    _l_(440801)

    # Display message then reset the game to its initial state
    # Blank out the screen
    _c_(440749, _a_(440746, _a_(440745, _n_(440744, "self", lambda: self), "screen"), "fill"), _c_(440748, _n_(440747, "Color", lambda: Color), "Black"))
    _l_(440750)
    # Create the font we’ll use
    textFont = _c_(440755, _a_(440752, _n_(440751, "font", lambda: font), "Font"), None, (_a_(440754, _n_(440753, "self", lambda: self), "displaySize")[0] / 6))
    _l_(440756)
    textString = ""
    _l_(440757)
    if _n_(440758, "winner", lambda: winner) == "draw":
        _l_(440762)

        textString = "It was a draw!"
        _l_(440759)
    else:
        textString = _n_(440760, "winner", lambda: winner) + " Wins!"
        _l_(440761)
    # Create the text surface
    text = _c_(440768, _a_(440764, _n_(440763, "textFont", lambda: textFont), "render"), _n_(440765, "textString", lambda: textString),True,_c_(440767, _n_(440766, "Color", lambda: Color), "white"))
    _l_(440769)
    textRect = _c_(440772, _a_(440771, _n_(440770, "text", lambda: text), "get_rect"))
    _l_(440773)
    _n_(440774, "textRect", lambda: textRect).centerx = _a_(440776, _n_(440775, "self", lambda: self), "displaySize")[0] / 2
    _l_(440777)
    _n_(440778, "textRect", lambda: textRect).centery = _a_(440780, _n_(440779, "self", lambda: self), "displaySize")[1] / 2
    _l_(440781)
    # Blit changes and update the display before we sleep
    _c_(440787, _a_(440784, _a_(440783, _n_(440782, "self", lambda: self), "screen"), "blit"), _n_(440785, "text", lambda: text), _n_(440786, "textRect", lambda: textRect))
    _l_(440788)
    _c_(440791, _a_(440790, _n_(440789, "display", lambda: display), "update"))
    _l_(440792)
    # time.wait comes from pygame libs
    _c_(440795, _a_(440794, _n_(440793, "time", lambda: time), "wait"), 2000)
    _l_(440796)
    # Set game to its initial state
    _c_(440799, _a_(440798, _n_(440797, "self", lambda: self), "reset"))
    _l_(440800)

def run(self):
    _l_(440830)

    while True:
        _l_(440829)

        # Our Game loop,Handle events
        _c_(440804, _a_(440803, _n_(440802, "self", lambda: self), "handleEvents"))
        _l_(440805)
        # Draw our background and grid
        _c_(440811, _a_(440808, _a_(440807, _n_(440806, "self", lambda: self), "background"), "draw"), _a_(440810, _n_(440809, "self", lambda: self), "screen"))
        _l_(440812)
        _c_(440818, _a_(440815, _a_(440814, _n_(440813, "self", lambda: self), "grid"), "draw"), _a_(440817, _n_(440816, "self", lambda: self), "screen"))
        _l_(440819)
        # Update our display
        _c_(440822, _a_(440821, _n_(440820, "display", lambda: display), "update"))
        _l_(440823)
        # Limit the game to 10 fps
        _c_(440827, _a_(440826, _a_(440825, _n_(440824, "self", lambda: self), "clock"), "tick"), 10)
        _l_(440828)

def handleEvents(self):
    _l_(440911)

    # We need to know if the mouse has been clicked later on
    mouseClicked = False
    _l_(440831)
    # Handle events, starting with quit
    for event in _c_(440835, _a_(440834, _a_(440833, _n_(440832, "pygame", lambda: pygame), "event"), "get")):
        _l_(440910)

        if _a_(440837, _n_(440836, "event", lambda: event), "type") == _n_(440838, "QUIT", lambda: QUIT):
            _l_(440909)

            _c_(440841, _a_(440840, _n_(440839, "pygame", lambda: pygame), "quit"))
            _l_(440842)
            _c_(440845, _a_(440844, _n_(440843, "sys", lambda: sys), "exit"))
            _l_(440846)
            if _a_(440848, _n_(440847, "event", lambda: event), "type") == _n_(440849, "MOUSEBUTTONUP", lambda: MOUSEBUTTONUP):
                _l_(440908)

                mouseClicked = True
                _l_(440850)
                # Get the co ordinate of the mouse mousex, mousey = mouse.get_pos() ,These are relative to the top left of the screen,and we need to make them relative to the top left of the grid
                mousex -= _a_(440853, _a_(440852, _n_(440851, "self", lambda: self), "grid"), "position")[0]
                _l_(440854)
                mousey -= _a_(440857, _a_(440856, _n_(440855, "self", lambda: self), "grid"), "position")[1]
                _l_(440858)
                # Find which rect the mouse is in
                for square in _a_(440861, _a_(440860, _n_(440859, "self", lambda: self), "grid"), "squares"):
                    _l_(440907)

                    if _c_(440867, _a_(440864, _a_(440863, _n_(440862, "square", lambda: square), "rect"), "collidepoint"), (_n_(440865, "mousex", lambda: mousex), _n_(440866, "mousey", lambda: mousey))):
                        _l_(440906)

                        if _n_(440868, "mouseClicked", lambda: mouseClicked):
                            _l_(440901)

                            _c_(440873, _a_(440870, _n_(440869, "square", lambda: square), "setState"), _a_(440872, _n_(440871, "self", lambda: self), "player"), True)
                            _l_(440874)
                            # Change to next player
                            if _a_(440876, _n_(440875, "self", lambda: self), "player") == "O":
                                _l_(440881)

                                _n_(440877, "self", lambda: self).player = "X"
                                _l_(440878)
                            else:
                                _n_(440879, "self", lambda: self).player = "O"
                                _l_(440880)
                            # Check for a winner
                            winner = _c_(440884, _a_(440883, _n_(440882, "self", lambda: self), "getWinner"))
                            _l_(440885)

                            if _n_(440886, "winner", lambda: winner):
                                _l_(440898)

                                _c_(440890, _a_(440888, _n_(440887, "self", lambda: self), "winMessage"), _n_(440889, "winner", lambda: winner))
                                _l_(440891)
                            else:
                                _c_(440896, _a_(440893, _n_(440892, "square", lambda: square), "setState"), _a_(440895, _n_(440894, "self", lambda: self), "player"))
                                _l_(440897)
                        else:
                                # Set it to blank, only if
                            _n_(440899, "permanentState", lambda: permanentState) == False
                            _l_(440900)
                        _c_(440904, _a_(440903, _n_(440902, "square", lambda: square), "setState"), "")
                        _l_(440905)

if _n_(440912, "__name__", lambda: __name__) == "__main__":
    _l_(440920)

    game = _c_(440914, _n_(440913, "OAndX", lambda: OAndX))
    _l_(440915)
    _c_(440918, _a_(440917, _n_(440916, "game", lambda: game), "run"))
    _l_(440919)