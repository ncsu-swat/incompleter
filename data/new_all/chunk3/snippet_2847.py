# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61030988/pygame-attributeerror-pygame-surface-object-has-no-attribute-display
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame, sys, os
    _l_(543193)

except ImportError:
    pass
try:
    from pygame.locals import *
    _l_(543195)

except ImportError:
    pass
red = (255,0,0)
_l_(543196)
_c_(543199, _a_(543198, _n_(543197, "pygame", lambda: pygame), "init"))
_l_(543200)
window = _c_(543204, _a_(543203, _a_(543202, _n_(543201, "pygame", lambda: pygame), "display"), "set_mode"), (1000,600))
_l_(543205)
_c_(543209, _a_(543208, _a_(543207, _n_(543206, "pygame", lambda: pygame), "display"), "set_caption"), 'Slither.eat - The Snake Game')
_l_(543210)
screen = _c_(543214, _a_(543213, _a_(543212, _n_(543211, "pygame", lambda: pygame), "display"), "get_surface"))
_l_(543215)
_c_(543219, _a_(543217, _n_(543216, "screen", lambda: screen), "fill"), _n_(543218, "red", lambda: red))
_l_(543220)
_c_(543224, _a_(543223, _a_(543222, _n_(543221, "screen", lambda: screen), "display"), "set_caption"), "Snake")
_l_(543225)
_c_(543229, _a_(543228, _a_(543227, _n_(543226, "pygame", lambda: pygame), "display"), "flip"))
_l_(543230)
while True:
    _l_(543235)

    _c_(543232, _n_(543231, "print", lambda: print), "Slither.eat - The Snake Game!")
    _l_(543233)
    pass
    _l_(543234)