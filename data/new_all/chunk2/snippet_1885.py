# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43403426/training-doc2vec-on-20newsgroups-dataset-getting-exception-attributeerror-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(425339, _a_(425332, _n_(425331, "model", lambda: model), "train"), _n_(425333, "train_docs", lambda: train_docs), total_examples = _c_(425336, _n_(425334, "len", lambda: len), _n_(425335, "train_docs", lambda: train_docs)), epochs = _a_(425338, _n_(425337, "model", lambda: model), "iter"))
_l_(425340)
_n_(425341, "model", lambda: model).train_words = False
_l_(425342)
_n_(425343, "model", lambda: model).train_labels = True
_l_(425344)
_c_(425353, _a_(425346, _n_(425345, "model", lambda: model), "train"), _n_(425347, "test_docs", lambda: test_docs), total_examples = _c_(425350, _n_(425348, "len", lambda: len), _n_(425349, "test_docs", lambda: test_docs)), epochs = _a_(425352, _n_(425351, "model", lambda: model), "iter"))
_l_(425354)

_c_(425358, _a_(425356, _n_(425355, "model", lambda: model), "save"), _n_(425357, "output", lambda: output))
_l_(425359)