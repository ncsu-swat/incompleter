# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72214567/nameerror-name-not-defined-for-function-that-is-already-defined-above-the-line
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""
Created on Wed May  4 12:13:50 2022

% Problema Balisticii cu rezistenta aerului, Miron Alexandra, 222
"""
try:
    import numpy as np
    _l_(627484)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(627486)

except ImportError:
    pass
try:
    import math as math
    _l_(627488)

except ImportError:
    pass
#%%Ex 1- sol analitica - fara rezistenta aerului

def Problema_Balisticii(m,v0,theta0,g):
    _l_(627552)

    #b
    tmax=2*_n_(627489, "v0", lambda: v0)*_c_(627493, _a_(627491, _n_(627490, "np", lambda: np), "sin"), _n_(627492, "theta0", lambda: theta0))/_n_(627494, "g", lambda: g)
    _l_(627495)
    xmax=_n_(627496, "v0", lambda: v0)**2*_c_(627500, _a_(627498, _n_(627497, "np", lambda: np), "sin"), 2*_n_(627499, "theta0", lambda: theta0))/_n_(627501, "g", lambda: g)
    _l_(627502)
    _c_(627506, _n_(627503, "print", lambda: print), 'Distanta strabatuta este', _n_(627504, "xmax", lambda: xmax), 'si timpul de zbor este ', _n_(627505, "tmax", lambda: tmax))
    _l_(627507)
    t=_c_(627511, _a_(627509, _n_(627508, "np", lambda: np), "linspace"), 0,_n_(627510, "tmax", lambda: tmax),1000)
    _l_(627512)
    #discretizam intervalul de timp [0,tmax]
    #a
    x=_n_(627513, "v0", lambda: v0)*_c_(627517, _a_(627515, _n_(627514, "np", lambda: np), "cos"), _n_(627516, "theta0", lambda: theta0))*_n_(627518, "t", lambda: t)
    _l_(627519)
    y=_n_(627520, "v0", lambda: v0)*_c_(627524, _a_(627522, _n_(627521, "np", lambda: np), "sin"), _n_(627523, "theta0", lambda: theta0))*_n_(627525, "t", lambda: t)- _n_(627526, "g", lambda: g)*_n_(627527, "t", lambda: t)**2/2
    _l_(627528)
    #c ttmax=t tilda max
    ttmax=_n_(627529, "v0", lambda: v0)*_c_(627533, _a_(627531, _n_(627530, "np", lambda: np), "sin"), _n_(627532, "theta0", lambda: theta0))/_n_(627534, "g", lambda: g)
    _l_(627535)
    ymax=(_n_(627536, "v0", lambda: v0)*_c_(627540, _a_(627538, _n_(627537, "np", lambda: np), "sin"), _n_(627539, "theta0", lambda: theta0)))**2/(2*_n_(627541, "g", lambda: g))
    _l_(627542)
    _c_(627546, _n_(627543, "print", lambda: print), 'Inaltimea maxima este', _n_(627544, "ymax", lambda: ymax), 'si se atinge la momentul de timp t=',_n_(627545, "ttmax", lambda: ttmax))
    _l_(627547)
    aux = _n_(627548, "t", lambda: t),_n_(627549, "x", lambda: x),_n_(627550, "y", lambda: y)
    _l_(627551)
    
    return aux

#%% traiectorie-fara rezistenta aerului 
m=4
_l_(627553)
v0=10
_l_(627554)
g=9.81
_l_(627555)

t1,x1,y1=_c_(627562, _n_(627556, "Problema_Balisticii", lambda: Problema_Balisticii), _n_(627557, "m", lambda: m),_n_(627558, "v0", lambda: v0),_a_(627560, _n_(627559, "np", lambda: np), "pi")/6,_n_(627561, "g", lambda: g))
_l_(627563)
t2,x2,y2=_c_(627570, _n_(627564, "Problema_Balisticii", lambda: Problema_Balisticii), _n_(627565, "m", lambda: m),_n_(627566, "v0", lambda: v0),_a_(627568, _n_(627567, "np", lambda: np), "pi")/4,_n_(627569, "g", lambda: g))
_l_(627571)
t3,x3,y3=_c_(627578, _n_(627572, "Problema_Balisticii", lambda: Problema_Balisticii), _n_(627573, "m", lambda: m),_n_(627574, "v0", lambda: v0),_a_(627576, _n_(627575, "np", lambda: np), "pi")/3,_n_(627577, "g", lambda: g))
_l_(627579)
t4,x4,y4=_c_(627586, _n_(627580, "Problema_Balisticii", lambda: Problema_Balisticii), _n_(627581, "m", lambda: m),_n_(627582, "v0", lambda: v0),_a_(627584, _n_(627583, "np", lambda: np), "pi")/2.5,_n_(627585, "g", lambda: g))
_l_(627587)
t5,x5,y5=_c_(627594, _n_(627588, "Problema_Balisticii", lambda: Problema_Balisticii), _n_(627589, "m", lambda: m),_n_(627590, "v0", lambda: v0),_a_(627592, _n_(627591, "np", lambda: np), "pi")/2,_n_(627593, "g", lambda: g))
_l_(627595)

_c_(627598, _a_(627597, _n_(627596, "plt", lambda: plt), "figure"))
_l_(627599)
_c_(627604, _a_(627601, _n_(627600, "plt", lambda: plt), "plot"), _n_(627602, "x1", lambda: x1),_n_(627603, "y1", lambda: y1), label='$\pi/6$')
_l_(627605)
_c_(627610, _a_(627607, _n_(627606, "plt", lambda: plt), "plot"), _n_(627608, "x2", lambda: x2),_n_(627609, "y2", lambda: y2), label='$\pi/4$')
_l_(627611)
_c_(627616, _a_(627613, _n_(627612, "plt", lambda: plt), "plot"), _n_(627614, "x3", lambda: x3),_n_(627615, "y3", lambda: y3), label='$\pi/3$')
_l_(627617)
_c_(627622, _a_(627619, _n_(627618, "plt", lambda: plt), "plot"), _n_(627620, "x4", lambda: x4),_n_(627621, "y4", lambda: y4), label='$\pi/2.5$')
_l_(627623)
_c_(627628, _a_(627625, _n_(627624, "plt", lambda: plt), "plot"), _n_(627626, "x5", lambda: x5),_n_(627627, "y5", lambda: y5), label='$\pi/2$')
_l_(627629)
_c_(627632, _a_(627631, _n_(627630, "plt", lambda: plt), "legend"))
_l_(627633)
_c_(627636, _a_(627635, _n_(627634, "plt", lambda: plt), "title"), 'Problema balisticii fara rezistenta aerului')
_l_(627637)

#%% animatie miscare
_c_(627640, _a_(627639, _n_(627638, "plt", lambda: plt), "figure"))
_l_(627641)
_c_(627652, _a_(627643, _n_(627642, "plt", lambda: plt), "axis"), [0, _c_(627647, _a_(627645, _n_(627644, "np", lambda: np), "max"), _n_(627646, "x2", lambda: x2))+0.1,-0.1,_c_(627651, _a_(627649, _n_(627648, "np", lambda: np), "max"), _n_(627650, "y3", lambda: y3))+0.1])
_l_(627653)
for i in _c_(627658, _n_(627654, "range", lambda: range), _c_(627657, _n_(627655, "len", lambda: len), _n_(627656, "x1", lambda: x1))):
    _l_(627687)

    _c_(627665, _a_(627660, _n_(627659, "plt", lambda: plt), "plot"), _n_(627661, "x1", lambda: x1)[_n_(627662, "i", lambda: i)],_n_(627663, "y1", lambda: y1)[_n_(627664, "i", lambda: i)],'bo')
    _l_(627666)
    _c_(627673, _a_(627668, _n_(627667, "plt", lambda: plt), "plot"), _n_(627669, "x2", lambda: x2)[_n_(627670, "i", lambda: i)],_n_(627671, "y2", lambda: y2)[_n_(627672, "i", lambda: i)],'r*')
    _l_(627674)
    _c_(627681, _a_(627676, _n_(627675, "plt", lambda: plt), "plot"), _n_(627677, "x3", lambda: x3)[_n_(627678, "i", lambda: i)],_n_(627679, "y3", lambda: y3)[_n_(627680, "i", lambda: i)],'gp')
    _l_(627682)
    _c_(627685, _a_(627684, _n_(627683, "plt", lambda: plt), "pause"), 0.1)
    _l_(627686)
#%%
#sol numerica-sist de e.d.o
def Balistica_Euler_explicit_sist_Fara_rez(m,v0,theta0,g,t0,tf,h):
    _l_(627786)

    N=_c_(627693, _a_(627689, _n_(627688, "math", lambda: math), "floor"), (_n_(627690, "tf", lambda: tf)-_n_(627691, "t0", lambda: t0))/_n_(627692, "h", lambda: h))+1
    _l_(627694)
    t=_c_(627698, _a_(627696, _n_(627695, "np", lambda: np), "zeros"), _n_(627697, "N", lambda: N))
    _l_(627699)
    z1=_c_(627703, _a_(627701, _n_(627700, "np", lambda: np), "zeros"), _n_(627702, "N", lambda: N))
    _l_(627704)
    z2=_c_(627708, _a_(627706, _n_(627705, "np", lambda: np), "zeros"), _n_(627707, "N", lambda: N))
    _l_(627709)
    z3=_c_(627713, _a_(627711, _n_(627710, "np", lambda: np), "zeros"), _n_(627712, "N", lambda: N))
    _l_(627714)
    z4=_c_(627718, _a_(627716, _n_(627715, "np", lambda: np), "zeros"), _n_(627717, "N", lambda: N))
    _l_(627719)
    _n_(627720, "t", lambda: t)[0]=_n_(627721, "t0", lambda: t0)
    _l_(627722)
    _n_(627723, "z1", lambda: z1)[0]=0
    _l_(627724)
    _n_(627725, "z2", lambda: z2)[0]=_n_(627726, "v0", lambda: v0)*_c_(627730, _a_(627728, _n_(627727, "np", lambda: np), "cos"), _n_(627729, "theta0", lambda: theta0))
    _l_(627731)
    _n_(627732, "z3", lambda: z3)[0]=0
    _l_(627733)
    _n_(627734, "z4", lambda: z4)[0]=_n_(627735, "v0", lambda: v0)*_c_(627739, _a_(627737, _n_(627736, "np", lambda: np), "sin"), _n_(627738, "theta0", lambda: theta0))
    _l_(627740)
    for i in _c_(627743, _n_(627741, "range", lambda: range), 1,_n_(627742, "N", lambda: N)):
        _l_(627779)

        _n_(627744, "t", lambda: t)[_n_(627745, "i", lambda: i)]=_n_(627746, "t0", lambda: t0)+_n_(627747, "i", lambda: i)*_n_(627748, "h", lambda: h)
        _l_(627749)
        _n_(627750, "z1", lambda: z1)[_n_(627751, "i", lambda: i)]=_n_(627752, "z1", lambda: z1)[_n_(627753, "i", lambda: i)-1]+_n_(627754, "h", lambda: h)*_n_(627755, "z2", lambda: z2)[_n_(627756, "i", lambda: i)-1]
        _l_(627757)
        _n_(627758, "z2", lambda: z2)[_n_(627759, "i", lambda: i)]=_n_(627760, "z2", lambda: z2)[_n_(627761, "i", lambda: i)-1]+_n_(627762, "h", lambda: h)*0
        _l_(627763)
        _n_(627764, "z3", lambda: z3)[_n_(627765, "i", lambda: i)]=_n_(627766, "z3", lambda: z3)[_n_(627767, "i", lambda: i)-1]+_n_(627768, "h", lambda: h)*_n_(627769, "z4", lambda: z4)[_n_(627770, "i", lambda: i)-1]
        _l_(627771)
        _n_(627772, "z4", lambda: z4)[_n_(627773, "i", lambda: i)]=_n_(627774, "z4", lambda: z4)[_n_(627775, "i", lambda: i)-1]+_n_(627776, "h", lambda: h)*(-_n_(627777, "g", lambda: g))
        _l_(627778)
    aux = _n_(627780, "t", lambda: t), _n_(627781, "z1", lambda: z1),_n_(627782, "z2", lambda: z2),_n_(627783, "z3", lambda: z3),_n_(627784, "z4", lambda: z4)
    _l_(627785)
    return aux

#%%
#sol numerica-sist de e.d.o
def Balistica_Euler_explicit_sist_cu_rez(m,v0,theta0,g,t0,tf,h):
    _l_(627908)

    N=_c_(627792, _a_(627788, _n_(627787, "math", lambda: math), "floor"), (_n_(627789, "tf", lambda: tf)-_n_(627790, "t0", lambda: t0))/_n_(627791, "h", lambda: h))+1
    _l_(627793)
    k=_c_(627797, _n_(627794, "int", lambda: int), _c_(627796, _n_(627795, "input", lambda: input), "Coeficientul de rezistenta al aerului este: "))
    _l_(627798)
    if _n_(627799, "k", lambda: k) <= 0:
        _l_(627808)

        _c_(627801, _n_(627800, "print", lambda: print), "Coeficientul de rezistenta trebuie sa fie mai mare ca 0, reintroduceti")
        _l_(627802)
        k=_c_(627806, _n_(627803, "int", lambda: int), _c_(627805, _n_(627804, "input", lambda: input), "Coeficientul de rezistenta al aerului este: "))
        _l_(627807)
    t=_c_(627812, _a_(627810, _n_(627809, "np", lambda: np), "zeros"), _n_(627811, "N", lambda: N))
    _l_(627813)
    z1=_c_(627817, _a_(627815, _n_(627814, "np", lambda: np), "zeros"), _n_(627816, "N", lambda: N))
    _l_(627818)
    z2=_c_(627822, _a_(627820, _n_(627819, "np", lambda: np), "zeros"), _n_(627821, "N", lambda: N))
    _l_(627823)
    z3=_c_(627827, _a_(627825, _n_(627824, "np", lambda: np), "zeros"), _n_(627826, "N", lambda: N))
    _l_(627828)
    z4=_c_(627832, _a_(627830, _n_(627829, "np", lambda: np), "zeros"), _n_(627831, "N", lambda: N))
    _l_(627833)
    _n_(627834, "t", lambda: t)[0]=_n_(627835, "t0", lambda: t0)
    _l_(627836)
    _n_(627837, "z1", lambda: z1)[0]=0
    _l_(627838)
    _n_(627839, "z2", lambda: z2)[0]=_n_(627840, "v0", lambda: v0)*_c_(627844, _a_(627842, _n_(627841, "np", lambda: np), "cos"), _n_(627843, "theta0", lambda: theta0))
    _l_(627845)
    _n_(627846, "z3", lambda: z3)[0]=0
    _l_(627847)
    _n_(627848, "z4", lambda: z4)[0]=_n_(627849, "v0", lambda: v0)*_c_(627853, _a_(627851, _n_(627850, "np", lambda: np), "sin"), _n_(627852, "theta0", lambda: theta0))
    _l_(627854)
    for i in _c_(627857, _n_(627855, "range", lambda: range), 1,_n_(627856, "N", lambda: N)):
        _l_(627901)

        _n_(627858, "t", lambda: t)[_n_(627859, "i", lambda: i)]=_n_(627860, "t0", lambda: t0)+_n_(627861, "i", lambda: i)*_n_(627862, "h", lambda: h)
        _l_(627863)
        _n_(627864, "z1", lambda: z1)[_n_(627865, "i", lambda: i)]=_n_(627866, "z1", lambda: z1)[_n_(627867, "i", lambda: i)-1]+_n_(627868, "h", lambda: h)*_n_(627869, "z2", lambda: z2)[_n_(627870, "i", lambda: i)-1]
        _l_(627871)
        _n_(627872, "z2", lambda: z2)[_n_(627873, "i", lambda: i)]=_n_(627874, "z2", lambda: z2)[_n_(627875, "i", lambda: i)-1]+_n_(627876, "h", lambda: h)*(0-_n_(627877, "g", lambda: g)*_n_(627878, "k", lambda: k)**2*_n_(627879, "z2", lambda: z2)[_n_(627880, "i", lambda: i)-1])
        _l_(627881)
        _n_(627882, "z3", lambda: z3)[_n_(627883, "i", lambda: i)]=_n_(627884, "z3", lambda: z3)[_n_(627885, "i", lambda: i)-1]+_n_(627886, "h", lambda: h)*_n_(627887, "z4", lambda: z4)[_n_(627888, "i", lambda: i)-1]
        _l_(627889)
        _n_(627890, "z4", lambda: z4)[_n_(627891, "i", lambda: i)]=_n_(627892, "z4", lambda: z4)[_n_(627893, "i", lambda: i)-1]+_n_(627894, "h", lambda: h)*(-_n_(627895, "g", lambda: g)-_n_(627896, "g", lambda: g)*_n_(627897, "k", lambda: k)**2*_n_(627898, "z4", lambda: z4)[_n_(627899, "i", lambda: i)-1])
        _l_(627900)
    aux = _n_(627902, "t", lambda: t), _n_(627903, "z1", lambda: z1),_n_(627904, "z2", lambda: z2),_n_(627905, "z3", lambda: z3),_n_(627906, "z4", lambda: z4)
    _l_(627907)
    return aux

t0=0
_l_(627909)
tf=5
_l_(627910)
h=0.002
_l_(627911)
theta0=_a_(627913, _n_(627912, "np", lambda: np), "pi")/6
_l_(627914)
t,z1,z2,z3,z4=_c_(627923, _n_(627915, "Balistica_Euler_explicit_sist_cu_rez", lambda: Balistica_Euler_explicit_sist_cu_rez), _n_(627916, "m", lambda: m),_n_(627917, "v0", lambda: v0),_n_(627918, "theta0", lambda: theta0),_n_(627919, "g", lambda: g),_n_(627920, "t0", lambda: t0),_n_(627921, "tf", lambda: tf),_n_(627922, "h", lambda: h))
_l_(627924)
x=_n_(627925, "z1", lambda: z1)
_l_(627926)
y=_n_(627927, "z3", lambda: z3)
_l_(627928)

index=_c_(627932, _a_(627930, _n_(627929, "np", lambda: np), "where"), _n_(627931, "y", lambda: y)<0)[0][0]
_l_(627933)
_c_(627936, _a_(627935, _n_(627934, "plt", lambda: plt), "figure"))
_l_(627937)
_c_(627944, _a_(627939, _n_(627938, "plt", lambda: plt), "plot"), _n_(627940, "x", lambda: x)[:_n_(627941, "index", lambda: index)],_n_(627942, "y", lambda: y)[:_n_(627943, "index", lambda: index)])
_l_(627945)

t,z1,z2,z3,z4=_c_(627954, _n_(627946, "Balistica_Euler_explicit_sist_Fara_rez", lambda: Balistica_Euler_explicit_sist_Fara_rez), _n_(627947, "m", lambda: m),_n_(627948, "v0", lambda: v0),_n_(627949, "theta0", lambda: theta0),_n_(627950, "g", lambda: g),_n_(627951, "t0", lambda: t0),_n_(627952, "tf", lambda: tf),_n_(627953, "h", lambda: h))
_l_(627955)
x=_n_(627956, "z1", lambda: z1)
_l_(627957)
y=_n_(627958, "z3", lambda: z3)
_l_(627959)

index=_c_(627963, _a_(627961, _n_(627960, "np", lambda: np), "where"), _n_(627962, "y", lambda: y)<0)[0][0]
_l_(627964)
_c_(627967, _a_(627966, _n_(627965, "plt", lambda: plt), "figure"))
_l_(627968)
_c_(627975, _a_(627970, _n_(627969, "plt", lambda: plt), "plot"), _n_(627971, "x", lambda: x)[:_n_(627972, "index", lambda: index)],_n_(627973, "y", lambda: y)[:_n_(627974, "index", lambda: index)])
_l_(627976)