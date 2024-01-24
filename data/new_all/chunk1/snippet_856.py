# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61584592/python3-typeerror-generator-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(408085)

except ImportError:
    pass
try:
    import numpy as np
    _l_(408087)

except ImportError:
    pass
try:
    from scipy import stats
    _l_(408089)

except ImportError:
    pass

max_event = 1000000
_l_(408090)
a_bin = 10  # number each bin from 0-->10 where cumulant calculation will be done
_l_(408091)  # number each bin from 0-->10 where cumulant calculation will be done

# Define 2D array for [ bin, here 0->10][proton in each bin]
pArray = (() for nn in _c_(408094, _n_(408092, "range", lambda: range), _n_(408093, "a_bin", lambda: a_bin)))
_l_(408095)
neve = (0 for mm in _c_(408098, _n_(408096, "range", lambda: range), _n_(408097, "a_bin", lambda: a_bin)))
_l_(408099)

for ii in _c_(408102, _n_(408100, "range", lambda: range), 0, _n_(408101, "max_event", lambda: max_event)):
    _l_(408136)


    _a = _c_(408106, _a_(408105, _a_(408104, _n_(408103, "np", lambda: np), "random"), "randint"), 10)
    _l_(408107)
    _b = _c_(408111, _a_(408110, _a_(408109, _n_(408108, "np", lambda: np), "random"), "randint"), 120)
    _l_(408112)

    if _n_(408113, "ii", lambda: ii) % 1000 == 0:
        _l_(408120)

        _c_(408118, _n_(408114, "print", lambda: print), _n_(408115, "ii", lambda: ii), _n_(408116, "_a", lambda: _a), _n_(408117, "_b", lambda: _b))
        _l_(408119)

    for j in _c_(408122, _n_(408121, "range", lambda: range), 0, 10):
        _l_(408135)

        if _n_(408123, "_a", lambda: _a) == _n_(408124, "j", lambda: j):
            _l_(408134)

            _c_(408129, _a_(408127, _n_(408125, "pArray", lambda: pArray)[_n_(408126, "j", lambda: j)], "append"), _n_(408128, "_b", lambda: _b))
            _l_(408130)
            _n_(408131, "neve", lambda: neve)[_n_(408132, "j", lambda: j)] += 1
            _l_(408133)


_c_(408138, _n_(408137, "print", lambda: print), "filling done!")
_l_(408139)

for k in _c_(408142, _n_(408140, "range", lambda: range), 0, _n_(408141, "a_bin", lambda: a_bin)):
    _l_(408165)


    mu2 = _c_(408148, _a_(408145, _a_(408144, _n_(408143, "stats", lambda: stats), "mstats"), "moment"), _n_(408146, "pArray", lambda: pArray)[_n_(408147, "k", lambda: k)], moment=2)
    _l_(408149)
    mu4 = _c_(408155, _a_(408152, _a_(408151, _n_(408150, "stats", lambda: stats), "mstats"), "moment"), _n_(408153, "pArray", lambda: pArray)[_n_(408154, "k", lambda: k)], moment=4)
    _l_(408156)

    _c_(408163, _n_(408157, "print", lambda: print), 'serial = %d, mu_2 = %f , mu_4 = %f, event = %d' %
          (_n_(408158, "k", lambda: k), _n_(408159, "mu2", lambda: mu2), _n_(408160, "mu4", lambda: mu4), _n_(408161, "neve", lambda: neve)[_n_(408162, "k", lambda: k)]))
    _l_(408164)

_c_(408167, _n_(408166, "print", lambda: print), "calculation done!")
_l_(408168)