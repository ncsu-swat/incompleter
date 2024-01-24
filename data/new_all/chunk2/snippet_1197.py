# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52066118/i-keep-getting-the-error-typeerror-integer-argument-expected-got-float-in-pyt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(444249)

except ImportError:
    pass

_c_(444252, _a_(444251, _n_(444250, "pygame", lambda: pygame), "init"))
_l_(444253)

black = (0,0,0)
_l_(444254)
white = (255,255,255)
_l_(444255)
red = (255,0,0)
_l_(444256)
blue = (0,0,255)
_l_(444257)
sky_blue = (0,150,225)
_l_(444258)
green = (0,255,0)
_l_(444259)

displayWidth = 800
_l_(444260)

displayHeight = 600
_l_(444261)
#Final :- pygame.display.set_mode((1365, 1050))
gameDisplay = _c_(444267, _a_(444264, _a_(444263, _n_(444262, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(444265, "displayWidth", lambda: displayWidth),_n_(444266, "displayHeight", lambda: displayHeight)))
_l_(444268)
_c_(444272, _a_(444271, _a_(444270, _n_(444269, "pygame", lambda: pygame), "display"), "set_caption"), 'Super Mario')
_l_(444273)
clock = _c_(444277, _a_(444276, _a_(444275, _n_(444274, "pygame", lambda: pygame), "time"), "Clock"))
_l_(444278)

crashed = False
_l_(444279)

timeOut = False
_l_(444280)

Quit = False
_l_(444281)

#50,75
marioStanding = _c_(444285, _a_(444284, _a_(444283, _n_(444282, "pygame", lambda: pygame), "image"), "load"), 'Super_Mario_Standing.jpg')
_l_(444286)
marioStanding = _c_(444293, _a_(444289, _a_(444288, _n_(444287, "pygame", lambda: pygame), "transform"), "scale"), _n_(444290, "marioStanding", lambda: marioStanding), (_n_(444291, "displayWidth", lambda: displayWidth)/40,_n_(444292, "displayHeight", lambda: displayHeight)/8))
_l_(444294)

def Stand(x,y):
    _l_(444302)

    _c_(444300, _a_(444296, _n_(444295, "gameDisplay", lambda: gameDisplay), "blit"), _n_(444297, "marioStanding", lambda: marioStanding),(_n_(444298, "x", lambda: x),_n_(444299, "y", lambda: y)))
    _l_(444301)

x = (_n_(444303, "displayWidth", lambda: displayWidth) * 0.45)
_l_(444304)
y = (_n_(444305, "displayHeight", lambda: displayHeight) * 0.8)
_l_(444306)

while not _n_(444307, "crashed", lambda: crashed) and not _n_(444308, "timeOut", lambda: timeOut) and not _n_(444309, "Quit", lambda: Quit):
    _l_(444344)


    for event in _c_(444313, _a_(444312, _a_(444311, _n_(444310, "pygame", lambda: pygame), "event"), "get")):
        _l_(444320)

        if _a_(444315, _n_(444314, "event", lambda: event), "type") == _a_(444317, _n_(444316, "pygame", lambda: pygame), "QUIT"):
            _l_(444319)

            Quit = True
            _l_(444318)

    _c_(444323, _n_(444321, "print", lambda: print), _n_(444322, "event", lambda: event))
    _l_(444324)

    _c_(444328, _a_(444326, _n_(444325, "gameDisplay", lambda: gameDisplay), "fill"), _n_(444327, "sky_blue", lambda: sky_blue))
    _l_(444329)
    _c_(444333, _n_(444330, "Stand", lambda: Stand), _n_(444331, "x", lambda: x),_n_(444332, "y", lambda: y))
    _l_(444334)

    _c_(444338, _a_(444337, _a_(444336, _n_(444335, "pygame", lambda: pygame), "display"), "update"))
    _l_(444339)
    _c_(444342, _a_(444341, _n_(444340, "clock", lambda: clock), "tick"), 24)
    _l_(444343)

_c_(444347, _a_(444346, _n_(444345, "pygame", lambda: pygame), "quit"))
_l_(444348)
_c_(444350, _n_(444349, "quit", lambda: quit))
_l_(444351)