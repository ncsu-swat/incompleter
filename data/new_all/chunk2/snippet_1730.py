# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60097310/typeerror-unhashable-type-numpy-ndarray-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(426609, _n_(426608, "open", lambda: open), 'SJC324.txt') as f:
    _l_(426633)

    data=[]
    _l_(426610)
    for line in _n_(426611, "f", lambda: f):
        _l_(426628)

        x,y=_c_(426616, _a_(426615, _c_(426614, _a_(426613, _n_(426612, "line", lambda: line), "strip"), '\n'), "split"))
        _l_(426617)
        _c_(426626, _a_(426619, _n_(426618, "data", lambda: data), "append"), [_c_(426622, _n_(426620, "int", lambda: int), _n_(426621, "x", lambda: x)),_c_(426625, _n_(426623, "int", lambda: int), _n_(426624, "y", lambda: y))])
        _l_(426627)
    _c_(426631, _n_(426629, "initialisation", lambda: initialisation), _n_(426630, "data", lambda: data))
    _l_(426632)