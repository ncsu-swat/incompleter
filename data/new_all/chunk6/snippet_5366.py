# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61292051/hyperopt-typeerror-because-of-passing-parameters-to-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from hyperopt import fmin, hp, tpe
    _l_(345947)

except ImportError:
    pass
space4mean = ({'model_class': _n_(345948, "func_model", lambda: func_model),
             'data': _n_(345949, "small_df", lambda: small_df),
             'init_a': [],
             'init_k': {_c_(345955, _a_(345951, _n_(345950, "hp", lambda: hp), "choice"), 'winsize', _c_(345954, _a_(345953, _n_(345952, "np", lambda: np), "arange"), 100))},
             'train_a': [],
             'train_k': {},
             'pred_a': [],
             'pred_k': {_c_(345958, _a_(345957, _n_(345956, "hp", lambda: hp), "choice"), 'use_new_points', [True, False])}
              })
_l_(345959)
best = _c_(345965, _n_(345960, "fmin", lambda: fmin), _n_(345961, "optifunc", lambda: optifunc),
    _n_(345962, "space4mean", lambda: space4mean),
    algo=_a_(345964, _n_(345963, "tpe", lambda: tpe), "suggest"),
    max_evals=100)
_l_(345966)