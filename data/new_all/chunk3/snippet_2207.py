# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58040108/attributeerror-str-object-has-no-attribute-mean-validation-score-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
GridMean = [_a_(528540, _n_(528539, "result", lambda: result), "mean_validation_score") for result in 
_a_(528542, _n_(528541, "gridA", lambda: gridA), "cv_results_")]
_l_(528543)
_c_(528546, _n_(528544, "print", lambda: print), _n_(528545, "GridMean", lambda: GridMean))
_l_(528547)
_c_(528552, _a_(528549, _n_(528548, "plt", lambda: plt), "plot"), _n_(528550, "k_values", lambda: k_values), _n_(528551, "GridMean", lambda: GridMean))
_l_(528553)
_c_(528556, _a_(528555, _n_(528554, "plt", lambda: plt), "xlabel"), 'Value of "K" for KNN')
_l_(528557)
_c_(528560, _a_(528559, _n_(528558, "plt", lambda: plt), "ylabel"), 'CrossValidated Accuracy')
_l_(528561)