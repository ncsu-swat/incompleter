# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53272808/tensorflow-keras-typeerror-value-passed-to-parameter-labels-has-datatype-f
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(573407)

except ImportError:
    pass
#tf.enable_eager_execution()
vocab_size=100
_l_(573408)
embedding_dim=256
_l_(573409)
seq_len=10
_l_(573410)
model=_c_(573414, _a_(573413, _a_(573412, _n_(573411, "tf", lambda: tf), "keras"), "Sequential"))
_l_(573415)
_c_(573426, _a_(573417, _n_(573416, "model", lambda: model), "add"), _c_(573425, _a_(573421, _a_(573420, _a_(573419, _n_(573418, "tf", lambda: tf), "keras"), "layers"), "Embedding"), _n_(573422, "vocab_size", lambda: vocab_size), _n_(573423, "embedding_dim", lambda: embedding_dim), input_length=_n_(573424, "seq_len", lambda: seq_len)))
_l_(573427)
_c_(573436, _a_(573429, _n_(573428, "model", lambda: model), "add"), _c_(573435, _a_(573433, _a_(573432, _a_(573431, _n_(573430, "tf", lambda: tf), "keras"), "layers"), "Dense"), _n_(573434, "vocab_size", lambda: vocab_size)))
_l_(573437)
_c_(573447, _a_(573439, _n_(573438, "model", lambda: model), "compile"), optimizer = _c_(573443, _a_(573442, _a_(573441, _n_(573440, "tf", lambda: tf), "train"), "GradientDescentOptimizer"), 1.0),loss = _a_(573446, _a_(573445, _n_(573444, "tf", lambda: tf), "losses"), "sparse_softmax_cross_entropy"))#tf.keras.metrics.sparse_categorical_crossentropy
_l_(573448)#tf.keras.metrics.sparse_categorical_crossentropy