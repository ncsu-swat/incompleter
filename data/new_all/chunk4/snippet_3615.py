# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71272910/attributeerror-spacy-tokenizer-tokenizer-object-has-no-attribute-tokens-from
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
X_train_lemma = _c_(582078, _a_(582076, _n_(582075, "lemma_vect", lambda: lemma_vect), "fit_transform"), _n_(582077, "text_train", lambda: text_train))
_l_(582079)
_c_(582085, _n_(582080, "print", lambda: print), _c_(582084, _a_(582081, "X_train_lemma.shape: {}", "format"), _a_(582083, _n_(582082, "X_train_lemma", lambda: X_train_lemma), "shape")))
_l_(582086)

vect = _c_(582091, _a_(582089, _c_(582088, _n_(582087, "CountVectorizer", lambda: CountVectorizer), min_df=5), "fit"), _n_(582090, "text_train", lambda: text_train))
_l_(582092)
X_train = _c_(582096, _a_(582094, _n_(582093, "vect", lambda: vect), "transform"), _n_(582095, "text_train", lambda: text_train))
_l_(582097)
_c_(582103, _n_(582098, "print", lambda: print), _c_(582102, _a_(582099, "X_train.shape: {}", "format"), _a_(582101, _n_(582100, "X_train", lambda: X_train), "shape")))
_l_(582104)