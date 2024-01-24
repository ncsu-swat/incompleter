# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52372576/typeerror-float-object-is-not-subscriptable-during-scipy-minimize
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy import log,sum,var
    _l_(694455)

except ImportError:
    pass
try:
    from numba import njit
    _l_(694457)

except ImportError:
    pass

@_n_(694458, "njit", lambda: njit)
def log_likelihood(params,surg_fx,surg_fx_ses):
    _l_(694490)

    mu_var = _n_(694459, "params", lambda: params)[0]
    _l_(694460)
    exp_var = _n_(694461, "mu_var", lambda: mu_var) + _n_(694462, "surg_fx_ses", lambda: surg_fx_ses)**2
    _l_(694463)
    log_lik = -(_n_(694464, "surg_fx", lambda: (surg_fx))**2 / (2*_n_(694465, "exp_var", lambda: exp_var))) - .5*_c_(694468, _n_(694466, "log", lambda: log), _n_(694467, "exp_var", lambda: exp_var))
    _l_(694469)
    neg_sum_log_lik = -_c_(694472, _n_(694470, "sum", lambda: sum), _n_(694471, "log_lik", lambda: log_lik))
    _l_(694473)
    _c_(694476, _n_(694474, "print", lambda: print), _n_(694475, "mu_var", lambda: mu_var))
    _l_(694477)
    _c_(694480, _n_(694478, "print", lambda: print), _n_(694479, "neg_sum_log_lik", lambda: neg_sum_log_lik))
    _l_(694481)
    if _c_(694485, _a_(694483, _n_(694482, "np", lambda: np), "isnan"), _n_(694484, "neg_sum_log_lik", lambda: neg_sum_log_lik)):
        _l_(694489)

        aux = 1e20
        _l_(694486)
        return aux
    else:
        aux = _n_(694487, "neg_sum_log_lik", lambda: neg_sum_log_lik)
        _l_(694488)
        return aux

@_n_(694491, "njit", lambda: njit)
def log_lik_jac(params,surg_fx,surg_fx_ses):
    _l_(694513)

    mu_var = _n_(694492, "params", lambda: params)[0]
    _l_(694493)
    exp_var = _n_(694494, "mu_var", lambda: mu_var) + _n_(694495, "surg_fx_ses", lambda: surg_fx_ses)**2
    _l_(694496)
    jc = -_c_(694501, _n_(694497, "sum", lambda: sum), (_n_(694498, "surg_fx", lambda: (surg_fx))**2 / (2*(_n_(694499, "exp_var", lambda: exp_var)**2))) - (.5/_n_(694500, "exp_var", lambda: exp_var)))
    _l_(694502)
    _c_(694505, _n_(694503, "print", lambda: print), _n_(694504, "mu_var", lambda: mu_var))
    _l_(694506)
    _c_(694509, _n_(694507, "print", lambda: print), _n_(694508, "jc", lambda: jc))
    _l_(694510)
    aux = _n_(694511, "jc", lambda: jc)
    _l_(694512)
    return aux

x0 = [_c_(694517, _a_(694515, _n_(694514, "np", lambda: np), "var"), _n_(694516, "cost_params3", lambda: cost_params3))]
_l_(694518)
shrinkage_est = _c_(694525, _n_(694519, "minimize", lambda: minimize), _n_(694520, "log_likelihood", lambda: log_likelihood),_n_(694521, "x0", lambda: x0),args=(_n_(694522, "cost_params3", lambda: cost_params3),_n_(694523, "cost_SEs3", lambda: cost_SEs3)),jac=_n_(694524, "log_lik_jac", lambda: log_lik_jac),options={'disp':True},method='BFGS')
_l_(694526)