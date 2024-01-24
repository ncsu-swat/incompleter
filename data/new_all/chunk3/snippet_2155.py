# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60849825/typeerror-kollision-missing-1-required-positional-argument-self
#Laden der Pygame Bibliothek
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(524168)

except ImportError:
    pass
try:
    import time
    _l_(524170)

except ImportError:
    pass
try:
    import random
    _l_(524172)

except ImportError:
    pass
#Initialisierung der Pygame Bibliothek
_c_(524175, _a_(524174, _n_(524173, "pygame", lambda: pygame), "init"))
_l_(524176)

# Spiel-Fenster erstellen
size = [700, 500]
_l_(524177)
screen = _c_(524182, _a_(524180, _a_(524179, _n_(524178, "pygame", lambda: pygame), "display"), "set_mode"), _n_(524181, "size", lambda: size))
_l_(524183)
_c_(524186, _a_(524185, _n_(524184, "screen", lambda: screen), "fill"), (255,255,255))
_l_(524187)
# Noetig um die fps zu begrenzen
clock = _c_(524191, _a_(524190, _a_(524189, _n_(524188, "pygame", lambda: pygame), "time"), "Clock"))
_l_(524192)

# Speichert ob das Spiel-Fenster geschlossen wurde
done = False
_l_(524193)


class Schlitten():
    _l_(524216)

    def __init__(self, px, py, pscreen):
        _l_(524215)

        _n_(524194, "self", lambda: self).FARBE1 = (139,87,66)
        _l_(524195)
        _n_(524196, "self", lambda: self).FARBE2 = (139,90,43)
        _l_(524197)
        _n_(524198, "self", lambda: self).braun = (104,73,71)
        _l_(524199)
        _n_(524200, "self", lambda: self).x = _n_(524201, "px", lambda: px)
        _l_(524202)
        _n_(524203, "self", lambda: self).grau = (118,122,121)
        _l_(524204)
        _n_(524205, "self", lambda: self).y = _n_(524206, "py", lambda: py)
        _l_(524207)
        _n_(524208, "self", lambda: self).red = (255,0,0)
        _l_(524209)
        _n_(524210, "self", lambda: self).screen = _n_(524211, "pscreen", lambda: pscreen)
        _l_(524212)
        _n_(524213, "self", lambda: self).treffer = False    
        _l_(524214)    