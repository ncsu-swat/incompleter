# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57941020/python-attribute-error-for-nearest-neighbor-classifier
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy.spatial import distance
    _l_(558746)

except ImportError:
    pass

def euc(a,b):
    _l_(558753)

    aux = _c_(558751, _a_(558748, _n_(558747, "distance", lambda: distance), "euclidean"), _n_(558749, "a", lambda: a),_n_(558750, "b", lambda: b))
    _l_(558752)
    return aux

class DavesKNN():
    _l_(558810)

    def fit(self, X_train, y_train):
        _l_(558760)

        _n_(558754, "self", lambda: self).X_train = _n_(558755, "X_train", lambda: X_train)
        _l_(558756)
        _n_(558757, "self", lambda: self).y_train = _n_(558758, "y_train", lambda: y_train)
        _l_(558759)

    def predict(self, X_test):
        _l_(558809)

        predictions = []
        _l_(558761)
        for row in _n_(558762, "X_test", lambda: X_test):
            _l_(558773)

            label = _c_(558766, _a_(558764, _n_(558763, "self", lambda: self), "closest"), _n_(558765, "row", lambda: row))
            _l_(558767)
            _c_(558771, _a_(558769, _n_(558768, "predictions", lambda: predictions), "append"), _n_(558770, "label", lambda: label))
            _l_(558772)
        aux = _n_(558774, "predictions", lambda: predictions)
        _l_(558775)
        return aux

        def closest(self, row):
            _l_(558808)

            best_dist = _c_(558780, _n_(558776, "euc", lambda: euc), _n_(558777, "row", lambda: row), _a_(558779, _n_(558778, "self", lambda: self), "X_train")[0])
            _l_(558781)
            best_index = 0
            _l_(558782)
            for i in _c_(558788, _n_(558783, "range", lambda: range), 1, _c_(558787, _n_(558784, "len", lambda: len), _a_(558786, _n_(558785, "self", lambda: self), "X_train"))):
                _l_(558803)

                dist = _c_(558794, _n_(558789, "euc", lambda: euc), _n_(558790, "row", lambda: row), _a_(558792, _n_(558791, "self", lambda: self), "X_train")[_n_(558793, "i", lambda: i)])
                _l_(558795)
                if _n_(558796, "dist", lambda: dist) < _n_(558797, "best_dist", lambda: best_dist):
                    _l_(558802)

                    best_dist = _n_(558798, "dist", lambda: dist)
                    _l_(558799)
                    best_index = _n_(558800, "i", lambda: i)
                    _l_(558801)
            aux = _a_(558805, _n_(558804, "self", lambda: self), "y_train")[_n_(558806, "best_index", lambda: best_index)]
            _l_(558807)
            return aux
try:
    from sklearn import datasets
    _l_(558812)

except ImportError:
    pass
iris = _c_(558815, _a_(558814, _n_(558813, "datasets", lambda: datasets), "load_iris"))
_l_(558816)

# Features and Labels
X = _a_(558818, _n_(558817, "iris", lambda: iris), "data")
_l_(558819)
y = _a_(558821, _n_(558820, "iris", lambda: iris), "target")
_l_(558822)
try:
    from sklearn.model_selection import train_test_split
    _l_(558824)

except ImportError:
    pass
X_train, X_test, y_train, y_test = _c_(558828, _n_(558825, "train_test_split", lambda: train_test_split), _n_(558826, "X", lambda: X), _n_(558827, "y", lambda: y), test_size = .5)
_l_(558829)

# from sklearn.neighbors import KNeighborsClassifier
# my_classifier = KNeighborsClassifier()
my_classifier = _c_(558831, _n_(558830, "DavesKNN", lambda: DavesKNN))
_l_(558832)

_c_(558837, _a_(558834, _n_(558833, "my_classifier", lambda: my_classifier), "fit"), _n_(558835, "X_train", lambda: X_train), _n_(558836, "y_train", lambda: y_train))
_l_(558838)

predictions = _c_(558842, _a_(558840, _n_(558839, "my_classifier", lambda: my_classifier), "predict"), _n_(558841, "X_test", lambda: X_test))
_l_(558843)
try:
    from sklearn.metrics import accuracy_score
    _l_(558845)

except ImportError:
    pass
_c_(558851, _n_(558846, "print", lambda: print), _c_(558850, _n_(558847, "accuracy_score", lambda: accuracy_score), _n_(558848, "y_test", lambda: y_test), _n_(558849, "predictions", lambda: predictions)))
_l_(558852)