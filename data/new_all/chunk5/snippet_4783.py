# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65702394/i-keep-getting-this-error-typeerror-lemmatize-missing-1-required-positional
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lemmatizer = _n_(658969, "WordNetLemmatizer", lambda: WordNetLemmatizer)
_l_(658970)

intents = _c_(658977, _a_(658972, _n_(658971, "json", lambda: json), "loads"), _c_(658976, _a_(658975, _c_(658974, _n_(658973, "open", lambda: open), 'intents.json'), "read")))
_l_(658978)

words = []
_l_(658979)
classes = []
_l_(658980)
documents = []
_l_(658981)
ignore_letters = ['?', '!', '.', ',']
_l_(658982)

for intent in _n_(658983, "intents", lambda: intents)['intents']:
    _l_(659010)

    for pattern in _n_(658984, "intent", lambda: intent)['patterns']:
        _l_(659009)

        word_list = _c_(658988, _a_(658986, _n_(658985, "nltk", lambda: nltk), "word_tokenize"), _n_(658987, "pattern", lambda: pattern))
        _l_(658989)
        _c_(658993, _a_(658991, _n_(658990, "words", lambda: words), "extend"), _n_(658992, "word_list", lambda: word_list))
        _l_(658994)
        _c_(658999, _a_(658996, _n_(658995, "documents", lambda: documents), "append"), (_n_(658997, "word_list", lambda: word_list), _n_(658998, "intent", lambda: intent)['tag']))
        _l_(659000)
        if _n_(659001, "intent", lambda: intent)['tag'] not in _n_(659002, "classes", lambda: classes):
            _l_(659008)

            _c_(659006, _a_(659004, _n_(659003, "classes", lambda: classes), "append"), _n_(659005, "intent", lambda: intent)['tag'])
            _l_(659007)

words = [_c_(659014, _a_(659012, _n_(659011, "lemmatizer", lambda: lemmatizer), "lemmatize"), _n_(659013, "word", lambda: word)) for word in _n_(659015, "words", lambda: words) if _n_(659016, "word", lambda: word) not in _n_(659017, "ignore_letters", lambda: ignore_letters)]
_l_(659018)
words = _c_(659023, _n_(659019, "sorted", lambda: sorted), _c_(659022, _n_(659020, "set", lambda: set), _n_(659021, "words", lambda: words)))
_l_(659024)