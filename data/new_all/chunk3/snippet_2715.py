# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65802508/attributeerror-pygame-surface-object-has-no-attribute-screen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(543326)

except ImportError:
    pass


class Ship:
    _l_(543418)

    '''A class to manage the ship'''
    _l_(543327)

    def __init__(self, alinv_game):
        _l_(543376)

        '''Initialize the ship and set its starting position'''
        _l_(543328)

        _n_(543329, "self", lambda: self).screen = _a_(543331, _n_(543330, "alinv_game", lambda: alinv_game), "screen")
        _l_(543332)
        _n_(543333, "self", lambda: self).settings = _a_(543335, _n_(543334, "alinv_game", lambda: alinv_game), "settings")
        _l_(543336)
        _n_(543337, "self", lambda: self).screen_rect = _c_(543341, _a_(543340, _a_(543339, _n_(543338, "alinv_game", lambda: alinv_game), "screen"), "get_rect"))
        _l_(543342)

        '''Load the ship image and get its rect'''
        _l_(543343)
        _n_(543344, "self", lambda: self).image = _c_(543348, _a_(543347, _a_(543346, _n_(543345, "pygame", lambda: pygame), "image"), "load"), 'images/ship.bmp')
        _l_(543349)
        _n_(543350, "self", lambda: self).rect = _c_(543354, _a_(543353, _a_(543352, _n_(543351, "self", lambda: self), "image"), "get_rect"))
        _l_(543355)

        '''Start each new ship at the bottom-center of the screen'''
        _l_(543356)
        _a_(543358, _n_(543357, "self", lambda: self), "rect").midbottom = _a_(543361, _a_(543360, _n_(543359, "self", lambda: self), "screen_rect"), "midbottom")
        _l_(543362)

        '''Store a decimal value for ship's horizontal position'''
        _l_(543363)
        _n_(543364, "self", lambda: self).x = _c_(543369, _n_(543365, "float", lambda: float), _a_(543368, _a_(543367, _n_(543366, "self", lambda: self), "rect"), "x"))
        _l_(543370)

        '''Movement Flag'''
        _l_(543371)
        _n_(543372, "self", lambda: self).moving_right = False
        _l_(543373)
        _n_(543374, "self", lambda: self).moving_left = False
        _l_(543375)

    def update(self):
        _l_(543406)

        
        if _a_(543378, _n_(543377, "self", lambda: self), "moving_right") and _a_(543381, _a_(543380, _n_(543379, "self", lambda: self), "rect"), "right") < _a_(543384, _a_(543383, _n_(543382, "self", lambda: self), "screen_rect"), "right"):
            _l_(543389)

            _n_(543385, "self", lambda: self).x += _a_(543387, _n_(543386, "self", lambda: self), "settings").ship_speed
            _l_(543388)
        if _a_(543391, _n_(543390, "self", lambda: self), "moving_left") and _a_(543394, _a_(543393, _n_(543392, "self", lambda: self), "rect"), "left") > 0:
            _l_(543399)

            _n_(543395, "self", lambda: self).x -= _a_(543397, _n_(543396, "self", lambda: self), "settings").ship_speed
            _l_(543398)

        '''Update rect obj from self.x'''
        _l_(543400)
        _a_(543402, _n_(543401, "self", lambda: self), "rect").x = _a_(543404, _n_(543403, "self", lambda: self), "x")
        _l_(543405)

    def blitme(self):
        _l_(543417)

        '''Draw the ship at its current location.'''
        _l_(543407)
        _c_(543415, _a_(543410, _a_(543409, _n_(543408, "self", lambda: self), "screen"), "blit"), _a_(543412, _n_(543411, "self", lambda: self), "image"), _a_(543414, _n_(543413, "self", lambda: self), "rect"))
        _l_(543416)