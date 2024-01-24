# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47715289/typeerror-not-supported-between-instances-of-float-and-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import infection
    _l_(464758)

except ImportError:
    pass

def isResistent(virus):
    _l_(464765)

    if _c_(464761, _a_(464760, _n_(464759, "virus", lambda: virus), "find"), 'AAA') > -1:
        _l_(464764)

        aux = True
        _l_(464762)
        return aux
    else:
        aux = False
        _l_(464763)
        return aux

def simulate(viruses, mortalityProb, mutationProb, maxReproductionProb, maxPopulation, timesteps = 500):
    _l_(464798)

    activation_cure = 400
    _l_(464766)
    while _n_(464767, "timesteps", lambda: timesteps) > -1:
        _l_(464793)

        survivors = _c_(464772, _a_(464769, _n_(464768, "infection", lambda: infection), "kill"), _n_(464770, "viruses", lambda: viruses), _n_(464771, "mortalityProb", lambda: mortalityProb))
        _l_(464773)
        for virus in _n_(464774, "viruses", lambda: viruses):
            _l_(464791)

            if _n_(464775, "timesteps", lambda: timesteps) < _n_(464776, "activation_cure", lambda: activation_cure) and _c_(464779, _n_(464777, "isResistent", lambda: isResistent), _n_(464778, "virus", lambda: virus)):
                _l_(464790)

                reproductionProb = _a_(464781, _n_(464780, "infection", lambda: infection), "reproductionProbability")
                _l_(464782)
                _c_(464788, _a_(464784, _n_(464783, "infection", lambda: infection), "reproduce"), _n_(464785, "viruses", lambda: viruses), _n_(464786, "mutationProb", lambda: mutationProb), _n_(464787, "reproductionProb", lambda: reproductionProb))
                _l_(464789)
        timesteps -= 1
        _l_(464792)
    aux = _c_(464796, _n_(464794, "len", lambda: len), _n_(464795, "viruses", lambda: viruses))
    _l_(464797)
    return aux

def experiment(numberOfPatients):
    _l_(464827)

    cured = 0
    _l_(464799)
    viruses = []
    _l_(464800)
    for i in _c_(464802, _n_(464801, "range", lambda: range), 10):
        _l_(464810)

        _c_(464808, _a_(464804, _n_(464803, "viruses", lambda: viruses), "append"), _c_(464807, _a_(464806, _n_(464805, "infection", lambda: infection), "generateVirus"), 16))
        _l_(464809)
    for i in _c_(464813, _n_(464811, "range", lambda: range), _n_(464812, "numberOfPatients", lambda: numberOfPatients)):
        _l_(464824)

        remaining_virus = _c_(464816, _n_(464814, "simulate", lambda: simulate), _n_(464815, "viruses", lambda: viruses), 0.05, 0.1, 0.07, 1000)
        _l_(464817)
        if _n_(464818, "remaining_virus", lambda: remaining_virus)[_c_(464821, _n_(464819, "len", lambda: len), _n_(464820, "remaining_virus", lambda: remaining_virus))-1] == 0:
            _l_(464823)

            cured += 1
            _l_(464822)
    aux = _n_(464825, "cured", lambda: cured)
    _l_(464826)
    return aux

_c_(464831, _n_(464828, "print", lambda: print), _c_(464830, _n_(464829, "experiment", lambda: experiment), 5))
_l_(464832)