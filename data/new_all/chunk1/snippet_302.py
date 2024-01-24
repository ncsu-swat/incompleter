# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61769186/h2otypeerror-training-frame-must-be-a-valid-h2oframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
gbm = _c_(415584, _a_(415580, _n_(415579, "h2o", lambda: h2o), "get_model"), _c_(415583, _a_(415582, _n_(415581, "sorted_final_grid", lambda: sorted_final_grid), "sorted_metric_table"))['model_ids'][0])
_l_(415585)

params = _a_(415587, _n_(415586, "gbm", lambda: gbm), "params")
_l_(415588)
new_params = {"nfolds":5, "model_id":None}
_l_(415589)
for key in _c_(415592, _a_(415591, _n_(415590, "new_params", lambda: new_params), "keys")):
    _l_(415598)

    _n_(415593, "params", lambda: params)[_n_(415594, "key", lambda: key)]['actual'] = _n_(415595, "new_params", lambda: new_params)[_n_(415596, "key", lambda: key)] 
    _l_(415597) 
gbm_best = _c_(415600, _n_(415599, "H2OGradientBoostingEstimator", lambda: H2OGradientBoostingEstimator))
_l_(415601)
for key in _c_(415604, _a_(415603, _n_(415602, "params", lambda: params), "keys")):
    _l_(415623)

    if _n_(415605, "key", lambda: key) in _c_(415608, _n_(415606, "dir", lambda: dir), _n_(415607, "gbm_best", lambda: gbm_best)) and _c_(415612, _n_(415609, "getattr", lambda: getattr), _n_(415610, "gbm_best", lambda: gbm_best),_n_(415611, "key", lambda: key)) != _n_(415613, "params", lambda: params)[_n_(415614, "key", lambda: key)]['actual']:
        _l_(415622)

        _c_(415620, _n_(415615, "setattr", lambda: setattr), _n_(415616, "gbm_best", lambda: gbm_best),_n_(415617, "key", lambda: key),_n_(415618, "params", lambda: params)[_n_(415619, "key", lambda: key)]['actual'])
        _l_(415621)