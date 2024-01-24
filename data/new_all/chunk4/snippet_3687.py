# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(586996)

except ImportError:
    pass

#screen settings
WIDTH = 1000
_l_(586997)
HEIGHT = 400
_l_(586998)

screen = _c_(587004, _a_(587001, _a_(587000, _n_(586999, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(587002, "WIDTH", lambda: WIDTH), _n_(587003, "HEIGHT", lambda: HEIGHT)))
_l_(587005)
_c_(587009, _a_(587008, _a_(587007, _n_(587006, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(587010)
_c_(587013, _a_(587012, _n_(587011, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(587014)

#load bullets
bullets = _c_(587020, _a_(587019, _c_(587018, _a_(587017, _a_(587016, _n_(587015, "pygame", lambda: pygame), "image"), "load"), 'car/bullet.png'), "convert_alpha"))
_l_(587021)

#groups
bullet_group = _c_(587025, _a_(587024, _a_(587023, _n_(587022, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(587026)

#player class
class Player(_a_(587029, _a_(587028, _n_(587027, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(587174)

    def __init__(self, scale, speed):
        _l_(587107)

        _c_(587035, _a_(587033, _a_(587032, _a_(587031, _n_(587030, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(587034, "self", lambda: self))
        _l_(587036)

        _n_(587037, "self", lambda: self).speed = _n_(587038, "speed", lambda: speed)
        _l_(587039)
        #self.x = x
        #self.y = y
        _n_(587040, "self", lambda: self).moving = True
        _l_(587041)
        _n_(587042, "self", lambda: self).frame = 0
        _l_(587043)
        _n_(587044, "self", lambda: self).flip = False
        _l_(587045)
        _n_(587046, "self", lambda: self).direction = 0
        _l_(587047)

        #load car
        _n_(587048, "self", lambda: self).images = []
        _l_(587049)
        img = _c_(587055, _a_(587054, _c_(587053, _a_(587052, _a_(587051, _n_(587050, "pygame", lambda: pygame), "image"), "load"), 'car/car.png'), "convert_alpha"))
        _l_(587056)
        img = _c_(587073, _a_(587059, _a_(587058, _n_(587057, "pygame", lambda: pygame), "transform"), "scale"), _n_(587060, "img", lambda: img), (_c_(587065, _n_(587061, "int", lambda: int), _c_(587064, _a_(587063, _n_(587062, "img", lambda: img), "get_width"))) * _n_(587066, "scale", lambda: scale), (_c_(587071, _n_(587067, "int", lambda: int), _c_(587070, _a_(587069, _n_(587068, "img", lambda: img), "get_height"))) * _n_(587072, "scale", lambda: scale))))
        _l_(587074)
        _c_(587079, _a_(587077, _a_(587076, _n_(587075, "self", lambda: self), "images"), "append"), _n_(587078, "img", lambda: img))
        _l_(587080)
        _n_(587081, "self", lambda: self).image = _a_(587083, _n_(587082, "self", lambda: self), "images")[0]
        _l_(587084)
        _n_(587085, "self", lambda: self).rect = _c_(587089, _a_(587088, _a_(587087, _n_(587086, "self", lambda: self), "image"), "get_rect"))
        _l_(587090)
        _n_(587091, "self", lambda: self).update_time = _c_(587095, _a_(587094, _a_(587093, _n_(587092, "pygame", lambda: pygame), "time"), "get_ticks"))
        _l_(587096)
        _n_(587097, "self", lambda: self).movingLeft = False
        _l_(587098)
        _n_(587099, "self", lambda: self).movingRight = False
        _l_(587100)
        _a_(587102, _n_(587101, "self", lambda: self), "rect").x = 465
        _l_(587103)
        _a_(587105, _n_(587104, "self", lambda: self), "rect").y = 325
        _l_(587106)

    #draw car to screen
    def draw(self):
        _l_(587120)

        _c_(587118, _a_(587109, _n_(587108, "screen", lambda: screen), "blit"), _a_(587111, _n_(587110, "self", lambda: self), "image"), (_a_(587114, _a_(587113, _n_(587112, "self", lambda: self), "rect"), "centerx"), _a_(587117, _a_(587116, _n_(587115, "self", lambda: self), "rect"), "centery")))
        _l_(587119)

    #move car
    def move(self):
        _l_(587155)

        #reset the movement variables
        dx = 0
        _l_(587121)
        dy = 0
        _l_(587122)

        #moving variables
        if _a_(587124, _n_(587123, "self", lambda: self), "movingLeft") and _a_(587127, _a_(587126, _n_(587125, "self", lambda: self), "rect"), "x") > 33:
            _l_(587134)

            dx -= _n_(587128, "self", lambda: self).speed
            _l_(587129)
            _n_(587130, "self", lambda: self).flip = True
            _l_(587131)
            _n_(587132, "self", lambda: self).direction = -1
            _l_(587133)
        if _a_(587136, _n_(587135, "self", lambda: self), "movingRight") and _a_(587139, _a_(587138, _n_(587137, "self", lambda: self), "rect"), "x") < 900:
            _l_(587146)

            dx += _n_(587140, "self", lambda: self).speed
            _l_(587141)
            _n_(587142, "self", lambda: self).flip = False
            _l_(587143)
            _n_(587144, "self", lambda: self).direction = 1
            _l_(587145)

        #update rectangle position
        _a_(587148, _n_(587147, "self", lambda: self), "rect").x += _n_(587149, "dx", lambda: dx)
        _l_(587150)
        _a_(587152, _n_(587151, "self", lambda: self), "rect").y += _n_(587153, "dy", lambda: dy)
        _l_(587154)

    #shoot
    def shoot(self):
        _l_(587173)

        bullet = _c_(587166, _a_(587157, _n_(587156, "bullets", lambda: bullets), "Bullet"), _a_(587160, _a_(587159, _n_(587158, "self", lambda: self), "rect"), "centerx") + 18, _a_(587163, _a_(587162, _n_(587161, "self", lambda: self), "rect"), "y") + 30, _a_(587165, _n_(587164, "self", lambda: self), "direction"))
        _l_(587167)
        _c_(587171, _a_(587169, _n_(587168, "bullet_group", lambda: bullet_group), "add"), _n_(587170, "bullet", lambda: bullet))
        _l_(587172)