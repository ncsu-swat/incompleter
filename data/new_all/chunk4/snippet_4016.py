# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63684600/typeerror-float-argument-must-be-a-string-or-a-number-not-tuple-valueerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def integrand_x1(x, Kte_1, Ktc_1, Kae_1, Kac_1, Kre_1, Krc_1, Wdz):
    _l_(630691)

    r = 0.0002
    _l_(630633)
    f = 2/360*10**(-5)
    _l_(630634)
    S = _n_(630635, "r", lambda: r) + _n_(630636, "f", lambda: f)*_c_(630639, _n_(630637, "sin", lambda: sin), _n_(630638, "x", lambda: x)) - _c_(630646, _n_(630640, "sqrt", lambda: sqrt), _n_(630641, "r", lambda: r)**2 - (_n_(630642, "f", lambda: f)**2)*_c_(630645, _n_(630643, "cos", lambda: cos), _n_(630644, "x", lambda: x))**2)
    _l_(630647)
    
    dFa_1 = (_n_(630648, "Kac_1", lambda: Kac_1)*_n_(630649, "S", lambda: S) + _n_(630650, "Kae_1", lambda: Kae_1))*_n_(630651, "Wdz", lambda: Wdz)
    _l_(630652)
    dFr_1 = (_n_(630653, "Krc_1", lambda: Krc_1)*_n_(630654, "S", lambda: S) + _n_(630655, "Kre_1", lambda: Kre_1))*_n_(630656, "Wdz", lambda: Wdz)
    _l_(630657)
    dFt_1 = (_n_(630658, "Ktc_1", lambda: Ktc_1)*_n_(630659, "S", lambda: S) + _n_(630660, "Kte_1", lambda: Kte_1))*_n_(630661, "Wdz", lambda: Wdz)
    _l_(630662)
    aux = (_c_(630665, _n_(630663, "cos", lambda: cos), 30*_n_(630664, "pi", lambda: pi)/180)*_n_(630666, "dFa_1", lambda: dFa_1) + _c_(630669, _n_(630667, "sin", lambda: sin), 30*_n_(630668, "pi", lambda: pi)/180)*_c_(630672, _n_(630670, "cos", lambda: cos), 5.4*_n_(630671, "pi", lambda: pi)/180)*_n_(630673, "dFr_1", lambda: dFr_1) - _c_(630676, _n_(630674, "sin", lambda: sin), 30*_n_(630675, "pi", lambda: pi)/180)*_c_(630679, _n_(630677, "sin", lambda: sin), 5.4*_n_(630678, "pi", lambda: pi)/180)*_n_(630680, "dFt_1", lambda: dFt_1))/(_c_(630683, _n_(630681, "cos", lambda: cos), 30*_n_(630682, "pi", lambda: pi)/180)**2 + _c_(630686, _n_(630684, "sin", lambda: sin), 30*_n_(630685, "pi", lambda: pi)/180)**2*_c_(630689, _n_(630687, "cos", lambda: cos), 2*5.4*_n_(630688, "pi", lambda: pi)/180))
    _l_(630690)
    
    return aux
def integrand_x2(x, Kte_2, Ktc_2, Kae_2, Kac_2, Kre_2, Krc_2, Wdz):
    _l_(630750)

    r = 0.0002
    _l_(630692)
    f = 2/360*10**(-5)
    _l_(630693)
    S = _n_(630694, "r", lambda: r) + _n_(630695, "f", lambda: f)*_c_(630698, _n_(630696, "sin", lambda: sin), _n_(630697, "x", lambda: x)) - _c_(630705, _n_(630699, "sqrt", lambda: sqrt), _n_(630700, "r", lambda: r)**2 - (_n_(630701, "f", lambda: f)**2)*_c_(630704, _n_(630702, "cos", lambda: cos), _n_(630703, "x", lambda: x))**2)    
    _l_(630706)    

    dFa_2 = (_n_(630707, "Kac_2", lambda: Kac_2)*_n_(630708, "S", lambda: S) + _n_(630709, "Kae_2", lambda: Kae_2))*_n_(630710, "Wdz", lambda: Wdz)
    _l_(630711)
    dFr_2 = (_n_(630712, "Krc_2", lambda: Krc_2)*_n_(630713, "S", lambda: S) + _n_(630714, "Kre_2", lambda: Kre_2))*_n_(630715, "Wdz", lambda: Wdz)
    _l_(630716)
    dFt_2 = (_n_(630717, "Ktc_2", lambda: Ktc_2)*_n_(630718, "S", lambda: S) + _n_(630719, "Kte_2", lambda: Kte_2))*_n_(630720, "Wdz", lambda: Wdz)
    _l_(630721)
    aux = (_c_(630724, _n_(630722, "cos", lambda: cos), 30*_n_(630723, "pi", lambda: pi)/180)*_n_(630725, "dFa_2", lambda: dFa_2) + _c_(630728, _n_(630726, "sin", lambda: sin), 30*_n_(630727, "pi", lambda: pi)/180)*_c_(630731, _n_(630729, "cos", lambda: cos), 5.4*_n_(630730, "pi", lambda: pi)/180)*_n_(630732, "dFr_2", lambda: dFr_2) - _c_(630735, _n_(630733, "sin", lambda: sin), 30*_n_(630734, "pi", lambda: pi)/180)*_c_(630738, _n_(630736, "sin", lambda: sin), 5.4*_n_(630737, "pi", lambda: pi)/180)*_n_(630739, "dFt_2", lambda: dFt_2))/(_c_(630742, _n_(630740, "cos", lambda: cos), 30*_n_(630741, "pi", lambda: pi)/180)**2 + _c_(630745, _n_(630743, "sin", lambda: sin), 30*_n_(630744, "pi", lambda: pi)/180)**2*_c_(630748, _n_(630746, "cos", lambda: cos), 2*5.4*_n_(630747, "pi", lambda: pi)/180))
    _l_(630749)
    
    return aux
