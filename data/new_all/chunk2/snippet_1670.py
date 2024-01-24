# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65076219/filenotfounderror-no-such-file-or-directory-in-pygame
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(426785)

except ImportError:
    pass
screen = _c_(426789, _a_(426788, _a_(426787, _n_(426786, "pygame", lambda: pygame), "display"), "set_mode"), (800,600))
_l_(426790)
_c_(426794, _a_(426793, _a_(426792, _n_(426791, "pygame", lambda: pygame), "display"), "set_caption"), "Space vaders")
_l_(426795)
fond = _c_(426801, _a_(426798, _a_(426797, _n_(426796, "pygame", lambda: pygame), "image"), "load"), _a_(426800, _n_(426799, "testingfield", lambda: testingfield), "png"))
_l_(426802)