# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62131223/typeerror-cannot-unpack-non-iterable-nonetype-object-while-using-operator-packa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import operator
    _l_(703647)

except ImportError:
    pass

class Point():
    _l_(703663)

    def __init__(self,x,y):
        _l_(703654)

        _n_(703648, "self", lambda: self).x=_n_(703649, "x", lambda: x)
        _l_(703650)
        _n_(703651, "self", lambda: self).y=_n_(703652, "y", lambda: y)
        _l_(703653)
    def __repr__(self):
        _l_(703662)

        aux = _c_(703660, _a_(703655, '<{0},{1}>', "format"), _a_(703657, _n_(703656, "self", lambda: self), "x"),_a_(703659, _n_(703658, "self", lambda: self), "y"))
        _l_(703661)
        return aux


def distance(a,b):
    _l_(703675)

    aux = _c_(703673, _n_(703664, "abs", lambda: abs), (_a_(703666, _n_(703665, "a", lambda: a), "x")-_a_(703668, _n_(703667, "b", lambda: b), "x"))**2+(_a_(703670, _n_(703669, "a", lambda: a), "y")-_a_(703672, _n_(703671, "b", lambda: b), "y"))**2)**.5
    _l_(703674)
    return aux

def closest(points):
    _l_(703823)

    n = _c_(703678, _n_(703676, "len", lambda: len), _n_(703677, "points", lambda: points))
    _l_(703679)
    if _n_(703680, "n", lambda: n)<=1:
        _l_(703822)

        _c_(703682, _n_(703681, "print", lambda: print), "invalid input")
        _l_(703683)
    elif _n_(703684, "n", lambda: n)==2:
        _l_(703821)

        aux = (_n_(703685, "points", lambda: points)[0],_n_(703686, "points", lambda: points)[1])
        _l_(703687)
        return aux
    elif _n_(703688, "n", lambda: n)==3:
        _l_(703820)

        (a,b,c)=_n_(703689, "points", lambda: points)
        _l_(703690)
        ret = (_n_(703691, "a", lambda: a),_n_(703692, "b", lambda: b)) if _c_(703696, _n_(703693, "distance", lambda: distance), _n_(703694, "a", lambda: a),_n_(703695, "b", lambda: b)) < _c_(703700, _n_(703697, "distance", lambda: distance), _n_(703698, "b", lambda: b),_n_(703699, "c", lambda: c)) else (_n_(703701, "a", lambda: a),_n_(703702, "c", lambda: c))
        _l_(703703)
        ret = (_n_(703704, "ret", lambda: ret)[0],_n_(703705, "ret", lambda: ret)[1]) if _c_(703709, _n_(703706, "distance", lambda: distance), _n_(703707, "ret", lambda: ret)[0],_n_(703708, "ret", lambda: ret)[1])<_c_(703713, _n_(703710, "distance", lambda: distance), _n_(703711, "b", lambda: b),_n_(703712, "c", lambda: c)) else (_n_(703714, "b", lambda: b),_n_(703715, "c", lambda: c))
        _l_(703716)
    else:
        points = _c_(703722, _n_(703717, "sorted", lambda: sorted), _n_(703718, "points", lambda: points),key=_c_(703721, _a_(703720, _n_(703719, "operator", lambda: operator), "attrgetter"), 'x'))
        _l_(703723)
        leftPoints = _n_(703724, "points", lambda: points)[:_n_(703725, "n", lambda: n)//2]
        _l_(703726)
        rightPoints = _n_(703727, "points", lambda: points)[_n_(703728, "n", lambda: n)//2:]
        _l_(703729)
        (left_a,left_b) = _c_(703732, _n_(703730, "closest", lambda: closest), _n_(703731, "leftPoints", lambda: leftPoints))
        _l_(703733)
        (right_a,right_b) = _c_(703736, _n_(703734, "closest", lambda: closest), _n_(703735, "rightPoints", lambda: rightPoints))
        _l_(703737)
        d = _c_(703747, _n_(703738, "min", lambda: min), _c_(703742, _n_(703739, "distance", lambda: distance), _n_(703740, "left_a", lambda: left_a),_n_(703741, "left_b", lambda: left_b)),_c_(703746, _n_(703743, "distance", lambda: distance), _n_(703744, "right_a", lambda: right_a),_n_(703745, "right_b", lambda: right_b)))
        _l_(703748)
        mid = (_a_(703751, _n_(703749, "points", lambda: points)[_n_(703750, "n", lambda: n)//2], "x")+_a_(703754, _n_(703752, "points", lambda: points)[_n_(703753, "n", lambda: n)//2+1], "x"))/2
        _l_(703755)
        midRange = _c_(703766, _n_(703756, "filter", lambda: filter), lambda pt:_a_(703758, _n_(703757, "pt", lambda: pt), "x") >=_n_(703759, "mid", lambda: mid)-_n_(703760, "d", lambda: d) and _a_(703762, _n_(703761, "pt", lambda: pt), "x")<=_n_(703763, "mid", lambda: mid)+_n_(703764, "d", lambda: d),_n_(703765, "points", lambda: points))
        _l_(703767)
        midRange = _c_(703773, _n_(703768, "sorted", lambda: sorted), _n_(703769, "midRange", lambda: midRange),key=_c_(703772, _a_(703771, _n_(703770, "operator", lambda: operator), "attrgetter"), 'y'))
        _l_(703774)
        ret = None
        _l_(703775)
        localMin = None
        _l_(703776)
        for i in _c_(703781, _n_(703777, "range", lambda: range), _c_(703780, _n_(703778, "len", lambda: len), _n_(703779, "midRange", lambda: midRange))):
            _l_(703817)

            a = _n_(703782, "midRange", lambda: midRange)[_n_(703783, "i", lambda: i)]
            _l_(703784)
            for j in _c_(703790, _n_(703785, "range", lambda: range), _n_(703786, "i", lambda: i)+1,_c_(703789, _n_(703787, "len", lambda: len), _n_(703788, "midRange", lambda: midRange))):
                _l_(703816)

                b = _n_(703791, "midRange", lambda: midRange)[_n_(703792, "j", lambda: j)]
                _l_(703793)
                if(not _n_(703794, "ret", lambda: ret))or (_c_(703800, _n_(703795, "abs", lambda: abs), _a_(703797, _n_(703796, "a", lambda: a), "y")-_a_(703799, _n_(703798, "b", lambda: b), "y"))<=_n_(703801, "d", lambda: d) and _c_(703805, _n_(703802, "distance", lambda: distance), _n_(703803, "a", lambda: a),_n_(703804, "b", lambda: b))<_n_(703806, "localMin", lambda: localMin)):
                    _l_(703815)

                    localMin= _c_(703810, _n_(703807, "distance", lambda: distance), _n_(703808, "a", lambda: a),_n_(703809, "c", lambda: c))
                    _l_(703811)
                    ret = (_n_(703812, "a", lambda: a),_n_(703813, "b", lambda: b))
                    _l_(703814)
        aux = _n_(703818, "ret", lambda: ret)
        _l_(703819)
        return aux
points =[_c_(703825, _n_(703824, "Point", lambda: Point), 1,2),_c_(703827, _n_(703826, "Point", lambda: Point), 0,0),_c_(703829, _n_(703828, "Point", lambda: Point), 3,6),_c_(703831, _n_(703830, "Point", lambda: Point), 4,7),_c_(703833, _n_(703832, "Point", lambda: Point), 5,5),_c_(703835, _n_(703834, "Point", lambda: Point), 8,4),_c_(703837, _n_(703836, "Point", lambda: Point), 2,9),_c_(703839, _n_(703838, "Point", lambda: Point), 4,5),_c_(703841, _n_(703840, "Point", lambda: Point), 8,1),_c_(703843, _n_(703842, "Point", lambda: Point), 4,3),_c_(703845, _n_(703844, "Point", lambda: Point), 3,3)]
_l_(703846)
_c_(703851, _n_(703847, "print", lambda: print), _c_(703850, _n_(703848, "closest", lambda: closest), _n_(703849, "points", lambda: points)))
_l_(703852)