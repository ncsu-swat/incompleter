# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75353814/python-google-or-tools-surgical-booking-attributeerror-dataframe
# Input data from excel sheet columns

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dfP = _c_(448402, _a_(448400, _n_(448399, "pd", lambda: pd), "DataFrame"), _n_(448401, "data", lambda: data), columns=["Procedure"])
_l_(448403)
dfP = _c_(448408, _a_(448407, _a_(448406, _a_(448405, _n_(448404, "dfP", lambda: dfP), "iloc")[:, :], "values"), "tolist"))
_l_(448409)
dfP = [_n_(448410, "x", lambda: x) for y in _n_(448411, "dfP", lambda: dfP) for x in _n_(448412, "y", lambda: y)]
_l_(448413)

dfD = _c_(448417, _a_(448415, _n_(448414, "pd", lambda: pd), "DataFrame"), _n_(448416, "data", lambda: data), columns=["Date"])
_l_(448418)
dfD = _c_(448423, _a_(448422, _a_(448421, _a_(448420, _n_(448419, "dfD", lambda: dfD), "iloc")[:, :], "values"), "tolist"))
_l_(448424)
dfD = [_n_(448425, "x", lambda: x) for y in _n_(448426, "dfD", lambda: dfD) for x in _n_(448427, "y", lambda: y)]
_l_(448428)

dfE = _c_(448432, _a_(448430, _n_(448429, "pd", lambda: pd), "DataFrame"), _n_(448431, "data", lambda: data), columns=["Book Dur"])
_l_(448433)
dfE = _c_(448438, _a_(448437, _a_(448436, _a_(448435, _n_(448434, "dfE", lambda: dfE), "iloc")[:, :], "values"), "tolist"))
_l_(448439)
dfE = [_n_(448440, "x", lambda: x) for y in _n_(448441, "dfE", lambda: dfE) for x in _n_(448442, "y", lambda: y)]
_l_(448443)

dfA = _c_(448447, _a_(448445, _n_(448444, "pd", lambda: pd), "DataFrame"), _n_(448446, "data", lambda: data), columns=["Actual Dur"])
_l_(448448)
dfA = _c_(448453, _a_(448452, _a_(448451, _a_(448450, _n_(448449, "dfA", lambda: dfA), "iloc")[:, :], "values"), "tolist"))
_l_(448454)
dfA =  [_n_(448455, "x", lambda: x) for y in _n_(448456, "dfA", lambda: dfA) for x in _n_(448457, "y", lambda: y)]
_l_(448458)