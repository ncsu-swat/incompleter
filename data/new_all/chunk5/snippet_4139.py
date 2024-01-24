# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62480756/nameerror-name-bullets-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(683795)

except ImportError:
    pass
try:
    import pygame
    _l_(683797)

except ImportError:
    pass
try:
    from bullet import Bullet
    _l_(683799)

except ImportError:
    pass

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    _l_(683830)

    """Respond to keypresses."""
    if _a_(683801, _n_(683800, "event", lambda: event), "key") == _a_(683803, _n_(683802, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(683829)

        _n_(683804, "ship", lambda: ship).moving_right = True
        _l_(683805)
    elif _a_(683807, _n_(683806, "event", lambda: event), "key") == _a_(683809, _n_(683808, "pygame", lambda: pygame), "K_LEFT"):
        _l_(683828)

        _n_(683810, "ship", lambda: ship).moving_left = True
        _l_(683811)
    elif _a_(683813, _n_(683812, "event", lambda: event), "key") == _a_(683815, _n_(683814, "pygame", lambda: pygame), "K_SPACE"):
        _l_(683827)

        # Create a new bullet and add it to the bullets group.
        new_bullet = _c_(683820, _n_(683816, "Bullet", lambda: Bullet), _n_(683817, "ai_settings", lambda: ai_settings), _n_(683818, "screen", lambda: screen), _n_(683819, "ship", lambda: ship))
        _l_(683821)
        _c_(683825, _a_(683823, _n_(683822, "bullets", lambda: bullets), "add"), _n_(683824, "new_bullet", lambda: new_bullet))
        _l_(683826)

def check_keyup_events(event, ship):
    _l_(683845)

    """Respond to key releases."""
    if _a_(683832, _n_(683831, "event", lambda: event), "key") == _a_(683834, _n_(683833, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(683844)

        _n_(683835, "ship", lambda: ship).moving_right = False
        _l_(683836)
    elif _a_(683838, _n_(683837, "event", lambda: event), "key") == _a_(683840, _n_(683839, "pygame", lambda: pygame), "K_LEFT"):
        _l_(683843)

        _n_(683841, "ship", lambda: ship).moving_left = False
        _l_(683842)


def check_events(ai_settings, screen, ship, bullets):
    _l_(683884)

    """Respond to keypresses and mouse events."""
    for event in _c_(683849, _a_(683848, _a_(683847, _n_(683846, "pygame", lambda: pygame), "event"), "get")):
        _l_(683883)

        if _a_(683851, _n_(683850, "event", lambda: event), "type") == _a_(683853, _n_(683852, "pygame", lambda: pygame), "QUIT"):
            _l_(683882)

            _c_(683856, _a_(683855, _n_(683854, "sys", lambda: sys), "exit"))
            _l_(683857)
        elif _a_(683859, _n_(683858, "event", lambda: event), "type") == _a_(683861, _n_(683860, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(683881)

            _c_(683868, _n_(683862, "check_keydown_events", lambda: check_keydown_events), _n_(683863, "event", lambda: event), _n_(683864, "ai_settings", lambda: ai_settings), _n_(683865, "screen", lambda: screen), _n_(683866, "ship", lambda: ship), _n_(683867, "bullets", lambda: bullets))
            _l_(683869)
        elif _a_(683871, _n_(683870, "event", lambda: event), "type") == _a_(683873, _n_(683872, "pygame", lambda: pygame), "KEYUP"):
            _l_(683880)

            _c_(683878, _n_(683874, "check_keyup_events", lambda: check_keyup_events), _n_(683875, "event", lambda: event), _n_(683876, "ai_settings", lambda: ai_settings), _n_(683877, "ship", lambda: ship))
            _l_(683879)

# Redraw all bullets behind ship and aliens.
for bullet in _c_(683887, _a_(683886, _n_(683885, "Bullet", lambda: Bullet), "sprites")):
    _l_(683892)

    _c_(683890, _a_(683889, _n_(683888, "bullet", lambda: bullet), "draw_bullet"))
    _l_(683891)

def update_screen(ai_settings, screen, ship, bullets):
    _l_(683916)

    """Update images on the screenand flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    _c_(683897, _a_(683894, _n_(683893, "screen", lambda: screen), "fill"), _a_(683896, _n_(683895, "ai_settings", lambda: ai_settings), "bg_color"))
    _l_(683898)
    # Redraw all bullets behind ship and aliens.
    for bullet in _c_(683901, _a_(683900, _n_(683899, "Bullet", lambda: Bullet), "sprites")):
        _l_(683906)

        _c_(683904, _a_(683903, _n_(683902, "bullet", lambda: bullet), "draw_bullet"))
        _l_(683905)
    _c_(683909, _a_(683908, _n_(683907, "ship", lambda: ship), "blitme"))
    _l_(683910)

    # Make the most recently drawn screen visible.
    _c_(683914, _a_(683913, _a_(683912, _n_(683911, "pygame", lambda: pygame), "display"), "flip"))
    _l_(683915)