# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74254584/typeerror-invalid-rect-assignment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(638579)

except ImportError:
    pass

# normal setup
_c_(638582, _a_(638581, _n_(638580, "pygame", lambda: pygame), "init"))
_l_(638583)
screen = _c_(638589, _a_(638586, _a_(638585, _n_(638584, "pygame", lambda: pygame), "display"), "set_mode"), (700, 700), _a_(638588, _n_(638587, "pygame", lambda: pygame), "RESIZABLE"))
_l_(638590)
_c_(638594, _a_(638593, _a_(638592, _n_(638591, "pygame", lambda: pygame), "display"), "set_caption"), 'ZAP!')
_l_(638595)
icon = _c_(638599, _a_(638598, _a_(638597, _n_(638596, "pygame", lambda: pygame), "image"), "load"), 'download.jpg')
_l_(638600)
_c_(638605, _a_(638603, _a_(638602, _n_(638601, "pygame", lambda: pygame), "display"), "set_icon"), _n_(638604, "icon", lambda: icon))
_l_(638606)
clock = _c_(638610, _a_(638609, _a_(638608, _n_(638607, "pygame", lambda: pygame), "time"), "Clock"))
_l_(638611)
running = True  # while loop running so after ending game i can still run
_l_(638612)  # while loop running so after ending game i can still run

# bg
bg = _c_(638616, _a_(638615, _a_(638614, _n_(638613, "pygame", lambda: pygame), "image"), "load"), 'ok_proper.jpg')
_l_(638617)
bg_pic = _c_(638622, _a_(638620, _a_(638619, _n_(638618, "pygame", lambda: pygame), "transform"), "scale"), _n_(638621, "bg", lambda: bg), (700, 700))
_l_(638623)


