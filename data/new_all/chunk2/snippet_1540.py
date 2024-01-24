# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37057027/attributeerror-pygame-surface-object-has-no-attribute-add-internal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame, sys, os
    _l_(474779)

except ImportError:
    pass
try:
    from pygame.locals import *
    _l_(474781)

except ImportError:
    pass
_c_(474784, _a_(474783, _n_(474782, "pygame", lambda: pygame), "init"))
_l_(474785)
screen = _c_(474789, _a_(474788, _a_(474787, _n_(474786, "pygame", lambda: pygame), "display"), "set_mode"), (100, 100))
_l_(474790)

tile_l1_list = _c_(474794, _a_(474793, _a_(474792, _n_(474791, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(474795)

image = _c_(474799, _a_(474798, _a_(474797, _n_(474796, "pygame", lambda: pygame), "image"), "load"), "box.png")
_l_(474800)
image = _c_(474803, _a_(474802, _n_(474801, "image", lambda: image), "convert_alpha"))
_l_(474804)
a=_c_(474808, _a_(474806, _n_(474805, "screen", lambda: screen), "blit"), _n_(474807, "image", lambda: image), (10,10))
_l_(474809)
_c_(474813, _a_(474812, _a_(474811, _n_(474810, "pygame", lambda: pygame), "display"), "flip"))
_l_(474814)
_c_(474818, _a_(474816, _n_(474815, "tile_l1_list", lambda: tile_l1_list), "add"), _n_(474817, "image", lambda: image))
_l_(474819)


####################################

while True:
    _l_(474825)

    _c_(474823, _a_(474822, _a_(474821, _n_(474820, "pygame", lambda: pygame), "display"), "flip"))
    _l_(474824)

_c_(474828, _a_(474827, _n_(474826, "pygame", lambda: pygame), "quit"))
_l_(474829)