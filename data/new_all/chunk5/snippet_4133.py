# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62480756/nameerror-name-bullets-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(699108)

except ImportError:
    pass
try:
    import pygame
    _l_(699110)

except ImportError:
    pass
try:
    from bullet import Bullet
    _l_(699112)

except ImportError:
    pass

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    _l_(699143)

    """Respond to keypresses."""
    if _a_(699114, _n_(699113, "event", lambda: event), "key") == _a_(699116, _n_(699115, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(699142)

        _n_(699117, "ship", lambda: ship).moving_right = True
        _l_(699118)
    elif _a_(699120, _n_(699119, "event", lambda: event), "key") == _a_(699122, _n_(699121, "pygame", lambda: pygame), "K_LEFT"):
        _l_(699141)

        _n_(699123, "ship", lambda: ship).moving_left = True
        _l_(699124)
    elif _a_(699126, _n_(699125, "event", lambda: event), "key") == _a_(699128, _n_(699127, "pygame", lambda: pygame), "K_SPACE"):
        _l_(699140)

        # Create a new bullet and add it to the bullets group.
        new_bullet = _c_(699133, _n_(699129, "Bullet", lambda: Bullet), _n_(699130, "ai_settings", lambda: ai_settings), _n_(699131, "screen", lambda: screen), _n_(699132, "ship", lambda: ship))
        _l_(699134)
        _c_(699138, _a_(699136, _n_(699135, "bullets", lambda: bullets), "add"), _n_(699137, "new_bullet", lambda: new_bullet))
        _l_(699139)

def check_keyup_events(event, ship):
    _l_(699158)

    """Respond to key releases."""
    if _a_(699145, _n_(699144, "event", lambda: event), "key") == _a_(699147, _n_(699146, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(699157)

        _n_(699148, "ship", lambda: ship).moving_right = False
        _l_(699149)
    elif _a_(699151, _n_(699150, "event", lambda: event), "key") == _a_(699153, _n_(699152, "pygame", lambda: pygame), "K_LEFT"):
        _l_(699156)

        _n_(699154, "ship", lambda: ship).moving_left = False
        _l_(699155)


def check_events(ai_settings, screen, ship, bullets):
    _l_(699197)

    """Respond to keypresses and mouse events."""
    for event in _c_(699162, _a_(699161, _a_(699160, _n_(699159, "pygame", lambda: pygame), "event"), "get")):
        _l_(699196)

        if _a_(699164, _n_(699163, "event", lambda: event), "type") == _a_(699166, _n_(699165, "pygame", lambda: pygame), "QUIT"):
            _l_(699195)

            _c_(699169, _a_(699168, _n_(699167, "sys", lambda: sys), "exit"))
            _l_(699170)
        elif _a_(699172, _n_(699171, "event", lambda: event), "type") == _a_(699174, _n_(699173, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(699194)

            _c_(699181, _n_(699175, "check_keydown_events", lambda: check_keydown_events), _n_(699176, "event", lambda: event), _n_(699177, "ai_settings", lambda: ai_settings), _n_(699178, "screen", lambda: screen), _n_(699179, "ship", lambda: ship), _n_(699180, "bullets", lambda: bullets))
            _l_(699182)
        elif _a_(699184, _n_(699183, "event", lambda: event), "type") == _a_(699186, _n_(699185, "pygame", lambda: pygame), "KEYUP"):
            _l_(699193)

            _c_(699191, _n_(699187, "check_keyup_events", lambda: check_keyup_events), _n_(699188, "event", lambda: event), _n_(699189, "ai_settings", lambda: ai_settings), _n_(699190, "ship", lambda: ship))
            _l_(699192)

# Redraw all bullets behind ship and aliens.
for bullet in _c_(699200, _a_(699199, _n_(699198, "Bullet", lambda: Bullet), "sprites")):
    _l_(699205)

    _c_(699203, _a_(699202, _n_(699201, "bullet", lambda: bullet), "draw_bullet"))
    _l_(699204)

def update_screen(ai_settings, screen, ship, bullets):
    _l_(699229)

    """Update images on the screenand flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    _c_(699210, _a_(699207, _n_(699206, "screen", lambda: screen), "fill"), _a_(699209, _n_(699208, "ai_settings", lambda: ai_settings), "bg_color"))
    _l_(699211)
    # Redraw all bullets behind ship and aliens.
    for bullet in _c_(699214, _a_(699213, _n_(699212, "Bullet", lambda: Bullet), "sprites")):
        _l_(699219)

        _c_(699217, _a_(699216, _n_(699215, "bullet", lambda: bullet), "draw_bullet"))
        _l_(699218)
    _c_(699222, _a_(699221, _n_(699220, "ship", lambda: ship), "blitme"))
    _l_(699223)

    # Make the most recently drawn screen visible.
    _c_(699227, _a_(699226, _a_(699225, _n_(699224, "pygame", lambda: pygame), "display"), "flip"))
    _l_(699228)