class Bullet(_a_(638626, _a_(638625, _n_(638624, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(638670)

    def __init__(self,pos):
        _l_(638669)

        _c_(638629, _a_(638628, _n_(638627, "super", lambda: super)(), "__init__"))
        _l_(638630)
        _n_(638631, "self", lambda: self).image = _c_(638643, _a_(638634, _a_(638633, _n_(638632, "pygame", lambda: pygame), "transform"), "rotate"), _c_(638642, _a_(638637, _a_(638636, _n_(638635, "pygame", lambda: pygame), "transform"), "scale"), _c_(638641, _a_(638640, _a_(638639, _n_(638638, "pygame", lambda: pygame), "image"), "load"), 'Graphics/yes.png'),(100,100)),90)
        _l_(638644)
        _n_(638645, "self", lambda: self).rect = _c_(638650, _a_(638648, _a_(638647, _n_(638646, "self", lambda: self), "image"), "get_rect"), topright = _n_(638649, "pos", lambda: (pos)))
        _l_(638651)
        _n_(638652, "self", lambda: self).speed = 10
        _l_(638653)
        _a_(638655, _n_(638654, "self", lambda: self), "rect").y -= _n_(638656, "self", lambda: self).speed
        _l_(638657)
        if _a_(638660, _a_(638659, _n_(638658, "self", lambda: self), "rect"), "y") < 0:
            _l_(638668)

            _n_(638661, "self", lambda: self).rect = _c_(638666, _a_(638664, _a_(638663, _n_(638662, "self", lambda: self), "image"), "get_rect"), topright= _n_(638665, "pos", lambda: (pos)))
            _l_(638667)




class Spaceship(_a_(638673, _a_(638672, _n_(638671, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(638797)

    def __init__(self):
        _l_(638704)

        _c_(638676, _a_(638675, _n_(638674, "super", lambda: super)(), "__init__"))
        _l_(638677)
        _n_(638678, "self", lambda: self).image = _c_(638682, _a_(638681, _a_(638680, _n_(638679, "pygame", lambda: pygame), "image"), "load"), 'Graphics/spaceship.png')
        _l_(638683)
        _n_(638684, "self", lambda: self).rect = _c_(638688, _a_(638687, _a_(638686, _n_(638685, "self", lambda: self), "image"), "get_rect"), bottomleft=(250, 700))
        _l_(638689)
        _n_(638690, "self", lambda: self).speed = 5
        _l_(638691)
        _n_(638692, "self", lambda: self).laser_time = 0
        _l_(638693)
        _n_(638694, "self", lambda: self).laser_cooldown = 600
        _l_(638695)
        _n_(638696, "self", lambda: self).ready = True
        _l_(638697)
        _n_(638698, "self", lambda: self).shoot = _c_(638702, _a_(638701, _a_(638700, _n_(638699, "pygame", lambda: pygame), "sprite"), "Group"))
        _l_(638703)

    def movement(self):
        _l_(638760)

        keys = _c_(638708, _a_(638707, _a_(638706, _n_(638705, "pygame", lambda: pygame), "key"), "get_pressed"))
        _l_(638709)
        if (_n_(638710, "keys", lambda: keys)[_a_(638712, _n_(638711, "pygame", lambda: pygame), "K_RIGHT")] or _n_(638713, "keys", lambda: keys)[_a_(638715, _n_(638714, "pygame", lambda: pygame), "K_d")]) and _a_(638718, _a_(638717, _n_(638716, "self", lambda: self), "rect"), "right") + _a_(638720, _n_(638719, "self", lambda: self), "speed") < 699:
            _l_(638759)

            _a_(638722, _n_(638721, "self", lambda: self), "rect").x += _n_(638723, "self", lambda: self).speed
            _l_(638724)
        elif (_n_(638725, "keys", lambda: keys)[_a_(638727, _n_(638726, "pygame", lambda: pygame), "K_LEFT")] or _n_(638728, "keys", lambda: keys)[_a_(638730, _n_(638729, "pygame", lambda: pygame), "K_a")]) and _a_(638733, _a_(638732, _n_(638731, "self", lambda: self), "rect"), "x") - _a_(638735, _n_(638734, "self", lambda: self), "speed") > 0:
            _l_(638758)

            _a_(638737, _n_(638736, "self", lambda: self), "rect").x -= _n_(638738, "self", lambda: self).speed
            _l_(638739)
        elif _n_(638740, "keys", lambda: keys)[_a_(638742, _n_(638741, "pygame", lambda: pygame), "K_SPACE")] and _a_(638744, _n_(638743, "self", lambda: self), "ready"):
            _l_(638757)

            _c_(638747, _a_(638746, _n_(638745, "self", lambda: self), "shootlaser"))
            _l_(638748)
            _n_(638749, "self", lambda: self).ready = False
            _l_(638750)
            _n_(638751, "self", lambda: self).laser_time = _c_(638755, _a_(638754, _a_(638753, _n_(638752, "pygame", lambda: pygame), "time"), "get_ticks"))
            _l_(638756)

    def shootlaser(self):
        _l_(638787)

        if not _a_(638762, _n_(638761, "self", lambda: self), "ready"):
            _l_(638786)

            timeoflaser = _c_(638766, _a_(638765, _a_(638764, _n_(638763, "pygame", lambda: pygame), "time"), "get_ticks"))
            _l_(638767)
            if _a_(638769, _n_(638768, "self", lambda: self), "laser_time") - _n_(638770, "timeoflaser", lambda: timeoflaser) == _a_(638772, _n_(638771, "self", lambda: self), "laser_cooldown"):
                _l_(638775)

                _n_(638773, "self", lambda: self).ready = True
                _l_(638774)
        else:
            _c_(638784, _a_(638778, _a_(638777, _n_(638776, "self", lambda: self), "shoot"), "add"), _c_(638783, _n_(638779, "Bullet", lambda: Bullet), _a_(638782, _a_(638781, _n_(638780, "self", lambda: self), "rect"), "topright")))
            _l_(638785)



    def update(self):
        _l_(638796)

        _c_(638790, _a_(638789, _n_(638788, "self", lambda: self), "movement"))
        _l_(638791)
        _c_(638794, _a_(638793, _n_(638792, "self", lambda: self), "shootlaser"))
        _l_(638795)

# spaceship
spaceship = _c_(638799, _n_(638798, "Spaceship", lambda: Spaceship))
_l_(638800)
# spaceship = pygame.sprite.GroupSingle()
# spaceship.add(Spaceship())

# bullet
bullet = _c_(638803, _n_(638801, "Bullet", lambda: Bullet), _n_(638802, "spaceship", lambda: spaceship))
_l_(638804)

while _n_(638805, "running", lambda: running):
    _l_(638851)

    _c_(638808, _a_(638807, _n_(638806, "clock", lambda: clock), "tick"), 60)
    _l_(638809)
    _c_(638813, _a_(638811, _n_(638810, "screen", lambda: screen), "blit"), _n_(638812, "bg_pic", lambda: bg_pic), (0, 0))  # background
    _l_(638814)  # background
    for event in _c_(638818, _a_(638817, _a_(638816, _n_(638815, "pygame", lambda: pygame), "event"), "get")):
        _l_(638825)

        if _a_(638820, _n_(638819, "event", lambda: event), "type") == _a_(638822, _n_(638821, "pygame", lambda: pygame), "QUIT"):
            _l_(638824)

            running = False
            _l_(638823)
    _c_(638832, _a_(638827, _n_(638826, "screen", lambda: screen), "blit"), _a_(638829, _n_(638828, "spaceship", lambda: spaceship), "image"),_a_(638831, _n_(638830, "spaceship", lambda: spaceship), "rect"))
    _l_(638833)
    _c_(638840, _a_(638835, _n_(638834, "screen", lambda: screen), "blit"), _a_(638837, _n_(638836, "bullet", lambda: bullet), "image"),_a_(638839, _n_(638838, "bullet", lambda: bullet), "rect"))
    _l_(638841)
    _c_(638844, _a_(638843, _n_(638842, "spaceship", lambda: spaceship), "update"))
    _l_(638845)
    # spaceship.draw(screen)
    _c_(638849, _a_(638848, _a_(638847, _n_(638846, "pygame", lambda: pygame), "display"), "update"))
    _l_(638850)