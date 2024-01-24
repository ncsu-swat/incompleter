# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67485998/estimator-predict-typeerror-expected-any-non-tensor-type-got-a-tensor-instea
# Create the classifier
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(588096, _n_(588092, "print", lambda: print), _c_(588095, _a_(588093, "Creating classifier from {}", "format"), _n_(588094, "checkpoint_path", lambda: checkpoint_path)))
_l_(588097)
classifier = _c_(588104, _a_(588100, _a_(588099, _n_(588098, "tf", lambda: tf), "estimator"), "Estimator"), model_fn=_n_(588101, "vgg_model_fn", lambda: vgg_model_fn),
    params=_n_(588102, "params", lambda: params),
    model_dir=_n_(588103, "checkpoint_path", lambda: checkpoint_path),
)
_l_(588105)

_c_(588107, _n_(588106, "print", lambda: print), "Computing predictions")
_l_(588108)
predictions = _c_(588117, _a_(588110, _n_(588109, "classifier", lambda: classifier), "predict"), input_fn=_c_(588116, _a_(588114, _a_(588113, _a_(588112, _n_(588111, "tf", lambda: tf), "estimator"), "inputs"), "numpy_input_fn"), {"x": _n_(588115, "video", lambda: video)},
        batch_size=1,
        shuffle=False,
    )
)
_l_(588118)

# Print predictions
predictions = _c_(588121, _n_(588119, "list", lambda: list), _n_(588120, "predictions", lambda: predictions))
_l_(588122)
predicted_class = _n_(588123, "predictions", lambda: predictions)["classes"]
_l_(588124)
top_k_classes = _c_(588127, _a_(588126, (-_n_(588125, "predictions", lambda: predictions)["probabilities"]), "argsort"))[:_c_(588130, _n_(588128, "int", lambda: int), _n_(588129, "k", lambda: k))]
_l_(588131)