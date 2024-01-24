# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53692117/attributeerror-list-object-has-no-attribute-isdigit-specifying-pos-of-each
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, nltk, re
    _l_(435181)

except ImportError:
    pass
try:
    from nltk.corpus import stopwords
    _l_(435183)

except ImportError:
    pass
try:
    from unidecode import unidecode
    _l_(435185)

except ImportError:
    pass
try:
    from nltk.tokenize import word_tokenize, sent_tokenize
    _l_(435187)

except ImportError:
    pass
try:
    from nltk.tag import pos_tag
    _l_(435189)

except ImportError:
    pass


def read_data():
    _l_(435205)

    global tokenized_raw_data
    _l_(435190)
    with _c_(435192, _n_(435191, "open", lambda: open), "path//merge_text_results_pu.txt", 'r', encoding='utf-8', errors = 'replace') as f:
        _l_(435204)

        raw_data = _c_(435195, _a_(435194, _n_(435193, "f", lambda: f), "read"))
        _l_(435196)
        tokenized_raw_data = _c_(435202, _a_(435197, '\n', "join"), _c_(435201, _a_(435199, _n_(435198, "nltk", lambda: nltk), "line_tokenize"), _n_(435200, "raw_data", lambda: raw_data)))
        _l_(435203)
_c_(435207, _n_(435206, "read_data", lambda: read_data))
_l_(435208)

def function1():
    _l_(435256)

    tokens_sentences = _c_(435213, _n_(435209, "sent_tokenize", lambda: sent_tokenize), _c_(435212, _a_(435211, _n_(435210, "tokenized_raw_data", lambda: tokenized_raw_data), "lower")))
    _l_(435214)
    unfiltered_tokens = [[_n_(435215, "word", lambda: word) for word in _c_(435218, _n_(435216, "word_tokenize", lambda: word_tokenize), _n_(435217, "word", lambda: word))] for word in _n_(435219, "tokens_sentences", lambda: tokens_sentences)]
    _l_(435220)
    tagged_tokens = _c_(435224, _a_(435222, _n_(435221, "nltk", lambda: nltk), "pos_tag"), _n_(435223, "unfiltered_tokens", lambda: unfiltered_tokens))
    _l_(435225)
    nouns = [_c_(435228, _a_(435227, _n_(435226, "word", lambda: word), "encode"), 'utf-8') for word,pos in _n_(435229, "tagged_tokens", lambda: tagged_tokens)
            if (_n_(435230, "pos", lambda: pos) == 'NN' or _n_(435231, "pos", lambda: pos) == 'NNP' or _n_(435232, "pos", lambda: pos) == 'NNS' or _n_(435233, "pos", lambda: pos) ==  'NNPS')]
    _l_(435234)
    joined_nouns_text = _c_(435243, _a_(435242, _c_(435241, _a_(435235, ' ', "join"), _c_(435240, _n_(435236, "map", lambda: map), _a_(435238, _n_(435237, "bytes", lambda: bytes), "decode"), _n_(435239, "nouns", lambda: nouns))), "strip"))
    _l_(435244)
    noun_tokens = [_n_(435245, "t", lambda: t) for t in _c_(435248, _n_(435246, "wordpunct_tokenize", lambda: wordpunct_tokenize), _n_(435247, "joined_nouns_text", lambda: joined_nouns_text))]
    _l_(435249)
    stop_words = _c_(435254, _n_(435250, "set", lambda: set), _c_(435253, _a_(435252, _n_(435251, "stopwords", lambda: stopwords), "words"), "english"))
    _l_(435255)
_c_(435258, _n_(435257, "function1", lambda: function1))
_l_(435259)