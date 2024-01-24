# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75832035/no-properties-such-as-wordngram-is-retrievable-from-fasttext-model-object-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fasttext
    _l_(618914)

except ImportError:
    pass

model = _c_(618917, _a_(618916, _n_(618915, "fasttext", lambda: fasttext), "load_model"), "path/to/model.bin")
_l_(618918)

_a_(618920, _n_(618919, "model", lambda: model), "wordNgrams")
_l_(618921)
# `AttributeError: '_FastText' object has no attribute 'wordNgrams'`

_c_(618924, _n_(618922, "dir", lambda: dir), _n_(618923, "model", lambda: model))
_l_(618925)

# ['__class__',
#  '__contains__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  '_labels',
#  '_words',
#  'f',
#  'get_analogies',
#  'get_dimension',
#  'get_input_matrix',
#  'get_input_vector',
#  'get_label_id',
#  'get_labels',
#  'get_line',
#  'get_meter',
#  'get_nearest_neighbors',
#  'get_output_matrix',
#  'get_sentence_vector',
#  'get_subword_id',
#  'get_subwords',
#  'get_word_id',
#  'get_word_vector',
#  'get_words',
#  'is_quantized',
#  'labels',
#  'predict',
#  'quantize',
#  'save_model',
#  'set_args',
#  'set_matrices',
#  'test',
#  'test_label',
#  'words']