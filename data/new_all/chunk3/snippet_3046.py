# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51731348/how-to-access-attributes-of-the-groups-object-attributeerror-group-object-h
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(551526)

except ImportError:
    pass

class GeoFence(_a_(551529, _a_(551528, _n_(551527, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(551563)

    def __init__(self, rect, risk_level, *groups):
        _l_(551562)

        # we set a _layer attribute before adding this sprite to the sprite groups
        _n_(551530, "self", lambda: self)._layer = 1
        _l_(551531)
        _c_(551538, _a_(551535, _a_(551534, _a_(551533, _n_(551532, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(551536, "self", lambda: self), _n_(551537, "groups", lambda: groups))
        _l_(551539)
        _n_(551540, "self", lambda: self).image = _c_(551548, _a_(551543, _a_(551542, _n_(551541, "pygame", lambda: pygame), "surface"), "Surface"), (_a_(551545, _n_(551544, "rect", lambda: rect), "width"), _a_(551547, _n_(551546, "rect", lambda: rect), "height")))
        _l_(551549)
        _c_(551554, _a_(551552, _a_(551551, _n_(551550, "self", lambda: self), "image"), "fill"), _n_(551553, "GREEN", lambda: GREEN))
        _l_(551555)
        _n_(551556, "self", lambda: self).rect = _n_(551557, "rect", lambda: rect)
        _l_(551558)
        _n_(551559, "self", lambda: self).risk_level = _n_(551560, "risk_level", lambda: risk_level)
        _l_(551561)


class Worker(_a_(551566, _a_(551565, _n_(551564, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(551747)


    # we introduce to possible states: RUNNING and IDLE
    RUNNING = 0
    _l_(551567)
    IDLE = 1
    _l_(551568)
    NUMBER_OF_ACCIDENTS = 0
    _l_(551569)

    def __init__(self, image_running, image_idle, location, *groups):
        _l_(551634)


        # each state has it's own image
        _n_(551570, "self", lambda: self).images = {
            _a_(551572, _n_(551571, "Worker", lambda: Worker), "RUNNING"): _c_(551579, _a_(551575, _a_(551574, _n_(551573, "pygame", lambda: pygame), "transform"), "scale"), _c_(551578, _n_(551576, "get_image", lambda: get_image), _n_(551577, "image_running", lambda: image_running)), (45, 45)),
            _a_(551581, _n_(551580, "Worker", lambda: Worker), "IDLE"): _c_(551588, _a_(551584, _a_(551583, _n_(551582, "pygame", lambda: pygame), "transform"), "scale"), _c_(551587, _n_(551585, "get_image", lambda: get_image), _n_(551586, "image_idle", lambda: image_idle)), (20, 45))
        }
        _l_(551589)

        # we set a _layer attribute before adding this sprite to the sprite groups
        # we want the workers on top
        _n_(551590, "self", lambda: self)._layer = 2
        _l_(551591)
        _c_(551598, _a_(551595, _a_(551594, _a_(551593, _n_(551592, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(551596, "self", lambda: self), _n_(551597, "groups", lambda: groups))
        _l_(551599)

        # let's keep track of the state and how long we are in this state already            
        _n_(551600, "self", lambda: self).state = _a_(551602, _n_(551601, "Worker", lambda: Worker), "IDLE")
        _l_(551603)
        _n_(551604, "self", lambda: self).ticks_in_state = 0
        _l_(551605)

        _n_(551606, "self", lambda: self).image = _a_(551608, _n_(551607, "self", lambda: self), "images")[_a_(551610, _n_(551609, "self", lambda: self), "state")]
        _l_(551611)
        _n_(551612, "self", lambda: self).rect = _c_(551617, _a_(551615, _a_(551614, _n_(551613, "self", lambda: self), "image"), "get_rect"), topleft=_n_(551616, "location", lambda: location))
        _l_(551618)

        _n_(551619, "self", lambda: self).direction = _c_(551623, _a_(551622, _a_(551621, _n_(551620, "pygame", lambda: pygame), "math"), "Vector2"), 0, 0)
        _l_(551624)
        _n_(551625, "self", lambda: self).speed = _c_(551628, _a_(551627, _n_(551626, "random", lambda: random), "randint"), 1, 3)
        _l_(551629)
        _c_(551632, _a_(551631, _n_(551630, "self", lambda: self), "set_random_direction"))
        _l_(551633)


    def set_random_direction(self):
        _l_(551702)

        # random new direction or standing still
        vec = _c_(551644, _a_(551637, _a_(551636, _n_(551635, "pygame", lambda: pygame), "math"), "Vector2"), _c_(551640, _a_(551639, _n_(551638, "random", lambda: random), "randint"), -100,100), _c_(551643, _a_(551642, _n_(551641, "random", lambda: random), "randint"), -100,100)) if _c_(551647, _a_(551646, _n_(551645, "random", lambda: random), "randint"), 0, 5) > 1 else _c_(551651, _a_(551650, _a_(551649, _n_(551648, "pygame", lambda: pygame), "math"), "Vector2"), 0, 0)
        _l_(551652)

        # check the new vector and decide if we are running or fooling around
        length = _c_(551655, _a_(551654, _n_(551653, "vec", lambda: vec), "length"))
        _l_(551656)
        speed = _c_(551668, _n_(551657, "sum", lambda: sum), (_c_(551662, _n_(551658, "abs", lambda: abs), _c_(551661, _n_(551659, "int", lambda: int), _n_(551660, "v", lambda: v))) for v in _c_(551665, _a_(551664, _n_(551663, "vec", lambda: vec), "normalize")) * _a_(551667, _n_(551666, "self", lambda: self), "speed"))) if _n_(551669, "length", lambda: length) > 0 else 0
        _l_(551670)

        if _n_(551671, "length", lambda: length) == 0 or _n_(551672, "speed", lambda: speed) == 0:
            _l_(551690)

            new_state = _a_(551674, _n_(551673, "Worker", lambda: Worker), "IDLE")
            _l_(551675)
            _n_(551676, "self", lambda: self).direction = _c_(551680, _a_(551679, _a_(551678, _n_(551677, "pygame", lambda: pygame), "math"), "Vector2"), 0, 0)
            _l_(551681)
        else:
            new_state = _a_(551683, _n_(551682, "Worker", lambda: Worker), "RUNNING")
            _l_(551684)
            _n_(551685, "self", lambda: self).direction = _c_(551688, _a_(551687, _n_(551686, "vec", lambda: vec), "normalize"))
            _l_(551689)

        _n_(551691, "self", lambda: self).ticks_in_state = 0
        _l_(551692)
        _n_(551693, "self", lambda: self).state = _n_(551694, "new_state", lambda: new_state)
        _l_(551695)

        # use the right image for the current state
        _n_(551696, "self", lambda: self).image = _a_(551698, _n_(551697, "self", lambda: self), "images")[_a_(551700, _n_(551699, "self", lambda: self), "state")]
        _l_(551701)


    def update(self, screen):
        _l_(551746)

        _n_(551703, "self", lambda: self).ticks_in_state += 1
        _l_(551704)
        # the longer we are in a certain state, the more likely is we change direction
        if _c_(551709, _a_(551706, _n_(551705, "random", lambda: random), "randint"), 0, _a_(551708, _n_(551707, "self", lambda: self), "ticks_in_state")) > 70:
            _l_(551714)

            _c_(551712, _a_(551711, _n_(551710, "self", lambda: self), "set_random_direction"))
            _l_(551713)

        # now let's multiply our direction with our speed and move the rect
        vec = [_c_(551717, _n_(551715, "int", lambda: int), _n_(551716, "v", lambda: v)) for v in _a_(551719, _n_(551718, "self", lambda: self), "direction") * _a_(551721, _n_(551720, "self", lambda: self), "speed")]
        _l_(551722)
        _c_(551727, _a_(551725, _a_(551724, _n_(551723, "self", lambda: self), "rect"), "move_ip"), *_n_(551726, "vec", lambda: vec))
        _l_(551728)

        if _c_(551739, _n_(551729, "any", lambda: any), (_n_(551730, "s", lambda: s) for s in _c_(551736, _a_(551733, _a_(551732, _n_(551731, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(551734, "self", lambda: self), _n_(551735, "fences", lambda: fences), False) if _n_(551737, "s", lambda: s) != _n_(551738, "self", lambda: self))):
            _l_(551745)

            _c_(551743, _n_(551740, "print", lambda: print), "RISK_LEVEL: ",_a_(551742, _n_(551741, "fences", lambda: fences), "risk_level"))
            _l_(551744)


all_sprites = _c_(551751, _a_(551750, _a_(551749, _n_(551748, "pygame", lambda: pygame), "sprite"), "LayeredUpdates"))
_l_(551752)
workers = _c_(551756, _a_(551755, _a_(551754, _n_(551753, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(551757)
fences = _c_(551761, _a_(551760, _a_(551759, _n_(551758, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(551762)

screen = _c_(551768, _a_(551765, _a_(551764, _n_(551763, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(551766, "SCREENWIDTH", lambda: SCREENWIDTH), _n_(551767, "SCREENHEIGHT", lambda: SCREENHEIGHT)))
_l_(551769)
_c_(551773, _a_(551772, _a_(551771, _n_(551770, "pygame", lambda: pygame), "display"), "set_caption"), "TEST")
_l_(551774)

# create multiple workers
for pos in ((30,30), (50, 400), (200, 100), (700, 200)):
    _l_(551782)

    _c_(551780, _n_(551775, "Worker", lambda: Worker), "w1.png", "w2.png", _n_(551776, "pos", lambda: pos), _n_(551777, "all_sprites", lambda: all_sprites), _n_(551778, "workers", lambda: workers), _n_(551779, "fences", lambda: fences))
    _l_(551781)

# create multiple geo-fences
risks = ["HIGH","MEDIUM","LOW"]
_l_(551783)
for rect in (_c_(551786, _a_(551785, _n_(551784, "pygame", lambda: pygame), "Rect"), 510,150,75,52), _c_(551789, _a_(551788, _n_(551787, "pygame", lambda: pygame), "Rect"), 450,250,68,40), _c_(551792, _a_(551791, _n_(551790, "pygame", lambda: pygame), "Rect"), 450,370,68,48)):
    _l_(551805)

    risk = _n_(551793, "risks", lambda: risks)[_c_(551796, _a_(551795, _n_(551794, "random", lambda: random), "randint"), 0,2)]
    _l_(551797)
    _c_(551803, _n_(551798, "GeoFence", lambda: GeoFence), _n_(551799, "rect", lambda: rect), _n_(551800, "risk", lambda: risk), _n_(551801, "all_sprites", lambda: all_sprites), _n_(551802, "fences", lambda: fences))
    _l_(551804)