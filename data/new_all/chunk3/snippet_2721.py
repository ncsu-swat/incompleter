# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65583745/isolation-forest-typeerror-invalid-type-promotion
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.ensemble import IsolationForest
    _l_(544222)

except ImportError:
    pass

contamination = 0.05
_l_(544223)

model = _c_(544226, _n_(544224, "IsolationForest", lambda: IsolationForest), contamination=_n_(544225, "contamination", lambda: contamination), n_estimators=10000)
_l_(544227)
_c_(544231, _a_(544229, _n_(544228, "model", lambda: model), "fit"), _n_(544230, "df", lambda: df))
_l_(544232)

_n_(544233, "df", lambda: df)["iforest"] = _c_(544240, _a_(544235, _n_(544234, "pd", lambda: pd), "Series"), _c_(544239, _a_(544237, _n_(544236, "model", lambda: model), "predict"), _n_(544238, "df", lambda: df)))
_l_(544241)
_n_(544242, "df", lambda: df)["iforest"] = _c_(544245, _a_(544244, _n_(544243, "df", lambda: df)["iforest"], "map"), {1: 0, -1: 1})
_l_(544246)
_n_(544247, "df", lambda: df)["score"] = _c_(544251, _a_(544249, _n_(544248, "model", lambda: model), "decision_function"), _n_(544250, "df", lambda: df))
_l_(544252)
_c_(544255, _a_(544254, _n_(544253, "df", lambda: df), "sort_values"), "score")
_l_(544256)