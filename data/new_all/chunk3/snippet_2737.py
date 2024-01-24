# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64801852/attributeerror-builtin-function-or-method-object-has-no-attribute-blit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(564724)

except ImportError:
    pass
try:
    import neat
    _l_(564726)

except ImportError:
    pass
try:
    import os
    _l_(564728)

except ImportError:
    pass
try:
    import time
    _l_(564730)

except ImportError:
    pass
try:
    import random
    _l_(564732)

except ImportError:
    pass

WIN_WIDTH = 500
_l_(564733)
WIN_HEIGHT = 800
_l_(564734)

BIRD_IMGS = [_c_(564746, _a_(564737, _a_(564736, _n_(564735, "pygame", lambda: pygame), "transform"), "scale2x"), _c_(564745, _a_(564740, _a_(564739, _n_(564738, "pygame", lambda: pygame), "image"), "load"), _c_(564744, _a_(564743, _a_(564742, _n_(564741, "os", lambda: os), "path"), "join"), r"C:\Users\pc\Desktop\PYTHON\Flappy bird AI\imgs", "bird1.png"))), _c_(564758, _a_(564749, _a_(564748, _n_(564747, "pygame", lambda: pygame), "transform"), "scale2x"), _c_(564757, _a_(564752, _a_(564751, _n_(564750, "pygame", lambda: pygame), "image"), "load"), _c_(564756, _a_(564755, _a_(564754, _n_(564753, "os", lambda: os), "path"), "join"), r"C:\Users\pc\Desktop\PYTHON\Flappy bird AI\imgs", "bird2.png"))), _c_(564770, _a_(564761, _a_(564760, _n_(564759, "pygame", lambda: pygame), "transform"), "scale2x"), _c_(564769, _a_(564764, _a_(564763, _n_(564762, "pygame", lambda: pygame), "image"), "load"), _c_(564768, _a_(564767, _a_(564766, _n_(564765, "os", lambda: os), "path"), "join"), r"C:\Users\pc\Desktop\PYTHON\Flappy bird AI\imgs", "bird3.png")))]
_l_(564771)
PIPE_IMGS = [_c_(564783, _a_(564774, _a_(564773, _n_(564772, "pygame", lambda: pygame), "transform"), "scale2x"), _c_(564782, _a_(564777, _a_(564776, _n_(564775, "pygame", lambda: pygame), "image"), "load"), _c_(564781, _a_(564780, _a_(564779, _n_(564778, "os", lambda: os), "path"), "join"), r"C:\Users\pc\Desktop\PYTHON\Flappy bird AI\imgs", "pipe.png")))]
_l_(564784)
BASE_IMGS = [_c_(564796, _a_(564787, _a_(564786, _n_(564785, "pygame", lambda: pygame), "transform"), "scale2x"), _c_(564795, _a_(564790, _a_(564789, _n_(564788, "pygame", lambda: pygame), "image"), "load"), _c_(564794, _a_(564793, _a_(564792, _n_(564791, "os", lambda: os), "path"), "join"), r"C:\Users\pc\Desktop\PYTHON\Flappy bird AI\imgs", "base.png")))]
_l_(564797)
BG_IMG = _c_(564809, _a_(564800, _a_(564799, _n_(564798, "pygame", lambda: pygame), "transform"), "scale2x"), _c_(564808, _a_(564803, _a_(564802, _n_(564801, "pygame", lambda: pygame), "image"), "load"), _c_(564807, _a_(564806, _a_(564805, _n_(564804, "os", lambda: os), "path"), "join"), r"C:\Users\pc\Desktop\PYTHON\Flappy bird AI\imgs", "bg.png")))
_l_(564810)

