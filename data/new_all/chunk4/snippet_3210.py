# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77346201/nameerror-name-bg-img-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(623159)

except ImportError:
    pass
try:
    import pickle
    _l_(623161)

except ImportError:
    pass
try:
    import os
    _l_(623163)

except ImportError:
    pass
try:
    from os import path
    _l_(623165)

except ImportError:
    pass
try:
    import time
    _l_(623167)

except ImportError:
    pass
try:
    import json
    _l_(623169)

except ImportError:
    pass
try:
    import webbrowser
    _l_(623171)

except ImportError:
    pass
try:
    from assets import *
    _l_(623173)

except ImportError:
    pass
try:
    from fonts import *
    _l_(623175)

except ImportError:
    pass
# further Code

while _n_(623176, "run", lambda: run):
    _l_(623187)

    _c_(623180, _a_(623178, _n_(623177, "clock", lambda: clock), "tick"), _n_(623179, "fps", lambda: fps))
    _l_(623181)

    _c_(623185, _a_(623183, _n_(623182, "screen", lambda: screen), "blit"), _n_(623184, "bg_img", lambda: bg_img), (0, 0))
    _l_(623186)