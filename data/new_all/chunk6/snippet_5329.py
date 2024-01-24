# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66407561/multiplication-of-matrix-in-python3-i-am-using-below-one-line-code-but-i-get-e
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(339893)

except ImportError:
    pass
try:
    import operator
    _l_(339895)

except ImportError:
    pass
def prod(iterable):
    _l_(339902)

    aux = _c_(339900, _n_(339896, "reduce", lambda: reduce), _a_(339898, _n_(339897, "operator", lambda: operator), "mul"),_n_(339899, "iterable", lambda: iterable),1)
    _l_(339901)
    return aux
X = [[1,7,3],
    [3,5,8],
    [6,8,9]]
_l_(339903)
Y = [[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]
_l_(339904)
resultTranspose=[_c_(339907, _n_(339905, "list", lambda: list), _n_(339906, "i", lambda: i)) for i in _c_(339910, _n_(339908, "zip", lambda: zip), *_n_(339909, "Y", lambda: Y))]
_l_(339911)

result=[[_c_(339925, _n_(339912, "list", lambda: list), _c_(339924, _n_(339913, "map", lambda: map), _n_(339914, "sum", lambda: sum),_c_(339923, _n_(339915, "list", lambda: list), _c_(339922, _n_(339916, "map", lambda: map), _n_(339917, "prod", lambda: prod),_c_(339921, _n_(339918, "zip", lambda: zip), _n_(339919, "i", lambda: i),_n_(339920, "j", lambda: j)))))) for j in _n_(339926, "resultTranspose", lambda: resultTranspose)]
for i in _n_(339927, "X", lambda: X)]
_l_(339928)