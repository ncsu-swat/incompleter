# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54051501/typeerror-ensemble-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.ensemble import VotingClassifier
    _l_(568939)

except ImportError:
    pass
try:
    from sklearn.ensemble import BaggingClassifier
    _l_(568941)

except ImportError:
    pass
try:
    from sklearn.ensemble import AdaBoostClassifier
    _l_(568943)

except ImportError:
    pass
try:
    from sklearn import model_selection
    _l_(568945)

except ImportError:
    pass

classifier_names = ["logistic regression", "linear SVM", "nearest centroids", "decision tree"]
_l_(568946)
classifiers = [_n_(568947, "LogisticRegression", lambda: LogisticRegression), _n_(568948, "LinearSVC", lambda: LinearSVC), _n_(568949, "NearestCentroid", lambda: NearestCentroid), _n_(568950, "DecisionTreeClassifier", lambda: DecisionTreeClassifier)]
_l_(568951)

ensemble1 = _c_(568954, _n_(568952, "VotingClassifier", lambda: VotingClassifier), _n_(568953, "classifiers", lambda: classifiers))
_l_(568955)
ensemble2 = _c_(568958, _n_(568956, "BaggingClassifier", lambda: BaggingClassifier), _n_(568957, "classifiers", lambda: classifiers))
_l_(568959)
ensemble3 = _c_(568962, _n_(568960, "AdaBoostClassifier", lambda: AdaBoostClassifier), _n_(568961, "classifiers", lambda: classifiers))
_l_(568963)
ensembles = [_n_(568964, "ensemble1", lambda: ensemble1), _n_(568965, "ensemble2", lambda: ensemble2), _n_(568966, "ensemble3", lambda: ensemble3)]
_l_(568967)
seed = 7  
_l_(568968)  

for ensemble in _n_(568969, "ensembles", lambda: ensembles):
    _l_(568996)

    kfold = _c_(568973, _a_(568971, _n_(568970, "model_selection", lambda: model_selection), "KFold"), n_splits=10, random_state=_n_(568972, "seed", lambda: seed))
    _l_(568974)
    for classifier in _n_(568975, "classifiers", lambda: classifiers):
        _l_(568995)

        model = _c_(568979, _n_(568976, "ensemble", lambda: ensemble), base_estimator=_n_(568977, "classifier", lambda: classifier), random_state=_n_(568978, "seed", lambda: seed))
        _l_(568980)
        results = _c_(568987, _a_(568982, _n_(568981, "model_selection", lambda: model_selection), "cross_val_score"), _n_(568983, "ensemble", lambda: ensemble), _n_(568984, "X", lambda: X), _n_(568985, "Y", lambda: Y), cv=_n_(568986, "kfold", lambda: kfold))
        _l_(568988)
        _c_(568993, _n_(568989, "print", lambda: print), _c_(568992, _a_(568991, _n_(568990, "results", lambda: results), "mean")))    
        _l_(568994)    