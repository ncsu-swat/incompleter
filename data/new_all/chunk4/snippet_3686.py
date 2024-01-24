# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(591564)

except ImportError:
    pass
try:
    import car
    _l_(591566)

except ImportError:
    pass
try:
    import debris
    _l_(591568)

except ImportError:
    pass

_c_(591571, _a_(591570, _n_(591569, "pygame", lambda: pygame), "init"))
_l_(591572)

#screen settings
WIDTH = 1000
_l_(591573)
HEIGHT = 400
_l_(591574)

screen = _c_(591580, _a_(591577, _a_(591576, _n_(591575, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(591578, "WIDTH", lambda: WIDTH), _n_(591579, "HEIGHT", lambda: HEIGHT)))
_l_(591581)
_c_(591585, _a_(591584, _a_(591583, _n_(591582, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(591586)
_c_(591589, _a_(591588, _n_(591587, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(591590)

#fps
FPS = 120
_l_(591591)
clock = _c_(591595, _a_(591594, _a_(591593, _n_(591592, "pygame", lambda: pygame), "time"), "Clock"))
_l_(591596)

#load images
bg = _c_(591602, _a_(591601, _c_(591600, _a_(591599, _a_(591598, _n_(591597, "pygame", lambda: pygame), "image"), "load"), 'background/street.png'), "convert_alpha")) # background
_l_(591603) # background

#define game variables


######################CAR/DEBRIS##########################

player = _c_(591606, _a_(591605, _n_(591604, "car", lambda: car), "Player"), 1, 5)
_l_(591607)
debris = _c_(591610, _a_(591609, _n_(591608, "debris", lambda: debris), "Debris"), 1, 5)
_l_(591611)

##########################################################

#groups
bullet_group = _c_(591615, _a_(591614, _a_(591613, _n_(591612, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(591616)
debris_group = _c_(591620, _a_(591619, _a_(591618, _n_(591617, "pygame", lambda: pygame), "sprite"), "Group"))
_l_(591621)

_c_(591625, _a_(591623, _n_(591622, "debris_group", lambda: debris_group), "add"), _n_(591624, "debris", lambda: debris))
_l_(591626)

#game runs here
run = True
_l_(591627)
while _n_(591628, "run", lambda: run):
    _l_(591734)


    #draw street
    _c_(591632, _a_(591630, _n_(591629, "screen", lambda: screen), "blit"), _n_(591631, "bg", lambda: bg), [0, 0])
    _l_(591633)

    #update groups
    _c_(591636, _a_(591635, _n_(591634, "bullet_group", lambda: bullet_group), "update"))
    _l_(591637)
    _c_(591641, _a_(591639, _n_(591638, "bullet_group", lambda: bullet_group), "draw"), _n_(591640, "screen", lambda: screen))
    _l_(591642)

    #draw debris
    _c_(591645, _a_(591644, _n_(591643, "debris", lambda: debris), "draw"))
    _l_(591646)

    #draw car
    _c_(591649, _a_(591648, _n_(591647, "player", lambda: player), "draw"))
    _l_(591650)
    _c_(591653, _a_(591652, _n_(591651, "player", lambda: player), "move"))
    _l_(591654)

    for event in _c_(591658, _a_(591657, _a_(591656, _n_(591655, "pygame", lambda: pygame), "event"), "get")):
        _l_(591718)

        if _a_(591660, _n_(591659, "event", lambda: event), "type") == _a_(591662, _n_(591661, "pygame", lambda: pygame), "QUIT"):
            _l_(591664)

            run = False
            _l_(591663)

        #check if key is down
        if _a_(591666, _n_(591665, "event", lambda: event), "type") == _a_(591668, _n_(591667, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(591698)

            if _a_(591670, _n_(591669, "event", lambda: event), "key") == _a_(591672, _n_(591671, "pygame", lambda: pygame), "K_ESCAPE"):
                _l_(591674)

                run = False
                _l_(591673)
            if _a_(591676, _n_(591675, "event", lambda: event), "key") == _a_(591678, _n_(591677, "pygame", lambda: pygame), "K_a"):
                _l_(591681)

                _n_(591679, "player", lambda: player).movingLeft = True
                _l_(591680)
            if _a_(591683, _n_(591682, "event", lambda: event), "key") == _a_(591685, _n_(591684, "pygame", lambda: pygame), "K_d"):
                _l_(591688)

                _n_(591686, "player", lambda: player).movingRight = True
                _l_(591687)
            if _a_(591690, _n_(591689, "event", lambda: event), "key") == _a_(591692, _n_(591691, "pygame", lambda: pygame), "K_SPACE"):
                _l_(591697)

                _c_(591695, _a_(591694, _n_(591693, "player", lambda: player), "shoot"))
                _l_(591696)

        #check if key is up
        if _a_(591700, _n_(591699, "event", lambda: event), "type") == _a_(591702, _n_(591701, "pygame", lambda: pygame), "KEYUP"):
            _l_(591717)

            if _a_(591704, _n_(591703, "event", lambda: event), "key") == _a_(591706, _n_(591705, "pygame", lambda: pygame), "K_a"):
                _l_(591709)

                _n_(591707, "player", lambda: player).movingLeft = False
                _l_(591708)
            if _a_(591711, _n_(591710, "event", lambda: event), "key") == _a_(591713, _n_(591712, "pygame", lambda: pygame), "K_d"):
                _l_(591716)

                _n_(591714, "player", lambda: player).movingRight = False
                _l_(591715)

    #update the display
    _c_(591722, _a_(591721, _a_(591720, _n_(591719, "pygame", lambda: pygame), "display"), "update"))
    _l_(591723)
    _c_(591727, _a_(591726, _a_(591725, _n_(591724, "pygame", lambda: pygame), "display"), "flip"))
    _l_(591728)
    _c_(591732, _a_(591730, _n_(591729, "clock", lambda: clock), "tick"), _n_(591731, "FPS", lambda: FPS))
    _l_(591733)

_c_(591737, _a_(591736, _n_(591735, "pygame", lambda: pygame), "quit"))
_l_(591738)