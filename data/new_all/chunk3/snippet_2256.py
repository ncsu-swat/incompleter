# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55533645/nameerror-when-using-composite-pseudovoigt-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from lmfit.models import LorentzianModel, PseudoVoigtModel
    _l_(528986)

except ImportError:
    pass
try:
    import numpy as np
    _l_(528988)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(528990)

except ImportError:
    pass

def make_model_L(num):
    _l_(529028)

    pref = _c_(528993, _a_(528991, "f{0}_", "format"), _n_(528992, "num", lambda: num))
    _l_(528994)
    model = _c_(528997, _n_(528995, "LorentzianModel", lambda: LorentzianModel), prefix = _n_(528996, "pref", lambda: pref))
    _l_(528998)
    _c_(529006, _a_(529000, _n_(528999, "model", lambda: model), "set_param_hint"), _n_(529001, "pref", lambda: pref)+'amplitude', value=_n_(529002, "amplitude", lambda: amplitude)[_n_(529003, "num", lambda: num)], min=0, max=5*_n_(529004, "amplitude", lambda: amplitude)[_n_(529005, "num", lambda: num)])
    _l_(529007)
    _c_(529017, _a_(529009, _n_(529008, "model", lambda: model), "set_param_hint"), _n_(529010, "pref", lambda: pref)+'center', value=_n_(529011, "center", lambda: center)[_n_(529012, "num", lambda: num)], min=_n_(529013, "center", lambda: center)[_n_(529014, "num", lambda: num)]-0.5, max=_n_(529015, "center", lambda: center)[_n_(529016, "num", lambda: num)]+0.5)
    _l_(529018)
    _c_(529024, _a_(529020, _n_(529019, "model", lambda: model), "set_param_hint"), _n_(529021, "pref", lambda: pref)+'sigma', value=_n_(529022, "width", lambda: width)[_n_(529023, "num", lambda: num)], min=0, max=2)
    _l_(529025)
    aux = _n_(529026, "model", lambda: model)
    _l_(529027)
    return aux


def make_model_V(num):
    _l_(529093)

    pref = _c_(529031, _a_(529029, "f{0}_", "format"), _n_(529030, "num", lambda: num))
    _l_(529032)
    model = _c_(529035, _n_(529033, "PseudoVoigtModel", lambda: PseudoVoigtModel), prefix = _n_(529034, "pref", lambda: pref))
    _l_(529036)
    _c_(529040, _n_(529037, "print", lambda: print), 'before',_a_(529039, _n_(529038, "model", lambda: model), "param_names"))
    _l_(529041)
    _c_(529045, _a_(529043, _n_(529042, "model", lambda: model), "set_param_hint"), _n_(529044, "pref", lambda: pref)+'fraction',value = 0.7, vary = False)
    _l_(529046)
    _c_(529054, _a_(529048, _n_(529047, "model", lambda: model), "set_param_hint"), _n_(529049, "pref", lambda: pref)+'amplitude', value=_n_(529050, "amplitude", lambda: amplitude)[_n_(529051, "num", lambda: num)], min=0, max=5*_n_(529052, "amplitude", lambda: amplitude)[_n_(529053, "num", lambda: num)])
    _l_(529055)
    _c_(529065, _a_(529057, _n_(529056, "model", lambda: model), "set_param_hint"), _n_(529058, "pref", lambda: pref)+'center', value=_n_(529059, "center", lambda: center)[_n_(529060, "num", lambda: num)], min=_n_(529061, "center", lambda: center)[_n_(529062, "num", lambda: num)]-0.5, max=_n_(529063, "center", lambda: center)[_n_(529064, "num", lambda: num)]+0.5)
    _l_(529066)
    _c_(529070, _a_(529068, _n_(529067, "model", lambda: model), "set_param_hint"), _n_(529069, "pref", lambda: pref)+'fwhm', value=3, min=3/5, max=3*5)
    _l_(529071)
    _c_(529075, _a_(529073, _n_(529072, "model", lambda: model), "set_param_hint"), _n_(529074, "pref", lambda: pref)+'sigma', value=1, min=0, max=2)
    _l_(529076)
    _c_(529084, _a_(529078, _n_(529077, "model", lambda: model), "set_param_hint"), _n_(529079, "pref", lambda: pref)+'height', value=1, min=-_a_(529081, _n_(529080, "np", lambda: np), "inf"), max=_a_(529083, _n_(529082, "np", lambda: np), "inf"), expr='(((1-fraction)*amplitude)/(sigma*sqrt(pi/log(2)))+(fraction*amplitude)/(pi*sigma))')
    _l_(529085)
    _c_(529089, _n_(529086, "print", lambda: print), _a_(529088, _n_(529087, "model", lambda: model), "param_names"))
    _l_(529090)
    aux = _n_(529091, "model", lambda: model)
    _l_(529092)
    return aux

# Some really coarse "data"
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
_l_(529094)
y = [1,1,1,1,3,4,5,6,5,4,3,1,1,1,1,1,1,1,1,3,4,5,6,5,4,3,1,1,1,1]
_l_(529095)

peaks_in_interval = _c_(529098, _a_(529097, _n_(529096, "np", lambda: np), "array"), [43, 159, 191, 296, 435, 544])
_l_(529099)
amplitude = [3,3]
_l_(529100)
width = [1,1]
_l_(529101)
center = [7,21]
_l_(529102)

mod = None
_l_(529103)
for i in _c_(529108, _n_(529104, "range", lambda: range), _c_(529107, _n_(529105, "len", lambda: len), _n_(529106, "center", lambda: center))):
    _l_(529120)

    #this_mod = make_model_L(i)
    this_mod = _c_(529111, _n_(529109, "make_model_V", lambda: make_model_V), _n_(529110, "i", lambda: i))
    _l_(529112)
    if _n_(529113, "mod", lambda: mod) is None:
        _l_(529119)

        mod = _n_(529114, "this_mod", lambda: this_mod)
        _l_(529115)
    else:
        mod = _n_(529116, "mod", lambda: mod) + _n_(529117, "this_mod", lambda: this_mod)
        _l_(529118)

out=_c_(529125, _a_(529122, _n_(529121, "mod", lambda: mod), "fit"), _n_(529123, "y", lambda: y), x=_n_(529124, "x", lambda: x), method='leastsq')
_l_(529126)
_c_(529129, _a_(529128, _n_(529127, "plt", lambda: plt), "interactive"), True)
_l_(529130)
_c_(529135, _n_(529131, "print", lambda: print), _c_(529134, _a_(529133, _n_(529132, "out", lambda: out), "fit_report")))
_l_(529136)
_c_(529141, _a_(529138, _n_(529137, "plt", lambda: plt), "plot"), _n_(529139, "x", lambda: x), _n_(529140, "y", lambda: y))
_l_(529142)
_c_(529148, _a_(529144, _n_(529143, "plt", lambda: plt), "plot"), _n_(529145, "x", lambda: x), _a_(529147, _n_(529146, "out", lambda: out), "best_fit"), label='best fit')
_l_(529149)
_c_(529155, _a_(529151, _n_(529150, "plt", lambda: plt), "plot"), _n_(529152, "x", lambda: x), _a_(529154, _n_(529153, "out", lambda: out), "init_fit"), 'r--', label='fit with initial values')
_l_(529156)
_c_(529159, _a_(529158, _n_(529157, "plt", lambda: plt), "show"))
_l_(529160)