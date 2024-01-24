# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48377146/typeerror-numpy-ndarray-object-is-not-callable-in-my-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(365445)

except ImportError:
    pass
try:
    import csv
    _l_(365447)

except ImportError:
    pass

x = _c_(365451, _a_(365449, _n_(365448, "np", lambda: np), "genfromtxt"), "boston_housing.csv",dtype=_n_(365450, "float", lambda: float),delimiter=',',skip_header=1,usecols = (0,1,2,3,4,5,6,7,8,9,10,11,12))
_l_(365452)
xx = _n_(365453, "x", lambda: x)
_l_(365454)
y = _c_(365458, _a_(365456, _n_(365455, "np", lambda: np), "genfromtxt"), "boston_housing.csv",dtype=_n_(365457, "float", lambda: float),delimiter=',',skip_header=1,usecols = (13))
_l_(365459)

"""
ave = np.zeros(13)
sum = np.zeros(13)
mn = [x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5],x[0][6],x[0][7],x[0][8],x[0][9],x[0][10],x[0][11],x[0][12]]
mx = [x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5],x[0][6],x[0][7],x[0][8],x[0][9],x[0][10],x[0][11],x[0][12]]
for row in x:
    for i in range(0,13):
        sum[i] = sum[i] + row[i]
        mn[i] = min(mn[i],row[i])
        mx[i] = max(mx[i],row[i])
"""
alpha = 0.001
_l_(365460)
theta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
_l_(365461)
for ll in _c_(365463, _n_(365462, "range", lambda: range), 0,1):
    _l_(365582)

    temp = []
    _l_(365464)
    grad0 = (1.0/506)*_c_(365510, _n_(365465, "sum", lambda: sum), [(_n_(365466, "theta", lambda: theta)[0] + _n_(365467, "theta", lambda: theta)[1]*_n_(365468, "xx", lambda: xx)[_n_(365469, "i", lambda: i)][0] + _n_(365470, "theta", lambda: theta)[2]*_n_(365471, "xx", lambda: xx)[_n_(365472, "i", lambda: i)][1] + _n_(365473, "theta", lambda: theta)[3]*_n_(365474, "xx", lambda: xx)[_n_(365475, "i", lambda: i)][2] + _n_(365476, "theta", lambda: theta)[4]*_n_(365477, "xx", lambda: xx)[_n_(365478, "i", lambda: i)][3] + _n_(365479, "theta", lambda: theta)[5]*_n_(365480, "xx", lambda: xx)[_n_(365481, "i", lambda: i)][4] + _n_(365482, "theta", lambda: theta)[6]*_n_(365483, "xx", lambda: xx)[_n_(365484, "i", lambda: i)][5]
                        + _n_(365485, "theta", lambda: theta)[7]*_n_(365486, "xx", lambda: xx)[_n_(365487, "i", lambda: i)][6] + _n_(365488, "theta", lambda: theta)[8]*_n_(365489, "xx", lambda: xx)[_n_(365490, "i", lambda: i)][7] + _n_(365491, "theta", lambda: theta)[9]*_n_(365492, "xx", lambda: xx)[_n_(365493, "i", lambda: i)][8] + _n_(365494, "theta", lambda: theta)[10]*_n_(365495, "xx", lambda: xx)[_n_(365496, "i", lambda: i)][9] + _n_(365497, "theta", lambda: theta)[11]*_n_(365498, "xx", lambda: xx)[_n_(365499, "i", lambda: i)][10] + _n_(365500, "theta", lambda: theta)[12]*_n_(365501, "xx", lambda: xx)[_n_(365502, "i", lambda: i)][11]
                        + _n_(365503, "theta", lambda: theta)[13]*_n_(365504, "xx", lambda: xx)[_n_(365505, "i", lambda: i)][12] - _n_(365506, "y", lambda: y)[_n_(365507, "i", lambda: i)]) for i in _c_(365509, _n_(365508, "range", lambda: range), 506)])
    _l_(365511)
    _c_(365517, _a_(365513, _n_(365512, "temp", lambda: temp), "append"), _n_(365514, "theta", lambda: theta)[0] - (_n_(365515, "alpha", lambda: alpha) * _n_(365516, "grad0", lambda: grad0)))
    _l_(365518)
    for j in _c_(365520, _n_(365519, "range", lambda: range), 1,14):
        _l_(365579)

        grad0 = (1.0/506)*_c_(365569, _n_(365521, "sum", lambda: sum), [(_n_(365522, "theta", lambda: theta)[0] + _n_(365523, "theta", lambda: theta)[1]*_n_(365524, "xx", lambda: xx)[_n_(365525, "i", lambda: i)][0] + _n_(365526, "theta", lambda: theta)[2]*_n_(365527, "xx", lambda: xx)[_n_(365528, "i", lambda: i)][1] + _n_(365529, "theta", lambda: theta)[3]*_n_(365530, "xx", lambda: xx)[_n_(365531, "i", lambda: i)][2] + _n_(365532, "theta", lambda: theta)[4]*_n_(365533, "xx", lambda: xx)[_n_(365534, "i", lambda: i)][3] + _n_(365535, "theta", lambda: theta)[5]*_n_(365536, "xx", lambda: xx)[_n_(365537, "i", lambda: i)][4] + _n_(365538, "theta", lambda: theta)[6]*_n_(365539, "xx", lambda: xx)[_n_(365540, "i", lambda: i)][5]
                            + _n_(365541, "theta", lambda: theta)[7]*_n_(365542, "xx", lambda: xx)[_n_(365543, "i", lambda: i)][6] + _n_(365544, "theta", lambda: theta)[8]*_n_(365545, "xx", lambda: xx)[_n_(365546, "i", lambda: i)][7] + _n_(365547, "theta", lambda: theta)[9]*_n_(365548, "xx", lambda: xx)[_n_(365549, "i", lambda: i)][8] + _n_(365550, "theta", lambda: theta)[10]*_n_(365551, "xx", lambda: xx)[_n_(365552, "i", lambda: i)][9] + _n_(365553, "theta", lambda: theta)[11]*_n_(365554, "xx", lambda: xx)[_n_(365555, "i", lambda: i)][10] + _n_(365556, "theta", lambda: theta)[12]*_n_(365557, "xx", lambda: xx)[_n_(365558, "i", lambda: i)][11]
                            + _n_(365559, "theta", lambda: theta)[13]*_n_(365560, "xx", lambda: xx)[_n_(365561, "i", lambda: i)][12] - _n_(365562, "y", lambda: y)[_n_(365563, "i", lambda: i)])*_n_(365564, "xx", lambda: xx)[_n_(365565, "i", lambda: i)][_n_(365566, "j", lambda: j)-1] for i in _c_(365568, _n_(365567, "range", lambda: range), 506)])
        _l_(365570)
        _c_(365577, _a_(365572, _n_(365571, "temp", lambda: temp), "append"), _n_(365573, "theta", lambda: theta)[_n_(365574, "j", lambda: j)] - (_n_(365575, "alpha", lambda: alpha) * _n_(365576, "grad0", lambda: grad0)))
        _l_(365578)
    theta = _n_(365580, "temp", lambda: temp)
    _l_(365581)
yy = [0.02501,35,4.15,1,0.77,8.78,81.3,2.5051,24,666,17,382.8,11.48]
_l_(365583)
ans = 0
_l_(365584)
for i in _c_(365586, _n_(365585, "range", lambda: range), 0,13):
    _l_(365593)

    ans = _n_(365587, "ans", lambda: ans) + (_n_(365588, "yy", lambda: yy)[_n_(365589, "i", lambda: i)] * _n_(365590, "theta", lambda: theta)[_n_(365591, "i", lambda: i)+1])
    _l_(365592)
ans = _n_(365594, "ans", lambda: ans) + _n_(365595, "theta", lambda: theta)[0]
_l_(365596)
_c_(365599, _n_(365597, "print", lambda: print), _n_(365598, "theta", lambda: theta))
_l_(365600)
_c_(365603, _n_(365601, "print", lambda: print), _n_(365602, "ans", lambda: ans))
_l_(365604)