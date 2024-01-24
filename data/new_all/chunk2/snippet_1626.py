# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(468887, "converter", lambda: converter).representative_dataset = _c_(468890, _n_(468888, "my_batch_generator", lambda: my_batch_generator), _n_(468889, "data", lambda: data))
_l_(468891)
_n_(468892, "converter", lambda: converter).optimizations = [_a_(468896, _a_(468895, _a_(468894, _n_(468893, "tf", lambda: tf), "lite"), "Optimize"), "DEFAULT")]
_l_(468897)
_a_(468899, _n_(468898, "converter", lambda: converter), "target_spec").supported_ops = [_a_(468903, _a_(468902, _a_(468901, _n_(468900, "tf", lambda: tf), "lite"), "OpsSet"), "TFLITE_BUILTINS"), _a_(468907, _a_(468906, _a_(468905, _n_(468904, "tf", lambda: tf), "lite"), "OpsSet"), "SELECT_TF_OPS")]
_l_(468908)
_n_(468909, "converter", lambda: converter)._experimental_lower_tensor_list_ops = False
_l_(468910)
quantized_tflite_model = _c_(468913, _a_(468912, _n_(468911, "converter", lambda: converter), "convert"))
_l_(468914)