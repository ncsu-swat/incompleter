# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54377670/error-while-defining-my-keras-model-attributeerror-nonetype-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import keras
    _l_(462840)

except ImportError:
    pass
try:
    from keras.layers import *
    _l_(462842)

except ImportError:
    pass
try:
    from keras.models import Model
    _l_(462844)

except ImportError:
    pass
try:
    from keras.activations import softmax
    _l_(462846)

except ImportError:
    pass
try:
    import keras.backend as K
    _l_(462848)

except ImportError:
    pass

query = _c_(462850, _n_(462849, "Input", lambda: Input), name='query', shape=(10,))
_l_(462851)
doc = _c_(462853, _n_(462852, "Input", lambda: Input), name='doc', shape=(100,))
_l_(462854)
embedding = _c_(462856, _n_(462855, "Embedding", lambda: Embedding), 1125, 50, trainable=True)
_l_(462857)
q_embed = _c_(462860, _n_(462858, "embedding", lambda: embedding), _n_(462859, "query", lambda: query))
_l_(462861)
d_embed = _c_(462864, _n_(462862, "embedding", lambda: embedding), _n_(462863, "doc", lambda: doc))
_l_(462865)
q_w = _c_(462869, _c_(462867, _n_(462866, "Dense", lambda: Dense), 1, use_bias=False), _n_(462868, "q_embed", lambda: q_embed))
_l_(462870)
q_w = _c_(462877, _c_(462875, _n_(462871, "Lambda", lambda: Lambda), lambda x: _c_(462874, _n_(462872, "softmax", lambda: softmax), _n_(462873, "x", lambda: x), axis=1), output_shape=(10,)), _n_(462876, "q_w", lambda: q_w))
_l_(462878)
q_w_layer = _c_(462886, _c_(462884, _n_(462879, "Lambda", lambda: Lambda), lambda x: _c_(462883, _a_(462881, _n_(462880, "K", lambda: K), "repeat_elements"), _n_(462882, "q_w", lambda: q_w), rep=50, axis=2)), _n_(462885, "q_w", lambda: q_w))
_l_(462887)
q_embed = _c_(462892, _c_(462889, _n_(462888, "Multiply", lambda: Multiply)), [_n_(462890, "q_w_layer", lambda: q_w_layer), _n_(462891, "q_embed", lambda: q_embed)])
_l_(462893)
cross = _c_(462898, _c_(462895, _n_(462894, "Dot", lambda: Dot), axes=[2, 2], normalize=False), [_n_(462896, "q_embed", lambda: q_embed), _n_(462897, "d_embed", lambda: d_embed)])
_l_(462899)
cross = _c_(462903, _c_(462901, _n_(462900, "Permute", lambda: Permute), (2, 1)), _n_(462902, "cross", lambda: cross))
_l_(462904)
contxt = _c_(462908, _c_(462906, _n_(462905, "Conv1D", lambda: Conv1D), 30, 5, strides=5, activation='relu', name="conv"), _n_(462907, "cross", lambda: cross))
_l_(462909)
contxt = _c_(462913, _c_(462911, _n_(462910, "BatchNormalization", lambda: BatchNormalization)), _n_(462912, "contxt", lambda: contxt))
_l_(462914)
contxt = _c_(462918, _c_(462916, _n_(462915, "Dropout", lambda: Dropout), 0.2), _n_(462917, "contxt", lambda: contxt))
_l_(462919)
attention = _c_(462923, _c_(462921, _n_(462920, "Dense", lambda: Dense), 1, use_bias=False), _n_(462922, "contxt", lambda: contxt))
_l_(462924)
attention = _c_(462928, _c_(462926, _n_(462925, "Activation", lambda: Activation), 'softmax'), _n_(462927, "attention", lambda: attention))
_l_(462929)
contxt = _c_(462934, _c_(462931, _n_(462930, "Multiply", lambda: Multiply)), [_n_(462932, "contxt", lambda: contxt), _n_(462933, "attention", lambda: attention)])
_l_(462935)
important_context = _c_(462937, _n_(462936, "MaxPooling1D", lambda: MaxPooling1D), pool_size=2, strides=2)
_l_(462938)
contxt = _c_(462941, _n_(462939, "important_context", lambda: important_context), _n_(462940, "contxt", lambda: contxt))
_l_(462942)
word_level = _c_(462946, _c_(462944, _n_(462943, "Permute", lambda: Permute), (2, 1)), _n_(462945, "cross", lambda: cross))
_l_(462947)

