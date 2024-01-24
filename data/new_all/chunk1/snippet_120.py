# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65366442/cannot-convert-a-symbolic-keras-input-output-to-a-numpy-array-typeerror-when-usi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import tensorflow as tf
  _l_(415874)

except ImportError:
  pass
try:
  import numpy as np
  _l_(415876)

except ImportError:
  pass

 
TextVectorization = _a_(415882, _a_(415881, _a_(415880, _a_(415879, _a_(415878, _n_(415877, "tf", lambda: tf), "keras"), "layers"), "experimental"), "preprocessing"), "TextVectorization")
_l_(415883)

class SampledSoftmaxLoss:
  _l_(415929)


  def __init__(self, model, n_classes):
    _l_(415901)

    _n_(415884, "self", lambda: self).model = _n_(415885, "model", lambda: model)
    _l_(415886)
    output_layer = _a_(415888, _n_(415887, "model", lambda: model), "layers")[-1]
    _l_(415889)
    _n_(415890, "self", lambda: self).input = _a_(415892, _n_(415891, "output_layer", lambda: output_layer), "input")
    _l_(415893)
    _n_(415894, "self", lambda: self).weights = _a_(415896, _n_(415895, "output_layer", lambda: output_layer), "weights")
    _l_(415897)
    _n_(415898, "self", lambda: self).n_classes = _n_(415899, "n_classes", lambda: n_classes)
    _l_(415900)


  def loss(self, y_true, y_pred, **kwargs):
    _l_(415928)

    labels = _c_(415905, _a_(415903, _n_(415902, "tf", lambda: tf), "argmax"), _n_(415904, "y_true", lambda: y_true), axis=1)
    _l_(415906)
    labels = _c_(415910, _a_(415908, _n_(415907, "tf", lambda: tf), "expand_dims"), _n_(415909, "labels", lambda: labels), -1)
    _l_(415911)
    loss = _c_(415924, _a_(415914, _a_(415913, _n_(415912, "tf", lambda: tf), "nn"), "sampled_softmax_loss"), weights=_a_(415916, _n_(415915, "self", lambda: self), "weights")[0],
        biases=_a_(415918, _n_(415917, "self", lambda: self), "weights")[1],
        labels=_n_(415919, "labels", lambda: labels),
        inputs=_a_(415921, _n_(415920, "self", lambda: self), "input"),
        num_sampled = 3,
        num_classes = _a_(415923, _n_(415922, "self", lambda: self), "n_classes")
    )
    _l_(415925)
    aux = _n_(415926, "loss", lambda: loss)
    _l_(415927)
    return aux


max_features = 50  # Maximum vocab size.
_l_(415930)  # Maximum vocab size.
max_len = 10  # Sequence length to pad the outputs to.
_l_(415931)  # Sequence length to pad the outputs to.
embedding_dims = 5
_l_(415932)

input_data = _c_(415935, _a_(415934, _n_(415933, "np", lambda: np), "array"), [ 
    "Python Machine Learning",
    "Data Science from Scratch: First Principles with Python", 
    "Hands-On Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools, and Techniques for Building Intelligent Systems",
    "Introduction to Machine Learning with Python: A Guide for Data Scientists",
    "Vital Introduction to Machine Learning with Python: Best Practices to Improve and Optimize Machine Learning Systems and Algorithms",
    "Machine Learning in Python: Essential Techniques for Predictive Analysis",
    "Python Data Science Handbook: Essential Tools for Working with Data",
    "Introducing Data Science: Big Data, Machine Learning, and more, using Python tools",
    "Real-World Machine Learning"])
_l_(415936)

