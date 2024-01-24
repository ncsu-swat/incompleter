# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29078786/strange-nameerror-name-math-is-not-defined-while-import-math
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sigma as sgm
    _l_(407546)

except ImportError:
    pass
try:
    import math
    _l_(407548)

except ImportError:
    pass
def sigma_crit(sigmaX, sigmaY, sigmaZ, Theta, Pw, Pres, nu, alpha, No):
    _l_(407590)

    """
    Return value of critical stress calculated for one of three failure criterias.
    No: 1 - Simplified Mohr-Coulomb
        2 - Mohr-Coulomb
        3 - Drucker-Prager
        4 - list with 3 model's resutls
    sigmaX - stress at X wellbore axis
    sigmaY - stress at Y wellbore axis
    Theta - azimuth,anticlokwise from SH_max
    nu - Poisson's ratio
    alpha - Biot's  coefficient
    """ 
    sigma_theta = _c_(407559, _a_(407550, _n_(407549, "sgm", lambda: sgm), "sigma_calc"), _n_(407551, "sigmaX", lambda: sigmaX), _n_(407552, "sigmaY", lambda: sigmaY), _n_(407553, "sigmaZ", lambda: sigmaZ), _n_(407554, "Theta", lambda: Theta), _n_(407555, "Pw", lambda: Pw), _n_(407556, "Pres", lambda: Pres), _n_(407557, "nu", lambda: nu), _n_(407558, "alpha", lambda: alpha), 1)
    _l_(407560)
    sigma_zi = _c_(407571, _a_(407562, _n_(407561, "sgm", lambda: sgm), "sigma_calc"), _n_(407563, "sigmaX", lambda: sigmaX), _n_(407564, "sigmaY", lambda: sigmaY), _n_(407565, "sigmaZ", lambda: sigmaZ), _n_(407566, "Theta", lambda: Theta), _n_(407567, "Pw", lambda: Pw), _n_(407568, "Pres", lambda: Pres), _n_(407569, "nu", lambda: nu), _n_(407570, "alpha", lambda: alpha), 2)
    _l_(407572)
    sigma_thzi = _c_(407583, _a_(407574, _n_(407573, "sgm", lambda: sgm), "sigma_calc"), _n_(407575, "sigmaX", lambda: sigmaX), _n_(407576, "sigmaY", lambda: sigmaY), _n_(407577, "sigmaZ", lambda: sigmaZ), _n_(407578, "Theta", lambda: Theta), _n_(407579, "Pw", lambda: Pw), _n_(407580, "Pres", lambda: Pres), _n_(407581, "nu", lambda: nu), _n_(407582, "alpha", lambda: alpha),3)
    _l_(407584)
    # Conerting degrees to radians for below equations...Caution above functions has built-in converter
    Theta = _c_(407588, _a_(407586, _n_(407585, "math", lambda: math), "radians"), _n_(407587, "Theta", lambda: Theta))
    _l_(407589)