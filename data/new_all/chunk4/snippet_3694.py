# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69707447/attributeerror-list-object-has-no-attribute-write
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def modifytext2():
    _l_(644265)

    file1 = _c_(644246, _n_(644245, "open", lambda: open), 'data_user1.txt' , 'r') #read from txt file
    _l_(644247) #read from txt file
    f = _c_(644250, _a_(644249, _n_(644248, "file1", lambda: file1), "readlines"))
    _l_(644251)
    g = [_c_(644254, _a_(644253, _n_(644252, "i", lambda: i), "replace"), '@','---') for i in _n_(644255, "f", lambda: f)]
    _l_(644256)
    
    _c_(644259, _n_(644257, "print", lambda: print), _n_(644258, "g", lambda: g))
    _l_(644260)
    _c_(644263, _a_(644262, _n_(644261, "file1", lambda: file1), "close"))
    _l_(644264)

_c_(644267, _n_(644266, "modifytext2", lambda: modifytext2))
_l_(644268)