# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48719937/getting-typeerror-reduction-operation-argmax-not-allowed-for-this-dtype-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.linear_model import LogisticRegression
    _l_(401486)

except ImportError:
    pass
try:
    from sklearn.cross_validation import KFold, cross_val_score
    _l_(401488)

except ImportError:
    pass
try:
    from sklearn.metrics import confusion_matrix, precision_recall_curve, auc, \
    roc_auc_score, roc_curve, recall_score, classification_report
    _l_(401490)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(401492)

except ImportError:
    pass
try:
    import numpy as np
    _l_(401494)

except ImportError:
    pass


def print_kfold_scores(X_training, y_training):
    _l_(401615)

    _c_(401496, _n_(401495, "print", lambda: print), '\nKFold\n')
    _l_(401497)

    fold = _c_(401502, _n_(401498, "KFold", lambda: KFold), _c_(401501, _n_(401499, "len", lambda: len), _n_(401500, "y_training", lambda: y_training)), 5, shuffle=False)
    _l_(401503)

    c_param_range = [0.01, 0.1, 1, 10, 100]
    _l_(401504)

    results = _c_(401512, _a_(401506, _n_(401505, "pd", lambda: pd), "DataFrame"), index=_c_(401511, _n_(401507, "range", lambda: range), _c_(401510, _n_(401508, "len", lambda: len), _n_(401509, "c_param_range", lambda: c_param_range)), 2), columns=['C_parameter', 'Mean recall score'])
    _l_(401513)
    _n_(401514, "results", lambda: results)['C_parameter'] = _n_(401515, "c_param_range", lambda: c_param_range)
    _l_(401516)

    j = 0
    _l_(401517)
    for c_param in _n_(401518, "c_param_range", lambda: c_param_range):
        _l_(401596)

        _c_(401520, _n_(401519, "print", lambda: print), '-------------------------------------------')
        _l_(401521)
        _c_(401524, _n_(401522, "print", lambda: print), 'C parameter: ', _n_(401523, "c_param", lambda: c_param))
        _l_(401525)
        _c_(401527, _n_(401526, "print", lambda: print), '\n-------------------------------------------')
        _l_(401528)

        recall_accs = []
        _l_(401529)
        for iteration, indices in _c_(401532, _n_(401530, "enumerate", lambda: enumerate), _n_(401531, "fold", lambda: fold), start=1):
            _l_(401576)

            lr = _c_(401535, _n_(401533, "LogisticRegression", lambda: LogisticRegression), C=_n_(401534, "c_param", lambda: c_param), penalty='l1')
            _l_(401536)
            _c_(401548, _a_(401538, _n_(401537, "lr", lambda: lr), "fit"), _a_(401540, _n_(401539, "X_training", lambda: X_training), "iloc")[_n_(401541, "indices", lambda: indices)[0], :], _c_(401547, _a_(401546, _a_(401545, _a_(401543, _n_(401542, "y_training", lambda: y_training), "iloc")[_n_(401544, "indices", lambda: indices)[0], :], "values"), "ravel")))
            _l_(401549)

            y_prediction_undersampled = _c_(401556, _a_(401551, _n_(401550, "lr", lambda: lr), "predict"), _a_(401555, _a_(401553, _n_(401552, "X_training", lambda: X_training), "iloc")[_n_(401554, "indices", lambda: indices)[1], :], "values"))
            _l_(401557)
            recall_acc = _c_(401564, _n_(401558, "recall_score", lambda: recall_score), _a_(401562, _a_(401560, _n_(401559, "y_training", lambda: y_training), "iloc")[_n_(401561, "indices", lambda: indices)[1], :], "values"), _n_(401563, "y_prediction_undersampled", lambda: y_prediction_undersampled))
            _l_(401565)
            _c_(401569, _a_(401567, _n_(401566, "recall_accs", lambda: recall_accs), "append"), _n_(401568, "recall_acc", lambda: recall_acc))
            _l_(401570)
            _c_(401574, _n_(401571, "print", lambda: print), 'Iteration ', _n_(401572, "iteration", lambda: iteration), ': recall score = ', _n_(401573, "recall_acc", lambda: recall_acc))
            _l_(401575)

        _a_(401578, _n_(401577, "results", lambda: results), "ix")[_n_(401579, "j", lambda: j), 'Mean recall score'] = _c_(401583, _a_(401581, _n_(401580, "np", lambda: np), "mean"), _n_(401582, "recall_accs", lambda: recall_accs))
        _l_(401584)
        j += 1
        _l_(401585)
        _c_(401591, _n_(401586, "print", lambda: print), '\nMean recall score ', _c_(401590, _a_(401588, _n_(401587, "np", lambda: np), "mean"), _n_(401589, "recall_accs", lambda: recall_accs)))
        _l_(401592)
        _c_(401594, _n_(401593, "print", lambda: print), '\n')
        _l_(401595)

    best_c_param = _a_(401598, _n_(401597, "results", lambda: results), "loc")[_c_(401601, _a_(401600, _n_(401599, "results", lambda: results)['Mean recall score'], "idxmax"))]['C_parameter'] # Error occurs on this line
    _l_(401602) # Error occurs on this line

    _c_(401604, _n_(401603, "print", lambda: print), '*****************************************************************')
    _l_(401605)
    _c_(401608, _n_(401606, "print", lambda: print), 'Best model to choose from cross validation is with C parameter = ', _n_(401607, "best_c_param", lambda: best_c_param))
    _l_(401609)
    _c_(401611, _n_(401610, "print", lambda: print), '*****************************************************************')
    _l_(401612)
    aux = _n_(401613, "best_c_param", lambda: best_c_param)
    _l_(401614)

    return aux