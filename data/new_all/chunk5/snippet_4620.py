# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54042911/attributeerror-when-use-cv-score-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(662049)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(662051)

except ImportError:
    pass
try:
    import calendar
    _l_(662053)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(662055)

except ImportError:
    pass
try:
    import numpy as np
    _l_(662057)

except ImportError:
    pass
try:
    from sklearn import tree
    _l_(662059)

except ImportError:
    pass
try:
    from sklearn.tree import DecisionTreeClassifier
    _l_(662061)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(662063)

except ImportError:
    pass
try:
    from matplotlib import pyplot as plt
    _l_(662065)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(662067)

except ImportError:
    pass
try:
    import reshape
    _l_(662069)

except ImportError:
    pass
try:
    from sklearn.ensemble import ExtraTreesClassifier
    _l_(662071)

except ImportError:
    pass
try:
    from sklearn import datasets
    _l_(662073)

except ImportError:
    pass
try:
    from sklearn import metrics
    _l_(662075)

except ImportError:
    pass
try:
    import csv
    _l_(662077)

except ImportError:
    pass
try:
    from sklearn.impute import SimpleImputer
    _l_(662079)

except ImportError:
    pass
try:
    from sklearn.preprocessing import StandardScaler
    _l_(662081)

except ImportError:
    pass
try:
    import operator
    _l_(662083)

except ImportError:
    pass
try:
    from scipy.stats import pearsonr
    _l_(662085)

except ImportError:
    pass
try:
    from sklearn.model_selection import GridSearchCV
    _l_(662087)

except ImportError:
    pass
try:
    from sklearn.ensemble import RandomForestRegressor
    _l_(662089)

except ImportError:
    pass
try:
    from operator import itemgetter
    _l_(662091)

except ImportError:
    pass
try:
    from sklearn.model_selection import GridSearchCV
    _l_(662093)

except ImportError:
    pass
clf = _c_(662097, _n_(662094, "GridSearchCV", lambda: GridSearchCV), _n_(662095, "RFR", lambda: RFR), _n_(662096, "parameters", lambda: parameters))
_l_(662098)
_c_(662104, _a_(662100, _n_(662099, "clf", lambda: clf), "fit"), _n_(662101, "mov", lambda: mov)[_n_(662102, "num_cat_key_feat", lambda: num_cat_key_feat)],_n_(662103, "labels", lambda: labels))
_l_(662105)
# Utility function to report best scores
def report(grid_scores, n_top=3):
    _l_(662145)

    top_scores = _c_(662110, _n_(662106, "sorted", lambda: sorted), _n_(662107, "grid_scores", lambda: grid_scores), key=_c_(662109, _n_(662108, "itemgetter", lambda: itemgetter), 1), reverse=True)[:_n_(662111, "n_top", lambda: n_top)]
    _l_(662112)
    for i, score in _c_(662115, _n_(662113, "enumerate", lambda: enumerate), _n_(662114, "top_scores", lambda: top_scores)):
        _l_(662144)

        _c_(662120, _n_(662116, "print", lambda: print), _c_(662119, _a_(662117, "Rank: {0}", "format"), _n_(662118, "i", lambda: i) + 1))
        _l_(662121)
        _c_(662132, _n_(662122, "print", lambda: print), _c_(662131, _a_(662123, "Mean validation score: {0:.3f} (std: {1:.3f})", "format"), _a_(662125, _n_(662124, "score", lambda: score), "mean_validation_score"),
              _c_(662130, _a_(662127, _n_(662126, "np", lambda: np), "std"), _a_(662129, _n_(662128, "score", lambda: score), "cv_validation_scores"))))
        _l_(662133)
        _c_(662139, _n_(662134, "print", lambda: print), _c_(662138, _a_(662135, "Parameters: {0}", "format"), _a_(662137, _n_(662136, "score", lambda: score), "parameters")))
        _l_(662140)
        _c_(662142, _n_(662141, "print", lambda: print), "")
        _l_(662143)
_c_(662149, _n_(662146, "report", lambda: report), _a_(662148, _n_(662147, "clf", lambda: clf), "cv_scores_"))
_l_(662150)