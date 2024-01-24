# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63684600/typeerror-float-argument-must-be-a-string-or-a-number-not-tuple-valueerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def integrand_x1(x, Kte_1, Ktc_1, Kae_1, Kac_1, Kre_1, Krc_1, Wdz):
    _l_(645403)

    r = 0.0002
    _l_(645345)
    f = 2/360*10**(-5)
    _l_(645346)
    S = _n_(645347, "r", lambda: r) + _n_(645348, "f", lambda: f)*_c_(645351, _n_(645349, "sin", lambda: sin), _n_(645350, "x", lambda: x)) - _c_(645358, _n_(645352, "sqrt", lambda: sqrt), _n_(645353, "r", lambda: r)**2 - (_n_(645354, "f", lambda: f)**2)*_c_(645357, _n_(645355, "cos", lambda: cos), _n_(645356, "x", lambda: x))**2)
    _l_(645359)
    
    dFa_1 = (_n_(645360, "Kac_1", lambda: Kac_1)*_n_(645361, "S", lambda: S) + _n_(645362, "Kae_1", lambda: Kae_1))*_n_(645363, "Wdz", lambda: Wdz)
    _l_(645364)
    dFr_1 = (_n_(645365, "Krc_1", lambda: Krc_1)*_n_(645366, "S", lambda: S) + _n_(645367, "Kre_1", lambda: Kre_1))*_n_(645368, "Wdz", lambda: Wdz)
    _l_(645369)
    dFt_1 = (_n_(645370, "Ktc_1", lambda: Ktc_1)*_n_(645371, "S", lambda: S) + _n_(645372, "Kte_1", lambda: Kte_1))*_n_(645373, "Wdz", lambda: Wdz)
    _l_(645374)
    aux = (_c_(645377, _n_(645375, "cos", lambda: cos), 30*_n_(645376, "pi", lambda: pi)/180)*_n_(645378, "dFa_1", lambda: dFa_1) + _c_(645381, _n_(645379, "sin", lambda: sin), 30*_n_(645380, "pi", lambda: pi)/180)*_c_(645384, _n_(645382, "cos", lambda: cos), 5.4*_n_(645383, "pi", lambda: pi)/180)*_n_(645385, "dFr_1", lambda: dFr_1) - _c_(645388, _n_(645386, "sin", lambda: sin), 30*_n_(645387, "pi", lambda: pi)/180)*_c_(645391, _n_(645389, "sin", lambda: sin), 5.4*_n_(645390, "pi", lambda: pi)/180)*_n_(645392, "dFt_1", lambda: dFt_1))/(_c_(645395, _n_(645393, "cos", lambda: cos), 30*_n_(645394, "pi", lambda: pi)/180)**2 + _c_(645398, _n_(645396, "sin", lambda: sin), 30*_n_(645397, "pi", lambda: pi)/180)**2*_c_(645401, _n_(645399, "cos", lambda: cos), 2*5.4*_n_(645400, "pi", lambda: pi)/180))
    _l_(645402)
    
    return aux
def integrand_x2(x, Kte_2, Ktc_2, Kae_2, Kac_2, Kre_2, Krc_2, Wdz):
    _l_(645462)

    r = 0.0002
    _l_(645404)
    f = 2/360*10**(-5)
    _l_(645405)
    S = _n_(645406, "r", lambda: r) + _n_(645407, "f", lambda: f)*_c_(645410, _n_(645408, "sin", lambda: sin), _n_(645409, "x", lambda: x)) - _c_(645417, _n_(645411, "sqrt", lambda: sqrt), _n_(645412, "r", lambda: r)**2 - (_n_(645413, "f", lambda: f)**2)*_c_(645416, _n_(645414, "cos", lambda: cos), _n_(645415, "x", lambda: x))**2)    
    _l_(645418)    

    dFa_2 = (_n_(645419, "Kac_2", lambda: Kac_2)*_n_(645420, "S", lambda: S) + _n_(645421, "Kae_2", lambda: Kae_2))*_n_(645422, "Wdz", lambda: Wdz)
    _l_(645423)
    dFr_2 = (_n_(645424, "Krc_2", lambda: Krc_2)*_n_(645425, "S", lambda: S) + _n_(645426, "Kre_2", lambda: Kre_2))*_n_(645427, "Wdz", lambda: Wdz)
    _l_(645428)
    dFt_2 = (_n_(645429, "Ktc_2", lambda: Ktc_2)*_n_(645430, "S", lambda: S) + _n_(645431, "Kte_2", lambda: Kte_2))*_n_(645432, "Wdz", lambda: Wdz)
    _l_(645433)
    aux = (_c_(645436, _n_(645434, "cos", lambda: cos), 30*_n_(645435, "pi", lambda: pi)/180)*_n_(645437, "dFa_2", lambda: dFa_2) + _c_(645440, _n_(645438, "sin", lambda: sin), 30*_n_(645439, "pi", lambda: pi)/180)*_c_(645443, _n_(645441, "cos", lambda: cos), 5.4*_n_(645442, "pi", lambda: pi)/180)*_n_(645444, "dFr_2", lambda: dFr_2) - _c_(645447, _n_(645445, "sin", lambda: sin), 30*_n_(645446, "pi", lambda: pi)/180)*_c_(645450, _n_(645448, "sin", lambda: sin), 5.4*_n_(645449, "pi", lambda: pi)/180)*_n_(645451, "dFt_2", lambda: dFt_2))/(_c_(645454, _n_(645452, "cos", lambda: cos), 30*_n_(645453, "pi", lambda: pi)/180)**2 + _c_(645457, _n_(645455, "sin", lambda: sin), 30*_n_(645456, "pi", lambda: pi)/180)**2*_c_(645460, _n_(645458, "cos", lambda: cos), 2*5.4*_n_(645459, "pi", lambda: pi)/180))
    _l_(645461)
    
    return aux
