# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61109095/typeerror-nonetype-object-is-not-subscriptable-when-i-train-a-cnn-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
kappa_metrics = _c_(547749, _n_(547748, "Metrics", lambda: Metrics))
_l_(547750)

history = _c_(547760, _a_(547752, _n_(547751, "model", lambda: model), "fit"), _n_(547753, "data_generator", lambda: data_generator),
    steps_per_epoch = _a_(547755, _n_(547754, "x_train", lambda: x_train), "shape")[0] / _n_(547756, "BATCH_SIZE", lambda: BATCH_SIZE),
    epochs = 15,
    validation_data = (_n_(547757, "x_val", lambda: x_val), _n_(547758, "y_val", lambda: y_val)),
    callbacks = [_n_(547759, "kappa_metrics", lambda: kappa_metrics)]
)
_l_(547761)