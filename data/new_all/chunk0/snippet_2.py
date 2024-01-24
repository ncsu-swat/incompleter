# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21764770/typeerror-got-multiple-values-for-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
BOX_LENGTH = 100
_l_(48402)
_c_(48405, _a_(48404, _n_(48403, "turtle", lambda: turtle), "speed"), 0)
_l_(48406)
fill = 0
_l_(48407)
for i in _c_(48409, _n_(48408, "range", lambda: range), 8):
    _l_(48435)

    fill += 1
    _l_(48410)
    if _n_(48411, "fill", lambda: fill) % 2 == 0:
        _l_(48420)

        _c_(48414, _n_(48412, "Horizontol_drawbox", lambda: Horizontol_drawbox), _n_(48413, "BOX_LENGTH", lambda: BOX_LENGTH), fillBox = False)
        _l_(48415)
    else:
        _c_(48418, _n_(48416, "Horizontol_drawbox", lambda: Horizontol_drawbox), _n_(48417, "BOX_LENGTH", lambda: BOX_LENGTH), fillBox = True)
        _l_(48419)

    for i in _c_(48422, _n_(48421, "range", lambda: range), 8):
        _l_(48434)

        fill += 1
        _l_(48423)
        if _n_(48424, "fill", lambda: fill) % 2 == 0:
            _l_(48433)

            _c_(48427, _n_(48425, "Vertical_drawbox", lambda: Vertical_drawbox), _n_(48426, "BOX_LENGTH", lambda: BOX_LENGTH),fillBox = False)
            _l_(48428)
        else:
            _c_(48431, _n_(48429, "Vertical_drawbox", lambda: Vertical_drawbox), _n_(48430, "BOX_LENGTH", lambda: BOX_LENGTH),fillBox = True)
            _l_(48432)