# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33182865/pygame-help-typeerror-add-argument-after-must-be-a-sequence-not-pygame-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(662662)

except ImportError:
    pass

class Player(_a_(662665, _a_(662664, _n_(662663, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(662744)

    def __init__(self, *groups):
        _l_(662689)

        _c_(662671, _a_(662669, _n_(662666, "super", lambda: super)(_n_(662667, "Player", lambda: Player), _n_(662668, "self", lambda: self)), "__init__"), *_n_(662670, "groups", lambda: groups))
        _l_(662672)
        _n_(662673, "self", lambda: self).image = _c_(662677, _a_(662676, _a_(662675, _n_(662674, "pygame", lambda: pygame), "image"), "load"), 'Mugger Space Cadet.jpg')
        _l_(662678)
        _n_(662679, "self", lambda: self).rect = _c_(662687, _a_(662682, _a_(662681, _n_(662680, "pygame", lambda: pygame), "rect"), "Rect"), (16, 32), _c_(662686, _a_(662685, _a_(662684, _n_(662683, "self", lambda: self), "image"), "get_size")))
        _l_(662688)

    def update(self, dt, game):
        _l_(662743)

        last = _c_(662693, _a_(662692, _a_(662691, _n_(662690, "self", lambda: self), "rect"), "copy"))
        _l_(662694)

        key = _c_(662698, _a_(662697, _a_(662696, _n_(662695, "pygame", lambda: pygame), "key"), "get_pressed"))
        _l_(662699)
        if _n_(662700, "key", lambda: key)[_a_(662702, _n_(662701, "pygame", lambda: pygame), "K_LEFT")]:
            _l_(662707)

            _a_(662704, _n_(662703, "self", lambda: self), "rect").x -= 150 * _n_(662705, "dt", lambda: dt)
            _l_(662706)
        if _n_(662708, "key", lambda: key)[_a_(662710, _n_(662709, "pygame", lambda: pygame), "K_RIGHT")]:
            _l_(662715)

            _a_(662712, _n_(662711, "self", lambda: self), "rect").x += 150 * _n_(662713, "dt", lambda: dt)
            _l_(662714)
        if _n_(662716, "key", lambda: key)[_a_(662718, _n_(662717, "pygame", lambda: pygame), "K_UP")]:
            _l_(662723)

            _a_(662720, _n_(662719, "self", lambda: self), "rect").y -= 150 * _n_(662721, "dt", lambda: dt)
            _l_(662722)
        if _n_(662724, "key", lambda: key)[_a_(662726, _n_(662725, "pygame", lambda: pygame), "K_DOWN")]:
            _l_(662731)

            _a_(662728, _n_(662727, "self", lambda: self), "rect").y += 150 * _n_(662729, "dt", lambda: dt)
            _l_(662730)

        for cell in _c_(662738, _a_(662734, _a_(662733, _n_(662732, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(662735, "self", lambda: self), _a_(662737, _n_(662736, "game", lambda: game), "walls"), False):
            _l_(662742)

            _n_(662739, "self", lambda: self).rect = _n_(662740, "last", lambda: last)
            _l_(662741)

class Game(_n_(662745, "object", lambda: object)):
    _l_(662861)

    def main(self, screen):
        _l_(662860)


        clock = _c_(662749, _a_(662748, _a_(662747, _n_(662746, "pygame", lambda: pygame), "time"), "Clock"))
        _l_(662750)

        background = _c_(662754, _a_(662753, _a_(662752, _n_(662751, "pygame", lambda: pygame), "image"), "load"), 'mockup level.png')
        _l_(662755)
        sprites = _c_(662759, _a_(662758, _a_(662757, _n_(662756, "pygame", lambda: pygame), "sprite"), "Group"))
        _l_(662760)
#       sprites.add(background)
        _n_(662761, "self", lambda: self).player = _c_(662764, _n_(662762, "Player", lambda: Player), _n_(662763, "sprites", lambda: sprites))
        _l_(662765)
        _n_(662766, "self", lambda: self).walls = _c_(662770, _a_(662769, _a_(662768, _n_(662767, "pygame", lambda: pygame), "sprite"), "Group"))
        _l_(662771)
        block = _c_(662775, _a_(662774, _a_(662773, _n_(662772, "pygame", lambda: pygame), "image"), "load"), 'block.png')
        _l_(662776)
        for x in _c_(662778, _n_(662777, "range", lambda: range), 0, 448, 32):
            _l_(662806)

            for y in _c_(662780, _n_(662779, "range", lambda: range), 0, 320, 32):
                _l_(662805)

                if _n_(662781, "x", lambda: x) in (0, 448-32) or _n_(662782, "y", lambda: y) in (0, 320-32):
                    _l_(662804)

                    wall = _c_(662788, _a_(662785, _a_(662784, _n_(662783, "pygame", lambda: pygame), "sprite"), "Sprite"), _a_(662787, _n_(662786, "self", lambda: self), "walls"))
                    _l_(662789)
                    _n_(662790, "wall", lambda: wall).image = _n_(662791, "block", lambda: block)
                    _l_(662792)
                    _n_(662793, "wall", lambda: wall).rect= _c_(662802, _a_(662796, _a_(662795, _n_(662794, "pygame", lambda: pygame), "rect"), "Rect"), (_n_(662797, "x", lambda: x), _n_(662798, "y", lambda: y)), _c_(662801, _a_(662800, _n_(662799, "block", lambda: block), "get_size")))
                    _l_(662803)
        _c_(662811, _a_(662808, _n_(662807, "sprites", lambda: sprites), "add"), _a_(662810, _n_(662809, "self", lambda: self), "walls"))
        _l_(662812)

        while True:
            _l_(662859)

            dt = _c_(662815, _a_(662814, _n_(662813, "clock", lambda: clock), "tick"), 30)
            _l_(662816)

            for event in _c_(662820, _a_(662819, _a_(662818, _n_(662817, "pygame", lambda: pygame), "event"), "get")):
                _l_(662837)

                if _a_(662822, _n_(662821, "event", lambda: event), "type") == _a_(662824, _n_(662823, "pygame", lambda: pygame), "QUIT"):
                    _l_(662826)

                    aux = ""
                    _l_(662825)
                    return aux
                if _a_(662828, _n_(662827, "event", lambda: event), "type") == _a_(662830, _n_(662829, "pygame", lambda: pygame), "KEYDOWN") and _a_(662832, _n_(662831, "event", lambda: event), "key") == _a_(662834, _n_(662833, "pygame", lambda: pygame), "K_ESCAPE"):
                    _l_(662836)

                    aux = ""
                    _l_(662835)
                    return aux

            _c_(662842, _a_(662839, _n_(662838, "sprites", lambda: sprites), "update"), _n_(662840, "dt", lambda: dt) / 1000., _n_(662841, "self", lambda: self))
            _l_(662843)
            _c_(662847, _a_(662845, _n_(662844, "screen", lambda: screen), "blit"), _n_(662846, "background", lambda: background), (0, 0))
            _l_(662848)
            _c_(662852, _a_(662850, _n_(662849, "sprites", lambda: sprites), "draw"), _n_(662851, "screen", lambda: screen))
            _l_(662853)
            _c_(662857, _a_(662856, _a_(662855, _n_(662854, "pygame", lambda: pygame), "display"), "flip"))
            _l_(662858)


if _n_(662862, "__name__", lambda: __name__) == '__main__':
    _l_(662878)

    _c_(662865, _a_(662864, _n_(662863, "pygame", lambda: pygame), "init"))
    _l_(662866)
    screen = _c_(662870, _a_(662869, _a_(662868, _n_(662867, "pygame", lambda: pygame), "display"), "set_mode"), (448, 320))
    _l_(662871)
    _c_(662876, _a_(662874, _c_(662873, _n_(662872, "Game", lambda: Game)), "main"), _n_(662875, "screen", lambda: screen))
    _l_(662877)