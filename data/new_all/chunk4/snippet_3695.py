# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69707447/attributeerror-list-object-has-no-attribute-write
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def modifytext2():
    _l_(629005)

    file1 = _c_(628980, _n_(628979, "open", lambda: open), 'data_user1.txt' , 'r') #read from txt file
    _l_(628981) #read from txt file
    f = _c_(628984, _a_(628983, _n_(628982, "file1", lambda: file1), "readlines"))
    _l_(628985)
    g = [_c_(628988, _a_(628987, _n_(628986, "i", lambda: i), "replace"), '@','---') for i in _n_(628989, "f", lambda: f)]
    _l_(628990)
    for x in _n_(628991, "g", lambda: g):
        _l_(628996)

        _c_(628994, _a_(628993, _n_(628992, "g", lambda: g), "write"), '\n')
        _l_(628995)
    _c_(628999, _n_(628997, "print", lambda: print), _n_(628998, "x", lambda: x))
    _l_(629000)
    _c_(629003, _a_(629002, _n_(629001, "file1", lambda: file1), "close"))
    _l_(629004)

_c_(629007, _n_(629006, "modifytext2", lambda: modifytext2))
_l_(629008)