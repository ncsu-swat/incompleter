# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58073224/typeerror-unhashable-type-numpy-ndarray-on-pivot-table
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
v2x_pivot = _c_(397148, _a_(397144, _n_(397143, "pd", lambda: pd), "pivot_table"), _n_(397145, "df", lambda: df)['2019-07-29':'2019-09-20'],
                           index=['XMStr'],
                           columns=['HasDiscrepency'],
                           values=['V2Xt'],
                           margins=True,
                           aggfunc=[_a_(397147, _n_(397146, "np", lambda: np), "mean")])
_l_(397149)