# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61292051/hyperopt-typeerror-because-of-passing-parameters-to-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from hyperopt import fmin, hp, tpe
    _l_(365818)

except ImportError:
    pass
space4mean = ({'model_class': _n_(365819, "func_model", lambda: func_model),
             'data': _n_(365820, "small_df", lambda: small_df),
             'init_a': [],
             'init_k': {_c_(365826, _a_(365822, _n_(365821, "hp", lambda: hp), "choice"), 'winsize', _c_(365825, _a_(365824, _n_(365823, "np", lambda: np), "arange"), 100))},
             'train_a': [],
             'train_k': {},
             'pred_a': [],
             'pred_k': {_c_(365829, _a_(365828, _n_(365827, "hp", lambda: hp), "choice"), 'use_new_points', [True, False])}
              })
_l_(365830)
best = _c_(365836, _n_(365831, "fmin", lambda: fmin), _n_(365832, "optifunc", lambda: optifunc),
    _n_(365833, "space4mean", lambda: space4mean),
    algo=_a_(365835, _n_(365834, "tpe", lambda: tpe), "suggest"),
    max_evals=100)
_l_(365837)