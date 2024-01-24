# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51712946/bad-number-of-pixels-type-error-when-rotating-skymap-using-healpy-rotator-rota
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(450512)

except ImportError:
    pass
try:
    import healpy as hp
    _l_(450514)

except ImportError:
    pass
try:
    from astropy.utils.data import download_file
    _l_(450516)

except ImportError:
    pass
try:
    from astropy. io import fits
    _l_(450518)

except ImportError:
    pass

def sin(x):
    _l_(450524)

    aux = _c_(450522, _a_(450520, _n_(450519, "np", lambda: np), "sin"), _n_(450521, "x", lambda: x))
    _l_(450523)
    return aux

def cos(x):
    _l_(450530)

    aux = _c_(450528, _a_(450526, _n_(450525, "np", lambda: np), "cos"), _n_(450527, "x", lambda: x))
    _l_(450529)
    return aux

theta_deg = 35 #degrees 
_l_(450531) #degrees 

phi = 0
_l_(450532)
theta = _c_(450536, _a_(450534, _n_(450533, "np", lambda: np), "radians"), _n_(450535, "theta_deg", lambda: theta_deg)) 
_l_(450537) 
psi = 0
_l_(450538)

a11 = (_c_(450541, _n_(450539, "cos", lambda: cos), _n_(450540, "psi", lambda: psi))*_c_(450544, _n_(450542, "cos", lambda: cos), _n_(450543, "theta", lambda: theta))) - (_c_(450547, _n_(450545, "cos", lambda: cos), _n_(450546, "theta", lambda: theta))*_c_(450550, _n_(450548, "sin", lambda: sin), _n_(450549, "phi", lambda: phi))*_c_(450553, _n_(450551, "sin", lambda: sin), _n_(450552, "psi", lambda: psi)))
_l_(450554)
a12  = (_c_(450557, _n_(450555, "cos", lambda: cos), _n_(450556, "psi", lambda: psi))*_c_(450560, _n_(450558, "sin", lambda: sin), _n_(450559, "phi", lambda: phi))) + (_c_(450563, _n_(450561, "cos", lambda: cos), _n_(450562, "theta", lambda: theta))*_c_(450566, _n_(450564, "cos", lambda: cos), _n_(450565, "phi", lambda: phi))*_c_(450569, _n_(450567, "sin", lambda: sin), _n_(450568, "psi", lambda: psi)))
_l_(450570)
a13  = _c_(450573, _n_(450571, "sin", lambda: sin), _n_(450572, "psi", lambda: psi))*_c_(450576, _n_(450574, "sin", lambda: sin), _n_(450575, "theta", lambda: theta))
_l_(450577)
a21  = (-_c_(450580, _n_(450578, "sin", lambda: sin), _n_(450579, "psi", lambda: psi))*_c_(450583, _n_(450581, "cos", lambda: cos), _n_(450582, "phi", lambda: phi))) - (_c_(450586, _n_(450584, "cos", lambda: cos), _n_(450585, "theta", lambda: theta))*_c_(450589, _n_(450587, "sin", lambda: sin), _n_(450588, "phi", lambda: phi))*_c_(450592, _n_(450590, "cos", lambda: cos), _n_(450591, "psi", lambda: psi)))
_l_(450593)
a22  = (-_c_(450596, _n_(450594, "sin", lambda: sin), _n_(450595, "psi", lambda: psi))*_c_(450599, _n_(450597, "sin", lambda: sin), _n_(450598, "phi", lambda: phi))) + (_c_(450602, _n_(450600, "cos", lambda: cos), _n_(450601, "theta", lambda: theta))*_c_(450605, _n_(450603, "cos", lambda: cos), _n_(450604, "phi", lambda: phi))*_c_(450608, _n_(450606, "cos", lambda: cos), _n_(450607, "psi", lambda: psi)))
_l_(450609)
a23 = _c_(450612, _n_(450610, "cos", lambda: cos), _n_(450611, "psi", lambda: psi))*_c_(450615, _n_(450613, "sin", lambda: sin), _n_(450614, "theta", lambda: theta))
_l_(450616)
a31 = _c_(450619, _n_(450617, "sin", lambda: sin), _n_(450618, "theta", lambda: theta))*_c_(450622, _n_(450620, "sin", lambda: sin), _n_(450621, "phi", lambda: phi))
_l_(450623)
a32 =   -_c_(450626, _n_(450624, "sin", lambda: sin), _n_(450625, "theta", lambda: theta))*_c_(450629, _n_(450627, "cos", lambda: cos), _n_(450628, "phi", lambda: phi))
_l_(450630)
a33 = _c_(450633, _n_(450631, "cos", lambda: cos), _n_(450632, "theta", lambda: theta))
_l_(450634)

euler_list = [_n_(450635, "a11", lambda: a11), _n_(450636, "a12", lambda: a12), _n_(450637, "a13", lambda: a13), _n_(450638, "a21", lambda: a21), _n_(450639, "a22", lambda: a22), _n_(450640, "a23", lambda: a23), _n_(450641, "a31", lambda: a31), _n_(450642, "a32", lambda: a32), _n_(450643, "a33", lambda: a33)]
_l_(450644)
euler_array = _c_(450648, _a_(450646, _n_(450645, "np", lambda: np), "asarray"), _n_(450647, "euler_list", lambda: euler_list))
_l_(450649)
euler_deg = _c_(450653, _a_(450651, _n_(450650, "np", lambda: np), "degrees"), _n_(450652, "euler_array", lambda: euler_array))
_l_(450654)
euler = _c_(450657, _a_(450656, _n_(450655, "euler_deg", lambda: euler_deg), "reshape"), (3,3))
_l_(450658)

url  = ('https://dcc.ligo.org/public/0145/T1700453/001/LALInference_v1.fits.gz')
_l_(450659)
filename = _c_(450662, _n_(450660, "download_file", lambda: download_file), _n_(450661, "url", lambda: url), cache=True)
_l_(450663)

r = _c_(450668, _a_(450666, _a_(450665, _n_(450664, "hp", lambda: hp), "rotator"), "Rotator"), _n_(450667, "euler", lambda: euler), deg = False, eulertype = 'ZXZ')
_l_(450669)

R = _c_(450676, _a_(450673, _a_(450672, _a_(450671, _n_(450670, "hp", lambda: hp), "rotator"), "Rotator"), "rotate_map"), _n_(450674, "filename", lambda: filename), _n_(450675, "euler", lambda: euler)) #doesn't like this line
_l_(450677) #doesn't like this line