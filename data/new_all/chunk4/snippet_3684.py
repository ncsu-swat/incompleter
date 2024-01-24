# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(644957)

except ImportError:
    pass

#screen settings
WIDTH = 1000
_l_(644958)
HEIGHT = 400
_l_(644959)

screen = _c_(644965, _a_(644962, _a_(644961, _n_(644960, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(644963, "WIDTH", lambda: WIDTH), _n_(644964, "HEIGHT", lambda: HEIGHT)))
_l_(644966)
_c_(644970, _a_(644969, _a_(644968, _n_(644967, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(644971)
_c_(644974, _a_(644973, _n_(644972, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(644975)

#debris class
class Debris(_a_(644978, _a_(644977, _n_(644976, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(645063)

    def __init__(self, scale, speed):
        _l_(645051)

        _c_(644984, _a_(644982, _a_(644981, _a_(644980, _n_(644979, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(644983, "self", lambda: self))
        _l_(644985)

        _n_(644986, "self", lambda: self).x = 400
        _l_(644987)
        _n_(644988, "self", lambda: self).y = _n_(644989, "HEIGHT", lambda: HEIGHT) / 2 - 200
        _l_(644990)
        _n_(644991, "self", lambda: self).speed = _n_(644992, "speed", lambda: speed)
        _l_(644993)
        _n_(644994, "self", lambda: self).vy = 0
        _l_(644995)
        _n_(644996, "self", lambda: self).on_ground = True
        _l_(644997)
        _n_(644998, "self", lambda: self).move = True
        _l_(644999)
        _n_(645000, "self", lambda: self).health = 100
        _l_(645001)
        _n_(645002, "self", lambda: self).max_health = _a_(645004, _n_(645003, "self", lambda: self), "health")
        _l_(645005)
        _n_(645006, "self", lambda: self).alive = True
        _l_(645007)

        #load debris
        _n_(645008, "self", lambda: self).images = []
        _l_(645009)
        img = _c_(645015, _a_(645014, _c_(645013, _a_(645012, _a_(645011, _n_(645010, "pygame", lambda: pygame), "image"), "load"), 'debris/cement.png'), "convert_alpha"))
        _l_(645016)
        img = _c_(645033, _a_(645019, _a_(645018, _n_(645017, "pygame", lambda: pygame), "transform"), "scale"), _n_(645020, "img", lambda: img), (_c_(645025, _n_(645021, "int", lambda: int), _c_(645024, _a_(645023, _n_(645022, "img", lambda: img), "get_width"))) * _n_(645026, "scale", lambda: scale), (_c_(645031, _n_(645027, "int", lambda: int), _c_(645030, _a_(645029, _n_(645028, "img", lambda: img), "get_height"))) * _n_(645032, "scale", lambda: scale))))
        _l_(645034)
        _c_(645039, _a_(645037, _a_(645036, _n_(645035, "self", lambda: self), "images"), "append"), _n_(645038, "img", lambda: img))
        _l_(645040)
        _n_(645041, "self", lambda: self).image = _a_(645043, _n_(645042, "self", lambda: self), "images")[0]
        _l_(645044)
        _n_(645045, "self", lambda: self).rect = _c_(645049, _a_(645048, _a_(645047, _n_(645046, "self", lambda: self), "image"), "get_rect"))
        _l_(645050)

    #draw debris to screen
    def draw(self):
        _l_(645062)

        _c_(645060, _a_(645053, _n_(645052, "screen", lambda: screen), "blit"), _a_(645055, _n_(645054, "self", lambda: self), "image"),(_a_(645057, _n_(645056, "self", lambda: self), "x"),_a_(645059, _n_(645058, "self", lambda: self), "y")))
        _l_(645061)