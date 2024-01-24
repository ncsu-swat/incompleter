# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76749399/how-to-solve-an-attribute-error-when-lemmatizing-a-list-lower
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(598804)

except ImportError:
    pass
try:
    import json
    _l_(598806)

except ImportError:
    pass
try:
    import pickle
    _l_(598808)

except ImportError:
    pass
try:
    import numpy as np
    _l_(598810)

except ImportError:
    pass
try:
    import nltk
    _l_(598812)

except ImportError:
    pass
try:
    from nltk.stem import WordNetLemmatizer
    _l_(598814)

except ImportError:
    pass
try:
    from tensorflow import keras
    _l_(598816)

except ImportError:
    pass
try:
    from keras.layers import Dense, Activation, Dropout
    _l_(598818)

except ImportError:
    pass
try:
    from keras.models import Sequential
    _l_(598820)

except ImportError:
    pass
try:
    from keras.optimizers import SGD
    _l_(598822)

except ImportError:
    pass


lemmatizer = _c_(598824, _n_(598823, "WordNetLemmatizer", lambda: WordNetLemmatizer))
_l_(598825)

intents = _c_(598832, _a_(598827, _n_(598826, "json", lambda: json), "loads"), _c_(598831, _a_(598830, _c_(598829, _n_(598828, "open", lambda: open), 'intents.json'), "read")))
_l_(598833)

words= []
_l_(598834)
classes = []
_l_(598835)
documents = []
_l_(598836)
ignore_letters = ['?', '!', '.', ',']
_l_(598837)

for intent in _n_(598838, "intents", lambda: intents)["intents"]:
    _l_(598865)

    for pattern in _n_(598839, "intent", lambda: intent)['patterns']:
        _l_(598864)

        word_list = _c_(598843, _a_(598841, _n_(598840, "nltk", lambda: nltk), "word_tokenize"), _n_(598842, "pattern", lambda: pattern))
        _l_(598844)
        _c_(598848, _a_(598846, _n_(598845, "words", lambda: words), "extend"), _n_(598847, "word_list", lambda: word_list))
        _l_(598849)
        _c_(598854, _a_(598851, _n_(598850, "documents", lambda: documents), "append"), (_n_(598852, "word_list", lambda: word_list), _n_(598853, "intent", lambda: intent)['tag']))
        _l_(598855)
        if _n_(598856, "intent", lambda: intent)['tag'] not in _n_(598857, "classes", lambda: classes):
            _l_(598863)

            _c_(598861, _a_(598859, _n_(598858, "classes", lambda: classes), "append"), _n_(598860, "intent", lambda: intent)['tag'])
            _l_(598862)

words = [_c_(598869, _a_(598867, _n_(598866, "lemmatizer", lambda: lemmatizer), "lemmatize"), _n_(598868, "word", lambda: word)) for word in _n_(598870, "words", lambda: words) if _n_(598871, "word", lambda: word) not in _n_(598872, "ignore_letters", lambda: ignore_letters)]
_l_(598873)
words = _c_(598878, _n_(598874, "sorted", lambda: sorted), _c_(598877, _n_(598875, "set", lambda: set), _n_(598876, "words", lambda: words)))
_l_(598879)


classes = _c_(598884, _n_(598880, "sorted", lambda: sorted), _c_(598883, _n_(598881, "set", lambda: set), _n_(598882, "classes", lambda: classes)))
_l_(598885)


_c_(598891, _a_(598887, _n_(598886, "pickle", lambda: pickle), "dump"), _n_(598888, "words", lambda: words), _c_(598890, _n_(598889, "open", lambda: open), 'words.pkl', 'wb'))
_l_(598892)
_c_(598898, _a_(598894, _n_(598893, "pickle", lambda: pickle), "dump"), _n_(598895, "words", lambda: words), _c_(598897, _n_(598896, "open", lambda: open), 'classes.pkl', 'wb'))
_l_(598899)


training=[]
_l_(598900)
output_empty = [0] * _c_(598903, _n_(598901, "len", lambda: len), _n_(598902, "classes", lambda: classes))
_l_(598904)

