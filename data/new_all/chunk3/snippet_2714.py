# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65802508/attributeerror-pygame-surface-object-has-no-attribute-screen
# Importing modules
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(539418)

except ImportError:
    pass
try:
    import pygame
    _l_(539420)

except ImportError:
    pass
try:
    from settings import Settings
    _l_(539422)

except ImportError:
    pass
try:
    from ship import Ship
    _l_(539424)

except ImportError:
    pass


class AlienInvasion:
    _l_(539587)

    '''Class to manage game assets and behavior'''
    _l_(539425)

    def __init__(self):
        _l_(539470)

        '''Constructor to initialize the game and its assets'''
        _l_(539426)
        _c_(539429, _a_(539428, _n_(539427, "pygame", lambda: pygame), "init"))
        _l_(539430)
        _n_(539431, "self", lambda: self).settings = _c_(539433, _n_(539432, "Settings", lambda: Settings))
        _l_(539434)

        _n_(539435, "self", lambda: self).screen = _c_(539441, _a_(539438, _a_(539437, _n_(539436, "pygame", lambda: pygame), "display"), "set_mode"), (0, 0), _a_(539440, _n_(539439, "pygame", lambda: pygame), "FULLSCREEN"))
        _l_(539442)
        _a_(539444, _n_(539443, "self", lambda: self), "settings").screen_width = _a_(539449, _c_(539448, _a_(539447, _a_(539446, _n_(539445, "self", lambda: self), "screen"), "get_rect")), "width")
        _l_(539450)
        _a_(539452, _n_(539451, "self", lambda: self), "settings").screen_height = _a_(539457, _c_(539456, _a_(539455, _a_(539454, _n_(539453, "self", lambda: self), "screen"), "get_rect")), "height")
        _l_(539458)

        _c_(539462, _a_(539461, _a_(539460, _n_(539459, "pygame", lambda: pygame), "display"), "set_caption"), "Alien Invasion")
        _l_(539463)

        _n_(539464, "self", lambda: self).ship = _c_(539468, _n_(539465, "Ship", lambda: Ship), _a_(539467, _n_(539466, "self", lambda: self), "screen"))
        _l_(539469)

    def run_game(self):
        _l_(539486)

        '''Starts the main loop for the game'''
        _l_(539471)
        while True:
            _l_(539485)

            _c_(539474, _a_(539473, _n_(539472, "self", lambda: self), "_check_events"))
            _l_(539475)
            _c_(539479, _a_(539478, _a_(539477, _n_(539476, "self", lambda: self), "ship"), "update"))
            _l_(539480)
            _c_(539483, _a_(539482, _n_(539481, "self", lambda: self), "_update_screen"))
            _l_(539484)

    def _check_events(self):
        _l_(539522)

        '''Watch for the keyboard and mouse events'''
        _l_(539487)
        for event in _c_(539491, _a_(539490, _a_(539489, _n_(539488, "pygame", lambda: pygame), "event"), "get")):
            _l_(539521)

            if _a_(539493, _n_(539492, "event", lambda: event), "type") == _a_(539495, _n_(539494, "pygame", lambda: pygame), "QUIT"):
                _l_(539520)

                _c_(539498, _a_(539497, _n_(539496, "sys", lambda: sys), "exit"))
                _l_(539499)

            elif _a_(539501, _n_(539500, "event", lambda: event), "type") == _a_(539503, _n_(539502, "pygame", lambda: pygame), "KEYDOWN"):
                _l_(539519)

                _c_(539507, _a_(539505, _n_(539504, "self", lambda: self), "_check_keydown_events"), _n_(539506, "event", lambda: event))
                _l_(539508)

            elif _a_(539510, _n_(539509, "event", lambda: event), "type") == _a_(539512, _n_(539511, "pygame", lambda: pygame), "KEYUP"):
                _l_(539518)

                _c_(539516, _a_(539514, _n_(539513, "self", lambda: self), "_check_keyup_events"), _n_(539515, "event", lambda: event))
                _l_(539517)

    def _check_keydown_events(self, event):
        _l_(539548)

        """Respond to keypresses."""
        if _a_(539524, _n_(539523, "event", lambda: event), "key") == _a_(539526, _n_(539525, "pygame", lambda: pygame), "K_RIGHT"):
            _l_(539547)

            _a_(539528, _n_(539527, "self", lambda: self), "ship").moving_right = True
            _l_(539529)
        elif _a_(539531, _n_(539530, "event", lambda: event), "key") == _a_(539533, _n_(539532, "pygame", lambda: pygame), "K_LEFT"):
            _l_(539546)

            _a_(539535, _n_(539534, "self", lambda: self), "ship").moving_left = True
            _l_(539536)
        elif _a_(539538, _n_(539537, "event", lambda: event), "key") == _a_(539540, _n_(539539, "pygame", lambda: pygame), "K_ESCAPE"):
            _l_(539545)

            _c_(539543, _a_(539542, _n_(539541, "sys", lambda: sys), "exit"))
            _l_(539544)

    def _check_keyup_events(self, event):
        _l_(539565)

        """Respond to key releases."""
        if _a_(539550, _n_(539549, "event", lambda: event), "key") == _a_(539552, _n_(539551, "pygame", lambda: pygame), "K_RIGHT"):
            _l_(539564)

            _a_(539554, _n_(539553, "self", lambda: self), "ship").moving_right = False
            _l_(539555)
        elif _a_(539557, _n_(539556, "event", lambda: event), "key") == _a_(539559, _n_(539558, "pygame", lambda: pygame), "K_LEFT"):
            _l_(539563)

            _a_(539561, _n_(539560, "self", lambda: self), "ship").moving_left = False
            _l_(539562)

    def _update_screen(self):
        _l_(539586)

        '''Redraw the screen during each pass of the loop'''
        _l_(539566)
        _c_(539573, _a_(539569, _a_(539568, _n_(539567, "self", lambda: self), "screen"), "fill"), _a_(539572, _a_(539571, _n_(539570, "self", lambda: self), "settings"), "bg_color"))
        _l_(539574)
        _c_(539578, _a_(539577, _a_(539576, _n_(539575, "self", lambda: self), "ship"), "blitme"))
        _l_(539579)
        '''Make the most recently drawn screen visible'''
        _l_(539580)
        _c_(539584, _a_(539583, _a_(539582, _n_(539581, "pygame", lambda: pygame), "display"), "flip"))
        _l_(539585)


if _n_(539588, "__name__", lambda: __name__) == '__main__':
    _l_(539597)

    '''Make a game instance, and run the game'''
    _l_(539589)
    alinv = _c_(539591, _n_(539590, "AlienInvasion", lambda: AlienInvasion))
    _l_(539592)
    _c_(539595, _a_(539594, _n_(539593, "alinv", lambda: alinv), "run_game"))
    _l_(539596)