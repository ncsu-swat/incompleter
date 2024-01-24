# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76508159/python-script-nameerror-in-power-bi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(610495)

except ImportError:
    pass
dataset = _c_(610500, _a_(610497, _n_(610496, "pandas", lambda: pandas), "DataFrame"), _n_(610498, "Agent", lambda: Agent), _n_(610499, "Resolved", lambda: Resolved))
_l_(610501)
dataset = _c_(610504, _a_(610503, _n_(610502, "dataset", lambda: dataset), "drop_duplicates"))
_l_(610505)
_c_(610508, _a_(610507, _n_(610506, "dataset", lambda: dataset), "plot"), kind='scatter', x='Agent', y='Resolved', color='green')
_l_(610509)
_c_(610512, _a_(610511, _n_(610510, "plt", lambda: plt), "show"))
_l_(610513)