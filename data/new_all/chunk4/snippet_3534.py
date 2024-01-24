# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72649359/numpy-related-attribute-error-in-using-seaborns-pairplot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import seaborn as sns
    _l_(634398)

except ImportError:
    pass
penguins = _c_(634401, _a_(634400, _n_(634399, "sns", lambda: sns), "load_dataset"), "penguins")
_l_(634402)
_c_(634406, _a_(634404, _n_(634403, "sns", lambda: sns), "pairplot"), _n_(634405, "penguins", lambda: penguins))
_l_(634407)