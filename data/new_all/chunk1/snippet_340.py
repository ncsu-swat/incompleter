# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57125779/how-to-fix-typeerror-invalid-keyword-argument-for-sort
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def compare_points( p, q ):
    _l_(377569)

    if _n_(377552, "p", lambda: p)[0] < _n_(377553, "q", lambda: q)[0] or (_n_(377554, "p", lambda: p)[0] == _n_(377555, "q", lambda: q)[0] and _n_(377556, "p", lambda: p)[1] < _n_(377557, "q", lambda: q)[1]):
        _l_(377568)

        aux = -1
        _l_(377558)
        return aux
    elif _n_(377559, "p", lambda: p)[0] > _n_(377560, "q", lambda: q)[0] or (_n_(377561, "p", lambda: p)[0] == _n_(377562, "q", lambda: q)[0] and _n_(377563, "p", lambda: p)[1] > _n_(377564, "q", lambda: q)[1]):
        _l_(377567)

        aux = 1
        _l_(377565)
        return aux
    else:
        aux = 0
        _l_(377566)
        return aux

#print(compare_points( [1,3], [5,6])) # outputs -1
#print(compare_points( [1,3], [1,6])) # ouputs -1
#print(compare_points( [1,3], [1,3])) # outputs 0
#print(compare_points( [1,3], [0,3])) # outputs 1


L = [ [5,8], [5,2], [12, 3], [1,3], [10,2], [12,1], [12,3] ]
_l_(377570)
_c_(377574, _a_(377572, _n_(377571, "L", lambda: L), "sort"), cmp=_n_(377573, "compare_points", lambda: compare_points))
_l_(377575)
_c_(377578, _n_(377576, "print", lambda: print), _n_(377577, "L", lambda: L))
_l_(377579)