class Bird:
    _l_(564979)

    IMGS = _n_(564811, "BIRD_IMGS", lambda: BIRD_IMGS)
    _l_(564812)
    MAX_ROTATION = 25
    _l_(564813)
    ROT_VEL = 20
    _l_(564814)
    ANIMATION_TIME = 5
    _l_(564815)

    def __init__(self, x, y):
        _l_(564838)

        _n_(564816, "self", lambda: self).x = _n_(564817, "x", lambda: x)
        _l_(564818)
        _n_(564819, "self", lambda: self).y = _n_(564820, "y", lambda: y)
        _l_(564821)
        _n_(564822, "self", lambda: self).tilt = 0
        _l_(564823)
        _n_(564824, "self", lambda: self).tick_count = 0
        _l_(564825)
        _n_(564826, "self", lambda: self).vel = 0
        _l_(564827)
        _n_(564828, "self", lambda: self).height = _a_(564830, _n_(564829, "self", lambda: self), "y") 
        _l_(564831) 
        _n_(564832, "self", lambda: self).img_count = 0
        _l_(564833)
        _n_(564834, "self", lambda: self).img = _a_(564836, _n_(564835, "self", lambda: self), "IMGS")[0]
        _l_(564837)

    def jump(self):
        _l_(564847)

        _n_(564839, "self", lambda: self).vel = -10.5
        _l_(564840)
        _n_(564841, "self", lambda: self).tick_count = 0
        _l_(564842)
        _n_(564843, "self", lambda: self).height = _a_(564845, _n_(564844, "self", lambda: self), "y")
        _l_(564846)
    
    def move(self):
        _l_(564889)

        _n_(564848, "self", lambda: self).tick_count += 1
        _l_(564849)

        d = _a_(564851, _n_(564850, "self", lambda: self), "vel")*_a_(564853, _n_(564852, "self", lambda: self), "tick_count") + 1.5*_a_(564855, _n_(564854, "self", lambda: self), "tick_count")**2
        _l_(564856)

        if _n_(564857, "d", lambda: d) >= 16:
            _l_(564859)

            d = 16
            _l_(564858)

        if _n_(564860, "d", lambda: d) < 0:
            _l_(564862)

            d -= 2
            _l_(564861)
        
        _n_(564863, "self", lambda: self).y = _a_(564865, _n_(564864, "self", lambda: self), "y") + _n_(564866, "d", lambda: d)
        _l_(564867)
        
        if _n_(564868, "d", lambda: d) < 0 or _a_(564870, _n_(564869, "self", lambda: self), "y") < _a_(564872, _n_(564871, "self", lambda: self), "height") + 50:
            _l_(564888)

            if _a_(564874, _n_(564873, "self", lambda: self), "tilt") < _a_(564876, _n_(564875, "self", lambda: self), "MAX_ROTATION"):
                _l_(564881)

                _n_(564877, "self", lambda: self).tilt = _a_(564879, _n_(564878, "self", lambda: self), "MAX_ROTATION")
                _l_(564880)

        else: 
            if _a_(564883, _n_(564882, "self", lambda: self), "tilt") >-90:
                _l_(564887)

                _n_(564884, "self", lambda: self).tilt -= _n_(564885, "self", lambda: self).ROT_VEL
                _l_(564886)

    # This draw function deals with flapping of wings animation.
    def draw(self, win):
        _l_(564978)

        _n_(564890, "self", lambda: self).img_count += 1
        _l_(564891)

        if _a_(564893, _n_(564892, "self", lambda: self), "img_count") < _a_(564895, _n_(564894, "self", lambda: self), "ANIMATION_TIME"):
            _l_(564938)

            _n_(564896, "self", lambda: self).img = _a_(564898, _n_(564897, "self", lambda: self), "IMGS")[0]
            _l_(564899)
        elif _a_(564901, _n_(564900, "self", lambda: self), "img_count") < _a_(564903, _n_(564902, "self", lambda: self), "ANIMATION_TIME")*2:
            _l_(564937)

            _n_(564904, "self", lambda: self).img_count = _a_(564906, _n_(564905, "self", lambda: self), "IMGS")[1]
            _l_(564907)
        elif _a_(564909, _n_(564908, "self", lambda: self), "img_count") < _a_(564911, _n_(564910, "self", lambda: self), "ANIMATION_TIME")*3:
            _l_(564936)

            _n_(564912, "self", lambda: self).img_count = _a_(564914, _n_(564913, "self", lambda: self), "IMGS")[2]
            _l_(564915)
        elif _a_(564917, _n_(564916, "self", lambda: self), "img_count") < _a_(564919, _n_(564918, "self", lambda: self), "ANIMATION_TIME")*4:
            _l_(564935)

            _n_(564920, "self", lambda: self).img_count = _a_(564922, _n_(564921, "self", lambda: self), "IMGS")[1]
            _l_(564923)
        elif _a_(564925, _n_(564924, "self", lambda: self), "img_count") == _a_(564927, _n_(564926, "self", lambda: self), "ANIMATION_TIME")*4 + 1:
            _l_(564934)

            _n_(564928, "self", lambda: self).img_count = _a_(564930, _n_(564929, "self", lambda: self), "IMGS")[0]
            _l_(564931)
            _n_(564932, "self", lambda: self).img_count = 0
            _l_(564933)

        if _a_(564940, _n_(564939, "self", lambda: self), "tilt") <= -80:
            _l_(564948)

            self = _a_(564942, _n_(564941, "self", lambda: self), "IMGS")[1]
            _l_(564943)
            _n_(564944, "self", lambda: self).img_count = _a_(564946, _n_(564945, "self", lambda: self), "ANIMATION_TIME")*2     
            _l_(564947)     

        rotated_image = _c_(564956, _a_(564951, _a_(564950, _n_(564949, "pygame", lambda: pygame), "transform"), "rotate"), _a_(564953, _n_(564952, "self", lambda: self), "img"), _a_(564955, _n_(564954, "self", lambda: self), "tilt"))       
        _l_(564957)       
        new_rect = _c_(564969, _a_(564959, _n_(564958, "rotated_image", lambda: rotated_image), "get_rect"), center = _a_(564968, _c_(564967, _a_(564962, _a_(564961, _n_(564960, "self", lambda: self), "img"), "get_rect"), topleft = (_a_(564964, _n_(564963, "self", lambda: self), "x"), _a_(564966, _n_(564965, "self", lambda: self), "y"))), "center"))
        _l_(564970)
        _c_(564976, _a_(564972, _n_(564971, "win", lambda: win), "blit"), _n_(564973, "rotated_image", lambda: rotated_image), _a_(564975, _n_(564974, "new_rect", lambda: new_rect), "topleft"))
        _l_(564977)


