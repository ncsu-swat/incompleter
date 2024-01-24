# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_batch(data_x,data_y,batch_size=32):
    _l_(522536)

    batch_n=_c_(522514, _n_(522512, "len", lambda: len), _n_(522513, "data_x", lambda: data_x))//_n_(522515, "batch_size", lambda: batch_size)
    _l_(522516)
    for i in _c_(522519, _n_(522517, "range", lambda: range), _n_(522518, "batch_n", lambda: batch_n)):
        _l_(522535)

        batch_x=_n_(522520, "data_x", lambda: data_x)[_n_(522521, "i", lambda: i)*_n_(522522, "batch_size", lambda: batch_size):(_n_(522523, "i", lambda: i)+1)*_n_(522524, "batch_size", lambda: batch_size)]
        _l_(522525)
        batch_y=_n_(522526, "data_y", lambda: data_y)[_n_(522527, "i", lambda: i)*_n_(522528, "batch_size", lambda: batch_size):(_n_(522529, "i", lambda: i)+1)*_n_(522530, "batch_size", lambda: batch_size)]
        _l_(522531)
        yield _n_(522532, "batch_x", lambda: batch_x),_n_(522533, "batch_y", lambda: batch_y)
        _l_(522534)

epochs = 25
_l_(522537)
train_collect = 20
_l_(522538)
train_print=_n_(522539, "train_collect", lambda: train_collect)*2
_l_(522540)

learning_rate_value = 0.001
_l_(522541)
batch_size=400
_l_(522542)

x_collect = []
_l_(522543)
train_loss_collect = []
_l_(522544)
train_acc_collect = []
_l_(522545)
valid_loss_collect = []
_l_(522546)
valid_acc_collect = []
_l_(522547)

saver = _c_(522551, _a_(522550, _a_(522549, _n_(522548, "tf", lambda: tf), "train"), "Saver"))
_l_(522552)