for document in _n_(598905, "documents", lambda: documents):
    _l_(598944)

    bag = []
    _l_(598906)
    word_patterns = _n_(598907, "documents", lambda: documents)[0]
    _l_(598908)
    word_patterns = [_c_(598914, _a_(598910, _n_(598909, "lemmatizer", lambda: lemmatizer), "lemmatize"), _c_(598913, _a_(598912, _n_(598911, "word", lambda: word), "lower"))) for word in _n_(598915, "word_patterns", lambda: word_patterns)]
    _l_(598916)
    for word in _n_(598917, "words", lambda: words):
        _l_(598927)

        _c_(598920, _a_(598919, _n_(598918, "bag", lambda: bag), "append"), 1) if _n_(598921, "word", lambda: word) in _n_(598922, "word_patterns", lambda: word_patterns) else _c_(598925, _a_(598924, _n_(598923, "bag", lambda: bag), "append"), 0)
        _l_(598926)
    

    output_row = _c_(598930, _n_(598928, "list", lambda: list), _n_(598929, "output_empty", lambda: output_empty) )
    _l_(598931)
    _n_(598932, "output_row", lambda: output_row)[_c_(598936, _a_(598934, _n_(598933, "classes", lambda: classes), "index"), _n_(598935, "document", lambda: document)[1])] = 1
    _l_(598937)
    _c_(598942, _a_(598939, _n_(598938, "training", lambda: training), "append"), _n_(598940, "bag", lambda: bag), _n_(598941, "output_row", lambda: output_row))
    _l_(598943)

_c_(598948, _a_(598946, _n_(598945, "random", lambda: random), "shuffle"), _n_(598947, "training", lambda: training))
_l_(598949)
training = _c_(598953, _a_(598951, _n_(598950, "np", lambda: np), "array"), _n_(598952, "training", lambda: training))
_l_(598954)

train_x = _c_(598957, _n_(598955, "list", lambda: list), _n_(598956, "training", lambda: training)[:,0])
_l_(598958)
train_y = _c_(598961, _n_(598959, "list", lambda: list), _n_(598960, "training", lambda: training)[:,1]) 
_l_(598962) 

#neural network


model = _c_(598964, _n_(598963, "Sequential", lambda: Sequential))
_l_(598965)
_c_(598973, _a_(598967, _n_(598966, "model", lambda: model), "add"), _c_(598972, _n_(598968, "Dense", lambda: Dense), 128,input_shape = (_c_(598971, _n_(598969, "len", lambda: len), _n_(598970, "train_x", lambda: train_x)[0]),),activation='relu'))
_l_(598974)
_c_(598979, _a_(598976, _n_(598975, "model", lambda: model), "add"), _c_(598978, _n_(598977, "Dropout", lambda: Dropout), 0.5))
_l_(598980)
_c_(598985, _a_(598982, _n_(598981, "model", lambda: model), "add"), _c_(598984, _n_(598983, "Dense", lambda: Dense), 64, activation='relu'))
_l_(598986)
_c_(598991, _a_(598988, _n_(598987, "model", lambda: model), "add"), _c_(598990, _n_(598989, "Dropout", lambda: Dropout), 0.5))
_l_(598992)
_c_(599000, _a_(598994, _n_(598993, "model", lambda: model), "add"), _c_(598999, _n_(598995, "Dense", lambda: Dense), _c_(598998, _n_(598996, "len", lambda: len), _n_(598997, "train_y", lambda: train_y)[0]), activation='softmax'))
_l_(599001)

sgd = _c_(599003, _n_(599002, "SGD", lambda: SGD), lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
_l_(599004)
_c_(599008, _a_(599006, _n_(599005, "model", lambda: model), "compile"), loss='categorical_crossentropy', optimizer=_n_(599007, "sgd", lambda: sgd), metrics=['accuracy'])
_l_(599009)

_c_(599020, _a_(599011, _n_(599010, "model", lambda: model), "fit"), _c_(599015, _a_(599013, _n_(599012, "np", lambda: np), "array"), _n_(599014, "train_x", lambda: train_x)), _c_(599019, _a_(599017, _n_(599016, "np", lambda: np), "array"), _n_(599018, "train_y", lambda: train_y)), epochs=200, batch_size=5, verbose=1)
_l_(599021)
_c_(599024, _a_(599023, _n_(599022, "model", lambda: model), "save"), 'chatbot_model.model')
_l_(599025)

_c_(599027, _n_(599026, "print", lambda: print), "done")
_l_(599028)