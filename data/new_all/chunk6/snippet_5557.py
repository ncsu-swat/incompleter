# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50939402/typeerror-range-object-does-not-support-item-assignment-how-to-fix-this
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
avail = _c_(343952, _n_(343950, "range", lambda: range), _n_(343951, "n_connections", lambda: n_connections))
_l_(343953)
for i in _c_(343956, _n_(343954, "range", lambda: range), 0,_n_(343955, "n_entities", lambda: n_entities)):
    _l_(343999)

    for j in _c_(343959, _n_(343957, "range", lambda: range), 0,_n_(343958, "n_connections", lambda: n_connections)):
        _l_(343998)

        if _n_(343960, "avail", lambda: avail)[_n_(343961, "j", lambda: j)] != -1:
            _l_(343997)

            if (((_n_(343962, "dat", lambda: dat)[_n_(343963, "j", lambda: j)][1] == 1)|((_n_(343964, "dat", lambda: dat)[_n_(343965, "j", lambda: j)][1] == 11))) & (_n_(343966, "dat", lambda: dat)[_n_(343967, "j", lambda: j)][2] == _n_(343968, "i", lambda: i))):
                _l_(343996)

                if ((_n_(343969, "dat", lambda: dat)[_n_(343970, "j", lambda: j)][3] == 3)|(_n_(343971, "dat", lambda: dat)[_n_(343972, "j", lambda: j)][3] == 13)):
                    _l_(343995)

                    _n_(343973, "avail", lambda: avail)[_n_(343974, "j", lambda: j)] = -1 # here error is coming how to fix this 
                    _l_(343975) # here error is coming how to fix this 
                   # n_connections = len(connectionx - 1)
                    for k in _c_(343978, _n_(343976, "range", lambda: range), 0,_n_(343977, "n_connections", lambda: n_connections)):
                        _l_(343994)

                        if _n_(343979, "avail", lambda: avail)[_n_(343980, "k", lambda: k)] != -1:
                            _l_(343993)

                            if (((_n_(343981, "dat", lambda: dat)[_n_(343982, "k", lambda: k)][1] == 3)|((_n_(343983, "dat", lambda: dat)[_n_(343984, "k", lambda: k)][1] == 13))) & (_n_(343985, "dat", lambda: dat)[_n_(343986, "k", lambda: k)][2] == _n_(343987, "dat", lambda: dat)[_n_(343988, "j", lambda: j)][4])):
                                _l_(343992)

                                _n_(343989, "avail", lambda: avail)[_n_(343990, "k", lambda: k)] = -1 # booking
                                _l_(343991) # booking