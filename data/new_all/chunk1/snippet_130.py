# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28502774/typeerror-cmp-is-an-invalid-keyword-argument-for-this-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def my_cmp(x,y):
    _l_(416080)

    counter = lambda x, items: _c_(416058, _n_(416048, "reduce", lambda: reduce), lambda a,b:_n_(416049, "a", lambda: a)+_n_(416050, "b", lambda: b), [_c_(416056, _a_(416054, _c_(416053, _n_(416051, "list", lambda: list), _n_(416052, "x", lambda: x)), "count"), _n_(416055, "xx", lambda: xx)) for xx in _n_(416057, "items", lambda: items)])
    _l_(416059)
    tmp =  _c_(416067, _n_(416060, "cmp", lambda: cmp), _c_(416063, _n_(416061, "counter", lambda: counter), _n_(416062, "x", lambda: x), [2,3,4,5]), _c_(416066, _n_(416064, "counter", lambda: counter), _n_(416065, "y", lambda: y), [2,3,4,5]))
    _l_(416068)
    aux = _n_(416069, "tmp", lambda: tmp) if _n_(416070, "tmp", lambda: tmp)!=0 else _c_(416078, _n_(416071, "cmp", lambda: cmp), _c_(416074, _n_(416072, "len", lambda: len), _n_(416073, "x", lambda: x)),_c_(416077, _n_(416075, "len", lambda: len), _n_(416076, "y", lambda: y))) 
    _l_(416079) 
    return aux 

for i, t in _c_(416095, _n_(416081, "enumerate", lambda: enumerate), [_n_(416082, "tmp", lambda: tmp)[0] for tmp in _c_(416094, _n_(416083, "sorted", lambda: sorted), _c_(416091, _n_(416084, "zip", lambda: zip), _n_(416085, "tracks", lambda: tracks), _a_(416090, _a_(416087, _n_(416086, "self", lambda: self), "mapping")[_n_(416088, "idx", lambda: idx)][_n_(416089, "track_selection", lambda: track_selection)[-1]], "iloc")[0]), cmp=_n_(416092, "my_cmp", lambda: my_cmp), key=lambda x:_n_(416093, "x", lambda: x)[1])]):
    _l_(416103)

    _n_(416096, "img", lambda: img)[_n_(416097, "i", lambda: i),:_c_(416100, _n_(416098, "len", lambda: len), _n_(416099, "t", lambda: t))] = _n_(416101, "t", lambda: t)
    _l_(416102)