Kte_1 = _a_(630752, _n_(630751, "df", lambda: df), "iloc")[_n_(630753, "i", lambda: i),4]
_l_(630754)
Kte_2 = _a_(630756, _n_(630755, "df", lambda: df), "iloc")[_n_(630757, "i", lambda: i),5]
_l_(630758)
Kre_1 = _a_(630760, _n_(630759, "df", lambda: df), "iloc")[_n_(630761, "i", lambda: i),6]
_l_(630762)
Kre_2 = _a_(630764, _n_(630763, "df", lambda: df), "iloc")[_n_(630765, "i", lambda: i),7]
_l_(630766)
Kae_1 = _a_(630768, _n_(630767, "df", lambda: df), "iloc")[_n_(630769, "i", lambda: i),8]
_l_(630770)
Kae_2 = _a_(630772, _n_(630771, "df", lambda: df), "iloc")[_n_(630773, "i", lambda: i),9]
_l_(630774)

Ktc_1 = _a_(630776, _n_(630775, "df", lambda: df), "iloc")[_n_(630777, "i", lambda: i),11]
_l_(630778)
Ktc_2 = _a_(630780, _n_(630779, "df", lambda: df), "iloc")[_n_(630781, "i", lambda: i),12]
_l_(630782)
Krc_1 = _a_(630784, _n_(630783, "df", lambda: df), "iloc")[_n_(630785, "i", lambda: i),13]
_l_(630786)
Krc_2 = _a_(630788, _n_(630787, "df", lambda: df), "iloc")[_n_(630789, "i", lambda: i),14]
_l_(630790)
Kac_1 = _a_(630792, _n_(630791, "df", lambda: df), "iloc")[_n_(630793, "i", lambda: i),15]
_l_(630794)
Kac_2 = _a_(630796, _n_(630795, "df", lambda: df), "iloc")[_n_(630797, "i", lambda: i),16]
_l_(630798)

t = (_a_(630800, _n_(630799, "df", lambda: df), "iloc")[_n_(630801, "i", lambda: i),0])
_l_(630802)
Wdz = _n_(630803, "t", lambda: t)/_c_(630806, _n_(630804, "sin", lambda: sin), 31.19*_n_(630805, "pi", lambda: pi)/180)
_l_(630807)

_n_(630808, "df", lambda: df)['Fx_1'] = 0
_l_(630809)
_n_(630810, "df", lambda: df)['Fy_1'] = 0
_l_(630811)
_n_(630812, "df", lambda: df)['Fz_1'] = 0
_l_(630813)
_n_(630814, "df", lambda: df)['Fx_2'] = 0
_l_(630815)
_n_(630816, "df", lambda: df)['Fy_2'] = 0
_l_(630817)
_n_(630818, "df", lambda: df)['Fz_2'] = 0
_l_(630819)
for i in _c_(630821, _n_(630820, "range", lambda: range), 0,1999,1):
    _l_(630849)

    _a_(630824, _a_(630823, _n_(630822, "df", lambda: df), "Fx_1"), "iloc")[_n_(630825, "i", lambda: i)] = _c_(630836, _n_(630826, "quad", lambda: quad), _n_(630827, "integrand_x1", lambda: integrand_x1), 95*_n_(630828, "pi", lambda: pi)/180, 0, args=(_n_(630829, "Kte_1", lambda: Kte_1), _n_(630830, "Ktc_1", lambda: Ktc_1), _n_(630831, "Kae_1", lambda: Kae_1), _n_(630832, "Kac_1", lambda: Kac_1), _n_(630833, "Kre_1", lambda: Kre_1), _n_(630834, "Krc_1", lambda: Krc_1), _n_(630835, "Wdz", lambda: Wdz))) + _c_(630847, _n_(630837, "quad", lambda: quad), _n_(630838, "integrand_x1", lambda: integrand_x1), 0, 15*_n_(630839, "pi", lambda: pi)/180, args=(_n_(630840, "Kte_1", lambda: Kte_1), _n_(630841, "Ktc_1", lambda: Ktc_1), _n_(630842, "Kae_1", lambda: Kae_1), _n_(630843, "Kac_1", lambda: Kac_1), _n_(630844, "Kre_1", lambda: Kre_1), _n_(630845, "Krc_1", lambda: Krc_1), _n_(630846, "Wdz", lambda: Wdz)))
    _l_(630848)