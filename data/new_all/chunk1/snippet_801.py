# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48348803/typeerror-not-supported-between-instances-of-int-and-list-in-numpy-inte
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
phone=_a_(395667, _n_(395666, "df_final_naFill", lambda: df_final_naFill), "iloc")[0,4]
_l_(395668)
_c_(395671, _n_(395669, "type", lambda: type), _n_(395670, "phone", lambda: phone)) # List
_l_(395672) # List
s=_c_(395676, _a_(395674, _n_(395673, "pd", lambda: pd), "Series"), _n_(395675, "phone", lambda: phone))
_l_(395677)
_c_(395680, _n_(395678, "type", lambda: type), _n_(395679, "s", lambda: s)) #pandas.core.series.Series
_l_(395681) #pandas.core.series.Series
a=_c_(395699, _a_(395683, _n_(395682, "pd", lambda: pd), "Series"), _c_(395698, _a_(395696, _c_(395695, _a_(395694, _c_(395693, _a_(395691, _c_(395690, _a_(395689, _c_(395688, _a_(395685, _n_(395684, "s", lambda: s), "apply"), _a_(395687, _n_(395686, "pd", lambda: pd), "Series")), "stack")), "astype"), _n_(395692, "int", lambda: int)), "groupby"), level=0), "apply"), _n_(395697, "list", lambda: list)))
_l_(395700)
phone_office=_a_(395702, _n_(395701, "df_final_naFill", lambda: df_final_naFill), "iloc")[0,6]
_l_(395703)
# type(phone_office) #List
h=_c_(395707, _a_(395705, _n_(395704, "pd", lambda: pd), "Series"), _n_(395706, "phone_office", lambda: phone_office))
_l_(395708)
phone_comb=_c_(395713, _a_(395710, _n_(395709, "np", lambda: np), "intersect1d"), _n_(395711, "a", lambda: a),_n_(395712, "h", lambda: h))
_l_(395714)