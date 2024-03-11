# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75092432/type-error-function-got-multiple-values-for-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
BOX_LENGTH = 100
_l_(600090)
_c_(600093, _a_(600092, _n_(600091, "turtle", lambda: turtle), "speed"), 0)
_l_(600094)
fill = 0
_l_(600095)
for i in _c_(600097, _n_(600096, "range", lambda: range), 8):
    _l_(600123)

    fill += 1
    _l_(600098)
    if _n_(600099, "fill", lambda: fill) % 2 == 0:
        _l_(600108)

        _c_(600102, _n_(600100, "Horizontol_drawbox", lambda: Horizontol_drawbox), _n_(600101, "BOX_LENGTH", lambda: BOX_LENGTH), fillBox = False)
        _l_(600103)
    else:
        _c_(600106, _n_(600104, "Horizontol_drawbox", lambda: Horizontol_drawbox), _n_(600105, "BOX_LENGTH", lambda: BOX_LENGTH), fillBox = True)
        _l_(600107)

    for i in _c_(600110, _n_(600109, "range", lambda: range), 8):
        _l_(600122)

        fill += 1
        _l_(600111)
        if _n_(600112, "fill", lambda: fill) % 2 == 0:
            _l_(600121)

            _c_(600115, _n_(600113, "Vertical_drawbox", lambda: Vertical_drawbox), _n_(600114, "BOX_LENGTH", lambda: BOX_LENGTH),fillBox = False)
            _l_(600116)
        else:
            _c_(600119, _n_(600117, "Vertical_drawbox", lambda: Vertical_drawbox), _n_(600118, "BOX_LENGTH", lambda: BOX_LENGTH),fillBox = True)
            _l_(600120)