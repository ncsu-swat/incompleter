# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50939402/typeerror-range-object-does-not-support-item-assignment-how-to-fix-this
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
avail = _c_(369489, _n_(369487, "range", lambda: range), _n_(369488, "n_connections", lambda: n_connections))
_l_(369490)
for i in _c_(369493, _n_(369491, "range", lambda: range), 0,_n_(369492, "n_entities", lambda: n_entities)):
    _l_(369536)

    for j in _c_(369496, _n_(369494, "range", lambda: range), 0,_n_(369495, "n_connections", lambda: n_connections)):
        _l_(369535)

        if _n_(369497, "avail", lambda: avail)[_n_(369498, "j", lambda: j)] != -1:
            _l_(369534)

            if (((_n_(369499, "dat", lambda: dat)[_n_(369500, "j", lambda: j)][1] == 1)|((_n_(369501, "dat", lambda: dat)[_n_(369502, "j", lambda: j)][1] == 11))) & (_n_(369503, "dat", lambda: dat)[_n_(369504, "j", lambda: j)][2] == _n_(369505, "i", lambda: i))):
                _l_(369533)

                if ((_n_(369506, "dat", lambda: dat)[_n_(369507, "j", lambda: j)][3] == 3)|(_n_(369508, "dat", lambda: dat)[_n_(369509, "j", lambda: j)][3] == 13)):
                    _l_(369532)

                    _n_(369510, "avail", lambda: avail)[_n_(369511, "j", lambda: j)] = -1 # here error is coming how to fix this 
                    _l_(369512) # here error is coming how to fix this 
                   # n_connections = len(connectionx - 1)
                    for k in _c_(369515, _n_(369513, "range", lambda: range), 0,_n_(369514, "n_connections", lambda: n_connections)):
                        _l_(369531)

                        if _n_(369516, "avail", lambda: avail)[_n_(369517, "k", lambda: k)] != -1:
                            _l_(369530)

                            if (((_n_(369518, "dat", lambda: dat)[_n_(369519, "k", lambda: k)][1] == 3)|((_n_(369520, "dat", lambda: dat)[_n_(369521, "k", lambda: k)][1] == 13))) & (_n_(369522, "dat", lambda: dat)[_n_(369523, "k", lambda: k)][2] == _n_(369524, "dat", lambda: dat)[_n_(369525, "j", lambda: j)][4])):
                                _l_(369529)

                                _n_(369526, "avail", lambda: avail)[_n_(369527, "k", lambda: k)] = -1 # booking
                                _l_(369528) # booking