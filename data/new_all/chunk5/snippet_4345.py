# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59443374/attribute-error-device-in-fast-ai-learner
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastai.vision import *
    _l_(703294)

except ImportError:
    pass

data = _c_(703302, _a_(703301, _c_(703300, _a_(703299, _c_(703298, _a_(703296, _n_(703295, "ImageList", lambda: ImageList), "from_df"), _n_(703297, "train_df", lambda: train_df), path='/working/'), "split_by_rand_pct"), 0.2), "label_from_df"), label_delim=',')
_l_(703303)

learner = _c_(703309, _n_(703304, "cnn_learner", lambda: cnn_learner), _n_(703305, "data", lambda: data), _a_(703307, _n_(703306, "models", lambda: models), "resnet18"), metrics=[_n_(703308, "accuracy", lambda: accuracy)])
_l_(703310)