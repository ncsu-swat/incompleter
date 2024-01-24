# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60689003/attributeerror-nonetype-object-has-no-attribute-register-forward-hook
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def hook_feature(module, in_, out_):
    _l_(534042)

    _c_(534040, _a_(534033, _n_(534032, "features", lambda: features), "append"), _c_(534039, _a_(534038, _a_(534037, _c_(534036, _a_(534035, _n_(534034, "out_", lambda: out_), "cpu")), "data"), "numpy")))
    _l_(534041)

_c_(534049, _a_(534047, _c_(534046, _a_(534045, _a_(534044, _n_(534043, "model", lambda: model), "_modules"), "get"), "0.conv"), "register_forward_hook"), _n_(534048, "hook_feature", lambda: hook_feature))
_l_(534050)