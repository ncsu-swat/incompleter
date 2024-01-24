# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31484492/typeerror-argument-1-must-be-pygame-surface-not-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(646497)

except ImportError:
    pass

_c_(646500, _a_(646499, _n_(646498, "pygame", lambda: pygame), "init"))
_l_(646501)

display_width = 800
_l_(646502)
display_height = 600
_l_(646503)

black = (0,0,0)
_l_(646504)
white = (255,255,255)
_l_(646505)
red = (200,0,0)
_l_(646506)
bright_red = (255,0,0)
_l_(646507)
green = (0,200,0)
_l_(646508)
bright_green = (0,255,0)
_l_(646509)
blue = (0,0,200)
_l_(646510)
bright_blue = (0,0,255)
_l_(646511)

gameDisplay = _c_(646517, _a_(646514, _a_(646513, _n_(646512, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(646515, "display_width", lambda: display_width),_n_(646516, "display_height", lambda: display_height)))
_l_(646518)
_c_(646522, _a_(646521, _a_(646520, _n_(646519, "pygame", lambda: pygame), "display"), "set_caption"), 'Le jeux')
_l_(646523)
clock = _c_(646527, _a_(646526, _a_(646525, _n_(646524, "pygame", lambda: pygame), "time"), "Clock"))
_l_(646528)

thatonething = _c_(646532, _a_(646531, _a_(646530, _n_(646529, "pygame", lambda: pygame), "image"), "load"), 'thatonething.png')
_l_(646533)

def thatonething(x,y):
    _l_(646541)

    _c_(646539, _a_(646535, _n_(646534, "gameDisplay", lambda: gameDisplay), "blit"), _n_(646536, "thatonething", lambda: thatonething),(_n_(646537, "x", lambda: x),_n_(646538, "y", lambda: y)))
    _l_(646540)

x = (_n_(646542, "display_width", lambda: display_width) * 0.45)
_l_(646543)
y = (_n_(646544, "display_height", lambda: display_height) * 0.8)
_l_(646545)

crashed = False
_l_(646546)

while not _n_(646547, "crashed", lambda: crashed):
    _l_(646582)


    for event in _c_(646551, _a_(646550, _a_(646549, _n_(646548, "pygame", lambda: pygame), "event"), "get")):
        _l_(646562)

        if _a_(646553, _n_(646552, "event", lambda: event), "type") == _a_(646555, _n_(646554, "pygame", lambda: pygame), "QUIT"):
            _l_(646557)

            crashed = True
            _l_(646556)
        _c_(646560, _n_(646558, "print", lambda: print), _n_(646559, "event", lambda: event)) 
        _l_(646561) 

    _c_(646566, _a_(646564, _n_(646563, "gameDisplay", lambda: gameDisplay), "fill"), _n_(646565, "white", lambda: white))
    _l_(646567)
    _c_(646571, _n_(646568, "thatonething", lambda: thatonething), _n_(646569, "x", lambda: x),_n_(646570, "y", lambda: y))
    _l_(646572)
    _c_(646576, _a_(646575, _a_(646574, _n_(646573, "pygame", lambda: pygame), "display"), "update")) 
    _l_(646577) 
    _c_(646580, _a_(646579, _n_(646578, "clock", lambda: clock), "tick"), 30) 
    _l_(646581) 

_c_(646585, _a_(646584, _n_(646583, "pygame", lambda: pygame), "quit")) 
_l_(646586) 
_c_(646588, _n_(646587, "quit", lambda: quit))
_l_(646589)