# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69720033/typeerror-not-supported-between-instances-of-int-and-str-when-i-run-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import train_test_split
    _l_(638469)

except ImportError:
    pass
train_X, test_X, train_y, test_y = _c_(638474, _n_(638470, "train_test_split", lambda: train_test_split), _n_(638471, "df", lambda: df)['Base_Reviews'], _n_(638472, "df", lambda: df)['My_Labels'],
                                                    stratify=_n_(638473, "df", lambda: df)['My_Labels'], 
                                                    test_size=0.25)
_l_(638475)
_c_(638479, _n_(638476, "print", lambda: print), "Train shape : ",_a_(638478, _n_(638477, "train_X", lambda: train_X), "shape"))
_l_(638480)
_c_(638484, _n_(638481, "print", lambda: print), "Test shape : ",_a_(638483, _n_(638482, "test_X", lambda: test_X), "shape"))
_l_(638485)
## Tokenize the sentences
tokenizer = _c_(638488, _n_(638486, "Tokenizer", lambda: Tokenizer), num_words= _n_(638487, "max_features", lambda: max_features))
_l_(638489)
_c_(638495, _a_(638491, _n_(638490, "tokenizer", lambda: tokenizer), "fit_on_texts"), _c_(638494, _n_(638492, "list", lambda: list), _n_(638493, "train_X", lambda: train_X)))
_l_(638496)
train_X = _c_(638500, _a_(638498, _n_(638497, "tokenizer", lambda: tokenizer), "texts_to_sequences"), _n_(638499, "train_X", lambda: train_X))
_l_(638501)
test_X = _c_(638505, _a_(638503, _n_(638502, "tokenizer", lambda: tokenizer), "texts_to_sequences"), _n_(638504, "test_X", lambda: test_X))
_l_(638506)

## Pad the sentences 
train_X = _c_(638510, _n_(638507, "pad_sequences", lambda: pad_sequences), _n_(638508, "train_X", lambda: train_X), maxlen=_n_(638509, "maxlen", lambda: maxlen))
_l_(638511)
test_X = _c_(638515, _n_(638512, "pad_sequences", lambda: pad_sequences), _n_(638513, "test_X", lambda: test_X), maxlen=_n_(638514, "maxlen", lambda: maxlen))
_l_(638516)