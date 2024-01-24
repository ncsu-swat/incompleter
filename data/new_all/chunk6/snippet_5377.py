# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61292051/hyperopt-typeerror-because-of-passing-parameters-to-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from hyperopt import fmin, hp, tpe
    _l_(357673)

except ImportError:
    pass
space4mean = ({'model_class': _n_(357674, "func_model", lambda: func_model),
             'data': _n_(357675, "small_df", lambda: small_df),
             'init_a': [],
             'init_k': {_c_(357681, _a_(357677, _n_(357676, "hp", lambda: hp), "choice"), 'winsize', _c_(357680, _a_(357679, _n_(357678, "np", lambda: np), "arange"), 100))},
             'train_a': [],
             'train_k': {},
             'pred_a': [],
             'pred_k': {_c_(357684, _a_(357683, _n_(357682, "hp", lambda: hp), "choice"), 'use_new_points', [True, False])}
              })
_l_(357685)
best = _c_(357691, _n_(357686, "fmin", lambda: fmin), _n_(357687, "optifunc", lambda: optifunc),
    _n_(357688, "space4mean", lambda: space4mean),
    algo=_a_(357690, _n_(357689, "tpe", lambda: tpe), "suggest"),
    max_evals=100)
_l_(357692)