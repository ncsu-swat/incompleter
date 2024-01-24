# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55347192/how-to-fix-this-nameerror-name-clf-is-not-defined
#Feature Selection --> Random Forest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def feature_importance(clf):
    _l_(445576)

    # Relative Importance (Features)
    _c_(445519, _a_(445516, _n_(445515, "clf", lambda: clf), "fit"), _n_(445517, "X_train", lambda: X_train),_n_(445518, "y_train", lambda: y_train))
    _l_(445520)
    # Get Feature Importance from the classifier
    feature_importance = _a_(445522, _n_(445521, "clf", lambda: clf), "feature_importances_")
    _l_(445523)
    # Normalize The Features
    feature_importance = 100.0 * (_n_(445524, "feature_importance", lambda: feature_importance) / _c_(445527, _a_(445526, _n_(445525, "feature_importance", lambda: feature_importance), "max")))
    _l_(445528)
    # Sort Features and Creat Horizontal Bar Plot
    sorted_idx = _c_(445532, _a_(445530, _n_(445529, "np", lambda: np), "argsort"), _n_(445531, "feature_importance", lambda: feature_importance))
    _l_(445533)
    pos = _c_(445538, _a_(445535, _n_(445534, "np", lambda: np), "arange"), _a_(445537, _n_(445536, "sorted_idx", lambda: sorted_idx), "shape")[0]) + .5
    _l_(445539)
    _c_(445542, _a_(445541, _n_(445540, "pl", lambda: pl), "figure"), figsize=(16, 12))
    _l_(445543)
    _c_(445549, _a_(445545, _n_(445544, "pl", lambda: pl), "barh"), _n_(445546, "pos", lambda: pos), _n_(445547, "feature_importance", lambda: feature_importance)[_n_(445548, "sorted_idx", lambda: sorted_idx)], align='center', color='#0033CC')
    _l_(445550)
    _c_(445562, _a_(445552, _n_(445551, "pl", lambda: pl), "yticks"), _n_(445553, "pos", lambda: pos), _c_(445560, _a_(445555, _n_(445554, "np", lambda: np), "asanyarray"), _c_(445559, _a_(445558, _a_(445557, _n_(445556, "df", lambda: df), "columns"), "tolist")))[_n_(445561, "sorted_idx", lambda: sorted_idx)])
    _l_(445563)
    _c_(445566, _a_(445565, _n_(445564, "pl", lambda: pl), "xlabel"), "Relative Importance")
    _l_(445567)
    _c_(445570, _a_(445569, _n_(445568, "pl", lambda: pl), "title"), "Variable Importance - Random Forest")
    _l_(445571)
    _c_(445574, _a_(445573, _n_(445572, "pl", lambda: pl), "show"))
    _l_(445575)


clf_NB = _c_(445578, _n_(445577, "GaussianNB", lambda: GaussianNB))
_l_(445579)
clf_SVC = _c_(445581, _n_(445580, "SVC", lambda: SVC))
_l_(445582)
clf_RF = _c_(445584, _n_(445583, "RandomForestClassifier", lambda: RandomForestClassifier), n_estimators = 100)
_l_(445585)

algorithms = [_n_(445586, "clf_NB", lambda: clf_NB),_n_(445587, "clf_SVC", lambda: clf_SVC),_n_(445588, "clf_RF", lambda: clf_RF)]
_l_(445589)

for model in _n_(445590, "algorithms", lambda: algorithms):
    _l_(445663)

    _c_(445592, _n_(445591, "print", lambda: print), "\n")
    _l_(445593)
    _c_(445595, _n_(445594, "print", lambda: print), "==============================")
    _l_(445596)
    _c_(445603, _n_(445597, "print", lambda: print), _c_(445602, _a_(445598, "Model: {}", "format"), _a_(445601, _a_(445600, _n_(445599, "model", lambda: model), "__class__"), "__name__")))
    _l_(445604)
    _c_(445606, _n_(445605, "print", lambda: print), "==============================")
    _l_(445607)
    _c_(445609, _n_(445608, "print", lambda: print), "\n")
    _l_(445610)
    _c_(445612, _n_(445611, "print", lambda: print), "**********************************************************")
    _l_(445613)
    _c_(445615, _n_(445614, "print", lambda: print), "**Training**")
    _l_(445616)
    _c_(445621, _n_(445617, "print", lambda: print), "Data Size:",_c_(445620, _n_(445618, "len", lambda: len), _n_(445619, "X_train", lambda: X_train)))
    _l_(445622)
    # Fit model to training data
    _c_(445627, _n_(445623, "train_classifier", lambda: train_classifier), _n_(445624, "model", lambda: model), _n_(445625, "X_train", lambda: X_train), _n_(445626, "y_train", lambda: y_train))
    _l_(445628)

    # Predict on training set and compute F1 score
    _c_(445633, _n_(445629, "predict_labels", lambda: predict_labels), _n_(445630, "model", lambda: model), _n_(445631, "X_train", lambda: X_train), _n_(445632, "y_train", lambda: y_train))
    _l_(445634)

    #Predict on Testing Data
    _c_(445636, _n_(445635, "print", lambda: print), "**********************************************************")
    _l_(445637)
    _c_(445639, _n_(445638, "print", lambda: print), "**Testing**")
    _l_(445640)
    _c_(445645, _n_(445641, "print", lambda: print), "Data Size:",_c_(445644, _n_(445642, "len", lambda: len), _n_(445643, "X_test", lambda: X_test)))
    _l_(445646)
    _c_(445651, _n_(445647, "predict_labels", lambda: predict_labels), _n_(445648, "model", lambda: model), _n_(445649, "X_test", lambda: X_test), _n_(445650, "y_test", lambda: y_test))
    _l_(445652)

    if _n_(445653, "clf", lambda: clf) == _n_(445654, "clf_RF", lambda: clf_RF):
        _l_(445662)

        _c_(445656, _n_(445655, "print", lambda: print), "\n")
        _l_(445657)
        _c_(445660, _n_(445658, "feature_importance", lambda: feature_importance), _n_(445659, "clf_RF", lambda: clf_RF))
        _l_(445661)