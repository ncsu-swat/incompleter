# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
value = 5.34343
_l_(1548995)
rounded_value = _c_(1548998, _n_(1548996, "round", lambda: round), _n_(1548997, "value", lambda: value), 2) # 5.34
_l_(1548999) # 5.34

