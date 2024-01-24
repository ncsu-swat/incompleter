# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77716362/typeerror-invalid-rect-assignment-in-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while _n_(354165, "running", lambda: running):
    _l_(354239)

    _c_(354167, _n_(354166, "setup_background", lambda: setup_background))
    _l_(354168)
    spriteimg = _n_(354169, "plumberright", lambda: plumberright)
    _l_(354170)

    _c_(354176, _a_(354172, _n_(354171, "screen", lambda: screen), "blit"), _n_(354173, "spriteimg", lambda: spriteimg),(_n_(354174, "x1", lambda: x1), _n_(354175, "y1", lambda: y1)))
    _l_(354177)

    for event in _c_(354181, _a_(354180, _a_(354179, _n_(354178, "pygame", lambda: pygame), "event"), "get")):
        _l_(354229)

        if _a_(354183, _n_(354182, "event", lambda: event), "type") == _a_(354185, _n_(354184, "pygame", lambda: pygame), "QUIT"):
            _l_(354228)

            running = False
            _l_(354186)
        elif _a_(354188, _n_(354187, "event", lambda: event), "type") == _a_(354190, _n_(354189, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(354227)

            if _a_(354192, _n_(354191, "event", lambda: event), "key") == _a_(354194, _n_(354193, "pygame", lambda: pygame), "K_UP"):
                _l_(354226)

                x1 = _n_(354195, "x1", lambda: x1) + 0
                _l_(354196)
                y1 = _n_(354197, "y1", lambda: y1) - 1
                _l_(354198)
            elif _a_(354200, _n_(354199, "event", lambda: event), "key") == _a_(354202, _n_(354201, "pygame", lambda: pygame), "K_DOWN"):
                _l_(354225)

                x1 = _n_(354203, "x1", lambda: x1) + 0
                _l_(354204)
                y1 = _n_(354205, "y1", lambda: y1) + 1
                _l_(354206)
            elif _a_(354208, _n_(354207, "event", lambda: event), "key") == _a_(354210, _n_(354209, "pygame", lambda: pygame), "K_LEFT"):
                _l_(354224)

                x1 = _n_(354211, "x1", lambda: x1) - 1
                _l_(354212)
                y1 = _n_(354213, "y1", lambda: y1) + 0
                _l_(354214)
            elif _a_(354216, _n_(354215, "event", lambda: event), "key") == _a_(354218, _n_(354217, "pygame", lambda: pygame), "K_RIGHT"):
                _l_(354223)

                x1 = _n_(354219, "x1", lambda: x1) + 1
                _l_(354220)
                y1 = _n_(354221, "y1", lambda: y1) + 0
                _l_(354222)

    _c_(354233, _a_(354232, _a_(354231, _n_(354230, "pygame", lambda: pygame), "display"), "flip"))
    _l_(354234)
    _c_(354237, _a_(354236, _n_(354235, "clock", lambda: clock), "tick"), 120)
    _l_(354238)