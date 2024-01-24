# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58783972/typeerror-error-while-checking-if-the-values-in-a-list-existed-in-a-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SifFile():
    _l_(425325)

    setting = {}
    _l_(425304)
    interesting_param = ['Temp', 'Pressure']
    _l_(425305)

    def __init__(self, get_param):
        _l_(425324)

        _n_(425306, "self", lambda: self).File_Type = "Andor Technology Multi-Channel File"
        _l_(425307)
        for k, v in _c_(425310, _a_(425309, _n_(425308, "get_param", lambda: get_param), "items")):
            _l_(425323)

            if _a_(425312, _n_(425311, "SifFile", lambda: SifFile), "interesting_param") in _n_(425313, "k", lambda: k):
                _l_(425322)

                _a_(425315, _n_(425314, "SifFile", lambda: SifFile), "setting")[_n_(425316, "k", lambda: k)] = _n_(425317, "v", lambda: v)
                _l_(425318)
                aux = _a_(425320, _n_(425319, "SifFile", lambda: SifFile), "setting")
                _l_(425321)
                return aux

get_parameter = {'Temp':75, 'Pressure':50, 'Helium':90, 'Exp':96}
_l_(425326)

sif = _c_(425329, _n_(425327, "SifFile", lambda: SifFile), _n_(425328, "get_parameter", lambda: get_parameter))
_l_(425330)