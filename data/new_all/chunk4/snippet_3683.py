# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(583115)

except ImportError:
    pass
try:
    from autopilot import debris, bullet_group
    _l_(583117)

except ImportError:
    pass

#screen settings
WIDTH = 1000
_l_(583118)
HEIGHT = 400
_l_(583119)

screen = _c_(583125, _a_(583122, _a_(583121, _n_(583120, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(583123, "WIDTH", lambda: WIDTH), _n_(583124, "HEIGHT", lambda: HEIGHT)))
_l_(583126)
_c_(583130, _a_(583129, _a_(583128, _n_(583127, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(583131)
_c_(583134, _a_(583133, _n_(583132, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(583135)

#load bullets
bullets = _c_(583141, _a_(583140, _c_(583139, _a_(583138, _a_(583137, _n_(583136, "pygame", lambda: pygame), "image"), "load"), 'car/bullet.png'), "convert_alpha"))
_l_(583142)

#bullet class
class Bullet(_a_(583145, _a_(583144, _n_(583143, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(583198)

    def __init__(self, x, y, direction):
        _l_(583172)

        _c_(583151, _a_(583149, _a_(583148, _a_(583147, _n_(583146, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(583150, "self", lambda: self))
        _l_(583152)

        _n_(583153, "self", lambda: self).speed = 5
        _l_(583154)
        _n_(583155, "self", lambda: self).image = _n_(583156, "bullets", lambda: bullets)
        _l_(583157)
        _n_(583158, "self", lambda: self).rect = _c_(583162, _a_(583161, _a_(583160, _n_(583159, "self", lambda: self), "image"), "get_rect"))
        _l_(583163)
        _a_(583165, _n_(583164, "self", lambda: self), "rect").center = (_n_(583166, "x", lambda: x),_n_(583167, "y", lambda: y))
        _l_(583168)
        _n_(583169, "self", lambda: self).direction = _n_(583170, "direction", lambda: direction)
        _l_(583171)

    def update(self):
        _l_(583197)

        _a_(583174, _n_(583173, "self", lambda: self), "rect").centery -= _n_(583175, "self", lambda: self).speed
        _l_(583176)
        #check if bullet has gone off screen
        if _a_(583179, _a_(583178, _n_(583177, "self", lambda: self), "rect"), "top") < 1:
            _l_(583184)

            _c_(583182, _a_(583181, _n_(583180, "self", lambda: self), "kill"))
            _l_(583183)
        #check collision with cement block
        if _c_(583190, _a_(583187, _a_(583186, _n_(583185, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(583188, "debris", lambda: debris), _n_(583189, "bullet_group", lambda: bullet_group), False):
            _l_(583196)

            if _a_(583192, _n_(583191, "debris", lambda: debris), "alive"):
                _l_(583195)

                _n_(583193, "debris", lambda: debris).health -= 25
                _l_(583194)