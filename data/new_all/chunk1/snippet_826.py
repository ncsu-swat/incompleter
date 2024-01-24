# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70646480/iterating-through-directory-error-filenotfounderror-errno-2-no-such-file-or
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(399601)

except ImportError:
    pass
try:
    import sys
    _l_(399603)

except ImportError:
    pass
try:
    import nltk
    _l_(399605)

except ImportError:
    pass
_c_(399608, _a_(399607, _n_(399606, "nltk", lambda: nltk), "download"))
_l_(399609)
try:
    from nltk import word_tokenize
    _l_(399611)

except ImportError:
    pass
try:
    from nltk.corpus import stopwords
    _l_(399613)

except ImportError:
    pass
try:
    from nltk.stem import WordNetLemmatizer
    _l_(399615)

except ImportError:
    pass
try:
    import io
    _l_(399617)

except ImportError:
    pass

files_path = _a_(399619, _n_(399618, "sys", lambda: sys), "argv")[1]
_l_(399620)
textfile_dictionary = _a_(399622, _n_(399621, "sys", lambda: sys), "argv")[2]
_l_(399623)

for filename in _c_(399627, _a_(399625, _n_(399624, "os", lambda: os), "listdir"), _n_(399626, "files_path", lambda: files_path)):
    _l_(399714)

    if _c_(399630, _a_(399629, _n_(399628, "filename", lambda: filename), "endswith"), ".txt"):
        _l_(399713)


        #accessing file for processing
        file = _c_(399633, _n_(399631, "open", lambda: open), _n_(399632, "filename", lambda: filename), "rt")
        _l_(399634)
        text = _c_(399637, _a_(399636, _n_(399635, "file", lambda: file), "read"))
        _l_(399638)

        #tokenize text file
        tokens = _c_(399641, _n_(399639, "word_tokenize", lambda: word_tokenize), _n_(399640, "text", lambda: text))
        _l_(399642)

        #remove non-alphabetical characters
        words = []
        _l_(399643)

        for word in _n_(399644, "tokens", lambda: tokens):
            _l_(399654)

            if _c_(399647, _a_(399646, _n_(399645, "word", lambda: word), "isalpha")):
                _l_(399653)

                _c_(399651, _a_(399649, _n_(399648, "words", lambda: words), "append"), _n_(399650, "word", lambda: word))
                _l_(399652)

        #remove stopwords
        stop_words = _c_(399657, _a_(399656, _n_(399655, "stopwords", lambda: stopwords), "words"), "english")
        _l_(399658)
        words_without_stops = []
        _l_(399659)

        for w in _n_(399660, "words", lambda: words):
            _l_(399669)

            if not _n_(399661, "w", lambda: w) in _n_(399662, "stop_words", lambda: stop_words):
                _l_(399668)

                _c_(399666, _a_(399664, _n_(399663, "words_without_stops", lambda: words_without_stops), "append"), _n_(399665, "w", lambda: w))
                _l_(399667)

        #lemmatize remaining tokens and print
        lemmatizer = _c_(399671, _n_(399670, "WordNetLemmatizer", lambda: WordNetLemmatizer))
        _l_(399672)
        lemmas = []
        _l_(399673)
        for x in _n_(399674, "words_without_stops", lambda: words_without_stops):
            _l_(399685)

            _c_(399678, _a_(399676, _n_(399675, "lemmatizer", lambda: lemmatizer), "lemmatize"), _n_(399677, "x", lambda: x))
            _l_(399679)
            _c_(399683, _a_(399681, _n_(399680, "lemmas", lambda: lemmas), "append"), _n_(399682, "x", lambda: x))
            _l_(399684)

        #turn dictionary held in text file into a list of tokens
        file = _c_(399689, _a_(399687, _n_(399686, "io", lambda: io), "open"), _n_(399688, "textfile_dictionary", lambda: textfile_dictionary), mode="r", encoding="utf8")
        _l_(399690)
        dictionaryread = _c_(399693, _a_(399692, _n_(399691, "file", lambda: file), "read"))
        _l_(399694)
        dictionary = _c_(399697, _a_(399696, _n_(399695, "dictionaryread", lambda: dictionaryread), "split"))
        _l_(399698)

        #count instances of each word in dictionary in the novel and add them up
        word_count = 0
        _l_(399699)

        for element in _n_(399700, "dictionary", lambda: dictionary):
            _l_(399708)

            for lemma in _n_(399701, "lemmas", lambda: lemmas):
                _l_(399707)

                if _n_(399702, "lemma", lambda: lemma) == _n_(399703, "element", lambda: element):
                    _l_(399706)

                    word_count = _n_(399704, "word_count", lambda: word_count) + 1
                    _l_(399705)

        _c_(399711, _n_(399709, "print", lambda: print), _n_(399710, "word_count", lambda: word_count))
        _l_(399712)