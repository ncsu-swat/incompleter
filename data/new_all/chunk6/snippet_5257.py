# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77716362/typeerror-invalid-rect-assignment-in-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while _n_(351060, "running", lambda: running):
    _l_(351134)

    _c_(351062, _n_(351061, "setup_background", lambda: setup_background))
    _l_(351063)
    spriteimg = _n_(351064, "plumberright", lambda: plumberright)
    _l_(351065)

    _c_(351071, _a_(351067, _n_(351066, "screen", lambda: screen), "blit"), _n_(351068, "spriteimg", lambda: spriteimg),(_n_(351069, "x1", lambda: x1), _n_(351070, "y1", lambda: y1)))
    _l_(351072)

    for event in _c_(351076, _a_(351075, _a_(351074, _n_(351073, "pygame", lambda: pygame), "event"), "get")):
        _l_(351124)

        if _a_(351078, _n_(351077, "event", lambda: event), "type") == _a_(351080, _n_(351079, "pygame", lambda: pygame), "QUIT"):
            _l_(351123)

            running = False
            _l_(351081)
        elif _a_(351083, _n_(351082, "event", lambda: event), "type") == _a_(351085, _n_(351084, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(351122)

            if _a_(351087, _n_(351086, "event", lambda: event), "key") == _a_(351089, _n_(351088, "pygame", lambda: pygame), "K_UP"):
                _l_(351121)

                x1 = _n_(351090, "x1", lambda: x1) + 0
                _l_(351091)
                y1 = _n_(351092, "y1", lambda: y1) - 1
                _l_(351093)
            elif _a_(351095, _n_(351094, "event", lambda: event), "key") == _a_(351097, _n_(351096, "pygame", lambda: pygame), "K_DOWN"):
                _l_(351120)

                x1 = _n_(351098, "x1", lambda: x1) + 0
                _l_(351099)
                y1 = _n_(351100, "y1", lambda: y1) + 1
                _l_(351101)
            elif _a_(351103, _n_(351102, "event", lambda: event), "key") == _a_(351105, _n_(351104, "pygame", lambda: pygame), "K_LEFT"):
                _l_(351119)

                x1 = _n_(351106, "x1", lambda: x1) - 1
                _l_(351107)
                y1 = _n_(351108, "y1", lambda: y1) + 0
                _l_(351109)
            elif _a_(351111, _n_(351110, "event", lambda: event), "key") == _a_(351113, _n_(351112, "pygame", lambda: pygame), "K_RIGHT"):
                _l_(351118)

                x1 = _n_(351114, "x1", lambda: x1) + 1
                _l_(351115)
                y1 = _n_(351116, "y1", lambda: y1) + 0
                _l_(351117)

    _c_(351128, _a_(351127, _a_(351126, _n_(351125, "pygame", lambda: pygame), "display"), "flip"))
    _l_(351129)
    _c_(351132, _a_(351131, _n_(351130, "clock", lambda: clock), "tick"), 120)
    _l_(351133)