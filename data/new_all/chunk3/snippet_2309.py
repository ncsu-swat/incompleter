# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52298365/typeerror-when-writing-to-logfile
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
logger = _c_(548310, _a_(548308, _n_(548307, "logging", lambda: logging), "getLogger"), _n_(548309, "__name__", lambda: __name__))
_l_(548311)
_c_(548316, _a_(548313, _n_(548312, "logger", lambda: logger), "setLevel"), _a_(548315, _n_(548314, "logging", lambda: logging), "DEBUG"))
_l_(548317)
handler = _c_(548320, _a_(548319, _n_(548318, "logging", lambda: logging), "FileHandler"), filename='application.log', mode='a+')
_l_(548321)
_c_(548326, _a_(548323, _n_(548322, "handler", lambda: handler), "setLevel"), _a_(548325, _n_(548324, "logging", lambda: logging), "DEBUG"))
_l_(548327)
_c_(548331, _a_(548329, _n_(548328, "logger", lambda: logger), "addHandler"), _n_(548330, "handler", lambda: handler))
_l_(548332)