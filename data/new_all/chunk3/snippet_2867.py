# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60479597/error-attributeerror-dataframe-object-has-no-attribute-source-or-keyerr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
names = [_n_(549331, "data", lambda: data)['source'] == _n_(549332, "i", lambda: i) for i in _n_(549333, "indices", lambda: indices)]
_l_(549334)

_c_(549337, _a_(549336, _n_(549335, "plt", lambda: plt), "figure"))
_l_(549338)
_c_(549341, _a_(549340, _n_(549339, "plt", lambda: plt), "title"), "Feature Importance")
_l_(549342)
_c_(549351, _a_(549344, _n_(549343, "plt", lambda: plt), "bar"), _c_(549348, _n_(549345, "range", lambda: range), _a_(549347, _n_(549346, "source", lambda: source), "shape")[1]), _n_(549349, "importances", lambda: importances)[_n_(549350, "indices", lambda: indices)])
_l_(549352)
_c_(549360, _a_(549354, _n_(549353, "plt", lambda: plt), "xticks"), _c_(549358, _n_(549355, "range", lambda: range), _a_(549357, _n_(549356, "source", lambda: source), "shape")[1]), _n_(549359, "names", lambda: names), rotation=90)
_l_(549361)
_c_(549364, _a_(549363, _n_(549362, "plt", lambda: plt), "show"))
_l_(549365)