labels_one_hot = []
_l_(415937)
for i in _c_(415942, _n_(415938, "range", lambda: range), _c_(415941, _n_(415939, "len", lambda: len), _n_(415940, "input_data", lambda: input_data))):
  _l_(415957)

  labels = _c_(415947, _a_(415945, _a_(415944, _n_(415943, "np", lambda: np), "random"), "randint"), 0, 6, _n_(415946, "max_features", lambda: max_features))
  _l_(415948)
  _n_(415949, "labels", lambda: labels)[_n_(415950, "labels", lambda: labels)>1] = 1
  _l_(415951)
  _c_(415955, _a_(415953, _n_(415952, "labels_one_hot", lambda: labels_one_hot), "append"), _n_(415954, "labels", lambda: labels))
  _l_(415956)

labels_one_hot = _c_(415961, _a_(415959, _n_(415958, "np", lambda: np), "array"), _n_(415960, "labels_one_hot", lambda: labels_one_hot))
_l_(415962)
 
# Create the text categorical encoding layer.
vectorize_layer = _c_(415966, _n_(415963, "TextVectorization", lambda: TextVectorization), max_tokens=_n_(415964, "max_features", lambda: max_features),
         output_mode='int',
         output_sequence_length=_n_(415965, "max_len", lambda: max_len))
_l_(415967)
 
_c_(415971, _a_(415969, _n_(415968, "vectorize_layer", lambda: vectorize_layer), "adapt"), _n_(415970, "text_dataset", lambda: text_dataset))
_l_(415972)
inp = _c_(415978, _a_(415975, _a_(415974, _n_(415973, "tf", lambda: tf), "keras"), "Input"), shape=(1,), dtype=_a_(415977, _n_(415976, "tf", lambda: tf), "string"))
_l_(415979)
idxs = _c_(415982, _n_(415980, "vectorize_layer", lambda: vectorize_layer), _n_(415981, "inp", lambda: inp))
_l_(415983)
embed = _c_(415993, _c_(415991, _a_(415987, _a_(415986, _a_(415985, _n_(415984, "tf", lambda: tf), "keras"), "layers"), "Embedding"), _n_(415988, "max_features", lambda: max_features) + 1, _n_(415989, "embedding_dims", lambda: embedding_dims),input_length=_n_(415990, "max_len", lambda: max_len)), _n_(415992, "idxs", lambda: idxs))
_l_(415994)
flat = _c_(416001, _c_(415999, _a_(415998, _a_(415997, _a_(415996, _n_(415995, "tf", lambda: tf), "keras"), "layers"), "Flatten")), _n_(416000, "embed", lambda: embed))
_l_(416002)
out = _c_(416011, _c_(416009, _a_(416006, _a_(416005, _a_(416004, _n_(416003, "tf", lambda: tf), "keras"), "layers"), "Dense"), _a_(416008, _n_(416007, "labels_one_hot", lambda: labels_one_hot), "shape")[1]), _n_(416010, "flat", lambda: flat))
_l_(416012)

model = _c_(416019, _a_(416016, _a_(416015, _a_(416014, _n_(416013, "tf", lambda: tf), "keras"), "models"), "Model"), _n_(416017, "inp", lambda: inp), _n_(416018, "out", lambda: out))
_l_(416020)

softmax = _c_(416025, _n_(416021, "SampledSoftmaxLoss", lambda: SampledSoftmaxLoss), _n_(416022, "model", lambda: model), _a_(416024, _n_(416023, "labels_one_hot", lambda: labels_one_hot), "shape")[1])
_l_(416026)

_c_(416031, _a_(416028, _n_(416027, "model", lambda: model), "compile"), 'adam', loss=_a_(416030, _n_(416029, "softmax", lambda: softmax), "loss"))
_l_(416032)
_c_(416035, _a_(416034, _n_(416033, "model", lambda: model), "summary"))
_l_(416036)
_c_(416041, _a_(416038, _n_(416037, "model", lambda: model), "fit"), _n_(416039, "input_data", lambda: input_data), _n_(416040, "labels_one_hot", lambda: labels_one_hot))
_l_(416042)
_c_(416046, _a_(416044, _n_(416043, "model", lambda: model), "predict"), _n_(416045, "input_data", lambda: input_data))
_l_(416047)