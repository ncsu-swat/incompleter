# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45065390/error-attributeerror-module-pygame-has-no-attribute-colors
#Snake Game!
#Our game imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(602569)

except ImportError:
    pass
try:
    import sys
    _l_(602571)

except ImportError:
    pass
try:
    import random
    _l_(602573)

except ImportError:
    pass
try:
    import time
    _l_(602575)

except ImportError:
    pass

check_errors = _c_(602578, _a_(602577, _n_(602576, "pygame", lambda: pygame), "init"))
_l_(602579)

#(6,0)

if _n_(602580, "check_errors", lambda: check_errors)[1] > 0:
    _l_(602594)

    _c_(602585, _n_(602581, "print", lambda: print), _c_(602584, _a_(602582, "(!) Had {0} initializing error, exiting....", "format"), _n_(602583, "check_errors", lambda: check_errors)[1]))
    _l_(602586)
    _c_(602589, _a_(602588, _n_(602587, "sys", lambda: sys), "exit"), -1)
    _l_(602590)
else:
    _c_(602592, _n_(602591, "print", lambda: print), "(+) PyGame sucessfully initialized")
    _l_(602593)

# Play surface. Create a black surface for game


playSurface = _c_(602598, _a_(602597, _a_(602596, _n_(602595, "pygame", lambda: pygame), "display"), "set_mode"), (720,460))
_l_(602599)
_c_(602603, _a_(602602, _a_(602601, _n_(602600, "pygame", lambda: pygame), "display"), "set_caption"), "SNAKE GAME")
_l_(602604)
_c_(602607, _a_(602606, _n_(602605, "time", lambda: time), "sleep"), 5)
_l_(602608)

#Colors - r,g,b -- red green blue

red = _c_(602611, _a_(602610, _n_(602609, "pygame", lambda: pygame), "Colors"), 255,0,0) #gameover
_l_(602612) #gameover
green = _c_(602615, _a_(602614, _n_(602613, "pygame", lambda: pygame), "Colors"), 0,255,0) #snake
_l_(602616) #snake
#black
black = _c_(602619, _a_(602618, _n_(602617, "pygame", lambda: pygame), "Colors"), 0,0,0) #score
_l_(602620) #score
white = _c_(602623, _a_(602622, _n_(602621, "pygame", lambda: pygame), "Colors"), 255,255,255) #background
_l_(602624) #background
brown = _c_(602627, _a_(602626, _n_(602625, "pygame", lambda: pygame), "Colors"), 165,42,42) #food
_l_(602628) #food

# FPS frames per seconds controller 
fpsController = _c_(602632, _a_(602631, _a_(602630, _n_(602629, "pygame", lambda: pygame), "time"), "Clock"))
_l_(602633)

#where do you want the snake to start
#Important variables

snakePos = [100,50] #should be less than the screen size - (720,460)
_l_(602634) #should be less than the screen size - (720,460)
snakeBoday =  [[100,50],[90,50],[80,50]]
_l_(602635)

foodPos = [_c_(602638, _a_(602637, _n_(602636, "random", lambda: random), "randrange"), 1,72)*10,_c_(602641, _a_(602640, _n_(602639, "random", lambda: random), "randrange"), 1,46)*10]
_l_(602642)
foodSpawn = True
_l_(602643)

direction = 'RIGHT'
_l_(602644)
changeto = _n_(602645, "direction", lambda: direction)
_l_(602646)

#Game over function

def gameOver():
    _l_(602674)

    myFont = _c_(602650, _a_(602649, _a_(602648, _n_(602647, "pygame", lambda: pygame), "font"), "SysFont"), 'monaco',72)
    _l_(602651)
    GOsurf = _c_(602655, _a_(602653, _n_(602652, "myFont", lambda: myFont), "render"), 'Game Over!!', True, _n_(602654, "red", lambda: red))
    _l_(602656)
    GOrect = _c_(602659, _a_(602658, _n_(602657, "Gosurf", lambda: Gosurf), "get_rect"))
    _l_(602660)
    _n_(602661, "Gorect", lambda: Gorect).midtop = (360, 15)
    _l_(602662)
    _c_(602667, _a_(602664, _n_(602663, "playSurface", lambda: playSurface), "blit"), _n_(602665, "GOsurf", lambda: GOsurf),_n_(602666, "GOrect", lambda: GOrect))
    _l_(602668)
    _c_(602672, _a_(602671, _a_(602670, _n_(602669, "python", lambda: python), "display"), "flip"))
    _l_(602673)

_c_(602676, _n_(602675, "gameOver", lambda: gameOver))
_l_(602677)
_c_(602680, _a_(602679, _n_(602678, "time", lambda: time), "sleep"), 10)
_l_(602681)