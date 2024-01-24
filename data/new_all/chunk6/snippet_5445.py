# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49926774/gensim-word2vec-model-wv-index2word-typeerror-slice-indices-must-be-integers-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(369186, _n_(369185, "open", lambda: open), "metadata.tsv", "w+") as file_metadata:
    _l_(369205)

    for i,word in _c_(369192, _n_(369187, "enumerate", lambda: enumerate), _a_(369190, _a_(369189, _n_(369188, "model", lambda: model), "wv"), "index2word")[:_n_(369191, "max", lambda: max)]):
        _l_(369204)

        _n_(369193, "w2v", lambda: w2v)[_n_(369194, "i", lambda: i)] = _a_(369196, _n_(369195, "model", lambda: model), "wv")[_n_(369197, "word", lambda: word)]
        _l_(369198)
        _c_(369202, _a_(369200, _n_(369199, "file_metadata", lambda: file_metadata), "write"), _n_(369201, "word", lambda: word) + "\n")
        _l_(369203)