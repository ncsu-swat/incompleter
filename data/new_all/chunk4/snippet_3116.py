# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44190555/tensorflow-version-1-1-0-skcompat-attributeerror
#create estimator
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
vggnet_classifier = _c_(613810, _a_(613805, _n_(613804, "learn", lambda: learn), "SKCompat"), _c_(613809, _a_(613807, _n_(613806, "learn", lambda: learn), "Estimator"), model_fn=_n_(613808, "vggnet_model", lambda: vggnet_model), model_dir= "/tmp/vgg_net"))
_l_(613811)

# Set up logging for predictions
tensors_to_log = {"probabilities": "softmax_tensor"}
_l_(613812)
logging_hook = _c_(613817, _a_(613815, _a_(613814, _n_(613813, "tf", lambda: tf), "train"), "LoggingTensorHook"), tensors=_n_(613816, "tensors_to_log", lambda: tensors_to_log), every_n_iter=100)
_l_(613818)

#train model
_c_(613824, _a_(613820, _n_(613819, "vggnet_classifier", lambda: vggnet_classifier), "fit"), x=_n_(613821, "X_train", lambda: X_train),
    y=_n_(613822, "y_train", lambda: y_train),
    batch_size=100,
    steps=2,
    monitors=[_n_(613823, "logging_hook", lambda: logging_hook)])
_l_(613825)

# Configure the accuracy metric for evaluation
metrics = {
    "accuracy":
        _c_(613831, _a_(613827, _n_(613826, "learn", lambda: learn), "MetricSpec"), metric_fn=_a_(613830, _a_(613829, _n_(613828, "tf", lambda: tf), "metrics"), "accuracy"), prediction_key="classes"),}
_l_(613832)

# Evaluate the model and print results
eval_results = _c_(613838, _a_(613834, _n_(613833, "vggnet_classifier", lambda: vggnet_classifier), "evaluate"), x=_n_(613835, "X_val", lambda: X_val), y=_n_(613836, "y_val", lambda: y_val), metrics=_n_(613837, "metrics", lambda: metrics))
_l_(613839)
_c_(613842, _n_(613840, "print", lambda: print), _n_(613841, "eval_results", lambda: eval_results))
_l_(613843)