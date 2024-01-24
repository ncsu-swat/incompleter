# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65702394/i-keep-getting-this-error-typeerror-lemmatize-missing-1-required-positional
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lemmatizer = _n_(344511, "WordNetLemmatizer", lambda: WordNetLemmatizer)
_l_(344512)

intents = _c_(344519, _a_(344514, _n_(344513, "json", lambda: json), "loads"), _c_(344518, _a_(344517, _c_(344516, _n_(344515, "open", lambda: open), 'intents.json'), "read")))
_l_(344520)

words = []
_l_(344521)
classes = []
_l_(344522)
documents = []
_l_(344523)
ignore_letters = ['?', '!', '.', ',']
_l_(344524)

for intent in _n_(344525, "intents", lambda: intents)['intents']:
    _l_(344552)

    for pattern in _n_(344526, "intent", lambda: intent)['patterns']:
        _l_(344551)

        word_list = _c_(344530, _a_(344528, _n_(344527, "nltk", lambda: nltk), "word_tokenize"), _n_(344529, "pattern", lambda: pattern))
        _l_(344531)
        _c_(344535, _a_(344533, _n_(344532, "words", lambda: words), "extend"), _n_(344534, "word_list", lambda: word_list))
        _l_(344536)
        _c_(344541, _a_(344538, _n_(344537, "documents", lambda: documents), "append"), (_n_(344539, "word_list", lambda: word_list), _n_(344540, "intent", lambda: intent)['tag']))
        _l_(344542)
        if _n_(344543, "intent", lambda: intent)['tag'] not in _n_(344544, "classes", lambda: classes):
            _l_(344550)

            _c_(344548, _a_(344546, _n_(344545, "classes", lambda: classes), "append"), _n_(344547, "intent", lambda: intent)['tag'])
            _l_(344549)

words = [_c_(344556, _a_(344554, _n_(344553, "lemmatizer", lambda: lemmatizer), "lemmatize"), _n_(344555, "word", lambda: word)) for word in _n_(344557, "words", lambda: words) if _n_(344558, "word", lambda: word) not in _n_(344559, "ignore_letters", lambda: ignore_letters)]
_l_(344560)
words = _c_(344565, _n_(344561, "sorted", lambda: sorted), _c_(344564, _n_(344562, "set", lambda: set), _n_(344563, "words", lambda: words)))
_l_(344566)