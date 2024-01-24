# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60479597/error-attributeerror-dataframe-object-has-no-attribute-source-or-keyerr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(564642)

except ImportError:
    pass
try:
    import numpy as np
    _l_(564644)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(564646)

except ImportError:
    pass

data = _c_(564649, _a_(564648, _n_(564647, "pd", lambda: pd), "read_csv"), 'data_with_anomalies.csv')
_l_(564650)
source = _c_(564654, _a_(564652, _n_(564651, "pd", lambda: pd), "DataFrame"), _n_(564653, "data", lambda: data))
_l_(564655)
target = _n_(564656, "data", lambda: data)['Anomaly']
_l_(564657)
source = _c_(564660, _a_(564659, _n_(564658, "source", lambda: source), "drop"), columns = ['Anomaly_Tag'])
_l_(564661)

model = _c_(564663, _n_(564662, "ExtraTreesClassifier", lambda: ExtraTreesClassifier))
_l_(564664)
_c_(564669, _a_(564666, _n_(564665, "model", lambda: model), "fit"), _n_(564667, "source", lambda: source), _n_(564668, "target", lambda: target))
_l_(564670)
_c_(564674, _n_(564671, "print", lambda: print), _a_(564673, _n_(564672, "model", lambda: model), "feature_importances_"))
_l_(564675)

importances = _a_(564677, _n_(564676, "model", lambda: model), "feature_importances_")
_l_(564678)

# Below chunk is referred from another question on stackoverflow
# Sort feature importances in descending order
indices = _c_(564682, _a_(564680, _n_(564679, "np", lambda: np), "argsort"), _n_(564681, "importances", lambda: importances))[::-1]
_l_(564683)