# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76667512/attributeerror-settings-object-has-no-attribute-rect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(607721)

except ImportError:
    pass
try:
    from settings import Settings
    _l_(607723)

except ImportError:
    pass
try:
    from ship import Ship
    _l_(607725)

except ImportError:
    pass
try:
    import game_functions as gf
    _l_(607727)

except ImportError:
    pass
try:
    from pygame.sprite import Group
    _l_(607729)

except ImportError:
    pass

def run_game():
    _l_(607783)

    _c_(607732, _a_(607731, _n_(607730, "pygame", lambda: pygame), "init"))
    _l_(607733)
    ai_settings = _c_(607735, _n_(607734, "Settings", lambda: Settings))
    _l_(607736)
    screen = _c_(607744, _a_(607739, _a_(607738, _n_(607737, "pygame", lambda: pygame), "display"), "set_mode"), (_a_(607741, _n_(607740, "ai_settings", lambda: ai_settings), "screen_width"), _a_(607743, _n_(607742, "ai_settings", lambda: ai_settings), "screen_height")))
    _l_(607745)
    _c_(607749, _a_(607748, _a_(607747, _n_(607746, "pygame", lambda: pygame), "display"), "set_caption"), "Alien Invasion")
    _l_(607750)
    ship = _c_(607753, _n_(607751, "Ship", lambda: Ship), _n_(607752, "screen", lambda: screen))
    _l_(607754)
    bullets = _c_(607756, _n_(607755, "Group", lambda: Group))
    _l_(607757)

    while True:
        _l_(607782)

        _c_(607764, _a_(607759, _n_(607758, "gf", lambda: gf), "check_events"), _n_(607760, "ai_settings", lambda: ai_settings), _n_(607761, "screen", lambda: screen), _n_(607762, "ship", lambda: ship), _n_(607763, "bullets", lambda: bullets))
        _l_(607765)
        _c_(607768, _a_(607767, _n_(607766, "ship", lambda: ship), "update"))
        _l_(607769)
        _c_(607772, _a_(607771, _n_(607770, "bullets", lambda: bullets), "update"))
        _l_(607773)
        _c_(607780, _a_(607775, _n_(607774, "gf", lambda: gf), "update_screen"), _n_(607776, "ai_settings", lambda: ai_settings), _n_(607777, "screen", lambda: screen), _n_(607778, "ship", lambda: ship), _n_(607779, "bullets", lambda: bullets))
        _l_(607781)

_c_(607785, _n_(607784, "run_game", lambda: run_game))
_l_(607786)