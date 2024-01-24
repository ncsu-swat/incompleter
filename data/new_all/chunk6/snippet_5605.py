# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65702394/i-keep-getting-this-error-typeerror-lemmatize-missing-1-required-positional
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lemmatizer = _n_(342114, "WordNetLemmatizer", lambda: WordNetLemmatizer)
_l_(342115)

intents = _c_(342122, _a_(342117, _n_(342116, "json", lambda: json), "loads"), _c_(342121, _a_(342120, _c_(342119, _n_(342118, "open", lambda: open), 'intents.json'), "read")))
_l_(342123)

words = []
_l_(342124)
classes = []
_l_(342125)
documents = []
_l_(342126)
ignore_letters = ['?', '!', '.', ',']
_l_(342127)

for intent in _n_(342128, "intents", lambda: intents)['intents']:
    _l_(342155)

    for pattern in _n_(342129, "intent", lambda: intent)['patterns']:
        _l_(342154)

        word_list = _c_(342133, _a_(342131, _n_(342130, "nltk", lambda: nltk), "word_tokenize"), _n_(342132, "pattern", lambda: pattern))
        _l_(342134)
        _c_(342138, _a_(342136, _n_(342135, "words", lambda: words), "extend"), _n_(342137, "word_list", lambda: word_list))
        _l_(342139)
        _c_(342144, _a_(342141, _n_(342140, "documents", lambda: documents), "append"), (_n_(342142, "word_list", lambda: word_list), _n_(342143, "intent", lambda: intent)['tag']))
        _l_(342145)
        if _n_(342146, "intent", lambda: intent)['tag'] not in _n_(342147, "classes", lambda: classes):
            _l_(342153)

            _c_(342151, _a_(342149, _n_(342148, "classes", lambda: classes), "append"), _n_(342150, "intent", lambda: intent)['tag'])
            _l_(342152)

words = [_c_(342159, _a_(342157, _n_(342156, "lemmatizer", lambda: lemmatizer), "lemmatize"), _n_(342158, "word", lambda: word)) for word in _n_(342160, "words", lambda: words) if _n_(342161, "word", lambda: word) not in _n_(342162, "ignore_letters", lambda: ignore_letters)]
_l_(342163)
words = _c_(342168, _n_(342164, "sorted", lambda: sorted), _c_(342167, _n_(342165, "set", lambda: set), _n_(342166, "words", lambda: words)))
_l_(342169)