# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48917449/typeerror-a-bytes-like-object-is-required-not-str-when-converting-gensim-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(619354, _n_(619352, "open", lambda: open), _n_(619353, "outfiletsv", lambda: outfiletsv), 'w+b') as file_vector:
    _l_(619388)

    with _c_(619357, _n_(619355, "open", lambda: open), _n_(619356, "outfiletsvmeta", lambda: outfiletsvmeta), 'w+b') as file_metadata:
        _l_(619387)

        for word in _a_(619359, _n_(619358, "model", lambda: model), "index2word"):
            _l_(619386)

            _c_(619371, _a_(619361, _n_(619360, "file_metadata", lambda: file_metadata), "write"), _c_(619366, _a_(619364, _a_(619363, _n_(619362, "gensim", lambda: gensim), "utils"), "to_utf8"), _n_(619365, "word", lambda: word)) + _c_(619370, _a_(619369, _a_(619368, _n_(619367, "gensim", lambda: gensim), "utils"), "to_utf8"), '\n'))
            _l_(619372)
            vector_row = _c_(619379, _a_(619373, '\t', "join"), (_c_(619376, _n_(619374, "str", lambda: str), _n_(619375, "x", lambda: x)) for x in _n_(619377, "model", lambda: model)[_n_(619378, "word", lambda: word)]))
            _l_(619380)
            _c_(619384, _a_(619382, _n_(619381, "file_vector", lambda: file_vector), "write"), _n_(619383, "vector_row", lambda: vector_row) + '\n')
            _l_(619385)