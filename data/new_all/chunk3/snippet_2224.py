# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57099307/attributeerror-type-object-projectile-has-no-attribute-dir
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class player():
    _l_(573629)

    x = WIDTH / 2
    _l_(573609)
    y = HEIGHT / 2
    _l_(573610)
    width = 50
    _l_(573611)
    height = 50
    _l_(573612)
    speed = 1
    _l_(573613)

    def draw(self):
        _l_(573628)

        _c_(573626, _a_(573616, _a_(573615, _n_(573614, "pygame", lambda: pygame), "draw"), "rect"), _n_(573617, "win", lambda: win), (0, 0, 255), (_a_(573619, _n_(573618, "self", lambda: self), "x"), _a_(573621, _n_(573620, "self", lambda: self), "y"), _a_(573623, _n_(573622, "self", lambda: self), "width"), _a_(573625, _n_(573624, "self", lambda: self), "height")))
        _l_(573627)

class projectile():
    _l_(573690)


    radius = 10
    _l_(573630)
    speed = 8
    _l_(573631)

    def __init__(self, x, y, dir={}):
        _l_(573641)

        _n_(573632, "self", lambda: self).x = _n_(573633, "x", lambda: x)
        _l_(573634)
        _n_(573635, "self", lambda: self).y = _n_(573636, "y", lambda: y)
        _l_(573637)
        _n_(573638, "self", lambda: self).dir = _n_(573639, "dir", lambda: dir)
        _l_(573640)

    def shot(self):
        _l_(573676)

        for bullet in _n_(573642, "bullets", lambda: bullets):
            _l_(573675)

            if _a_(573644, _n_(573643, "self", lambda: self), "dir") == 'N':
                _l_(573650)

                _c_(573646, _n_(573645, "print", lambda: print), 'N')
                _l_(573647)
                _n_(573648, "self", lambda: self).y -= 1
                _l_(573649)
            if _a_(573652, _n_(573651, "self", lambda: self), "dir") == 'W':
                _l_(573658)

                _c_(573654, _n_(573653, "print", lambda: print), 'W')
                _l_(573655)
                _n_(573656, "self", lambda: self).x -= 1
                _l_(573657)
            if _a_(573660, _n_(573659, "self", lambda: self), "dir") == 'S':
                _l_(573666)

                _c_(573662, _n_(573661, "print", lambda: print), 'S')
                _l_(573663)
                _n_(573664, "self", lambda: self).y += 1
                _l_(573665)
            if _a_(573668, _n_(573667, "self", lambda: self), "dir") == 'E':
                _l_(573674)

                _c_(573670, _n_(573669, "print", lambda: print), 'E')
                _l_(573671)
                _n_(573672, "self", lambda: self).x += 1
                _l_(573673)

    def draw(self):
        _l_(573689)

        _c_(573687, _a_(573679, _a_(573678, _n_(573677, "pygame", lambda: pygame), "draw"), "circle"), _n_(573680, "win", lambda: win), (255, 0, 0), (_a_(573682, _n_(573681, "self", lambda: self), "x"), _a_(573684, _n_(573683, "self", lambda: self), "y")), _a_(573686, _n_(573685, "self", lambda: self), "radius"))
        _l_(573688)


