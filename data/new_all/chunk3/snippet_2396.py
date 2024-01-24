# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model=_c_(571349, _n_(571348, "multilayer_perceptron", lambda: multilayer_perceptron))
_l_(571350)
restorer=_c_(571354, _a_(571353, _a_(571352, _n_(571351, "tf", lambda: tf), "train"), "Saver"))
_l_(571355)
with _c_(571358, _a_(571357, _n_(571356, "tf", lambda: tf), "Session")) as sess:
    _l_(571377)

    _c_(571362, _a_(571360, _n_(571359, "restorer", lambda: restorer), "restore"), _n_(571361, "sess", lambda: sess),"./insurance2.ckpt")
    _l_(571363)
    feed={
        _a_(571365, _n_(571364, "pred1", lambda: pred1), "inputs"):_n_(571366, "test_data", lambda: test_data),
        _a_(571368, _n_(571367, "pred1", lambda: pred1), "is_training"):False
    }
    _l_(571369)
    test_predict=_c_(571375, _a_(571371, _n_(571370, "sess", lambda: sess), "run"), _a_(571373, _n_(571372, "pred1", lambda: pred1), "predicted"),feed_dict=_n_(571374, "feed", lambda: feed))
    _l_(571376)