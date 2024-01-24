# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60910850/pygame-typeerror-join-argument-must-be-str-bytes-or-os-pathlike-object-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""Contains the class used to generate towers"""
try:
    import os
    _l_(430767)

except ImportError:
    pass
try:
    import pygame
    _l_(430769)

except ImportError:
    pass
try:
    from scaling import get_scaling_info
    _l_(430771)

except ImportError:
    pass

_c_(430773, _n_(430772, "get_scaling_info", lambda: get_scaling_info))
_l_(430774)

class Tower:
    _l_(430851)

    """Tower information"""
    selection_dict = {49:"elf_tower.png", 50:"dwarf_tower.png"} #pygame keypress of 1 corresponds to value 49, 2 to 50.
    _l_(430775) #pygame keypress of 1 corresponds to value 49, 2 to 50.
    towers = []
    _l_(430776)
    def __init__(self, img, x, y, display_surface="game_surface"):
        _l_(430807)

        x_scale, y_scale = _c_(430778, _n_(430777, "get_scaling_info", lambda: get_scaling_info))[1:]
        _l_(430779)
        _n_(430780, "self", lambda: self).img = _c_(430789, _a_(430783, _a_(430782, _n_(430781, "pygame", lambda: pygame), "image"), "load"), _c_(430788, _a_(430786, _a_(430785, _n_(430784, "os", lambda: os), "path"), "join"), 'assets', _n_(430787, "img", lambda: img)))
        _l_(430790)
        _c_(430794, _n_(430791, "print", lambda: print), _a_(430793, _n_(430792, "self", lambda: self), "img")) # returns <Surface(40x40x32 SW)>
        _l_(430795) # returns <Surface(40x40x32 SW)>
        _n_(430796, "self", lambda: self).x_coord = _n_(430797, "x", lambda: x) * _n_(430798, "x_scale", lambda: x_scale)
        _l_(430799)
        _n_(430800, "self", lambda: self).y_coord = _n_(430801, "y", lambda: y) * _n_(430802, "y_scale", lambda: y_scale)
        _l_(430803)
        _n_(430804, "self", lambda: self).display_surface = _n_(430805, "display_surface", lambda: display_surface)
        _l_(430806)

    def create_tower(self):
        _l_(430826)

        """Creates a tower of the selected type and scales to the correct size"""
        _c_(430819, _a_(430810, _a_(430809, _n_(430808, "Tower", lambda: Tower), "towers"), "append"), _c_(430818, _n_(430811, "Tower", lambda: Tower), _a_(430813, _n_(430812, "self", lambda: self), "img"), _a_(430815, _n_(430814, "self", lambda: self), "x_coord"), _a_(430817, _n_(430816, "self", lambda: self), "y_coord")))
        _l_(430820)
        _c_(430824, _n_(430821, "print", lambda: print), _a_(430823, _n_(430822, "Tower", lambda: Tower), "towers"))
        _l_(430825)

    def draw(self):
        _l_(430850)

        """Draws the tower on the screen using the specified image at coordinates x and y"""
        _c_(430832, _a_(430829, _a_(430828, _n_(430827, "pygame", lambda: pygame), "transform"), "scale"), _a_(430831, _n_(430830, "self", lambda: self), "img"), (32, 32))
        _l_(430833)
        _c_(430843, _a_(430836, _a_(430835, _n_(430834, "self", lambda: self), "display_surface"), "blit"), _a_(430838, _n_(430837, "self", lambda: self), "img"), (_a_(430840, _n_(430839, "self", lambda: self), "x_coord"), _a_(430842, _n_(430841, "self", lambda: self), "y_coord")))
        _l_(430844)
        _c_(430848, _n_(430845, "print", lambda: print), _a_(430847, _n_(430846, "self", lambda: self), "img"))
        _l_(430849)