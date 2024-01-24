# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74719326/attributeerror-only-occurs-during-pytest-run-custom-classes-or-functions-expor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pytest
    _l_(435852)

except ImportError:
    pass
try:
    from fastai.vision.all import *
    _l_(435854)

except ImportError:
    pass
try:
    from project.predict import my_func, prediction
    _l_(435856)

except ImportError:
    pass


model = _c_(435858, _n_(435857, "load_learner", lambda: load_learner), 'model_path/', cpu=True)
_l_(435859)
_c_(435864, _a_(435861, _n_(435860, "model", lambda: model), "load"), _a_(435863, _n_(435862, "fast_ai_params", lambda: fast_ai_params), "weights"))
_l_(435865)


def my_test():
    _l_(435875)

    pred = _c_(435870, _n_(435866, "prediction", lambda: prediction), _n_(435867, "tile_params", lambda: tile_params), _n_(435868, "model", lambda: model), _n_(435869, "full_tile_path", lambda: full_tile_path))
    _l_(435871)

    assert _a_(435873, _n_(435872, "pred", lambda: pred), "shape")
    _l_(435874)