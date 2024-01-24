# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62131223/typeerror-cannot-unpack-non-iterable-nonetype-object-while-using-operator-packa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import operator
    _l_(706900)

except ImportError:
    pass

class Point():
    _l_(706916)

    def __init__(self,x,y):
        _l_(706907)

        _n_(706901, "self", lambda: self).x=_n_(706902, "x", lambda: x)
        _l_(706903)
        _n_(706904, "self", lambda: self).y=_n_(706905, "y", lambda: y)
        _l_(706906)
    def __repr__(self):
        _l_(706915)

        aux = _c_(706913, _a_(706908, '<{0},{1}>', "format"), _a_(706910, _n_(706909, "self", lambda: self), "x"),_a_(706912, _n_(706911, "self", lambda: self), "y"))
        _l_(706914)
        return aux


def distance(a,b):
    _l_(706928)

    aux = _c_(706926, _n_(706917, "abs", lambda: abs), (_a_(706919, _n_(706918, "a", lambda: a), "x")-_a_(706921, _n_(706920, "b", lambda: b), "x"))**2+(_a_(706923, _n_(706922, "a", lambda: a), "y")-_a_(706925, _n_(706924, "b", lambda: b), "y"))**2)**.5
    _l_(706927)
    return aux

def closest(points):
    _l_(707076)

    n = _c_(706931, _n_(706929, "len", lambda: len), _n_(706930, "points", lambda: points))
    _l_(706932)
    if _n_(706933, "n", lambda: n)<=1:
        _l_(707075)

        _c_(706935, _n_(706934, "print", lambda: print), "invalid input")
        _l_(706936)
    elif _n_(706937, "n", lambda: n)==2:
        _l_(707074)

        aux = (_n_(706938, "points", lambda: points)[0],_n_(706939, "points", lambda: points)[1])
        _l_(706940)
        return aux
    elif _n_(706941, "n", lambda: n)==3:
        _l_(707073)

        (a,b,c)=_n_(706942, "points", lambda: points)
        _l_(706943)
        ret = (_n_(706944, "a", lambda: a),_n_(706945, "b", lambda: b)) if _c_(706949, _n_(706946, "distance", lambda: distance), _n_(706947, "a", lambda: a),_n_(706948, "b", lambda: b)) < _c_(706953, _n_(706950, "distance", lambda: distance), _n_(706951, "b", lambda: b),_n_(706952, "c", lambda: c)) else (_n_(706954, "a", lambda: a),_n_(706955, "c", lambda: c))
        _l_(706956)
        ret = (_n_(706957, "ret", lambda: ret)[0],_n_(706958, "ret", lambda: ret)[1]) if _c_(706962, _n_(706959, "distance", lambda: distance), _n_(706960, "ret", lambda: ret)[0],_n_(706961, "ret", lambda: ret)[1])<_c_(706966, _n_(706963, "distance", lambda: distance), _n_(706964, "b", lambda: b),_n_(706965, "c", lambda: c)) else (_n_(706967, "b", lambda: b),_n_(706968, "c", lambda: c))
        _l_(706969)
    else:
        points = _c_(706975, _n_(706970, "sorted", lambda: sorted), _n_(706971, "points", lambda: points),key=_c_(706974, _a_(706973, _n_(706972, "operator", lambda: operator), "attrgetter"), 'x'))
        _l_(706976)
        leftPoints = _n_(706977, "points", lambda: points)[:_n_(706978, "n", lambda: n)//2]
        _l_(706979)
        rightPoints = _n_(706980, "points", lambda: points)[_n_(706981, "n", lambda: n)//2:]
        _l_(706982)
        (left_a,left_b) = _c_(706985, _n_(706983, "closest", lambda: closest), _n_(706984, "leftPoints", lambda: leftPoints))
        _l_(706986)
        (right_a,right_b) = _c_(706989, _n_(706987, "closest", lambda: closest), _n_(706988, "rightPoints", lambda: rightPoints))
        _l_(706990)
        d = _c_(707000, _n_(706991, "min", lambda: min), _c_(706995, _n_(706992, "distance", lambda: distance), _n_(706993, "left_a", lambda: left_a),_n_(706994, "left_b", lambda: left_b)),_c_(706999, _n_(706996, "distance", lambda: distance), _n_(706997, "right_a", lambda: right_a),_n_(706998, "right_b", lambda: right_b)))
        _l_(707001)
        mid = (_a_(707004, _n_(707002, "points", lambda: points)[_n_(707003, "n", lambda: n)//2], "x")+_a_(707007, _n_(707005, "points", lambda: points)[_n_(707006, "n", lambda: n)//2+1], "x"))/2
        _l_(707008)
        midRange = _c_(707019, _n_(707009, "filter", lambda: filter), lambda pt:_a_(707011, _n_(707010, "pt", lambda: pt), "x") >=_n_(707012, "mid", lambda: mid)-_n_(707013, "d", lambda: d) and _a_(707015, _n_(707014, "pt", lambda: pt), "x")<=_n_(707016, "mid", lambda: mid)+_n_(707017, "d", lambda: d),_n_(707018, "points", lambda: points))
        _l_(707020)
        midRange = _c_(707026, _n_(707021, "sorted", lambda: sorted), _n_(707022, "midRange", lambda: midRange),key=_c_(707025, _a_(707024, _n_(707023, "operator", lambda: operator), "attrgetter"), 'y'))
        _l_(707027)
        ret = None
        _l_(707028)
        localMin = None
        _l_(707029)
        for i in _c_(707034, _n_(707030, "range", lambda: range), _c_(707033, _n_(707031, "len", lambda: len), _n_(707032, "midRange", lambda: midRange))):
            _l_(707070)

            a = _n_(707035, "midRange", lambda: midRange)[_n_(707036, "i", lambda: i)]
            _l_(707037)
            for j in _c_(707043, _n_(707038, "range", lambda: range), _n_(707039, "i", lambda: i)+1,_c_(707042, _n_(707040, "len", lambda: len), _n_(707041, "midRange", lambda: midRange))):
                _l_(707069)

                b = _n_(707044, "midRange", lambda: midRange)[_n_(707045, "j", lambda: j)]
                _l_(707046)
                if(not _n_(707047, "ret", lambda: ret))or (_c_(707053, _n_(707048, "abs", lambda: abs), _a_(707050, _n_(707049, "a", lambda: a), "y")-_a_(707052, _n_(707051, "b", lambda: b), "y"))<=_n_(707054, "d", lambda: d) and _c_(707058, _n_(707055, "distance", lambda: distance), _n_(707056, "a", lambda: a),_n_(707057, "b", lambda: b))<_n_(707059, "localMin", lambda: localMin)):
                    _l_(707068)

                    localMin= _c_(707063, _n_(707060, "distance", lambda: distance), _n_(707061, "a", lambda: a),_n_(707062, "c", lambda: c))
                    _l_(707064)
                    ret = (_n_(707065, "a", lambda: a),_n_(707066, "b", lambda: b))
                    _l_(707067)
        aux = _n_(707071, "ret", lambda: ret)
        _l_(707072)
        return aux
points =[_c_(707078, _n_(707077, "Point", lambda: Point), 1,2),_c_(707080, _n_(707079, "Point", lambda: Point), 0,0),_c_(707082, _n_(707081, "Point", lambda: Point), 3,6),_c_(707084, _n_(707083, "Point", lambda: Point), 4,7),_c_(707086, _n_(707085, "Point", lambda: Point), 5,5),_c_(707088, _n_(707087, "Point", lambda: Point), 8,4),_c_(707090, _n_(707089, "Point", lambda: Point), 2,9),_c_(707092, _n_(707091, "Point", lambda: Point), 4,5),_c_(707094, _n_(707093, "Point", lambda: Point), 8,1),_c_(707096, _n_(707095, "Point", lambda: Point), 4,3),_c_(707098, _n_(707097, "Point", lambda: Point), 3,3)]
_l_(707099)
_c_(707104, _n_(707100, "print", lambda: print), _c_(707103, _n_(707101, "closest", lambda: closest), _n_(707102, "points", lambda: points)))
_l_(707105)