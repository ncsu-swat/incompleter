# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(596680)

except ImportError:
    pass

#screen settings
WIDTH = 1000
_l_(596681)
HEIGHT = 400
_l_(596682)

screen = _c_(596688, _a_(596685, _a_(596684, _n_(596683, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(596686, "WIDTH", lambda: WIDTH), _n_(596687, "HEIGHT", lambda: HEIGHT)))
_l_(596689)
_c_(596693, _a_(596692, _a_(596691, _n_(596690, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(596694)
_c_(596697, _a_(596696, _n_(596695, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(596698)

#load bullets
bullets = _c_(596704, _a_(596703, _c_(596702, _a_(596701, _a_(596700, _n_(596699, "pygame", lambda: pygame), "image"), "load"), 'car/bullet.png'), "convert_alpha"))
_l_(596705)

#groups
bullet_group = _c_(596709, _a_(596708, _a_(596707, _n_(596706, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(596710)

#player class
class Player(_a_(596713, _a_(596712, _n_(596711, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(596858)

    def __init__(self, scale, speed):
        _l_(596791)

        _c_(596719, _a_(596717, _a_(596716, _a_(596715, _n_(596714, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(596718, "self", lambda: self))
        _l_(596720)

        _n_(596721, "self", lambda: self).speed = _n_(596722, "speed", lambda: speed)
        _l_(596723)
        #self.x = x
        #self.y = y
        _n_(596724, "self", lambda: self).moving = True
        _l_(596725)
        _n_(596726, "self", lambda: self).frame = 0
        _l_(596727)
        _n_(596728, "self", lambda: self).flip = False
        _l_(596729)
        _n_(596730, "self", lambda: self).direction = 0
        _l_(596731)

        #load car
        _n_(596732, "self", lambda: self).images = []
        _l_(596733)
        img = _c_(596739, _a_(596738, _c_(596737, _a_(596736, _a_(596735, _n_(596734, "pygame", lambda: pygame), "image"), "load"), 'car/car.png'), "convert_alpha"))
        _l_(596740)
        img = _c_(596757, _a_(596743, _a_(596742, _n_(596741, "pygame", lambda: pygame), "transform"), "scale"), _n_(596744, "img", lambda: img), (_c_(596749, _n_(596745, "int", lambda: int), _c_(596748, _a_(596747, _n_(596746, "img", lambda: img), "get_width"))) * _n_(596750, "scale", lambda: scale), (_c_(596755, _n_(596751, "int", lambda: int), _c_(596754, _a_(596753, _n_(596752, "img", lambda: img), "get_height"))) * _n_(596756, "scale", lambda: scale))))
        _l_(596758)
        _c_(596763, _a_(596761, _a_(596760, _n_(596759, "self", lambda: self), "images"), "append"), _n_(596762, "img", lambda: img))
        _l_(596764)
        _n_(596765, "self", lambda: self).image = _a_(596767, _n_(596766, "self", lambda: self), "images")[0]
        _l_(596768)
        _n_(596769, "self", lambda: self).rect = _c_(596773, _a_(596772, _a_(596771, _n_(596770, "self", lambda: self), "image"), "get_rect"))
        _l_(596774)
        _n_(596775, "self", lambda: self).update_time = _c_(596779, _a_(596778, _a_(596777, _n_(596776, "pygame", lambda: pygame), "time"), "get_ticks"))
        _l_(596780)
        _n_(596781, "self", lambda: self).movingLeft = False
        _l_(596782)
        _n_(596783, "self", lambda: self).movingRight = False
        _l_(596784)
        _a_(596786, _n_(596785, "self", lambda: self), "rect").x = 465
        _l_(596787)
        _a_(596789, _n_(596788, "self", lambda: self), "rect").y = 325
        _l_(596790)

    #draw car to screen
    def draw(self):
        _l_(596804)

        _c_(596802, _a_(596793, _n_(596792, "screen", lambda: screen), "blit"), _a_(596795, _n_(596794, "self", lambda: self), "image"), (_a_(596798, _a_(596797, _n_(596796, "self", lambda: self), "rect"), "centerx"), _a_(596801, _a_(596800, _n_(596799, "self", lambda: self), "rect"), "centery")))
        _l_(596803)

    #move car
    def move(self):
        _l_(596839)

        #reset the movement variables
        dx = 0
        _l_(596805)
        dy = 0
        _l_(596806)

        #moving variables
        if _a_(596808, _n_(596807, "self", lambda: self), "movingLeft") and _a_(596811, _a_(596810, _n_(596809, "self", lambda: self), "rect"), "x") > 33:
            _l_(596818)

            dx -= _n_(596812, "self", lambda: self).speed
            _l_(596813)
            _n_(596814, "self", lambda: self).flip = True
            _l_(596815)
            _n_(596816, "self", lambda: self).direction = -1
            _l_(596817)
        if _a_(596820, _n_(596819, "self", lambda: self), "movingRight") and _a_(596823, _a_(596822, _n_(596821, "self", lambda: self), "rect"), "x") < 900:
            _l_(596830)

            dx += _n_(596824, "self", lambda: self).speed
            _l_(596825)
            _n_(596826, "self", lambda: self).flip = False
            _l_(596827)
            _n_(596828, "self", lambda: self).direction = 1
            _l_(596829)

        #update rectangle position
        _a_(596832, _n_(596831, "self", lambda: self), "rect").x += _n_(596833, "dx", lambda: dx)
        _l_(596834)
        _a_(596836, _n_(596835, "self", lambda: self), "rect").y += _n_(596837, "dy", lambda: dy)
        _l_(596838)

    #shoot
    def shoot(self):
        _l_(596857)

        bullet = _c_(596850, _a_(596841, _n_(596840, "bullets", lambda: bullets), "Bullet"), _a_(596844, _a_(596843, _n_(596842, "self", lambda: self), "rect"), "centerx") + 18, _a_(596847, _a_(596846, _n_(596845, "self", lambda: self), "rect"), "y") + 30, _a_(596849, _n_(596848, "self", lambda: self), "direction"))
        _l_(596851)
        _c_(596855, _a_(596853, _n_(596852, "bullet_group", lambda: bullet_group), "add"), _n_(596854, "bullet", lambda: bullet))
        _l_(596856)