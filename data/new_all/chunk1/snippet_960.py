# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64534019/typeerror-cant-pickle-weakref-objects
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(388014)

except ImportError:
    pass
try:
    import pickle as pkl
    _l_(388016)

except ImportError:
    pass

class OBJ():
    _l_(388025)

    def __init__(self):
        _l_(388024)

        _n_(388017, "self", lambda: self).model = _c_(388022, _a_(388021, _a_(388020, _a_(388019, _n_(388018, "tf", lambda: tf), "keras"), "models"), "Sequential"))
        _l_(388023)

save_location = 'your save location here'
_l_(388026)
_c_(388032, _a_(388028, _n_(388027, "pkl", lambda: pkl), "dump"), _c_(388030, _n_(388029, "OBJ", lambda: OBJ)), _n_(388031, "save_location", lambda: save_location))
_l_(388033)