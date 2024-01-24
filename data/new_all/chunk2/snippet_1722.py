# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60910850/pygame-typeerror-join-argument-must-be-str-bytes-or-os-pathlike-object-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""Gets the scaling info used in the other modules of the game"""
try:
    import pygame
    _l_(462587)

except ImportError:
    pass

def get_scaling_info():
    _l_(462616)

    """Gathers display info for scaling elements of the game"""
    _c_(462590, _a_(462589, _n_(462588, "pygame", lambda: pygame), "init"))
    _l_(462591)
    display_info = _c_(462595, _a_(462594, _a_(462593, _n_(462592, "pygame", lambda: pygame), "display"), "Info"))
    _l_(462596)
    scaling_info = _c_(462600, _a_(462599, _a_(462598, _n_(462597, "pygame", lambda: pygame), "display"), "Info"))
    _l_(462601)
    x_ratio = _a_(462603, _n_(462602, "display_info", lambda: display_info), "current_w")/_a_(462605, _n_(462604, "scaling_info", lambda: scaling_info), "current_w")
    _l_(462606)
    y_ratio = _a_(462608, _n_(462607, "display_info", lambda: display_info), "current_h")/_a_(462610, _n_(462609, "scaling_info", lambda: scaling_info), "current_h")
    _l_(462611)
    aux = _n_(462612, "scaling_info", lambda: scaling_info), _n_(462613, "x_ratio", lambda: x_ratio), _n_(462614, "y_ratio", lambda: y_ratio)
    _l_(462615)
    return aux