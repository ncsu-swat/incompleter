# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33773157/word-tokenize-typeerror-expected-string-or-buffer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from nltk.corpus import stopwords
    _l_(413173)

except ImportError:
    pass
try:
    from nltk.tokenize import word_tokenize
    _l_(413175)

except ImportError:
    pass

with _c_(413177, _n_(413176, "open", lambda: open), 'E:\\Book\\1500.txt', "r", encoding='ISO-8859-1') as File_1500:
    _l_(413197)

    stop_words = _c_(413182, _n_(413178, "set", lambda: set), _c_(413181, _a_(413180, _n_(413179, "stopwords", lambda: stopwords), "words"), "english"))
    _l_(413183)
    words = _c_(413186, _n_(413184, "word_tokenize", lambda: word_tokenize), _n_(413185, "File_1500", lambda: File_1500))
    _l_(413187)
    filtered_sentence = [_n_(413188, "w", lambda: w) for w in _n_(413189, "words", lambda: words) if not _n_(413190, "w", lambda: w) in _n_(413191, "stop_words", lambda: stop_words)]
    _l_(413192)
    _c_(413195, _n_(413193, "print", lambda: print), _n_(413194, "filtered_sentence", lambda: filtered_sentence))
    _l_(413196)