# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76667512/attributeerror-settings-object-has-no-attribute-rect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(619005)

except ImportError:
    pass
try:
    import pygame
    _l_(619007)

except ImportError:
    pass
try:
    from bullet import Bullet
    _l_(619009)

except ImportError:
    pass

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    _l_(619040)

    if _a_(619011, _n_(619010, "event", lambda: event), "key") == _a_(619013, _n_(619012, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(619039)

        _n_(619014, "ship", lambda: ship).moving_right = True
        _l_(619015)
    elif _a_(619017, _n_(619016, "event", lambda: event), "key") == _a_(619019, _n_(619018, "pygame", lambda: pygame), "K_LEFT"):
        _l_(619038)

        _n_(619020, "ship", lambda: ship).moving_left = True
        _l_(619021)
    elif _a_(619023, _n_(619022, "event", lambda: event), "key") == _a_(619025, _n_(619024, "pygame", lambda: pygame), "K_SPACE"):
        _l_(619037)

        new_bullet = _c_(619030, _n_(619026, "Bullet", lambda: Bullet), _n_(619027, "ai_settings", lambda: ai_settings), _n_(619028, "screen", lambda: screen), _n_(619029, "ship", lambda: ship))
        _l_(619031)
        _c_(619035, _a_(619033, _n_(619032, "bullets", lambda: bullets), "add"), _n_(619034, "new_bullet", lambda: new_bullet))
        _l_(619036)

def check_keyup_events(event, ship):
    _l_(619055)

    if _a_(619042, _n_(619041, "event", lambda: event), "key") == _a_(619044, _n_(619043, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(619054)

        _n_(619045, "ship", lambda: ship).moving_right = False
        _l_(619046)
    elif _a_(619048, _n_(619047, "event", lambda: event), "key") == _a_(619050, _n_(619049, "pygame", lambda: pygame), "K_LEFT"):
        _l_(619053)

        _n_(619051, "ship", lambda: ship).moving_left = False
        _l_(619052)

def check_events(ai_settings, screen, ship, bullets):
    _l_(619091)

    for event in _c_(619059, _a_(619058, _a_(619057, _n_(619056, "pygame", lambda: pygame), "event"), "get")):
        _l_(619090)

        if _a_(619061, _n_(619060, "event", lambda: event), "type") == _a_(619063, _n_(619062, "pygame", lambda: pygame), "QUIT"):
            _l_(619089)

            _c_(619066, _a_(619065, _n_(619064, "sys", lambda: sys), "exit"))
            _l_(619067)

        elif _a_(619069, _n_(619068, "event", lambda: event), "type") == _a_(619071, _n_(619070, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(619088)

            _c_(619078, _n_(619072, "check_keydown_events", lambda: check_keydown_events), _n_(619073, "event", lambda: event), _n_(619074, "ai_settings", lambda: ai_settings), _n_(619075, "screen", lambda: screen), _n_(619076, "ship", lambda: ship), _n_(619077, "bullets", lambda: bullets))
            _l_(619079)

        elif _a_(619081, _n_(619080, "event", lambda: event), "type") == _a_(619083, _n_(619082, "pygame", lambda: pygame), "KEYUP"):
            _l_(619087)

            _c_(619085, _n_(619084, "check_keyup_events", lambda: check_keyup_events))
            _l_(619086)

def update_screen(ai_settings, screen, ship, bullets):
    _l_(619115)

    _c_(619096, _a_(619093, _n_(619092, "screen", lambda: screen), "fill"), _a_(619095, _n_(619094, "ai_settings", lambda: ai_settings), "bg_color"))
    _l_(619097)
    _c_(619100, _a_(619099, _n_(619098, "ship", lambda: ship), "blitme"))
    _l_(619101)

    for bullet in _c_(619104, _a_(619103, _n_(619102, "bullets", lambda: bullets), "sprites")):
        _l_(619109)

        _c_(619107, _a_(619106, _n_(619105, "bullet", lambda: bullet), "draw_bullet"))
        _l_(619108)

    _c_(619113, _a_(619112, _a_(619111, _n_(619110, "pygame", lambda: pygame), "display"), "flip"))
    _l_(619114)