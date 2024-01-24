# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60910850/pygame-typeerror-join-argument-must-be-str-bytes-or-os-pathlike-object-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""Homebrew tower defense game using pygame and object oriented programming.
This is a learning project"""
try:
    import pygame
    _l_(427066)

except ImportError:
    pass
try:
    from tower import Tower
    _l_(427068)

except ImportError:
    pass
try:
    from scaling import get_scaling_info
    _l_(427070)

except ImportError:
    pass

_c_(427072, _n_(427071, "get_scaling_info", lambda: get_scaling_info))
_l_(427073)

def run_game():
    _l_(427234)

    """Runs the game"""
    _c_(427076, _a_(427075, _n_(427074, "pygame", lambda: pygame), "init"))
    _l_(427077)
    _c_(427079, _n_(427078, "get_scaling_info", lambda: get_scaling_info))
    _l_(427080)
    width, height = _c_(427082, _n_(427081, "get_scaling_info", lambda: get_scaling_info))[1:]
    _l_(427083)
    screen = _c_(427089, _a_(427086, _a_(427085, _n_(427084, "pygame", lambda: pygame), "display"), "set_mode"), (0, 0), _a_(427088, _n_(427087, "pygame", lambda: pygame), "FULLSCREEN"), 32)
    _l_(427090)
    _c_(427094, _a_(427093, _a_(427092, _n_(427091, "pygame", lambda: pygame), "display"), "set_caption"), "Tower Defense")
    _l_(427095)
    game_surface = _c_(427098, _a_(427097, _n_(427096, "screen", lambda: screen), "copy"))
    _l_(427099)

    def toggle_fullscreen():
        _l_(427122)

        """Toggles between fullscreen and windowed mode"""
        if _c_(427102, _a_(427101, _n_(427100, "screen", lambda: screen), "get_flags")) & _a_(427104, _n_(427103, "pygame", lambda: pygame), "FULLSCREEN"):
            _l_(427112)

            aux = _c_(427110, _a_(427107, _a_(427106, _n_(427105, "pygame", lambda: pygame), "display"), "set_mode"), (800, 600), _a_(427109, _n_(427108, "pygame", lambda: pygame), "RESIZABLE"))
            _l_(427111)
            return aux
        aux = _c_(427120, _a_(427115, _a_(427114, _n_(427113, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(427116, "width", lambda: width), _n_(427117, "height", lambda: height)), _a_(427119, _n_(427118, "pygame", lambda: pygame), "FULLSCREEN"))
        _l_(427121)
        return aux

    def update_display():
        _l_(427155)

        """Update the game display"""
        scaling_info = _c_(427124, _n_(427123, "get_scaling_info", lambda: get_scaling_info))[0]
        _l_(427125)
        _c_(427128, _a_(427127, _n_(427126, "screen", lambda: screen), "fill"), (0, 0, 0))
        _l_(427129)
        for tower in _a_(427131, _n_(427130, "Tower", lambda: Tower), "towers"):
            _l_(427136)

            _c_(427134, _a_(427133, _n_(427132, "tower", lambda: tower), "draw"))
            _l_(427135)
        _c_(427148, _a_(427138, _n_(427137, "screen", lambda: screen), "blit"), _c_(427147, _a_(427141, _a_(427140, _n_(427139, "pygame", lambda: pygame), "transform"), "scale"), _n_(427142, "game_surface", lambda: game_surface), (_a_(427144, _n_(427143, "scaling_info", lambda: scaling_info), "current_w"), _a_(427146, _n_(427145, "scaling_info", lambda: scaling_info), "current_h"))), (0, 0))
        _l_(427149)
        _c_(427153, _a_(427152, _a_(427151, _n_(427150, "pygame", lambda: pygame), "display"), "update"))
        _l_(427154)

    run = True
    _l_(427156)
    tower_type = 0
    _l_(427157)
    while _n_(427158, "run", lambda: run):
        _l_(427229)

        for event in _c_(427162, _a_(427161, _a_(427160, _n_(427159, "pygame", lambda: pygame), "event"), "get")):
            _l_(427225)

            if _a_(427164, _n_(427163, "event", lambda: event), "type") == _a_(427166, _n_(427165, "pygame", lambda: pygame), "QUIT"):
                _l_(427168)

                run = False
                _l_(427167)
            if _a_(427170, _n_(427169, "event", lambda: event), "type") == _a_(427172, _n_(427171, "pygame", lambda: pygame), "KEYDOWN"):
                _l_(427201)

                if _a_(427174, _n_(427173, "event", lambda: event), "key") == _a_(427176, _n_(427175, "pygame", lambda: pygame), "K_ESCAPE"):
                    _l_(427178)

                    run = False
                    _l_(427177)
                if _a_(427180, _n_(427179, "event", lambda: event), "key") == _a_(427182, _n_(427181, "pygame", lambda: pygame), "K_F11"):
                    _l_(427186)

                    _c_(427184, _n_(427183, "toggle_fullscreen", lambda: toggle_fullscreen))
                    _l_(427185)
                if _a_(427188, _n_(427187, "event", lambda: event), "key") == _a_(427190, _n_(427189, "pygame", lambda: pygame), "K_1") or _a_(427192, _n_(427191, "event", lambda: event), "key") == _a_(427194, _n_(427193, "pygame", lambda: pygame), "K_2"):
                    _l_(427200)

                    tower_type = _a_(427196, _n_(427195, "Tower", lambda: Tower), "selection_dict")[_a_(427198, _n_(427197, "event", lambda: event), "key")]
                    _l_(427199)
            if _a_(427203, _n_(427202, "event", lambda: event), "type") == _a_(427205, _n_(427204, "pygame", lambda: pygame), "MOUSEBUTTONDOWN") and _n_(427206, "tower_type", lambda: tower_type) != 0:
                _l_(427224)

                _c_(427209, _n_(427207, "print", lambda: print), _n_(427208, "tower_type", lambda: tower_type)) #returns elf_tower.png which is the expected result
                _l_(427210) #returns elf_tower.png which is the expected result
                mouse_x, mouse_y = _c_(427214, _a_(427213, _a_(427212, _n_(427211, "pygame", lambda: pygame), "mouse"), "get_pos"))
                _l_(427215)
                _c_(427222, _a_(427221, _c_(427220, _n_(427216, "Tower", lambda: Tower), _n_(427217, "tower_type", lambda: tower_type), _n_(427218, "mouse_x", lambda: mouse_x), _n_(427219, "mouse_y", lambda: mouse_y)), "create_tower"))
                _l_(427223)

        _c_(427227, _n_(427226, "update_display", lambda: update_display))
        _l_(427228)

    _c_(427232, _a_(427231, _n_(427230, "pygame", lambda: pygame), "quit"))
    _l_(427233)

_c_(427236, _n_(427235, "run_game", lambda: run_game))
_l_(427237)