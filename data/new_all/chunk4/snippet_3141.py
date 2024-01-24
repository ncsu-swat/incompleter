# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41323659/typeerror-cannot-convert-the-series-to-type-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scipy.special as sps
    _l_(598516)

except ImportError:
    pass
try:
    import numpy as np
    _l_(598518)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(598520)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(598522)

except ImportError:
    pass
try:
    from scipy.stats import norm
    _l_(598524)

except ImportError:
    pass
try:
    from scipy.stats import gamma
    _l_(598526)

except ImportError:
    pass
try:
    from math import exp
    _l_(598528)

except ImportError:
    pass
########################################

### DADOS


dados= [2.3572833,0.7383197,14.1423990,2.0310423,7.1052727,1.8851099,12.9464459,4.4056236,1.0471756,0.4672236]
_l_(598529)

temp = _c_(598533, _a_(598531, _n_(598530, "pd", lambda: pd), "DataFrame"), _n_(598532, "dados", lambda: dados))
_l_(598534)

##########################################

def fx(x, t):
    _l_(598560)

    prod = 1.0
    _l_(598535)
    for i in _c_(598540, _n_(598536, "range", lambda: range), 0, _c_(598539, _n_(598537, "len", lambda: len), _n_(598538, "x", lambda: x))):
        _l_(598559)

        prod *= ((_n_(598541, "t", lambda: t)[0]/_n_(598542, "t", lambda: t)[1])* _c_(598547, _n_(598543, "exp", lambda: exp), - (_n_(598544, "x", lambda: x)[_n_(598545, "i", lambda: i)]/_n_(598546, "t", lambda: t)[1]) ) * _c_(598555, _n_(598548, "exp", lambda: exp), -_n_(598549, "t", lambda: t)[0] * _c_(598554, _n_(598550, "exp", lambda: exp), -(_n_(598551, "x", lambda: x)[_n_(598552, "i", lambda: i)]/_n_(598553, "t", lambda: t)[1]) ) ) )
        _l_(598556)
        aux = _n_(598557, "prod", lambda: prod)
        _l_(598558)
        return aux

#########################

def L(x, t):
    _l_(598570)

    n = _c_(598563, _n_(598561, "len", lambda: len), _n_(598562, "x", lambda: x))
    _l_(598564)
    aux = _c_(598568, _n_(598565, "fx", lambda: fx), _n_(598566, "x", lambda: x),_n_(598567, "t", lambda: t))
    _l_(598569)
    return aux


##########################################

###  MCMC

