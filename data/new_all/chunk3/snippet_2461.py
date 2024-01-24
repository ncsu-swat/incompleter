# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67366751/typeerror-init-missing-2-required-positional-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(562616)

except ImportError:
    pass
try:
    from tqdm import tqdm
    _l_(562618)

except ImportError:
    pass
try:
    from utils import SOS, EOS, UNK, process
    _l_(562620)

except ImportError:
    pass


class Corpus(_n_(562621, "object", lambda: object)):
    _l_(562752)

    def __init__(self, path, path2, path3, order, lower=False, max_lines=-1):
        _l_(562665)

        _n_(562622, "self", lambda: self).order = _n_(562623, "order", lambda: order)
        _l_(562624)
        _n_(562625, "self", lambda: self).lower = _n_(562626, "lower", lambda: lower)
        _l_(562627)
        _n_(562628, "self", lambda: self).max_lines = _n_(562629, "max_lines", lambda: max_lines)
        _l_(562630)
        _n_(562631, "self", lambda: self).vocab = _c_(562633, _n_(562632, "set", lambda: set))
        _l_(562634)
        _n_(562635, "self", lambda: self).train = _c_(562643, _a_(562637, _n_(562636, "self", lambda: self), "tokenize"), _c_(562642, _a_(562640, _a_(562639, _n_(562638, "os", lambda: os), "path"), "join"), _n_(562641, "path", lambda: path)), training_set=True)
        _l_(562644)
        _n_(562645, "self", lambda: self).valid = _c_(562653, _a_(562647, _n_(562646, "self", lambda: self), "tokenize"), _c_(562652, _a_(562650, _a_(562649, _n_(562648, "os", lambda: os), "path"), "join"), _n_(562651, "path2", lambda: path2)))
        _l_(562654)
        _n_(562655, "self", lambda: self).test = _c_(562663, _a_(562657, _n_(562656, "self", lambda: self), "tokenize"), _c_(562662, _a_(562660, _a_(562659, _n_(562658, "os", lambda: os), "path"), "join"), _n_(562661, "path3", lambda: path3)))
        _l_(562664)

    def tokenize(self, path, training_set=False):
        _l_(562751)

        """Tokenizes a text file."""
        #assert os.path.exists(path)
        with _c_(562670, _n_(562666, "open", lambda: open), _n_(562667, "path", lambda: path), _n_(562668, "path2", lambda: path2), _n_(562669, "path3", lambda: path3)) as fin:
            _l_(562677)

            num_lines = _c_(562675, _n_(562671, "sum", lambda: sum), (1 for _ in _c_(562674, _a_(562673, _n_(562672, "fin", lambda: fin), "readlines"))))
            _l_(562676)
        with _c_(562682, _n_(562678, "open", lambda: open), _n_(562679, "path", lambda: path), _n_(562680, "path2", lambda: path2), _n_(562681, "path3", lambda: path3), 'r', encoding="utf8") as f:
            _l_(562748)

            words = []
            _l_(562683)
            for i, line in _c_(562689, _n_(562684, "enumerate", lambda: enumerate), _c_(562688, _n_(562685, "tqdm", lambda: tqdm), _n_(562686, "f", lambda: f), total=_n_(562687, "num_lines", lambda: num_lines))):
                _l_(562747)

                if _a_(562691, _n_(562690, "self", lambda: self), "max_lines") > 0 and _n_(562692, "i", lambda: i) > _a_(562694, _n_(562693, "self", lambda: self), "max_lines"):
                    _l_(562696)

                    break
                    _l_(562695)
                line = _c_(562699, _a_(562698, _n_(562697, "line", lambda: line), "strip"))
                _l_(562700)
                if not _n_(562701, "line", lambda: line):
                    _l_(562746)

                    continue  # Skip empty lines.
                    _l_(562702)  # Skip empty lines.
                elif _c_(562705, _a_(562704, _n_(562703, "line", lambda: line), "startswith"), '='):
                    _l_(562745)

                    continue  # Skip headers.
                    _l_(562706)  # Skip headers.
                else:
                    sentence = (_a_(562708, _n_(562707, "self", lambda: self), "order") - 1) * [_n_(562709, "SOS", lambda: SOS)] + \
                        [_c_(562714, _n_(562710, "process", lambda: process), _n_(562711, "word", lambda: word), _a_(562713, _n_(562712, "self", lambda: self), "lower")) for word in _c_(562717, _a_(562716, _n_(562715, "line", lambda: line), "split"))] + [_n_(562718, "EOS", lambda: EOS)]
                    _l_(562719)
                    if _n_(562720, "training_set", lambda: training_set):
                        _l_(562744)

                        _c_(562724, _a_(562722, _n_(562721, "words", lambda: words), "extend"), _n_(562723, "sentence", lambda: sentence))
                        _l_(562725)
                        _c_(562730, _a_(562728, _a_(562727, _n_(562726, "self", lambda: self), "vocab"), "update"), _n_(562729, "sentence", lambda: sentence))
                        _l_(562731)
                    else:
                        sentence = [_n_(562732, "word", lambda: word) if _n_(562733, "word", lambda: word) in _a_(562735, _n_(562734, "self", lambda: self), "vocab") else _n_(562736, "UNK", lambda: UNK) for word in _n_(562737, "sentence", lambda: sentence)]
                        _l_(562738)
                        _c_(562742, _a_(562740, _n_(562739, "words", lambda: words), "extend"), _n_(562741, "sentence", lambda: sentence))
                        _l_(562743)
        aux = _n_(562749, "words", lambda: words)
        _l_(562750)
        return aux


if _n_(562753, "__name__", lambda: __name__) == '__main__':
    _l_(562773)

    path = 'C://Users//supre//Documents//Python Programme//kenlm//wikitext-2//wiki.train.tokens'
    _l_(562754)
    path2 = 'C://Users//supre//Documents//Python Programme//kenlm//wikitext-2//wiki.valid.tokens'
    _l_(562755)
    path3 = 'C://Users//supre//Documents//Python Programme//kenlm//wikitext-2//wiki.test.tokens'
    _l_(562756)
    corpus = _c_(562759, _n_(562757, "Corpus", lambda: Corpus), _n_(562758, "path", lambda: path), order=3)
    _l_(562760)
    _c_(562766, _n_(562761, "print", lambda: print), _c_(562765, _n_(562762, "len", lambda: len), _a_(562764, _n_(562763, "corpus", lambda: corpus), "test")))
    _l_(562767)
    _c_(562771, _n_(562768, "print", lambda: print), _a_(562770, _n_(562769, "corpus", lambda: corpus), "test")[:100])
    _l_(562772)