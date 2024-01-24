# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67485998/estimator-predict-typeerror-expected-any-non-tensor-type-got-a-tensor-instea
# Create the classifier
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(595268, _n_(595264, "print", lambda: print), _c_(595267, _a_(595265, "Creating classifier from {}", "format"), _n_(595266, "checkpoint_path", lambda: checkpoint_path)))
_l_(595269)
classifier = _c_(595276, _a_(595272, _a_(595271, _n_(595270, "tf", lambda: tf), "estimator"), "Estimator"), model_fn=_n_(595273, "vgg_model_fn", lambda: vgg_model_fn),
    params=_n_(595274, "params", lambda: params),
    model_dir=_n_(595275, "checkpoint_path", lambda: checkpoint_path),
)
_l_(595277)

_c_(595279, _n_(595278, "print", lambda: print), "Computing predictions")
_l_(595280)
predictions = _c_(595289, _a_(595282, _n_(595281, "classifier", lambda: classifier), "predict"), input_fn=_c_(595288, _a_(595286, _a_(595285, _a_(595284, _n_(595283, "tf", lambda: tf), "estimator"), "inputs"), "numpy_input_fn"), {"x": _n_(595287, "video", lambda: video)},
        batch_size=1,
        shuffle=False,
    )
)
_l_(595290)

# Print predictions
predictions = _c_(595293, _n_(595291, "list", lambda: list), _n_(595292, "predictions", lambda: predictions))
_l_(595294)
predicted_class = _n_(595295, "predictions", lambda: predictions)["classes"]
_l_(595296)
top_k_classes = _c_(595299, _a_(595298, (-_n_(595297, "predictions", lambda: predictions)["probabilities"]), "argsort"))[:_c_(595302, _n_(595300, "int", lambda: int), _n_(595301, "k", lambda: k))]
_l_(595303)