# ############ This is the part that caused the problem

word_level_padd = _c_(462969, _a_(462949, _n_(462948, "K", lambda: K), "reshape"), _c_(462964, _c_(462955, _n_(462950, "ZeroPadding1D", lambda: ZeroPadding1D), (0, _a_(462952, _n_(462951, "contxt", lambda: contxt), "shape")[2] - _a_(462954, _n_(462953, "word_level", lambda: word_level), "shape")[2])), _c_(462963, _a_(462957, _n_(462956, "K", lambda: K), "reshape"), _n_(462958, "word_level", lambda: word_level),
                                (-1, 
                                 _a_(462960, _n_(462959, "word_level", lambda: word_level), "shape")[2], 
                                 _a_(462962, _n_(462961, "word_level", lambda: word_level), "shape")[1]
                                ))),
                           (-1, _a_(462966, _n_(462965, "word_level", lambda: word_level), "shape")[1], _a_(462968, _n_(462967, "contxt", lambda: contxt), "shape")[2])
                           ) if _a_(462971, _n_(462970, "word_level", lambda: word_level), "shape")[-1] < _a_(462973, _n_(462972, "contxt", lambda: contxt), "shape")[-1] else _n_(462974, "word_level", lambda: word_level)
_l_(462975)
contxt_padded = _c_(462997, _a_(462977, _n_(462976, "K", lambda: K), "reshape"), _c_(462992, _c_(462983, _n_(462978, "ZeroPadding1D", lambda: ZeroPadding1D), (0, _a_(462980, _n_(462979, "word_level", lambda: word_level), "shape")[2] -_a_(462982, _n_(462981, "contxt", lambda: contxt), "shape")[2])), _c_(462991, _a_(462985, _n_(462984, "K", lambda: K), "reshape"), _n_(462986, "contxt", lambda: contxt),
                            (-1, 
                             _a_(462988, _n_(462987, "contxt", lambda: contxt), "shape")[2], 
                             _a_(462990, _n_(462989, "contxt", lambda: contxt), "shape")[1]
                           ))), 
                         (-1, _a_(462994, _n_(462993, "contxt", lambda: contxt), "shape")[1], _a_(462996, _n_(462995, "word_level", lambda: word_level), "shape")[2])
                         ) if _a_(462999, _n_(462998, "contxt", lambda: contxt), "shape")[-1] < _a_(463001, _n_(463000, "word_level", lambda: word_level), "shape")[-1] else _n_(463002, "contxt", lambda: contxt)
_l_(463003)
contxt = _c_(463008, _c_(463005, _n_(463004, "Concatenate", lambda: Concatenate), axis=1, name="merge_levels"), [_n_(463006, "word_level_padd", lambda: word_level_padd), _n_(463007, "contxt_padded", lambda: contxt_padded)])
_l_(463009)

# This is the part that caused the problem #############

lstm_units = _c_(463013, _n_(463010, "int", lambda: int), _a_(463012, _n_(463011, "contxt", lambda: contxt), "shape")[1])
_l_(463014)
contxt = _c_(463021, _c_(463019, _n_(463015, "Bidirectional", lambda: Bidirectional), _c_(463018, _n_(463016, "LSTM", lambda: LSTM), _n_(463017, "lstm_units", lambda: lstm_units), return_sequences=False)), _n_(463020, "contxt", lambda: contxt))
_l_(463022)
contxt = _c_(463026, _c_(463024, _n_(463023, "BatchNormalization", lambda: BatchNormalization)), _n_(463025, "contxt", lambda: contxt))
_l_(463027)
contxt = _c_(463031, _c_(463029, _n_(463028, "Dropout", lambda: Dropout), 0.2), _n_(463030, "contxt", lambda: contxt))
_l_(463032)
out_ = _c_(463036, _c_(463034, _n_(463033, "Dense", lambda: Dense), 1), _n_(463035, "contxt", lambda: contxt))
_l_(463037)
model = _c_(463042, _n_(463038, "Model", lambda: Model), inputs=[_n_(463039, "query", lambda: query), _n_(463040, "doc", lambda: doc)], outputs=_n_(463041, "out_", lambda: out_))
_l_(463043)