Kte_1 = _a_(645464, _n_(645463, "df", lambda: df), "iloc")[_n_(645465, "i", lambda: i),4]
_l_(645466)
Kte_2 = _a_(645468, _n_(645467, "df", lambda: df), "iloc")[_n_(645469, "i", lambda: i),5]
_l_(645470)
Kre_1 = _a_(645472, _n_(645471, "df", lambda: df), "iloc")[_n_(645473, "i", lambda: i),6]
_l_(645474)
Kre_2 = _a_(645476, _n_(645475, "df", lambda: df), "iloc")[_n_(645477, "i", lambda: i),7]
_l_(645478)
Kae_1 = _a_(645480, _n_(645479, "df", lambda: df), "iloc")[_n_(645481, "i", lambda: i),8]
_l_(645482)
Kae_2 = _a_(645484, _n_(645483, "df", lambda: df), "iloc")[_n_(645485, "i", lambda: i),9]
_l_(645486)

Ktc_1 = _a_(645488, _n_(645487, "df", lambda: df), "iloc")[_n_(645489, "i", lambda: i),11]
_l_(645490)
Ktc_2 = _a_(645492, _n_(645491, "df", lambda: df), "iloc")[_n_(645493, "i", lambda: i),12]
_l_(645494)
Krc_1 = _a_(645496, _n_(645495, "df", lambda: df), "iloc")[_n_(645497, "i", lambda: i),13]
_l_(645498)
Krc_2 = _a_(645500, _n_(645499, "df", lambda: df), "iloc")[_n_(645501, "i", lambda: i),14]
_l_(645502)
Kac_1 = _a_(645504, _n_(645503, "df", lambda: df), "iloc")[_n_(645505, "i", lambda: i),15]
_l_(645506)
Kac_2 = _a_(645508, _n_(645507, "df", lambda: df), "iloc")[_n_(645509, "i", lambda: i),16]
_l_(645510)

t = (_a_(645512, _n_(645511, "df", lambda: df), "iloc")[_n_(645513, "i", lambda: i),0])
_l_(645514)
Wdz = _n_(645515, "t", lambda: t)/_c_(645518, _n_(645516, "sin", lambda: sin), 31.19*_n_(645517, "pi", lambda: pi)/180)
_l_(645519)

_n_(645520, "df", lambda: df)['Fx_1'] = 0
_l_(645521)
_n_(645522, "df", lambda: df)['Fy_1'] = 0
_l_(645523)
_n_(645524, "df", lambda: df)['Fz_1'] = 0
_l_(645525)
_n_(645526, "df", lambda: df)['Fx_2'] = 0
_l_(645527)
_n_(645528, "df", lambda: df)['Fy_2'] = 0
_l_(645529)
_n_(645530, "df", lambda: df)['Fz_2'] = 0
_l_(645531)
for i in _c_(645533, _n_(645532, "range", lambda: range), 0,1999,1):
    _l_(645561)

    _a_(645536, _a_(645535, _n_(645534, "df", lambda: df), "Fx_1"), "iloc")[_n_(645537, "i", lambda: i)] = _c_(645548, _n_(645538, "quad", lambda: quad), _n_(645539, "integrand_x1", lambda: integrand_x1), 95*_n_(645540, "pi", lambda: pi)/180, 0, args=(_n_(645541, "Kte_1", lambda: Kte_1), _n_(645542, "Ktc_1", lambda: Ktc_1), _n_(645543, "Kae_1", lambda: Kae_1), _n_(645544, "Kac_1", lambda: Kac_1), _n_(645545, "Kre_1", lambda: Kre_1), _n_(645546, "Krc_1", lambda: Krc_1), _n_(645547, "Wdz", lambda: Wdz))) + _c_(645559, _n_(645549, "quad", lambda: quad), _n_(645550, "integrand_x1", lambda: integrand_x1), 0, 15*_n_(645551, "pi", lambda: pi)/180, args=(_n_(645552, "Kte_1", lambda: Kte_1), _n_(645553, "Ktc_1", lambda: Ktc_1), _n_(645554, "Kae_1", lambda: Kae_1), _n_(645555, "Kac_1", lambda: Kac_1), _n_(645556, "Kre_1", lambda: Kre_1), _n_(645557, "Krc_1", lambda: Krc_1), _n_(645558, "Wdz", lambda: Wdz)))
    _l_(645560)