# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72426111/python3-error-typeerror-not-supported-between-instances-of-str-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_a_(630381, _a_(630380, _n_(630379, "config", lambda: config), "plugins"), "Times").Updattime = _c_(630383, _n_(630382, "ConfigIP", lambda: ConfigIP), default=[0, 0], auto_jump=False)
_l_(630384)
_a_(630388, _a_(630387, _a_(630386, _n_(630385, "config", lambda: config), "plugins"), "Times"), "Updattime").value = _c_(630396, _a_(630390, _n_(630389, "self", lambda: self), "Verif"), _a_(630395, _a_(630394, _a_(630393, _a_(630392, _n_(630391, "config", lambda: config), "plugins"), "Times"), "Updattime"), "value"))
_l_(630397)

def Verif(self, Valist):
        _l_(630432)

        if _c_(630400, _n_(630398, "int", lambda: int), _n_(630399, "Valist", lambda: Valist)[0]) < 10:
                _l_(630429)

                if _c_(630403, _n_(630401, "int", lambda: int), _n_(630402, "Valist", lambda: Valist)[1]) < 10:
                        _l_(630416)

                        Valist = ['0' + _c_(630406, _n_(630404, "str", lambda: str), _n_(630405, "Valist", lambda: Valist)[0]), '0' + _c_(630409, _n_(630407, "str", lambda: str), _n_(630408, "Valist", lambda: Valist)[1])]
                        _l_(630410)
                else:
                    Valist = ['0' + _c_(630413, _n_(630411, "str", lambda: str), _n_(630412, "Valist", lambda: Valist)[0]), _n_(630414, "Valist", lambda: Valist)[1]]
                    _l_(630415)
        elif _c_(630419, _n_(630417, "int", lambda: int), _n_(630418, "Valist", lambda: Valist)[1]) < 10:
                _l_(630428)

                Valist = [_n_(630420, "Valist", lambda: Valist)[0], '0' + _c_(630423, _n_(630421, "str", lambda: str), _n_(630422, "Valist", lambda: Valist)[1])]
                _l_(630424)
        else:
            Valist = [_n_(630425, "Valist", lambda: Valist)[0], _n_(630426, "Valist", lambda: Valist)[1]]
            _l_(630427)
        aux = _n_(630430, "Valist", lambda: Valist)
        _l_(630431)
        return aux