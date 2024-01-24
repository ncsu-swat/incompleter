# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65324684/typeerror-lemmatize-missing-3-required-positional-arguments-index-except
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _c_(549496, _a_(549495, _n_(549494, "pd", lambda: pd), "read_csv"), 'file.csv', sep=';')
_l_(549497)
try:
    from nltk.corpus import stopwords
    _l_(549499)

except ImportError:
    pass
try:
    import re
    _l_(549501)

except ImportError:
    pass
try:
    from nltk.tokenize import RegexpTokenizer
    _l_(549503)

except ImportError:
    pass
try:
    from spacy.lang.fr import French
    _l_(549505)

except ImportError:
    pass


stop_words = _c_(549510, _n_(549506, "set", lambda: set), _c_(549509, _a_(549508, _n_(549507, "stopwords", lambda: stopwords), "words"), 'french'))
_l_(549511)
tokenizer = _c_(549515, _a_(549514, _a_(549513, _n_(549512, "nltk", lambda: nltk), "tokenize"), "RegexpTokenizer"), r'\w+')
_l_(549516)
lemmatizer = _c_(549520, _a_(549519, _a_(549518, _n_(549517, "French", lambda: French), "Defaults"), "create_lemmatizer"))
_l_(549521)


def clean_text(text):
    _l_(549552)

    text = _c_(549524, _a_(549523, _n_(549522, "text", lambda: text), "lower"))  
    _l_(549525)  
    text = _c_(549529, _a_(549527, _n_(549526, "tokenizer", lambda: tokenizer), "tokenize"), _n_(549528, "text", lambda: text))
    _l_(549530)
    text = [_n_(549531, "word", lambda: word) for word in _n_(549532, "text", lambda: text) if not _n_(549533, "word", lambda: word) in _n_(549534, "stop_words", lambda: stop_words)]
    _l_(549535)
    text = [_c_(549539, _a_(549537, _n_(549536, "lemmatizer", lambda: lemmatizer), "lemmatize"), _n_(549538, "word", lambda: word)) for word in _n_(549540, "text", lambda: text)]
    _l_(549541)
    final_text = _c_(549548, _a_(549542, ' ', "join"), [_n_(549543, "w", lambda: w) for w in _n_(549544, "text", lambda: text) if _c_(549547, _n_(549545, "len", lambda: len), _n_(549546, "w", lambda: w))>2] ) 
    _l_(549549) 
    aux = _n_(549550, "final_text", lambda: final_text)
    _l_(549551)
    return aux

_n_(549553, "df", lambda: df)['comms_clean'] = _c_(549559, _a_(549555, _n_(549554, "df", lambda: df)['comms'], "apply"), lambda x : _c_(549558, _n_(549556, "clean_text", lambda: clean_text), _n_(549557, "x", lambda: x)))
_l_(549560)