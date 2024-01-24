# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54710756/python3-typeerror-numpy-float64-object-is-not-iterable
# creating odd list of K for KNN
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myList = _c_(571431, _n_(571428, "list", lambda: list), _c_(571430, _n_(571429, "range", lambda: range), 1,50))
_l_(571432)

# subsetting just the odd ones
neighbors = _c_(571436, _n_(571433, "filter", lambda: filter), lambda x: _n_(571434, "x", lambda: x) % 2 != 0, _n_(571435, "myList", lambda: myList))
_l_(571437)

# empty list that will hold cv scores
cv_scores = []
_l_(571438)

# perform 10-fold cross validation
for k in _n_(571439, "neighbors", lambda: neighbors):
    _l_(571457)

    knn = _c_(571442, _n_(571440, "KNN", lambda: KNN), n_neighbors=_n_(571441, "k", lambda: k), n_jobs = 6, metric = 'minkowski', contamination = 0.05)
    _l_(571443)
    scores = _c_(571448, _n_(571444, "cross_val_score", lambda: cross_val_score), _n_(571445, "knn", lambda: knn), _n_(571446, "X_test", lambda: X_test), _n_(571447, "pred", lambda: pred), cv=10, scoring='accuracy')
    _l_(571449)
    _c_(571455, _a_(571451, _n_(571450, "cv_scores", lambda: cv_scores), "append"), _c_(571454, _a_(571453, _n_(571452, "scores", lambda: scores), "mean")))
    _l_(571456)
try:
    import matplotlib.pyplot as plt
    _l_(571459)

except ImportError:
    pass
_c_(571463, _a_(571462, _a_(571461, _n_(571460, "plt", lambda: plt), "style"), "use"), 'ggplot')
_l_(571464)

# changing to misclassification error
MSE = [1 - _n_(571465, "x", lambda: x) for x in _n_(571466, "cv_scores", lambda: cv_scores)]
_l_(571467)

# determining best k
optimal_k = _n_(571468, "neighbors", lambda: neighbors)[_c_(571478, _a_(571470, _n_(571469, "MSE", lambda: MSE), "index"), _c_(571477, _n_(571471, "min", lambda: min), _c_(571476, _n_(571472, "next", lambda: next), _c_(571475, _n_(571473, "iter", lambda: iter), _n_(571474, "MSE", lambda: MSE)))))]
_l_(571479)
_c_(571482, _n_(571480, "print", lambda: print), "The optimal K neighbors number is %d" % _n_(571481, "optimal_k", lambda: optimal_k))
_l_(571483)

# plot misclassification error vs k
_c_(571488, _a_(571485, _n_(571484, "plt", lambda: plt), "plot"), _n_(571486, "neighbors", lambda: neighbors), _n_(571487, "MSE", lambda: MSE), figsize = (20,12))
_l_(571489)
_c_(571492, _a_(571491, _n_(571490, "plt", lambda: plt), "xlabel"), 'Number of Neighbors K')
_l_(571493)
_c_(571496, _a_(571495, _n_(571494, "plt", lambda: plt), "ylabel"), 'Misclassification Error')
_l_(571497)
_c_(571500, _a_(571499, _n_(571498, "plt", lambda: plt), "show"))
_l_(571501)