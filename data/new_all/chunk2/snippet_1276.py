# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58032310/pandas-resample-raises-type-error-for-index-consisting-of-datetime-objects
# %%
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(438614)

except ImportError:
    pass
_c_(438618, _n_(438615, "print", lambda: print), f"pandas version: {_a_(438617, _n_(438616, 'pd', lambda: pd), '__version__')}\n\n")
_l_(438619)

data = _c_(438622, _a_(438621, _n_(438620, "pd", lambda: pd), "DataFrame"), {"created": ['2019-03-07T11:01:07.361+0000',
                                 '2019-06-05T15:09:51.203+0100',
                                 '2019-06-05T15:09:51.203+0100'],
                     "value": [10, 20, 30]})
_l_(438623)

# %%
_c_(438629, _n_(438624, "print", lambda: print), f"original type: {_c_(438628, _n_(438625, 'type', lambda: type), _a_(438627, _n_(438626, 'data', lambda: data), 'created')[0])}\n")
_l_(438630)
_c_(438633, _a_(438632, _n_(438631, "data", lambda: data), "info"))
_l_(438634)

# %%
_n_(438635, "data", lambda: data).created = _c_(438640, _a_(438637, _n_(438636, "pd", lambda: pd), "to_datetime"), _a_(438639, _n_(438638, "data", lambda: data), "created"))
_l_(438641)

# %%
_c_(438647, _n_(438642, "print", lambda: print), f"updated type: {_c_(438646, _n_(438643, 'type', lambda: type), _a_(438645, _n_(438644, 'data', lambda: data), 'created')[0])}\n")
_l_(438648)
_c_(438651, _a_(438650, _n_(438649, "data", lambda: data), "info"))
_l_(438652)

# %%
_c_(438655, _a_(438654, _n_(438653, "data", lambda: data), "set_index"), "created", inplace=True)
_l_(438656)
_c_(438659, _a_(438658, _n_(438657, "data", lambda: data), "info"))
_l_(438660)

# %%
_c_(438665, _a_(438664, _c_(438663, _a_(438662, _n_(438661, "data", lambda: data), "resample"), "D"), "mean"))
_l_(438666)