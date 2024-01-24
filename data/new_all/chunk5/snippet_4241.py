# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60880915/typeerror-int-object-is-not-subscriptable-is-being-shown-even-though-the-vari
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def solution(l):
    _l_(697694)

    if 1 in _n_(697647, "l", lambda: l):
        _l_(697693)

        _c_(697653, _a_(697649, _n_(697648, "l", lambda: l), "pop"), _c_(697652, _a_(697651, _n_(697650, "l", lambda: l), "index"), 1))
        _l_(697654)
        k=[[_c_(697657, _n_(697655, "min", lambda: min), _n_(697656, "l", lambda: l))]]
        _l_(697658)
        _c_(697667, _a_(697660, _n_(697659, "l", lambda: l), "pop"), _c_(697666, _a_(697662, _n_(697661, "l", lambda: l), "index"), _c_(697665, _n_(697663, "min", lambda: min), _n_(697664, "l", lambda: l))))
        _l_(697668)
        for a in _n_(697669, "l", lambda: l):
            _l_(697688)

            for index,i in _c_(697672, _n_(697670, "enumerate", lambda: enumerate), _n_(697671, "k", lambda: k)):
                _l_(697687)

                if _n_(697673, "a", lambda: a)%_n_(697674, "i", lambda: i)[0]==0:
                    _l_(697686)

                    _c_(697679, _a_(697677, _n_(697675, "k", lambda: k)[_n_(697676, "index", lambda: index)], "append"), _n_(697678, "a", lambda: a))
                    _l_(697680)
                else:
                    _c_(697684, _a_(697682, _n_(697681, "k", lambda: k), "append"), _n_(697683, "a", lambda: a))
                    _l_(697685)
        _c_(697691, _n_(697689, "print", lambda: print), _n_(697690, "k", lambda: k))
        _l_(697692)

_c_(697696, _n_(697695, "solution", lambda: solution), [1, 2, 3, 4, 5, 6])
_l_(697697)