def get_input():
    _l_(573767)

    keys = _c_(573694, _a_(573693, _a_(573692, _n_(573691, "pygame", lambda: pygame), "key"), "get_pressed"))
    _l_(573695)
    ev = _c_(573699, _a_(573698, _a_(573697, _n_(573696, "pygame", lambda: pygame), "event"), "get"))
    _l_(573700)

    if _n_(573701, "keys", lambda: keys)[_a_(573703, _n_(573702, "pygame", lambda: pygame), "K_w")]:
        _l_(573710)

        _n_(573704, "player", lambda: player).y -= _n_(573705, "player", lambda: player).speed
        _l_(573706)
        _a_(573708, _n_(573707, "projectile", lambda: projectile), "dir") == 'N'
        _l_(573709)
    if _n_(573711, "keys", lambda: keys)[_a_(573713, _n_(573712, "pygame", lambda: pygame), "K_a")]:
        _l_(573720)

        _n_(573714, "player", lambda: player).x -= _n_(573715, "player", lambda: player).speed
        _l_(573716)
        _a_(573718, _n_(573717, "projectile", lambda: projectile), "dir") == 'W'
        _l_(573719)
    if _n_(573721, "keys", lambda: keys)[_a_(573723, _n_(573722, "pygame", lambda: pygame), "K_s")]:
        _l_(573730)

        _n_(573724, "player", lambda: player).y += _n_(573725, "player", lambda: player).speed
        _l_(573726)
        _a_(573728, _n_(573727, "projectile", lambda: projectile), "dir") == 'S'
        _l_(573729)
    if _n_(573731, "keys", lambda: keys)[_a_(573733, _n_(573732, "pygame", lambda: pygame), "K_d")]:
        _l_(573740)

        _n_(573734, "player", lambda: player).x += _n_(573735, "player", lambda: player).speed
        _l_(573736)
        _a_(573738, _n_(573737, "projectile", lambda: projectile), "dir") == 'E'
        _l_(573739)
    for event in _n_(573741, "ev", lambda: ev):
        _l_(573766)

        if _a_(573743, _n_(573742, "event", lambda: event), "type") == _a_(573745, _n_(573744, "pygame", lambda: pygame), "MOUSEBUTTONDOWN"):
            _l_(573765)

            _c_(573763, _a_(573747, _n_(573746, "bullets", lambda: bullets), "append"), _c_(573762, _n_(573748, "projectile", lambda: projectile), _c_(573754, _n_(573749, "round", lambda: round), _a_(573751, _n_(573750, "player", lambda: player), "x") + _a_(573753, _n_(573752, "player", lambda: player), "width")//2), _c_(573760, _n_(573755, "round", lambda: round), _a_(573757, _n_(573756, "player", lambda: player), "y") + _a_(573759, _n_(573758, "player", lambda: player), "height")//2), _n_(573761, "dir", lambda: dir)))
            _l_(573764)


def update():
    _l_(573798)

    _c_(573770, _a_(573769, _n_(573768, "clock", lambda: clock), "tick"), 300)
    _l_(573771)
    _c_(573774, _a_(573773, _n_(573772, "win", lambda: win), "fill"), (0, 0, 0))
    _l_(573775)
    _c_(573777, _n_(573776, "get_input", lambda: get_input))
    _l_(573778)
    _c_(573781, _a_(573780, _n_(573779, "player", lambda: player), "draw"))
    _l_(573782)
    for bullet in _n_(573783, "bullets", lambda: bullets):
        _l_(573792)

        _c_(573786, _a_(573785, _n_(573784, "bullet", lambda: bullet), "draw"))
        _l_(573787)
        _c_(573790, _a_(573789, _n_(573788, "bullet", lambda: bullet), "shot"))
        _l_(573791)
    _c_(573796, _a_(573795, _a_(573794, _n_(573793, "pygame", lambda: pygame), "display"), "update"))
    _l_(573797)


running = True
_l_(573799)
player = _c_(573801, _n_(573800, "player", lambda: player))
_l_(573802)
bullets = []
_l_(573803)

while _n_(573804, "running", lambda: running):
    _l_(573819)

    for event in _c_(573808, _a_(573807, _a_(573806, _n_(573805, "pygame", lambda: pygame), "event"), "get")):
        _l_(573815)

        if _a_(573810, _n_(573809, "event", lambda: event), "type") == _a_(573812, _n_(573811, "pygame", lambda: pygame), "QUIT"):
            _l_(573814)

            running = False
            _l_(573813)

    _c_(573817, _n_(573816, "update", lambda: update))
    _l_(573818)

#pygame.quit()