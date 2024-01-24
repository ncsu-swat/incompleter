# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21764770/typeerror-got-multiple-values-for-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
BOX_LENGTH = 100
_l_(406053)
_c_(406056, _a_(406055, _n_(406054, "turtle", lambda: turtle), "speed"), 0)
_l_(406057)
fill = 0
_l_(406058)
for i in _c_(406060, _n_(406059, "range", lambda: range), 8):
    _l_(406086)

    fill += 1
    _l_(406061)
    if _n_(406062, "fill", lambda: fill) % 2 == 0:
        _l_(406071)

        _c_(406065, _n_(406063, "Horizontol_drawbox", lambda: Horizontol_drawbox), _n_(406064, "BOX_LENGTH", lambda: BOX_LENGTH), fillBox = False)
        _l_(406066)
    else:
        _c_(406069, _n_(406067, "Horizontol_drawbox", lambda: Horizontol_drawbox), _n_(406068, "BOX_LENGTH", lambda: BOX_LENGTH), fillBox = True)
        _l_(406070)

    for i in _c_(406073, _n_(406072, "range", lambda: range), 8):
        _l_(406085)

        fill += 1
        _l_(406074)
        if _n_(406075, "fill", lambda: fill) % 2 == 0:
            _l_(406084)

            _c_(406078, _n_(406076, "Vertical_drawbox", lambda: Vertical_drawbox), _n_(406077, "BOX_LENGTH", lambda: BOX_LENGTH),fillBox = False)
            _l_(406079)
        else:
            _c_(406082, _n_(406080, "Vertical_drawbox", lambda: Vertical_drawbox), _n_(406081, "BOX_LENGTH", lambda: BOX_LENGTH),fillBox = True)
            _l_(406083)