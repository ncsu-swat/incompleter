# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45479406/transferring-int-values-into-dict-typeerror-int-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fwd = {1:1, 2:10, 3:100, 5:10000, 103: 103, 204:204, 205:205, 387:387}
_l_(685922)


fragment_dic = {}
_l_(685923)
count = 0
_l_(685924)

for fragment_num in _c_(685926, _n_(685925, "range", lambda: range), 0, 388, 1):
    _l_(685957)

    for pos in _c_(685928, _n_(685927, "range", lambda: range), 1,101, 1):
        _l_(685956)

        if _n_(685929, "fwd", lambda: fwd) == _n_(685930, "int", lambda: int):
            _l_(685944)

            _c_(685932, _n_(685931, "print", lambda: print))
            _l_(685933)
            genomic_position = _n_(685934, "fragment_num", lambda: fragment_num)*100 + _n_(685935, "pos", lambda: pos)
            _l_(685936)
            count += _n_(685937, "fwd", lambda: fwd)[_n_(685938, "genomic_position", lambda: genomic_position)] 
            _l_(685939) 
        elif _n_(685940, "fwd", lambda: fwd) != _n_(685941, "int", lambda: int):
            _l_(685943)

            pass
            _l_(685942)
        _n_(685945, "fragment_dic", lambda: fragment_dic)[_n_(685946, "fragment_num", lambda: fragment_num)] = _n_(685947, "count", lambda: count)
        _l_(685948)
        count = 0
        _l_(685949)
        for i in _n_(685950, "fwd", lambda: fwd):
            _l_(685955)

            _n_(685951, "fwd", lambda: fwd)[_n_(685952, "fragment_dic", lambda: fragment_dic)] = _n_(685953, "i", lambda: i)[0]
            _l_(685954)