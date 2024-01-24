# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58480212/attributeerror-python-crash-course
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys, pygame
    _l_(422639)

except ImportError:
    pass
try:
    from settings import Settings
    _l_(422641)

except ImportError:
    pass
try:
    from ship import Ship
    _l_(422643)

except ImportError:
    pass
try:
    from bullet import Bullet
    _l_(422645)

except ImportError:
    pass

class AlienInvasion:
    _l_(422829)

    """Overall class to manage game assests and behavior."""

    def __init__(self):
        _l_(422682)

        """Initialize the game and create game resources."""
        _c_(422648, _a_(422647, _n_(422646, "pygame", lambda: pygame), "init"))
        _l_(422649)
        _n_(422650, "self", lambda: self).settings = _c_(422652, _n_(422651, "Settings", lambda: Settings))
        _l_(422653)

        _n_(422654, "self", lambda: self).screen = _c_(422664, _a_(422657, _a_(422656, _n_(422655, "pygame", lambda: pygame), "display"), "set_mode"), (_a_(422660, _a_(422659, _n_(422658, "self", lambda: self), "settings"), "screen_width"), _a_(422663, _a_(422662, _n_(422661, "self", lambda: self), "settings"), "screen_height")))
        _l_(422665)
        _c_(422669, _a_(422668, _a_(422667, _n_(422666, "pygame", lambda: pygame), "display"), "set_caption"), "Alien Invasion")
        _l_(422670)

        _n_(422671, "self", lambda: self).ship = _c_(422674, _n_(422672, "Ship", lambda: Ship), _n_(422673, "self", lambda: self))
        _l_(422675)
        _n_(422676, "self", lambda: self).bullets = _c_(422680, _a_(422679, _a_(422678, _n_(422677, "pygame", lambda: pygame), "sprite"), "Group"))
        _l_(422681)

    def run_game(self):
        _l_(422702)

        """Start the main loop for the game."""
        while True:
            _l_(422701)

            _c_(422685, _a_(422684, _n_(422683, "self", lambda: self), "_check_events"))
            _l_(422686)
            _c_(422690, _a_(422689, _a_(422688, _n_(422687, "self", lambda: self), "ship"), "update"))
            _l_(422691)
            _c_(422695, _a_(422694, _a_(422693, _n_(422692, "self", lambda: self), "bullets"), "update"))
            _l_(422696)
            _c_(422699, _a_(422698, _n_(422697, "self", lambda: self), "_update_screen"))
            _l_(422700)

    def _check_events(self):
        _l_(422737)

        """Respond to keypresses and mouse events."""
        for event in _c_(422706, _a_(422705, _a_(422704, _n_(422703, "pygame", lambda: pygame), "event"), "get")):
            _l_(422736)

            if _a_(422708, _n_(422707, "event", lambda: event), "type") == _a_(422710, _n_(422709, "pygame", lambda: pygame), "QUIT"):
                _l_(422735)

                _c_(422713, _a_(422712, _n_(422711, "sys", lambda: sys), "exit"))
                _l_(422714)
            elif _a_(422716, _n_(422715, "event", lambda: event), "type") == _a_(422718, _n_(422717, "pygame", lambda: pygame), "KEYDOWN"):
                _l_(422734)

                _c_(422722, _a_(422720, _n_(422719, "self", lambda: self), "_check_keydown_events"), _n_(422721, "event", lambda: event))
                _l_(422723)
            elif _a_(422725, _n_(422724, "event", lambda: event), "type") == _a_(422727, _n_(422726, "pygame", lambda: pygame), "KEYUP"):
                _l_(422733)

                _c_(422731, _a_(422729, _n_(422728, "self", lambda: self), "_check_keyup_events"), _n_(422730, "event", lambda: event))
                _l_(422732)

    def _check_keydown_events(self, event):
        _l_(422772)

        if _a_(422739, _n_(422738, "event", lambda: event), "key") == _a_(422741, _n_(422740, "pygame", lambda: pygame), "K_RIGHT"):
            _l_(422771)

            _a_(422743, _n_(422742, "self", lambda: self), "ship").moving_right = True
            _l_(422744)
        elif _a_(422746, _n_(422745, "event", lambda: event), "key") == _a_(422748, _n_(422747, "pygame", lambda: pygame), "K_LEFT"):
            _l_(422770)

            _a_(422750, _n_(422749, "self", lambda: self), "ship").moving_left = True
            _l_(422751)
        elif _a_(422753, _n_(422752, "event", lambda: event), "key") == _a_(422755, _n_(422754, "pygame", lambda: pygame), "K_q"):
            _l_(422769)

            _c_(422758, _a_(422757, _n_(422756, "sys", lambda: sys), "exit"))
            _l_(422759)
        elif _a_(422761, _n_(422760, "event", lambda: event), "key") == _a_(422763, _n_(422762, "pygame", lambda: pygame), "K_SPACE"):
            _l_(422768)

            _c_(422766, _a_(422765, _n_(422764, "self", lambda: self), "_fire_bullet"))
            _l_(422767)

    def _check_keyup_events(self, event):
        _l_(422789)

        if _a_(422774, _n_(422773, "event", lambda: event), "key") == _a_(422776, _n_(422775, "pygame", lambda: pygame), "K_RIGHT"):
            _l_(422788)

            _a_(422778, _n_(422777, "self", lambda: self), "ship").moving_right = False
            _l_(422779)
        elif _a_(422781, _n_(422780, "event", lambda: event), "key") == _a_(422783, _n_(422782, "pygame", lambda: pygame), "K_LEFT"):
            _l_(422787)

            _a_(422785, _n_(422784, "self", lambda: self), "ship").moving_left = False
            _l_(422786)

    def _fire_bullet(self):
        _l_(422800)

        new_bullet = _c_(422792, _n_(422790, "Bullet", lambda: Bullet), _n_(422791, "self", lambda: self))
        _l_(422793)
        _c_(422798, _a_(422796, _a_(422795, _n_(422794, "self", lambda: self), "bullets"), "add"), _n_(422797, "new_bullet", lambda: new_bullet))
        _l_(422799)

    def _update_screen(self):
        _l_(422828)

        # Redraw the screen during each pass through the loop
        _c_(422807, _a_(422803, _a_(422802, _n_(422801, "self", lambda: self), "screen"), "fill"), _a_(422806, _a_(422805, _n_(422804, "self", lambda: self), "settings"), "bg_color"))
        _l_(422808)
        _c_(422812, _a_(422811, _a_(422810, _n_(422809, "self", lambda: self), "ship"), "blitme"))
        _l_(422813)

        for bullet in _c_(422817, _a_(422816, _a_(422815, _n_(422814, "self", lambda: self), "bullets"), "sprites")):
            _l_(422822)

            _c_(422820, _a_(422819, _n_(422818, "bullet", lambda: bullet), "draw_bullet"))
            _l_(422821)

        # Make the most recently drawn screen visible
        _c_(422826, _a_(422825, _a_(422824, _n_(422823, "pygame", lambda: pygame), "display"), "flip"))
        _l_(422827)