# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43940194/kivy-typeerror-on-keyboard-down-takes-2-positional-arguments-but-5-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PlayerImage(_n_(432689, "Image", lambda: Image)):
    _l_(432774)

    angle = _c_(432690, NumericProperty, 0)
    _l_(432691)

    def __init__(self,**kwargs):
        _l_(432728)

        _c_(432697, _a_(432695, _n_(432692, "super", lambda: super)(_n_(432693, "PlayerImage", lambda: PlayerImage), _n_(432694, "self", lambda: self)), "__init__"), **_n_(432696, "kwargs", lambda: kwargs))
        _l_(432698)
        _n_(432699, "self", lambda: self).states = {"personred/rest.png/": 0,
                       "person.zip/": 1}
        _l_(432700)
        _n_(432701, "self", lambda: self).currentstate = _a_(432703, _n_(432702, "self", lambda: self), "states")["personred/rest.png/"]
        _l_(432704)

        _n_(432705, "self", lambda: self).art = "./rpgArt/" + _c_(432709, _n_(432706, "str", lambda: str), _a_(432708, _n_(432707, "self", lambda: self), "currentstate"))
        _l_(432710)
        _n_(432711, "self", lambda: self)._keyboard = _c_(432715, _a_(432713, _n_(432712, "Window", lambda: Window), "request_keyboard"), _n_(432714, "self", lambda: self),None)
        _l_(432716)
        if not _a_(432718, _n_(432717, "self", lambda: self), "_keyboard"):
            _l_(432720)

            aux = ""
            _l_(432719)
            return aux
        _c_(432726, _a_(432723, _a_(432722, _n_(432721, "self", lambda: self), "_keyboard"), "bind"), on_key_down=_a_(432725, _n_(432724, "self", lambda: self), "on_keyboard_down"))
        _l_(432727)


    def on_keyboard_down(self, keycode):
        _l_(432737)

        if _n_(432729, "keycode", lambda: keycode)[1] == "right":
            _l_(432732)

            _n_(432730, "self", lambda: self).x += 10
            _l_(432731)
        if _n_(432733, "keycode", lambda: keycode)[1] == "left":
            _l_(432736)

            _n_(432734, "self", lambda: self).x -= 10
            _l_(432735)


    def on_touch_down(self, touch):
        _l_(432773)

        _n_(432738, "self", lambda: self).currentstate = _a_(432740, _n_(432739, "self", lambda: self), "states")["person.zip/"]
        _l_(432741)
        _c_(432745, _a_(432743, _n_(432742, "Animation", lambda: Animation), "cancel_all"), _n_(432744, "self", lambda: self))
        _l_(432746)
        angle = _c_(432758, _n_(432747, "degrees", lambda: degrees), _c_(432757, _n_(432748, "atan2", lambda: atan2), _a_(432750, _n_(432749, "touch", lambda: touch), "y") - _a_(432752, _n_(432751, "self", lambda: self), "center_y"),
                              _a_(432754, _n_(432753, "touch", lambda: touch), "x") - _a_(432756, _n_(432755, "self", lambda: self), "center_x")))
        _l_(432759)

        _c_(432767, _a_(432765, _c_(432764, _n_(432760, "Animation", lambda: Animation), center=_a_(432762, _n_(432761, "touch", lambda: touch), "pos"), angle=_n_(432763, "angle", lambda: angle)), "start"), _n_(432766, "self", lambda: self))
        _l_(432768)
        _n_(432769, "self", lambda: self).currentstate = _a_(432771, _n_(432770, "self", lambda: self), "states")["personred/rest.png/"]
        _l_(432772)