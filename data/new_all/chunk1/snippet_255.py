# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53307308/statmodels-ols-giving-a-typeerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
new_df0 = _c_(379629, _a_(379626, _n_(379625, "pd", lambda: pd), "concat"), [_n_(379627, "df_lex", lambda: df_lex)[0], _n_(379628, "summary_df", lambda: summary_df)[0]], axis = 0, join = 'inner')
_l_(379630)
new_df1 = _c_(379635, _a_(379632, _n_(379631, "pd", lambda: pd), "concat"), [_n_(379633, "df_lex", lambda: df_lex)[1], _n_(379634, "summary_df", lambda: summary_df)[1]], axis = 0, join = 'inner')
_l_(379636)
data = _c_(379641, _a_(379638, _n_(379637, "pd", lambda: pd), "concat"), [_n_(379639, "new_df0", lambda: new_df0), _n_(379640, "new_df1", lambda: new_df1)], axis = 1)
_l_(379642)
_c_(379646, _n_(379643, "print", lambda: print), _a_(379645, _n_(379644, "data", lambda: data), "shape"))
_l_(379647)
X = _a_(379649, _n_(379648, "data", lambda: data), "values")[0:6,:]
_l_(379650)
Y = _a_(379652, _n_(379651, "data", lambda: data), "values")[6,:]
_l_(379653)
Y = _c_(379656, _a_(379655, _n_(379654, "Y", lambda: Y), "reshape"), 1,88)
_l_(379657)
X = _a_(379659, _n_(379658, "X", lambda: X), "T")
_l_(379660)
Y = _a_(379662, _n_(379661, "Y", lambda: Y), "T")
_l_(379663)
X = _c_(379667, _a_(379665, _n_(379664, "X", lambda: X), "astype"), _n_(379666, "float", lambda: float))
_l_(379668)
model = _c_(379675, _a_(379674, _c_(379673, _a_(379670, _n_(379669, "sm", lambda: sm), "OLS"), _n_(379671, "Y", lambda: Y), _n_(379672, "X", lambda: X)), "fit"))
_l_(379676)
predictions = _c_(379680, _a_(379678, _n_(379677, "model", lambda: model), "predict"), _n_(379679, "X", lambda: X))
_l_(379681)
_c_(379686, _n_(379682, "print", lambda: print), _c_(379685, _a_(379684, _n_(379683, "model", lambda: model), "summary")))
_l_(379687)