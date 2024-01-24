# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54983241/gridsearchcv-and-randomizedsearchcv-sklearn-typeerror-call-missing-1-r
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
X, W = _c_(578528, _n_(578526, "train_test_split", lambda: train_test_split), _n_(578527, "all_data", lambda: all_data), test_size=0.2, random_state=42)
_l_(578529)
clf_lof = _c_(578531, _n_(578530, "LocalOutlierFactor", lambda: LocalOutlierFactor), novelty=True, contamination='auto')
_l_(578532)
lof_param_dist_rand = {'n_neighbors': _c_(578535, _a_(578534, _n_(578533, "np", lambda: np), "arange"), 6, 101, 1), 'leaf_size': 
                      _c_(578538, _a_(578537, _n_(578536, "np", lambda: np), "arange"), 30, 101, 10)}
_l_(578539)
lof_param_grid_exhaustive = {'n_neighbors': _c_(578542, _a_(578541, _n_(578540, "np", lambda: np), "arange"), 6, 101, 1), 
                           'leaf_size': _c_(578545, _a_(578544, _n_(578543, "np", lambda: np), "arange"), 30, 101, 10)}
_l_(578546)
_c_(578552, _n_(578547, "gridsearch", lambda: gridsearch), clf=_n_(578548, "clf_lof", lambda: clf_lof), param_dist_rand=_n_(578549, "lof_param_dist_rand", lambda: lof_param_dist_rand), 
param_grid_exhaustive=_n_(578550, "lof_param_grid_exhaustive", lambda: lof_param_grid_exhaustive), X=_n_(578551, "X", lambda: X))
_l_(578553)


clf_svm = _c_(578556, _a_(578555, _n_(578554, "svm", lambda: svm), "OneClassSVM"))
_l_(578557)
svm_param_dist_rand = {'nu': _c_(578560, _a_(578559, _n_(578558, "np", lambda: np), "arange"), 0, 1.1, 0.01), 'kernel': ['rbf', 
                     'linear','poly','sigmoid'], 'degree': _c_(578563, _a_(578562, _n_(578561, "np", lambda: np), "arange"), 0, 7, 
                      1), 'gamma': _c_(578567, _a_(578566, _a_(578565, _n_(578564, "scipy", lambda: scipy), "stats"), "expon"), scale=.1),}
_l_(578568)
svm_param_grid_exhaustive = {'nu': _c_(578571, _a_(578570, _n_(578569, "np", lambda: np), "arange"), 0, 1.1, 0.01), 'kernel': 
                            ['rbf', 'linear','poly','sigmoid'], 'degree': 
                            _c_(578574, _a_(578573, _n_(578572, "np", lambda: np), "arange"), 0, 7, 1), 'gamma': 0.25}
_l_(578575)
_c_(578581, _n_(578576, "gridsearch", lambda: gridsearch), clf=_n_(578577, "clf_svm", lambda: clf_svm), param_dist_rand=_n_(578578, "svm_param_dist_rand", lambda: svm_param_dist_rand), 
param_grid_exhaustive=_n_(578579, "svm_param_grid_exhaustive", lambda: svm_param_grid_exhaustive), X=_n_(578580, "X", lambda: X))
_l_(578582)