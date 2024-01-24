# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76069108/running-into-a-typeerror-can-only-concatenate-list-not-int-to-list-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = 1
_l_(371833)

for i, sub_list in _c_(371836, _n_(371834, "enumerate", lambda: enumerate), _n_(371835, "example_list", lambda: example_list)[1:-1], start=1):
    _l_(371855)

    for j, entry in _c_(371839, _n_(371837, "enumerate", lambda: enumerate), _n_(371838, "sub_list", lambda: sub_list)[1:-1][1:-1], start=2):
        _l_(371854)

        if _n_(371840, "j", lambda: j) > 1:
            _l_(371849)

            _n_(371841, "example_list", lambda: example_list)[_n_(371842, "j", lambda: j)] = _c_(371847, _n_(371843, "round", lambda: round), (_n_(371844, "example_list", lambda: example_list)[_n_(371845, "j", lambda: j)] + _n_(371846, "x", lambda: x)), 3)
            _l_(371848)
        _n_(371850, "example_list", lambda: example_list)[_n_(371851, "i", lambda: i)][_n_(371852, "j", lambda: j)] += 1
        _l_(371853)
_c_(371858, _n_(371856, "print", lambda: print), _n_(371857, "example_list", lambda: example_list))
_l_(371859)