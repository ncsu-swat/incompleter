# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64728441/python-crash-course-alien-invasion-attributeerror-bullet-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(559969)

except ImportError:
    pass
try:
    from bullet import Bullet
    _l_(559971)

except ImportError:
    pass

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    _l_(560002)

    if _a_(559973, _n_(559972, "event", lambda: event), "key") == _a_(559975, _n_(559974, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(560001)

        _n_(559976, "ship", lambda: ship).moving_right = True
        _l_(559977)
    elif _a_(559979, _n_(559978, "event", lambda: event), "key") == _a_(559981, _n_(559980, "pygame", lambda: pygame), "K_LEFT"):
        _l_(560000)

        _n_(559982, "ship", lambda: ship).moving_left = True
        _l_(559983)
    elif _a_(559985, _n_(559984, "event", lambda: event), "key") == _a_(559987, _n_(559986, "pygame", lambda: pygame), "K_SPACE"):
        _l_(559999)

        new_bullet =  _c_(559992, _n_(559988, "Bullet", lambda: Bullet), _n_(559989, "ai_settings", lambda: ai_settings), _n_(559990, "screen", lambda: screen), _n_(559991, "ship", lambda: ship))
        _l_(559993)
        _c_(559997, _a_(559995, _n_(559994, "bullets", lambda: bullets), "add"), _n_(559996, "new_bullet", lambda: new_bullet))
        _l_(559998)

def check_keyup_events(event, ship):
    _l_(560017)

    if _a_(560004, _n_(560003, "event", lambda: event), "key") == _a_(560006, _n_(560005, "pygame", lambda: pygame), "K_RIGHT"):
        _l_(560016)

        _n_(560007, "ship", lambda: ship).moving_right = False
        _l_(560008)
    elif _a_(560010, _n_(560009, "event", lambda: event), "key") == _a_(560012, _n_(560011, "pygame", lambda: pygame), "K_LEFT"):
        _l_(560015)

        _n_(560013, "ship", lambda: ship).moving_left = False
        _l_(560014)

def check_events(ai_settings, screen, ship, bullets):
    _l_(560078)


    for event in _c_(560021, _a_(560020, _a_(560019, _n_(560018, "pygame", lambda: pygame), "event"), "get")):
        _l_(560077)

        if _a_(560023, _n_(560022, "event", lambda: event), "type") == _a_(560025, _n_(560024, "pygame", lambda: pygame), "QUIT"):
            _l_(560076)

            _c_(560028, _a_(560027, _n_(560026, "sys", lambda: sys), "exit"))
            _l_(560029)

        elif _a_(560031, _n_(560030, "event", lambda: event), "type") == _a_(560033, _n_(560032, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(560075)

            _c_(560040, _n_(560034, "check_keydown_events", lambda: check_keydown_events), _n_(560035, "event", lambda: event),_n_(560036, "ship", lambda: ship), _n_(560037, "ai_settings", lambda: ai_settings), _n_(560038, "screen", lambda: screen), _n_(560039, "bullets", lambda: bullets))
            _l_(560041)
            if _a_(560043, _n_(560042, "event", lambda: event), "key") == _a_(560045, _n_(560044, "pygame", lambda: pygame), "K_RIGHT"):
                _l_(560055)

                _n_(560046, "ship", lambda: ship).moving_right = True
                _l_(560047)

            elif _a_(560049, _n_(560048, "event", lambda: event), "key") == _a_(560051, _n_(560050, "pygame", lambda: pygame), "K_LEFT"):
                _l_(560054)

                _n_(560052, "ship", lambda: ship).moving_left = True
                _l_(560053)

        elif _a_(560057, _n_(560056, "event", lambda: event), "type") == _a_(560059, _n_(560058, "pygame", lambda: pygame), "KEYUP"):
            _l_(560074)

            if _a_(560061, _n_(560060, "event", lambda: event), "key") == _a_(560063, _n_(560062, "pygame", lambda: pygame), "K_RIGHT"):
                _l_(560073)

                _n_(560064, "ship", lambda: ship).moving_right = False
                _l_(560065)

            elif _a_(560067, _n_(560066, "event", lambda: event), "key") == _a_(560069, _n_(560068, "pygame", lambda: pygame), "K_LEFT"):
                _l_(560072)

                _n_(560070, "ship", lambda: ship).moving_left = False
                _l_(560071)

def update_screen(ai_settings, bullets, screen, ship):
    _l_(560091)


    for bullet in _c_(560081, _a_(560080, _n_(560079, "bullets", lambda: bullets), "sprites")):
        _l_(560090)

        _c_(560084, _a_(560083, _n_(560082, "bullet", lambda: bullet), "draw_bullet"))
        _l_(560085)
        _c_(560088, _a_(560087, _n_(560086, "ship", lambda: ship), "blitme"))
        _l_(560089)