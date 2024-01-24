# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47779351/typeerror-logistic-missing-1-required-positional-argument-params
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy.stats import norm
    _l_(599727)

except ImportError:
    pass

# set up a function to return the log likelihood
def logistic_loglik(params,t,data,sig):
    _l_(599740)

    aux = _c_(599738, _n_(599728, "sum", lambda: sum), _c_(599737, _a_(599730, _n_(599729, "norm", lambda: norm), "logpdf"), _c_(599734, _n_(599731, "logistic", lambda: logistic), _n_(599732, "params", lambda: params),_n_(599733, "t", lambda: t)),_n_(599735, "data", lambda: data),_n_(599736, "sig", lambda: sig)))
    _l_(599739)
    return aux

# set standard deviations to be 10% of the population values
sig = _n_(599741, "ExRatio", lambda: ExRatio)/10
_l_(599742)

# parameters for the MCMC
reps = 50000
_l_(599743)
nparams = 3
_l_(599744)

# output matrix
par_out = _c_(599749, _a_(599746, _n_(599745, "np", lambda: np), "ones"), shape=(_n_(599747, "reps", lambda: reps),_n_(599748, "nparams", lambda: nparams)))
_l_(599750)
# acceptance 
accept = _c_(599755, _a_(599752, _n_(599751, "np", lambda: np), "zeros"), shape=(_n_(599753, "reps", lambda: reps),_n_(599754, "nparams", lambda: nparams)))
_l_(599756)
# proposal standard deviations. These have been pre-optimized.
propsigma = [0.05,20,5]
_l_(599757)

for i in _c_(599760, _n_(599758, "range", lambda: range), 1,_n_(599759, "reps", lambda: reps)):
    _l_(599825)

    # make a copy of previous parameters
    _n_(599761, "par_out", lambda: par_out)[_n_(599762, "i", lambda: i),] = _n_(599763, "par_out", lambda: par_out)[_n_(599764, "i", lambda: i)-1,]
    _l_(599765)
    for j in _c_(599768, _n_(599766, "range", lambda: range), _n_(599767, "npars", lambda: npars)):
        _l_(599775)

        proposed = _c_(599773, _a_(599770, _n_(599769, "np", lambda: np), "copy"), _n_(599771, "par_out", lambda: par_out)[_n_(599772, "i", lambda: i),:]) # we need to make a copy so that rejected moves don't affect the original matrix
        _l_(599774) # we need to make a copy so that rejected moves don't affect the original matrix
    _n_(599776, "proposed", lambda: proposed)[_n_(599777, "j", lambda: j)] = _n_(599778, "proposed", lambda: proposed)[_n_(599779, "j", lambda: j)] + _c_(599785, _a_(599782, _a_(599781, _n_(599780, "np", lambda: np), "random"), "normal"), 0,_n_(599783, "propsigma", lambda: propsigma)[_n_(599784, "j", lambda: j)])
    _l_(599786)
    if (_n_(599787, "proposed", lambda: proposed)[_n_(599788, "j", lambda: j)]>0):
        _l_(599824)

        alpha = _c_(599804, _a_(599790, _n_(599789, "np", lambda: np), "exp"), _c_(599796, _n_(599791, "logistic_loglik", lambda: logistic_loglik), _n_(599792, "proposed", lambda: proposed),_n_(599793, "time", lambda: time),_n_(599794, "ExRatio", lambda: ExRatio),_n_(599795, "sig", lambda: sig))-_c_(599803, _n_(599797, "logistic_loglik", lambda: logistic_loglik), _n_(599798, "par_out", lambda: par_out)[_n_(599799, "i", lambda: i)-1,],_n_(599800, "time", lambda: time),_n_(599801, "ExRatio", lambda: ExRatio),_n_(599802, "sig", lambda: sig)))
        _l_(599805)
        u = _c_(599809, _a_(599808, _a_(599807, _n_(599806, "np", lambda: np), "random"), "rand"))
        _l_(599810)
        if (_n_(599811, "u", lambda: u) < _n_(599812, "alpha", lambda: alpha)):
            _l_(599823)

            _n_(599813, "par_out", lambda: par_out)[_n_(599814, "i", lambda: i),_n_(599815, "j", lambda: j)] = _n_(599816, "proposed", lambda: proposed)[_n_(599817, "j", lambda: j)]
            _l_(599818)
            _n_(599819, "accept", lambda: accept)[_n_(599820, "i", lambda: i),_n_(599821, "j", lambda: j)] = 1
            _l_(599822)

#print(sum(accept[range(101,reps),:])/(reps-100))


#plt.plot(par_out[:,0])
#plt.plot(par_out[range(101,reps),0])
#plt.plot(par_out[:,0],par_out[:,2])
_c_(599832, _a_(599827, _n_(599826, "plt", lambda: plt), "hist"), _n_(599828, "par_out", lambda: par_out)[_c_(599831, _n_(599829, "range", lambda: range), 101,_n_(599830, "reps", lambda: reps)),0],50)
_l_(599833)
_c_(599835, _n_(599834, "print", lambda: print), '\n')
_l_(599836)
a=_c_(599843, _a_(599838, _n_(599837, "np", lambda: np), "mean"), _n_(599839, "par_out", lambda: par_out)[_c_(599842, _n_(599840, "range", lambda: range), 101,_n_(599841, "reps", lambda: reps)),0])
_l_(599844)