# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71044447/attributeerror-keyedvectors-object-has-no-attribute-get-keras-embedding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from gensim.models import KeyedVectors
    _l_(400256)

except ImportError:
    pass

wv = _c_(400259, _a_(400258, _n_(400257, "KeyedVectors", lambda: KeyedVectors), "load_word2vec_format"), "german.model", binary = True)
_l_(400260)
try:
    from keras.models import Sequential
    _l_(400262)

except ImportError:
    pass

model = _c_(400264, _n_(400263, "Sequential", lambda: Sequential))
_l_(400265)
_c_(400271, _a_(400267, _n_(400266, "model", lambda: model), "add"), _c_(400270, _a_(400269, _n_(400268, "wv", lambda: wv), "get_keras_embedding")))
_l_(400272)