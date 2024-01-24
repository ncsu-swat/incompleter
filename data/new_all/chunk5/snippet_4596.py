# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54792795/tensorflow-invalid-type-error-while-defining-a-tf-constant
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
CONTINUOUS_COLUMNS = ["age", "id", "sessions", "amount", "averageSessionDuration", "numberOfActiveDays"]
_l_(689707)
continuous_cols = {_n_(689708, "k", lambda: k): _c_(689714, _a_(689710, _n_(689709, "tf", lambda: tf), "constant"), _a_(689713, _n_(689711, "df", lambda: df)[_n_(689712, "k", lambda: k)], "values")) for k in _n_(689715, "CONTINUOUS_COLUMNS", lambda: CONTINUOUS_COLUMNS)}
_l_(689716)