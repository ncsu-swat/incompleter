# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59274292/type-error-when-trying-to-list-all-the-sub-directories-of-a-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
TRAIN_PATH_ARRAY=['New folder/train/']
_l_(551888)
TEST_PATH_ARRAY=['New folder/test/']
_l_(551889)
train_ids = _c_(551895, _n_(551890, "next", lambda: next), _c_(551894, _a_(551892, _n_(551891, "os", lambda: os), "walk"), _n_(551893, "TRAIN_PATH_ARRAY", lambda: TRAIN_PATH_ARRAY)))[1]
_l_(551896)
test_ids = _c_(551902, _n_(551897, "next", lambda: next), _c_(551901, _a_(551899, _n_(551898, "os", lambda: os), "walk"), _n_(551900, "TEST_PATH_ARRAY", lambda: TEST_PATH_ARRAY)))[1]
_l_(551903)
_c_(551907, _a_(551906, _a_(551905, _n_(551904, "np", lambda: np), "random"), "seed"), 10)
_l_(551908)