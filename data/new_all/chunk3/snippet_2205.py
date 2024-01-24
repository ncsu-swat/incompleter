# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58161798/attributeerror-float-object-has-no-attribute-split-while-running-larger-dat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def build_vocab(sentences, verbose=True):
    _l_(570880)


    vocab = {}
    _l_(570862)

    for sentence in _c_(570865, _n_(570863, "tqdm", lambda: tqdm), _n_(570864, "sentences", lambda: sentences)):
        _l_(570877)

        for word in _n_(570866, "sentence", lambda: sentence):
            _l_(570876)

            try:
                _l_(570875)

                _n_(570867, "vocab", lambda: vocab)[_n_(570868, "word", lambda: word)] += 1
                _l_(570869)
            except _n_(570870, "KeyError", lambda: KeyError):
                _l_(570874)

                _n_(570871, "vocab", lambda: vocab)[_n_(570872, "word", lambda: word)] = 1
                _l_(570873)
    aux = _n_(570878, "vocab", lambda: vocab)    
    _l_(570879)    

    return aux    
sentences = _a_(570887, _c_(570886, _a_(570882, _n_(570881, "train_df", lambda: train_df)["question_text"], "progress_apply"), lambda x: _c_(570885, _a_(570884, _n_(570883, "x", lambda: x), "split"))), "values")
_l_(570888)
vocab = _c_(570891, _n_(570889, "build_vocab", lambda: build_vocab), _n_(570890, "sentences", lambda: sentences))
_l_(570892)