def get_mask(self):
    _l_(564987)

    aux = _c_(564985, _a_(564982, _a_(564981, _n_(564980, "pygame", lambda: pygame), "mask"), "from_surface"), _a_(564984, _n_(564983, "self", lambda: self), "img"))
    _l_(564986)
    return aux

def draw_window(win, Bird):
    _l_(565006)

    _c_(564994, _a_(564989, _n_(564988, "win", lambda: win), "blit"), _n_(564990, "BG_IMG", lambda: BG_IMG), _c_(564993, _a_(564992, _n_(564991, "BG_IMG", lambda: BG_IMG), "get_rect")))
    _l_(564995)
    _c_(564999, _a_(564997, _n_(564996, "Bird", lambda: Bird), "draw"), _n_(564998, "bin", lambda: bin))
    _l_(565000)
    _c_(565004, _a_(565003, _a_(565002, _n_(565001, "pygame", lambda: pygame), "display"), "update"))
    _l_(565005)

def main():
    _l_(565054)

    bird = _c_(565008, _n_(565007, "Bird", lambda: Bird), 200, 200)
    _l_(565009)
    win = _c_(565015, _a_(565012, _a_(565011, _n_(565010, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(565013, "WIN_WIDTH", lambda: WIN_WIDTH), _n_(565014, "WIN_HEIGHT", lambda: WIN_HEIGHT)))
    _l_(565016)
    clock = _c_(565020, _a_(565019, _a_(565018, _n_(565017, "pygame", lambda: pygame), "time"), "Clock"))
    _l_(565021)
    run = True
    _l_(565022)
    while _n_(565023, "run", lambda: run):
        _l_(565053)

        _a_(565025, _n_(565024, "clock", lambda: clock), "tick")
        _l_(565026)
        for event in _c_(565030, _a_(565029, _a_(565028, _n_(565027, "pygame", lambda: pygame), "event"), "get")):
            _l_(565044)

            if _a_(565032, _n_(565031, "event", lambda: event), "type") == _a_(565034, _n_(565033, "pygame", lambda: pygame), "QUIT"):
                _l_(565043)

                run = False
                _l_(565035)
                _c_(565038, _a_(565037, _n_(565036, "pygame", lambda: pygame), "quit"))
                _l_(565039)
                _c_(565041, _n_(565040, "quit", lambda: quit))
                _l_(565042)

        _a_(565046, _n_(565045, "Bird", lambda: Bird), "move")
        _l_(565047)
        _c_(565051, _n_(565048, "draw_window", lambda: draw_window), _n_(565049, "win", lambda: win), _n_(565050, "bird", lambda: bird))
        _l_(565052)

_c_(565056, _n_(565055, "main", lambda: main))
_l_(565057)