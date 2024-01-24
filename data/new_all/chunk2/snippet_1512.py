# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47941740/file-not-found-error-even-though-file-was-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for root, dirs, files in _c_(426384, _a_(426382, _n_(426381, "os", lambda: os), "walk"), _n_(426383, "corpus_name", lambda: corpus_name)):
    _l_(426414)

    for file in _n_(426385, "files", lambda: files):
        _l_(426409)

        if _c_(426388, _a_(426387, _n_(426386, "file", lambda: file), "endswith"), ".v4_gold_conll"):
            _l_(426408)

            f= _c_(426391, _n_(426389, "open", lambda: open), _n_(426390, "file", lambda: file))
            _l_(426392)
            lines = _c_(426395, _a_(426394, _n_(426393, "f", lambda: f), "readlines"))
            _l_(426396)
            tokens = [_c_(426399, _a_(426398, _n_(426397, "line", lambda: line), "split"))[3] for line in _n_(426400, "lines", lambda: lines) if _c_(426403, _a_(426402, _n_(426401, "line", lambda: line), "strip")) 
and not _c_(426406, _a_(426405, _n_(426404, "line", lambda: line), "startswith"), "#")]
            _l_(426407)
    _c_(426412, _n_(426410, "print", lambda: print), _n_(426411, "tokens", lambda: tokens))
    _l_(426413)