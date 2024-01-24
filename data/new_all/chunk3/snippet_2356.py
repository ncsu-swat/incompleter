# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49154068/fixing-a-typeerror-when-using-pandas-after-replacing-a-string-with-a-floating-po
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
wt2 = _n_(529514, "wt", lambda: wt)[['Precip']]
_l_(529515)

_c_(529519, _a_(529517, _n_(529516, "wt2", lambda: wt2), "astype"), _n_(529518, "float", lambda: float))
_l_(529520)

_c_(529530, _a_(529529, _c_(529528, _a_(529527, _c_(529526, _a_(529522, _n_(529521, "wt2", lambda: wt2), "groupby"), _a_(529525, _a_(529524, _n_(529523, "wt2", lambda: wt2), "index"), "month"))['Precip'], "sum")), "plot"), kind='bar')
_l_(529531)