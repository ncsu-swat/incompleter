# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66407561/multiplication-of-matrix-in-python3-i-am-using-below-one-line-code-but-i-get-e
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(352527)

except ImportError:
    pass
try:
    import operator
    _l_(352529)

except ImportError:
    pass
def prod(iterable):
    _l_(352536)

    aux = _c_(352534, _n_(352530, "reduce", lambda: reduce), _a_(352532, _n_(352531, "operator", lambda: operator), "mul"),_n_(352533, "iterable", lambda: iterable),1)
    _l_(352535)
    return aux
X = [[1,7,3],
    [3,5,8],
    [6,8,9]]
_l_(352537)
Y = [[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]
_l_(352538)
resultTranspose=[_c_(352541, _n_(352539, "list", lambda: list), _n_(352540, "i", lambda: i)) for i in _c_(352544, _n_(352542, "zip", lambda: zip), *_n_(352543, "Y", lambda: Y))]
_l_(352545)

result=[[_c_(352559, _n_(352546, "list", lambda: list), _c_(352558, _n_(352547, "map", lambda: map), _n_(352548, "sum", lambda: sum),_c_(352557, _n_(352549, "list", lambda: list), _c_(352556, _n_(352550, "map", lambda: map), _n_(352551, "prod", lambda: prod),_c_(352555, _n_(352552, "zip", lambda: zip), _n_(352553, "i", lambda: i),_n_(352554, "j", lambda: j)))))) for j in _n_(352560, "resultTranspose", lambda: resultTranspose)]
for i in _n_(352561, "X", lambda: X)]
_l_(352562)