# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52731818/typeerror-issue-with-gridsearchcv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
parameter={'svm_C':(0.1, 1, 10, 100), 'svm_gamma':(0.001, 0.01, 0.1, 10)}
_l_(447496)
pipe=_c_(447501, _n_(447497, "Pipeline", lambda: Pipeline), [("scaler", _n_(447498, "StandardScaler", lambda: StandardScaler)), ("svm", _c_(447500, _n_(447499, "SVC", lambda: SVC)))])
_l_(447502)
_c_(447505, _n_(447503, "print", lambda: print), _n_(447504, "parameter", lambda: parameter))
_l_(447506)
_c_(447509, _n_(447507, "print", lambda: print), _n_(447508, "pipe", lambda: pipe))
_l_(447510)

_c_(447514, _n_(447511, "print", lambda: print), _a_(447513, _n_(447512, "xtrain", lambda: xtrain), "shape"))
_l_(447515)
_c_(447519, _n_(447516, "print", lambda: print), _a_(447518, _n_(447517, "ytrain1", lambda: ytrain1), "shape"))
_l_(447520)
grid=_c_(447524, _n_(447521, "GridSearchCV", lambda: GridSearchCV), _n_(447522, "pipe", lambda: pipe), _n_(447523, "parameter", lambda: parameter), cv=3, n_jobs=-1)
_l_(447525)
_c_(447530, _a_(447527, _n_(447526, "grid", lambda: grid), "fit"), _n_(447528, "xtrain", lambda: xtrain),_n_(447529, "ytrain1", lambda: ytrain1))
_l_(447531)
_c_(447537, _n_(447532, "print", lambda: print), _c_(447536, _a_(447533, "Best set score:{}", "format"), _a_(447535, _n_(447534, "grid", lambda: grid), "best_score_")))
_l_(447538)
_c_(447547, _n_(447539, "print", lambda: print), _c_(447546, _a_(447540, "Test set Score:{}", "format"), _c_(447545, _a_(447542, _n_(447541, "grid", lambda: grid), "score"), _n_(447543, "xtest", lambda: xtest),_n_(447544, "ytest1", lambda: ytest1))))
_l_(447548)
_c_(447554, _n_(447549, "print", lambda: print), _c_(447553, _a_(447550, "Best paameters:{}", "format"), _a_(447552, _n_(447551, "grid", lambda: grid), "best_params_")))
_l_(447555)
filename='finalized_svm.sav'
_l_(447556)
filename1='gridfinal_svm.sav'
_l_(447557)
_c_(447562, _a_(447559, _n_(447558, "joblib", lambda: joblib), "dump"), _n_(447560, "best_estimator_", lambda: best_estimator_), _n_(447561, "filename", lambda: filename))
_l_(447563)
_c_(447568, _a_(447565, _n_(447564, "joblib", lambda: joblib), "dump"), _n_(447566, "grid", lambda: grid), _n_(447567, "filename1", lambda: filename1))
_l_(447569)
pred=_c_(447573, _a_(447571, _n_(447570, "grid", lambda: grid), "predict"), _n_(447572, "xtest", lambda: xtest))
_l_(447574)
confusion=_c_(447578, _n_(447575, "confusion_matrix", lambda: confusion_matrix), _n_(447576, "ytest1", lambda: ytest1),_n_(447577, "pred", lambda: pred)), _c_(447581, _n_(447579, "print", lambda: print), _n_(447580, "confusion", lambda: confusion))
_l_(447582)