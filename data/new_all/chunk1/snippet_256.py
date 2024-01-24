# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53307308/statmodels-ols-giving-a-typeerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
new_df0 = _c_(419806, _a_(419803, _n_(419802, "pd", lambda: pd), "concat"), [_n_(419804, "df_len", lambda: df_len)[0], _n_(419805, "summary_df", lambda: summary_df)[0]], axis = 0, join = 'inner')
_l_(419807)
new_df1 = _c_(419812, _a_(419809, _n_(419808, "pd", lambda: pd), "concat"), [_n_(419810, "df_len", lambda: df_len)[1], _n_(419811, "summary_df", lambda: summary_df)[1]], axis = 0, join = 'inner')
_l_(419813)

data = _c_(419818, _a_(419815, _n_(419814, "pd", lambda: pd), "concat"), [_n_(419816, "new_df0", lambda: new_df0), _n_(419817, "new_df1", lambda: new_df1)], axis = 1)
_l_(419819)
_c_(419823, _n_(419820, "print", lambda: print), _a_(419822, _n_(419821, "data", lambda: data), "shape"))
_l_(419824)
X = _a_(419826, _n_(419825, "data", lambda: data), "values")[0:2,:]
_l_(419827)
Y = _a_(419829, _n_(419828, "data", lambda: data), "values")[2,:]
_l_(419830)
Y = _c_(419833, _a_(419832, _n_(419831, "Y", lambda: Y), "reshape"), 1,88)
_l_(419834)
X = _a_(419836, _n_(419835, "X", lambda: X), "T")
_l_(419837)
Y = _a_(419839, _n_(419838, "Y", lambda: Y), "T")
_l_(419840)
X = _c_(419844, _a_(419842, _n_(419841, "X", lambda: X), "astype"), _n_(419843, "float", lambda: float))
_l_(419845)
_c_(419849, _n_(419846, "print", lambda: print), _a_(419848, _n_(419847, "X", lambda: X), "shape"))
_l_(419850)
_c_(419854, _n_(419851, "print", lambda: print), _a_(419853, _n_(419852, "Y", lambda: Y), "shape"))
_l_(419855)

model = _c_(419862, _a_(419861, _c_(419860, _a_(419857, _n_(419856, "sm", lambda: sm), "OLS"), _n_(419858, "Y", lambda: Y), _n_(419859, "X", lambda: X)), "fit"))
_l_(419863)
predictions = _c_(419867, _a_(419865, _n_(419864, "model", lambda: model), "predict"), _n_(419866, "X", lambda: X))
_l_(419868)
_c_(419873, _n_(419869, "print", lambda: print), _c_(419872, _a_(419871, _n_(419870, "model", lambda: model), "summary")))
_l_(419874)