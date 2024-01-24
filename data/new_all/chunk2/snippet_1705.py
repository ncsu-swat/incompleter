# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61620754/plt-suptitle-typeerror-can-only-concatenate-tuple-not-str-to-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(428682)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(428684)

except ImportError:
    pass

dataset = _n_(428685, "df", lambda: df)
_l_(428686)
dfsize = _a_(428690, _n_(428687, "dataset", lambda: dataset)[_a_(428689, _n_(428688, "df", lambda: df), "columns")[0]], "size")
_l_(428691)
x = []
_l_(428692)
for i in _c_(428695, _n_(428693, "range", lambda: range), _n_(428694, "dfsize", lambda: dfsize)):
    _l_(428701)

    _c_(428699, _a_(428697, _n_(428696, "x", lambda: x), "append"), _n_(428698, "i", lambda: i))
    _l_(428700)

_a_(428703, _n_(428702, "dataset", lambda: dataset), "shape")
_l_(428704)
# dataset.dropna(inplace=True)
_a_(428707, _a_(428706, _n_(428705, "dataset", lambda: dataset), "columns"), "values")
_l_(428708)
var = ""
_l_(428709)
for i in _c_(428713, _n_(428710, "range", lambda: range), _a_(428712, _n_(428711, "dataset", lambda: dataset), "shape")[1]):
    _l_(428794)


    y = _a_(428718, _n_(428714, "dataset", lambda: dataset)[_a_(428716, _n_(428715, "dataset", lambda: dataset), "columns")[_n_(428717, "i", lambda: i)]], "values")
    _l_(428719)
    y = _c_(428723, _a_(428721, _n_(428720, "y", lambda: y), "astype"), _n_(428722, "float", lambda: float))
    _l_(428724)
    y = _c_(428727, _a_(428726, _n_(428725, "y", lambda: y), "reshape"), -1, 1)
    _l_(428728)
    _a_(428730, _n_(428729, "y", lambda: y), "shape")
    _l_(428731)
    try:
        from sklearn.impute import SimpleImputer
        _l_(428733)

    except ImportError:
        pass

    missingvalues = _c_(428737, _n_(428734, "SimpleImputer", lambda: SimpleImputer), missing_values=_a_(428736, _n_(428735, "np", lambda: np), "nan"), strategy='mean', verbose=0)
    _l_(428738)
    missingvalues = _c_(428742, _a_(428740, _n_(428739, "missingvalues", lambda: missingvalues), "fit"), _n_(428741, "y", lambda: y))
    _l_(428743)
    y = _c_(428747, _a_(428745, _n_(428744, "missingvalues", lambda: missingvalues), "transform"), _n_(428746, "y", lambda: y)[:, :])
    _l_(428748)
    try:
        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        _l_(428750)

    except ImportError:
        pass
    try:
        from sklearn.compose import ColumnTransformer
        _l_(428752)

    except ImportError:
        pass

    labelencoder_x = _c_(428754, _n_(428753, "LabelEncoder", lambda: LabelEncoder))
    _l_(428755)
    x = _c_(428759, _a_(428757, _n_(428756, "labelencoder_x", lambda: labelencoder_x), "fit_transform"), _n_(428758, "x", lambda: x))
    _l_(428760)
    try:
        from scipy.interpolate import *
        _l_(428762)

    except ImportError:
        pass

    p1 = _c_(428767, _a_(428764, _n_(428763, "np", lambda: np), "polyfit"), _n_(428765, "x", lambda: x), _n_(428766, "y", lambda: y), 1)
    _l_(428768)
    try:
        import matplotlib
        _l_(428770)

    except ImportError:
        pass
    _c_(428773, _a_(428772, _n_(428771, "matplotlib", lambda: matplotlib), "use"), 'Agg')
    _l_(428774)
    try:
        import matplotlib.pyplot as plt
        _l_(428776)

    except ImportError:
        pass

    _c_(428779, _a_(428778, _n_(428777, "plt", lambda: plt), "figure"))
    _l_(428780)
    _c_(428785, _a_(428782, _n_(428781, "plt", lambda: plt), "xticks"), _n_(428783, "x", lambda: x), _n_(428784, "months", lambda: months), rotation=25,fontsize=8)
    _l_(428786)
    _c_(428792, _a_(428788, _n_(428787, "plt", lambda: plt), "suptitle"), _a_(428790, _n_(428789, "dataset", lambda: dataset), "columns")[_n_(428791, "i", lambda: i)] + ' (xyz)', fontsize=10)
    _l_(428793)