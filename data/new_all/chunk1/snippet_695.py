# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55431356/typeerror-init-got-an-unexpected-keyword-argument-n-folds-sentiment-ana
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
grid_svm = _c_(394142, _n_(394136, "GridSearchCV", lambda: GridSearchCV), _n_(394137, "pipeline_svm", lambda: pipeline_svm), #object used to fit the data
    param_grid=_n_(394138, "param_svm", lambda: param_svm), 
    refit=True,  # fit using all data, on the best detected classifier
    n_jobs=-1,  # number of cores to use for parallelization; -1 for "all cores" i.e. to run on all CPUs
    scoring='accuracy',#optimizing parameter
    cv=_c_(394141, _n_(394139, "StratifiedKFold", lambda: StratifiedKFold), _n_(394140, "liked_train", lambda: liked_train),n_folds=5),
)
_l_(394143)