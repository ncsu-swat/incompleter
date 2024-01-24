# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55854898/typeerror-when-using-tf-keras-optimizers-apply-gradients-method-in-tensorflow-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
theta = _c_(449974, _a_(449968, _n_(449967, "tf", lambda: tf), "Variable"), _c_(449971, _a_(449970, _n_(449969, "tf", lambda: tf), "zeros"), 100), dtype=_a_(449973, _n_(449972, "tf", lambda: tf), "float32"), name='theta')
_l_(449975)

@_a_(449977, _n_(449976, "tf", lambda: tf), "function")
def p(x):
    _l_(450015)

    N = _c_(449986, _a_(449979, _n_(449978, "tf", lambda: tf), "cast"), _c_(449983, _a_(449981, _n_(449980, "tf", lambda: tf), "shape"), _n_(449982, "x", lambda: x))[0], _a_(449985, _n_(449984, "tf", lambda: tf), "int64"))
    _l_(449987)
    softmax = _c_(449991, _a_(449989, _n_(449988, "tf", lambda: tf), "ones"), [_n_(449990, "N", lambda: N), 1]) * _c_(449996, _a_(449994, _a_(449993, _n_(449992, "tf", lambda: tf), "math"), "softmax"), _n_(449995, "theta", lambda: theta))
    _l_(449997)
    idx_x = _c_(450007, _a_(449999, _n_(449998, "tf", lambda: tf), "stack"), [_c_(450005, _a_(450001, _n_(450000, "tf", lambda: tf), "range"), _n_(450002, "N", lambda: N), dtype=_a_(450004, _n_(450003, "tf", lambda: tf), "int64")), _n_(450006, "x", lambda: x)-1], axis=1)
    _l_(450008)
    aux = _c_(450013, _a_(450010, _n_(450009, "tf", lambda: tf), "gather_nd"), _n_(450011, "softmax", lambda: softmax), _n_(450012, "idx_x", lambda: idx_x))
    _l_(450014)
    return aux


@_a_(450017, _n_(450016, "tf", lambda: tf), "function")
def softmaxLoss(x):
    _l_(450029)

    aux = _c_(450027, _a_(450019, _n_(450018, "tf", lambda: tf), "reduce_mean"), -_c_(450026, _a_(450022, _a_(450021, _n_(450020, "tf", lambda: tf), "math"), "log"), _c_(450025, _n_(450023, "p", lambda: p), _n_(450024, "x", lambda: x))))
    _l_(450028)
    return aux


train_dset = _c_(450040, _a_(450038, _c_(450037, _a_(450036, _c_(450035, _a_(450033, _a_(450032, _a_(450031, _n_(450030, "tf", lambda: tf), "data"), "Dataset"), "from_tensor_slices"), _n_(450034, "data_train", lambda: data_train)), "repeat"), 1), "batch"), _n_(450039, "BATCH_SIZE", lambda: BATCH_SIZE))
_l_(450041)


# Create the metrics
loss_metric = _c_(450046, _a_(450045, _a_(450044, _a_(450043, _n_(450042, "tf", lambda: tf), "keras"), "metrics"), "Mean"), name='train_loss')
_l_(450047)
val_loss_metric = _c_(450052, _a_(450051, _a_(450050, _a_(450049, _n_(450048, "tf", lambda: tf), "keras"), "metrics"), "Mean"), name='val_loss')
_l_(450053)
optimizer = _c_(450058, _a_(450057, _a_(450056, _a_(450055, _n_(450054, "tf", lambda: tf), "keras"), "optimizers"), "Adam"), 0.001)
_l_(450059)

@_a_(450061, _n_(450060, "tf", lambda: tf), "function")
def train_step(inputs):
    _l_(450089)

    with _c_(450064, _a_(450063, _n_(450062, "tf", lambda: tf), "GradientTape")) as tape:
        _l_(450069)

        log_loss = _c_(450067, _n_(450065, "softmaxLoss", lambda: softmaxLoss), _n_(450066, "inputs", lambda: inputs))
        _l_(450068)
    gradients = _c_(450074, _a_(450071, _n_(450070, "tape", lambda: tape), "gradient"), _n_(450072, "log_loss", lambda: log_loss),_n_(450073, "theta", lambda: theta))
    _l_(450075)
    _c_(450082, _a_(450077, _n_(450076, "optimizer", lambda: optimizer), "apply_gradients"), _c_(450081, _n_(450078, "zip", lambda: zip), _n_(450079, "gradients", lambda: gradients), _n_(450080, "theta", lambda: theta)))
    _l_(450083)
    # Update the metrics
    _c_(450087, _a_(450085, _n_(450084, "loss_metric", lambda: loss_metric), "update_state"), _n_(450086, "log_loss", lambda: log_loss))
    _l_(450088)


for epoch in _c_(450092, _n_(450090, "range", lambda: range), _n_(450091, "NUM_EPOCHS", lambda: NUM_EPOCHS)):
    _l_(450107)

    # Reset the metrics
    _c_(450095, _a_(450094, _n_(450093, "loss_metric", lambda: loss_metric), "reset_states"))
    _l_(450096)

    # Shuffle dataset before each training epoch
    train_dset = _c_(450099, _a_(450098, _n_(450097, "train_dset", lambda: train_dset), "shuffle"), buffer_size=10000)
    _l_(450100)
    for inputs in _n_(450101, "train_dset", lambda: train_dset):
        _l_(450106)

        _c_(450104, _n_(450102, "train_step", lambda: train_step), _n_(450103, "inputs", lambda: inputs))
        _l_(450105)