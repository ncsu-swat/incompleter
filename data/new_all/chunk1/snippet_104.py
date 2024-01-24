# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64679139/nameerror-name-open-is-not-defined-when-trying-to-log-to-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
handler = _c_(416512, _a_(416511, _n_(416510, "logging", lambda: logging), "FileHandler"), filename="../logs/bot.log",
    mode="a")
_l_(416513)
formatter = _c_(416516, _a_(416515, _n_(416514, "logging", lambda: logging), "Formatter"), "%(asctime)s %(name)-30s %(levelname)-8s %(message)s")
_l_(416517)
_c_(416521, _a_(416519, _n_(416518, "handler", lambda: handler), "setFormatter"), _n_(416520, "formatter", lambda: formatter))
_l_(416522)
_c_(416527, _a_(416524, _n_(416523, "handler", lambda: handler), "setLevel"), _a_(416526, _n_(416525, "logging", lambda: logging), "DEBUG"))
_l_(416528)
_c_(416534, _a_(416532, _c_(416531, _a_(416530, _n_(416529, "logging", lambda: logging), "getLogger")), "addHandler"), _n_(416533, "handler", lambda: handler))
_l_(416535)