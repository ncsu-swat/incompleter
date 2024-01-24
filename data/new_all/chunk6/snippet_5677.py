# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48377146/typeerror-numpy-ndarray-object-is-not-callable-in-my-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(370707)

except ImportError:
    pass
try:
    import csv
    _l_(370709)

except ImportError:
    pass

x = _c_(370713, _a_(370711, _n_(370710, "np", lambda: np), "genfromtxt"), "boston_housing.csv",dtype=_n_(370712, "float", lambda: float),delimiter=',',skip_header=1,usecols = (0,1,2,3,4,5,6,7,8,9,10,11,12))
_l_(370714)

xx = _n_(370715, "x", lambda: x)
_l_(370716)
y = _c_(370720, _a_(370718, _n_(370717, "np", lambda: np), "genfromtxt"), "boston_housing.csv",dtype=_n_(370719, "float", lambda: float),delimiter=',',skip_header=1,usecols = (13))
_l_(370721)


ave = _c_(370724, _a_(370723, _n_(370722, "np", lambda: np), "zeros"), 13)
_l_(370725)
sum = _c_(370728, _a_(370727, _n_(370726, "np", lambda: np), "zeros"), 13)
_l_(370729)
mn = [_n_(370730, "x", lambda: x)[0][0],_n_(370731, "x", lambda: x)[0][1],_n_(370732, "x", lambda: x)[0][2],_n_(370733, "x", lambda: x)[0][3],_n_(370734, "x", lambda: x)[0][4],_n_(370735, "x", lambda: x)[0][5],_n_(370736, "x", lambda: x)[0][6],_n_(370737, "x", lambda: x)[0][7],_n_(370738, "x", lambda: x)[0][8],_n_(370739, "x", lambda: x)[0][9],_n_(370740, "x", lambda: x)[0][10],_n_(370741, "x", lambda: x)[0][11],_n_(370742, "x", lambda: x)[0][12]]
_l_(370743)
mx = [_n_(370744, "x", lambda: x)[0][0],_n_(370745, "x", lambda: x)[0][1],_n_(370746, "x", lambda: x)[0][2],_n_(370747, "x", lambda: x)[0][3],_n_(370748, "x", lambda: x)[0][4],_n_(370749, "x", lambda: x)[0][5],_n_(370750, "x", lambda: x)[0][6],_n_(370751, "x", lambda: x)[0][7],_n_(370752, "x", lambda: x)[0][8],_n_(370753, "x", lambda: x)[0][9],_n_(370754, "x", lambda: x)[0][10],_n_(370755, "x", lambda: x)[0][11],_n_(370756, "x", lambda: x)[0][12]]
_l_(370757)
for row in _n_(370758, "x", lambda: x):
    _l_(370787)

    for i in _c_(370760, _n_(370759, "range", lambda: range), 0,13):
        _l_(370786)

        _n_(370761, "sum", lambda: sum)[_n_(370762, "i", lambda: i)] = _n_(370763, "sum", lambda: sum)[_n_(370764, "i", lambda: i)] + _n_(370765, "row", lambda: row)[_n_(370766, "i", lambda: i)]
        _l_(370767)
        _n_(370768, "mn", lambda: mn)[_n_(370769, "i", lambda: i)] = _c_(370775, _n_(370770, "min", lambda: min), _n_(370771, "mn", lambda: mn)[_n_(370772, "i", lambda: i)],_n_(370773, "row", lambda: row)[_n_(370774, "i", lambda: i)])
        _l_(370776)
        _n_(370777, "mx", lambda: mx)[_n_(370778, "i", lambda: i)] = _c_(370784, _n_(370779, "max", lambda: max), _n_(370780, "mx", lambda: mx)[_n_(370781, "i", lambda: i)],_n_(370782, "row", lambda: row)[_n_(370783, "i", lambda: i)])
        _l_(370785)