def mcmc(N=[], k={"t1": 1, "t2": 1}, x=[]):
    _l_(598788)

    chute = {"t1": [1], "t2": [1]}
    _l_(598571)
    M = _n_(598572, "chute", lambda: chute)
    _l_(598573)
    hiper = {"t1": [0.1, 0.1], "t2": [0.1, 0.1]} 
    _l_(598574) 
    contador = {"t1": [], "t2": []} 
    _l_(598575) 

    thetas = _c_(598578, _a_(598577, _n_(598576, "M", lambda: M), "keys"))
    _l_(598579)
    for i in _c_(598582, _n_(598580, "range", lambda: range), _n_(598581, "N", lambda: N) - 1):
        _l_(598764)

        for j in _n_(598583, "thetas", lambda: thetas):
            _l_(598732)


            if _n_(598584, "j", lambda: j) == "t1":
                _l_(598731)


                _c_(598596, _a_(598587, _n_(598585, "M", lambda: M)[_n_(598586, "j", lambda: j)], "append"), _c_(598595, _a_(598590, _a_(598589, _n_(598588, "np", lambda: np), "random"), "gamma"), shape = _n_(598591, "M", lambda: M)[_n_(598592, "j", lambda: j)][-1], scale = _n_(598593, "k", lambda: k)[_n_(598594, "j", lambda: j)]) )
                _l_(598597)
                lista = [ [ _n_(598598, "M", lambda: M)[_n_(598599, "l", lambda: l)][-1] for l in _n_(598600, "thetas", lambda: thetas)] , [ _n_(598601, "M", lambda: M)[_n_(598602, "l", lambda: l)][-1] if _n_(598603, "l", lambda: l)!=_n_(598604, "j", lambda: j) else _n_(598605, "M", lambda: M)[_n_(598606, "l", lambda: l)][-2] for l in _n_(598607, "thetas", lambda: thetas) ] ]
                _l_(598608)
                t1 =  _c_(598617, _a_(598610, _n_(598609, "gamma", lambda: gamma), "pdf"), _n_(598611, "M", lambda: M)[_n_(598612, "j", lambda: j)][-1], a = _n_(598613, "hiper", lambda: hiper)[_n_(598614, "j", lambda: j)][0], scale = _n_(598615, "hiper", lambda: hiper)[_n_(598616, "j", lambda: j)][1]) * _c_(598621, _n_(598618, "L", lambda: L), _n_(598619, "x", lambda: x), _n_(598620, "lista", lambda: lista)[0]) * _c_(598630, _a_(598623, _n_(598622, "gamma", lambda: gamma), "pdf"), _n_(598624, "M", lambda: M)[_n_(598625, "j", lambda: j)][-2], a = _n_(598626, "M", lambda: M)[_n_(598627, "j", lambda: j)][-1], scale = _n_(598628, "k", lambda: k)[_n_(598629, "j", lambda: j)])
                _l_(598631)
                t2 =  _c_(598640, _a_(598633, _n_(598632, "gamma", lambda: gamma), "pdf"), _n_(598634, "M", lambda: M)[_n_(598635, "j", lambda: j)][-2], a = _n_(598636, "hiper", lambda: hiper)[_n_(598637, "j", lambda: j)][0], scale = _n_(598638, "hiper", lambda: hiper)[_n_(598639, "j", lambda: j)][1]) * _c_(598644, _n_(598641, "L", lambda: L), _n_(598642, "x", lambda: x), _n_(598643, "lista", lambda: lista)[1]) * _c_(598653, _a_(598646, _n_(598645, "gamma", lambda: gamma), "pdf"), _n_(598647, "M", lambda: M)[_n_(598648, "j", lambda: j)][-1], a = _n_(598649, "M", lambda: M)[_n_(598650, "j", lambda: j)][-2], scale = _n_(598651, "k", lambda: k)[_n_(598652, "j", lambda: j)])          
                _l_(598654)          

                teste = (_n_(598655, "t1", lambda: t1)/_n_(598656, "t2", lambda: t2))
                _l_(598657)


            else:

                _c_(598669, _a_(598660, _n_(598658, "M", lambda: M)[_n_(598659, "j", lambda: j)], "append"), _c_(598668, _a_(598663, _a_(598662, _n_(598661, "np", lambda: np), "random"), "gamma"), shape = _n_(598664, "M", lambda: M)[_n_(598665, "j", lambda: j)][-1], scale = _n_(598666, "k", lambda: k)[_n_(598667, "j", lambda: j)]) )
                _l_(598670)
                lista = [ [ _n_(598671, "M", lambda: M)[_n_(598672, "l", lambda: l)][-1] for l in _n_(598673, "thetas", lambda: thetas)] , [ _n_(598674, "M", lambda: M)[_n_(598675, "l", lambda: l)][-1] if _n_(598676, "l", lambda: l)!=_n_(598677, "j", lambda: j) else _n_(598678, "M", lambda: M)[_n_(598679, "l", lambda: l)][-2] for l in _n_(598680, "thetas", lambda: thetas) ] ]
                _l_(598681)
                t1 =  _c_(598690, _a_(598683, _n_(598682, "gamma", lambda: gamma), "pdf"), _n_(598684, "M", lambda: M)[_n_(598685, "j", lambda: j)][-1], a = _n_(598686, "hiper", lambda: hiper)[_n_(598687, "j", lambda: j)][0], scale = _n_(598688, "hiper", lambda: hiper)[_n_(598689, "j", lambda: j)][1]) * _c_(598694, _n_(598691, "L", lambda: L), _n_(598692, "x", lambda: x), _n_(598693, "lista", lambda: lista)[0]) * _c_(598703, _a_(598696, _n_(598695, "gamma", lambda: gamma), "pdf"), _n_(598697, "M", lambda: M)[_n_(598698, "j", lambda: j)][-2], a = _n_(598699, "M", lambda: M)[_n_(598700, "j", lambda: j)][-1], scale = _n_(598701, "k", lambda: k)[_n_(598702, "j", lambda: j)])
                _l_(598704)
                t2 =  _c_(598713, _a_(598706, _n_(598705, "gamma", lambda: gamma), "pdf"), _n_(598707, "M", lambda: M)[_n_(598708, "j", lambda: j)][-2], a = _n_(598709, "hiper", lambda: hiper)[_n_(598710, "j", lambda: j)][0], scale = _n_(598711, "hiper", lambda: hiper)[_n_(598712, "j", lambda: j)][1]) * _c_(598717, _n_(598714, "L", lambda: L), _n_(598715, "x", lambda: x), _n_(598716, "lista", lambda: lista)[1]) * _c_(598726, _a_(598719, _n_(598718, "gamma", lambda: gamma), "pdf"), _n_(598720, "M", lambda: M)[_n_(598721, "j", lambda: j)][-1], a = _n_(598722, "M", lambda: M)[_n_(598723, "j", lambda: j)][-2], scale = _n_(598724, "k", lambda: k)[_n_(598725, "j", lambda: j)])          
                _l_(598727)          

                teste = (_n_(598728, "t1", lambda: t1)/_n_(598729, "t2", lambda: t2))
                _l_(598730)

        if (_c_(598735, _n_(598733, "min", lambda: min), 1, _n_(598734, "teste", lambda: teste)) < _c_(598739, _a_(598738, _a_(598737, _n_(598736, "np", lambda: np), "random"), "uniform"), low=0, high=1)) or _c_(598743, _a_(598741, _n_(598740, "np", lambda: np), "isinf"), _n_(598742, "teste", lambda: teste)) or _c_(598747, _a_(598745, _n_(598744, "np", lambda: np), "isnan"), _n_(598746, "teste", lambda: teste)):
            _l_(598763)

            _n_(598748, "M", lambda: M)[_n_(598749, "j", lambda: j)][-1] = _n_(598750, "M", lambda: M)[_n_(598751, "j", lambda: j)][-2]
            _l_(598752)
            _c_(598756, _a_(598755, _n_(598753, "contador", lambda: contador)[_n_(598754, "j", lambda: j)], "append"), 0)
            _l_(598757)
        else:
            _c_(598761, _a_(598760, _n_(598758, "contador", lambda: contador)[_n_(598759, "j", lambda: j)], "append"), 1)
            _l_(598762)

    M = _c_(598769, _a_(598767, _a_(598766, _n_(598765, "pd", lambda: pd), "DataFrame"), "from_dict"), _n_(598768, "M", lambda: M))
    _l_(598770)
    contador = _c_(598775, _a_(598773, _a_(598772, _n_(598771, "pd", lambda: pd), "DataFrame"), "from_dict"), _n_(598774, "contador", lambda: contador))
    _l_(598776)
    cont = _c_(598780, _a_(598778, _n_(598777, "contador", lambda: contador), "apply"), _n_(598779, "sum", lambda: sum))
    _l_(598781)
    _c_(598784, _n_(598782, "print", lambda: print), _n_(598783, "cont", lambda: cont))
    _l_(598785)
    aux = _n_(598786, "M", lambda: (M))
    _l_(598787)

    return aux

N = _c_(598792, _n_(598789, "int", lambda: int), _c_(598791, _n_(598790, "input", lambda: input), "Entre com o N: "))
_l_(598793)

MP = _c_(598797, _n_(598794, "mcmc", lambda: mcmc), N=_n_(598795, "N", lambda: N), x=_n_(598796, "temp", lambda: temp))
_l_(598798)

_c_(598801, _n_(598799, "print", lambda: print), _n_(598800, "MP", lambda: MP))
_l_(598802)