# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54053849/attributeerror-str-object-has-no-attribute-mean-validation-score
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def report(grid_scores, n_top=3):
    _l_(398008)

    top_scores = _c_(397973, _n_(397969, "sorted", lambda: sorted), _n_(397970, "grid_scores", lambda: grid_scores), key=_c_(397972, _n_(397971, "itemgetter", lambda: itemgetter), 1), reverse=True)[:_n_(397974, "n_top", lambda: n_top)]
    _l_(397975)
    for i, score in _c_(397978, _n_(397976, "enumerate", lambda: enumerate), _n_(397977, "top_scores", lambda: top_scores)):
        _l_(398007)

        _c_(397983, _n_(397979, "print", lambda: print), _c_(397982, _a_(397980, "Rank: {0}", "format"), _n_(397981, "i", lambda: i) + 1))
        _l_(397984)
        _c_(397995, _n_(397985, "print", lambda: print), _c_(397994, _a_(397986, "Mean validation score: {0:.3f} (std: {1:.3f})", "format"), _a_(397988, _n_(397987, "score", lambda: score), "mean_validation_score"),
              _c_(397993, _a_(397990, _n_(397989, "np", lambda: np), "std"), _a_(397992, _n_(397991, "score", lambda: score), "cv_validation_scores"))))
        _l_(397996)
        _c_(398002, _n_(397997, "print", lambda: print), _c_(398001, _a_(397998, "Parameters: {0}", "format"), _a_(398000, _n_(397999, "score", lambda: score), "parameters")))
        _l_(398003)
        _c_(398005, _n_(398004, "print", lambda: print), "")
        _l_(398006)
_c_(398012, _n_(398009, "report", lambda: report), _a_(398011, _n_(398010, "clf", lambda: clf), "cv_results_"))
_l_(398013)