alpha = 0.001
_l_(370788)
theta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
_l_(370789)
for ll in _c_(370791, _n_(370790, "range", lambda: range), 0,1):
    _l_(370910)

    temp = []
    _l_(370792)
    grad0 = (1.0/506)*_c_(370838, _n_(370793, "sum", lambda: sum), [(_n_(370794, "theta", lambda: theta)[0] + _n_(370795, "theta", lambda: theta)[1]*_n_(370796, "xx", lambda: xx)[_n_(370797, "i", lambda: i)][0] + _n_(370798, "theta", lambda: theta)[2]*_n_(370799, "xx", lambda: xx)[_n_(370800, "i", lambda: i)][1] + _n_(370801, "theta", lambda: theta)[3]*_n_(370802, "xx", lambda: xx)[_n_(370803, "i", lambda: i)][2] + _n_(370804, "theta", lambda: theta)[4]*_n_(370805, "xx", lambda: xx)[_n_(370806, "i", lambda: i)][3] + _n_(370807, "theta", lambda: theta)[5]*_n_(370808, "xx", lambda: xx)[_n_(370809, "i", lambda: i)][4] + _n_(370810, "theta", lambda: theta)[6]*_n_(370811, "xx", lambda: xx)[_n_(370812, "i", lambda: i)][5]
                        + _n_(370813, "theta", lambda: theta)[7]*_n_(370814, "xx", lambda: xx)[_n_(370815, "i", lambda: i)][6] + _n_(370816, "theta", lambda: theta)[8]*_n_(370817, "xx", lambda: xx)[_n_(370818, "i", lambda: i)][7] + _n_(370819, "theta", lambda: theta)[9]*_n_(370820, "xx", lambda: xx)[_n_(370821, "i", lambda: i)][8] + _n_(370822, "theta", lambda: theta)[10]*_n_(370823, "xx", lambda: xx)[_n_(370824, "i", lambda: i)][9] + _n_(370825, "theta", lambda: theta)[11]*_n_(370826, "xx", lambda: xx)[_n_(370827, "i", lambda: i)][10] + _n_(370828, "theta", lambda: theta)[12]*_n_(370829, "xx", lambda: xx)[_n_(370830, "i", lambda: i)][11]
                        + _n_(370831, "theta", lambda: theta)[13]*_n_(370832, "xx", lambda: xx)[_n_(370833, "i", lambda: i)][12] - _n_(370834, "y", lambda: y)[_n_(370835, "i", lambda: i)]) for i in _c_(370837, _n_(370836, "range", lambda: range), 506)])
    _l_(370839)
    _c_(370845, _a_(370841, _n_(370840, "temp", lambda: temp), "append"), _n_(370842, "theta", lambda: theta)[0] - (_n_(370843, "alpha", lambda: alpha) * _n_(370844, "grad0", lambda: grad0)))
    _l_(370846)
    for j in _c_(370848, _n_(370847, "range", lambda: range), 1,14):
        _l_(370907)

        grad0 = (1.0/506)*_c_(370897, _n_(370849, "sum", lambda: sum), [(_n_(370850, "theta", lambda: theta)[0] + _n_(370851, "theta", lambda: theta)[1]*_n_(370852, "xx", lambda: xx)[_n_(370853, "i", lambda: i)][0] + _n_(370854, "theta", lambda: theta)[2]*_n_(370855, "xx", lambda: xx)[_n_(370856, "i", lambda: i)][1] + _n_(370857, "theta", lambda: theta)[3]*_n_(370858, "xx", lambda: xx)[_n_(370859, "i", lambda: i)][2] + _n_(370860, "theta", lambda: theta)[4]*_n_(370861, "xx", lambda: xx)[_n_(370862, "i", lambda: i)][3] + _n_(370863, "theta", lambda: theta)[5]*_n_(370864, "xx", lambda: xx)[_n_(370865, "i", lambda: i)][4] + _n_(370866, "theta", lambda: theta)[6]*_n_(370867, "xx", lambda: xx)[_n_(370868, "i", lambda: i)][5]
                            + _n_(370869, "theta", lambda: theta)[7]*_n_(370870, "xx", lambda: xx)[_n_(370871, "i", lambda: i)][6] + _n_(370872, "theta", lambda: theta)[8]*_n_(370873, "xx", lambda: xx)[_n_(370874, "i", lambda: i)][7] + _n_(370875, "theta", lambda: theta)[9]*_n_(370876, "xx", lambda: xx)[_n_(370877, "i", lambda: i)][8] + _n_(370878, "theta", lambda: theta)[10]*_n_(370879, "xx", lambda: xx)[_n_(370880, "i", lambda: i)][9] + _n_(370881, "theta", lambda: theta)[11]*_n_(370882, "xx", lambda: xx)[_n_(370883, "i", lambda: i)][10] + _n_(370884, "theta", lambda: theta)[12]*_n_(370885, "xx", lambda: xx)[_n_(370886, "i", lambda: i)][11]
                            + _n_(370887, "theta", lambda: theta)[13]*_n_(370888, "xx", lambda: xx)[_n_(370889, "i", lambda: i)][12] - _n_(370890, "y", lambda: y)[_n_(370891, "i", lambda: i)])*_n_(370892, "xx", lambda: xx)[_n_(370893, "i", lambda: i)][_n_(370894, "j", lambda: j)-1] for i in _c_(370896, _n_(370895, "range", lambda: range), 506)])
        _l_(370898)
        _c_(370905, _a_(370900, _n_(370899, "temp", lambda: temp), "append"), _n_(370901, "theta", lambda: theta)[_n_(370902, "j", lambda: j)] - (_n_(370903, "alpha", lambda: alpha) * _n_(370904, "grad0", lambda: grad0)))
        _l_(370906)
    theta = _n_(370908, "temp", lambda: temp)
    _l_(370909)
yy = [0.02501,35,4.15,1,0.77,8.78,81.3,2.5051,24,666,17,382.8,11.48]
_l_(370911)
ans = 0
_l_(370912)
for i in _c_(370914, _n_(370913, "range", lambda: range), 0,13):
    _l_(370921)

    ans = _n_(370915, "ans", lambda: ans) + (_n_(370916, "yy", lambda: yy)[_n_(370917, "i", lambda: i)] * _n_(370918, "theta", lambda: theta)[_n_(370919, "i", lambda: i)+1])
    _l_(370920)
ans = _n_(370922, "ans", lambda: ans) + _n_(370923, "theta", lambda: theta)[0]
_l_(370924)
_c_(370927, _n_(370925, "print", lambda: print), _n_(370926, "theta", lambda: theta))
_l_(370928)
_c_(370931, _n_(370929, "print", lambda: print), _n_(370930, "ans", lambda: ans)) 
_l_(370932) 