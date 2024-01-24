# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31484492/typeerror-argument-1-must-be-pygame-surface-not-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(631948)

except ImportError:
    pass

_c_(631951, _a_(631950, _n_(631949, "pygame", lambda: pygame), "init"))
_l_(631952)

display_width = 800
_l_(631953)
display_height = 600
_l_(631954)

black = (0,0,0)
_l_(631955)
white = (255,255,255)
_l_(631956)
red = (200,0,0)
_l_(631957)
bright_red = (255,0,0)
_l_(631958)
green = (0,200,0)
_l_(631959)
bright_green = (0,255,0)
_l_(631960)
blue = (0,0,200)
_l_(631961)
bright_blue = (0,0,255)
_l_(631962)

gameDisplay = _c_(631968, _a_(631965, _a_(631964, _n_(631963, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(631966, "display_width", lambda: display_width),_n_(631967, "display_height", lambda: display_height)))
_l_(631969)
_c_(631973, _a_(631972, _a_(631971, _n_(631970, "pygame", lambda: pygame), "display"), "set_caption"), 'Le jeux')
_l_(631974)
clock = _c_(631978, _a_(631977, _a_(631976, _n_(631975, "pygame", lambda: pygame), "time"), "Clock"))
_l_(631979)

thatonething = _c_(631983, _a_(631982, _a_(631981, _n_(631980, "pygame", lambda: pygame), "image"), "load"), 'thatonething.png')
_l_(631984)

def somefunction(x,y):
    _l_(631992)

    _c_(631990, _a_(631986, _n_(631985, "gameDisplay", lambda: gameDisplay), "blit"), _n_(631987, "thatonething", lambda: thatonething),(_n_(631988, "x", lambda: x),_n_(631989, "y", lambda: y)))
    _l_(631991)

x = (_n_(631993, "display_width", lambda: display_width) * 0.45)
_l_(631994)
y = (_n_(631995, "display_height", lambda: display_height) * 0.8)
_l_(631996)

crashed = False
_l_(631997)

while not _n_(631998, "crashed", lambda: crashed):
    _l_(632033)


    for event in _c_(632002, _a_(632001, _a_(632000, _n_(631999, "pygame", lambda: pygame), "event"), "get")):
        _l_(632013)

        if _a_(632004, _n_(632003, "event", lambda: event), "type") == _a_(632006, _n_(632005, "pygame", lambda: pygame), "QUIT"):
            _l_(632008)

            crashed = True
            _l_(632007)
        _c_(632011, _n_(632009, "print", lambda: print), _n_(632010, "event", lambda: event)) #This creates a log of the events that pygame has been handling.
        _l_(632012) #This creates a log of the events that pygame has been handling.

    _c_(632017, _a_(632015, _n_(632014, "gameDisplay", lambda: gameDisplay), "fill"), _n_(632016, "white", lambda: white))
    _l_(632018)
    _c_(632022, _n_(632019, "somefunction", lambda: somefunction), _n_(632020, "x", lambda: x),_n_(632021, "y", lambda: y))
    _l_(632023)
    _c_(632027, _a_(632026, _a_(632025, _n_(632024, "pygame", lambda: pygame), "display"), "update")) #Updates everything "pygame.display.flip()" updates just one thing
    _l_(632028) #Updates everything "pygame.display.flip()" updates just one thing
    _c_(632031, _a_(632030, _n_(632029, "clock", lambda: clock), "tick"), 30) #This defines the refresh rate i.e. 30 in brackets gives 30 fps
    _l_(632032) #This defines the refresh rate i.e. 30 in brackets gives 30 fps

_c_(632036, _a_(632035, _n_(632034, "pygame", lambda: pygame), "quit")) #Closes the game (with the next line)
_l_(632037) #Closes the game (with the next line)
_c_(632039, _n_(632038, "quit", lambda: quit))
_l_(632040)