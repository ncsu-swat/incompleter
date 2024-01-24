# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77291113/keras-model-add-nameerror-name-input-shape-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(347776)

except ImportError:
    pass
try:
    import pickle
    _l_(347778)

except ImportError:
    pass
try:
    import numpy as np
    _l_(347780)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(347782)

except ImportError:
    pass
try:
    from nltk.tokenize import RegexpTokenizer
    _l_(347784)

except ImportError:
    pass
try:
    from tensorflow.keras.models import Sequential, load_model
    _l_(347786)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import LSTM, Dense, Activation
    _l_(347788)

except ImportError:
    pass
try:
    from tensorflow.keras.optimizers import RMSprop
    _l_(347790)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import InputLayer
    _l_(347792)

except ImportError:
    pass
try:
    from keras.models import Sequential, load_model
    _l_(347794)

except ImportError:
    pass
try:
    from keras.layers import LSTM, Dense, Activation
    _l_(347796)

except ImportError:
    pass
try:
    from keras.optimizers import RMSprop
    _l_(347798)

except ImportError:
    pass
try:
    import keras
    _l_(347800)

except ImportError:
    pass


text = "This is an interisting text this is a text and i need to make this text longer otherwise it wont work"
_l_(347801)

tokenizer = _c_(347803, _n_(347802, "RegexpTokenizer", lambda: RegexpTokenizer), r"\w+")
_l_(347804)
tokens = _c_(347808, _a_(347806, _n_(347805, "tokenizer", lambda: tokenizer), "tokenize"), _n_(347807, "text", lambda: text))    # list of individual word with duplicates
_l_(347809)    # list of individual word with duplicates
#print(tokens)

unique_tokens = _c_(347813, _a_(347811, _n_(347810, "np", lambda: np), "unique"), _n_(347812, "tokens", lambda: tokens))
_l_(347814)
unique_token_index = {_n_(347815, "token", lambda: token): _n_(347816, "idx", lambda: idx) for idx, token in _c_(347819, _n_(347817, "enumerate", lambda: enumerate), _n_(347818, "unique_tokens", lambda: unique_tokens))}   
_l_(347820)   


n_words = 10
_l_(347821)
input_words = []
_l_(347822)
next_words = []
_l_(347823)

for i in _c_(347829, _n_(347824, "range", lambda: range), _c_(347827, _n_(347825, "len", lambda: len), _n_(347826, "tokens", lambda: tokens))- _n_(347828, "n_words", lambda: n_words)):
    _l_(347845)

    _c_(347836, _a_(347831, _n_(347830, "input_words", lambda: input_words), "append"), _n_(347832, "tokens", lambda: tokens)[_n_(347833, "i", lambda: i):_n_(347834, "i", lambda: i) + _n_(347835, "n_words", lambda: n_words)])  
    _l_(347837)  
    _c_(347843, _a_(347839, _n_(347838, "next_words", lambda: next_words), "append"), _n_(347840, "tokens", lambda: tokens)[_n_(347841, "i", lambda: i) + _n_(347842, "n_words", lambda: n_words)])   
    _l_(347844)   


X = _c_(347856, _a_(347847, _n_(347846, "np", lambda: np), "zeros"), (_c_(347850, _n_(347848, "len", lambda: len), _n_(347849, "input_words", lambda: input_words)), _n_(347851, "n_words", lambda: n_words), _c_(347854, _n_(347852, "len", lambda: len), _n_(347853, "unique_tokens", lambda: unique_tokens))), dtype=_n_(347855, "bool", lambda: bool))  
_l_(347857)  
Y = _c_(347867, _a_(347859, _n_(347858, "np", lambda: np), "zeros"), (_c_(347862, _n_(347860, "len", lambda: len), _n_(347861, "next_words", lambda: next_words)),_c_(347865, _n_(347863, "len", lambda: len), _n_(347864, "unique_tokens", lambda: unique_tokens))),dtype=_n_(347866, "bool", lambda: bool))
_l_(347868)



for i, words in _c_(347871, _n_(347869, "enumerate", lambda: enumerate), _n_(347870, "input_words", lambda: input_words)):
    _l_(347888)

    for j, word in _c_(347874, _n_(347872, "enumerate", lambda: enumerate), _n_(347873, "words", lambda: words)):
        _l_(347887)

        _n_(347875, "X", lambda: X)[_n_(347876, "i", lambda: i), _n_(347877, "j", lambda: j), _n_(347878, "unique_token_index", lambda: unique_token_index)[_n_(347879, "word", lambda: word)]] = 1
        _l_(347880)
        _n_(347881, "Y", lambda: Y)[_n_(347882, "i", lambda: i), _n_(347883, "unique_token_index", lambda: unique_token_index)[_n_(347884, "next_words", lambda: next_words)[_n_(347885, "i", lambda: i)]]] = 1
        _l_(347886)



model = _c_(347890, _n_(347889, "Sequential", lambda: Sequential))
_l_(347891)


_c_(347902, _a_(347893, _n_(347892, "model", lambda: model), "add"), _c_(347901, _n_(347894, "LSTM", lambda: LSTM), 128, _c_(347900, _n_(347895, "input_shape", lambda: input_shape), _n_(347896, "n_words", lambda: n_words), _c_(347899, _n_(347897, "len", lambda: len), _n_(347898, "unique_tokens", lambda: unique_tokens))), return_sequence=True))   
_l_(347903)   