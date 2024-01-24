# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52096549/when-using-tensor-flow-i-am-getting-error-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(646768)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(646770)

except ImportError:
    pass


# Input data files are available in the "../input/" directory.
# Any results you write to the current directory are saved as output.
#from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))


train = _c_(646773, _a_(646772, _n_(646771, "pd", lambda: pd), "read_csv"), 'C:/Users/gunjit.bedi/Desktop/Tensor Flow/input/train.csv')
_l_(646774)
_c_(646779, _n_(646775, "print", lambda: print), _c_(646778, _a_(646777, _n_(646776, "train", lambda: train), "head")))
_l_(646780)
try:
    import nltk as nl
    _l_(646782)

except ImportError:
    pass
_n_(646783, "train", lambda: train)['tokens'] = [_c_(646787, _a_(646785, _n_(646784, "nl", lambda: nl), "word_tokenize"), _n_(646786, "sentences", lambda: sentences)) for sentences in _a_(646789, _n_(646788, "train", lambda: train), "text")]
_l_(646790)
words = []
_l_(646791)
for item in _a_(646793, _n_(646792, "train", lambda: train), "tokens"):
    _l_(646799)

    _c_(646797, _a_(646795, _n_(646794, "words", lambda: words), "extend"), _n_(646796, "item", lambda: item))
    _l_(646798)

stemmer = _c_(646804, _a_(646803, _a_(646802, _a_(646801, _n_(646800, "nl", lambda: nl), "stem"), "lancaster"), "LancasterStemmer"))
_l_(646805)
words = [_c_(646809, _a_(646807, _n_(646806, "stemmer", lambda: stemmer), "stem"), _n_(646808, "word", lambda: word)) for word in _n_(646810, "words", lambda: words)]
_l_(646811)


filtered_words = [_n_(646812, "word", lambda: word) for word in _n_(646813, "words", lambda: words) if _n_(646814, "word", lambda: word) not in _c_(646819, _a_(646818, _a_(646817, _a_(646816, _n_(646815, "nl", lambda: nl), "corpus"), "stopwords"), "words"), 'english')]
_l_(646820)
try:
    import gensim
    _l_(646822)

except ImportError:
    pass
# let X be a list of tokenized texts (i.e. list of lists of tokens)
model = _c_(646827, _a_(646825, _a_(646824, _n_(646823, "gensim", lambda: gensim), "models"), "Word2Vec"), _n_(646826, "filtered_words", lambda: filtered_words), size=100)
_l_(646828)
w2v = _c_(646838, _n_(646829, "dict", lambda: dict), _c_(646837, _n_(646830, "zip", lambda: zip), _a_(646833, _a_(646832, _n_(646831, "model", lambda: model), "wv"), "index2word"), _a_(646836, _a_(646835, _n_(646834, "model", lambda: model), "wv"), "syn0")))
_l_(646839)

_c_(646842, _n_(646840, "print", lambda: print), _n_(646841, "w2v", lambda: w2v)['h'])
_l_(646843)

training = []
_l_(646844)
for index, item in _c_(646847, _a_(646846, _n_(646845, "train", lambda: train), "iterrows")):
    _l_(646894)

    vec = _c_(646850, _a_(646849, _n_(646848, "np", lambda: np), "zeros"), 100)
    _l_(646851)
    token_words = [_c_(646855, _a_(646853, _n_(646852, "stemmer", lambda: stemmer), "stem"), _n_(646854, "word", lambda: word)) for word in _n_(646856, "item", lambda: item)['tokens']]
    _l_(646857)
    token_words = [_n_(646858, "word", lambda: word) for word in _n_(646859, "token_words", lambda: token_words) if _n_(646860, "word", lambda: word) not in _c_(646865, _a_(646864, _a_(646863, _a_(646862, _n_(646861, "nl", lambda: nl), "corpus"), "stopwords"), "words"), 'english')]
    _l_(646866)
    for w in _n_(646867, "token_words", lambda: token_words):
        _l_(646874)

        if _n_(646868, "w", lambda: w) in _n_(646869, "w2v", lambda: w2v):
            _l_(646873)

            vec += _n_(646870, "w2v", lambda: w2v)[_n_(646871, "w", lambda: w)]
            _l_(646872)
    norm = _c_(646879, _a_(646877, _a_(646876, _n_(646875, "np", lambda: np), "linalg"), "norm"), _n_(646878, "vec", lambda: vec))
    _l_(646880)
    if _n_(646881, "norm", lambda: norm) != 0:
        _l_(646888)

        vec /= _c_(646886, _a_(646884, _a_(646883, _n_(646882, "np", lambda: np), "linalg"), "norm"), _n_(646885, "vec", lambda: vec))
        _l_(646887)

    _c_(646892, _a_(646890, _n_(646889, "training", lambda: training), "append"), _n_(646891, "vec", lambda: vec))
    _l_(646893)

training_new = _c_(646898, _a_(646896, _n_(646895, "np", lambda: np), "array"), _n_(646897, "training", lambda: training))
_l_(646899)
try:
    from numpy import array
    _l_(646901)

except ImportError:
    pass
try:
    from sklearn.preprocessing import LabelEncoder
    _l_(646903)

except ImportError:
    pass
try:
    from sklearn.preprocessing import OneHotEncoder
    _l_(646905)

except ImportError:
    pass

# integer encode
label_encoder = _c_(646907, _n_(646906, "LabelEncoder", lambda: LabelEncoder))
_l_(646908)
integer_encoded = _c_(646912, _a_(646910, _n_(646909, "label_encoder", lambda: label_encoder), "fit_transform"), _n_(646911, "training_new", lambda: training_new)[:,1])
_l_(646913)

# binary encode
onehot_encoder = _c_(646915, _n_(646914, "OneHotEncoder", lambda: OneHotEncoder), sparse=False)
_l_(646916)
integer_encoded = _c_(646922, _a_(646918, _n_(646917, "integer_encoded", lambda: integer_encoded), "reshape"), _c_(646921, _n_(646919, "len", lambda: len), _n_(646920, "integer_encoded", lambda: integer_encoded)), 1)
_l_(646923)
onehot_encoded = _c_(646927, _a_(646925, _n_(646924, "onehot_encoder", lambda: onehot_encoder), "fit_transform"), _n_(646926, "integer_encoded", lambda: integer_encoded))
_l_(646928)

train_y = _n_(646929, "onehot_encoded", lambda: onehot_encoded)
_l_(646930)

train_x = _c_(646933, _n_(646931, "list", lambda: list), _n_(646932, "training_new", lambda: training_new)[:,0])
_l_(646934)

_c_(646939, _n_(646935, "print", lambda: print), _c_(646938, _n_(646936, "len", lambda: len), _n_(646937, "train_x", lambda: train_x)))
_l_(646940)
_c_(646945, _n_(646941, "print", lambda: print), _c_(646944, _n_(646942, "type", lambda: type), _n_(646943, "train_x", lambda: train_x)))
_l_(646946)
try:
    import tensorflow as tf
    _l_(646948)

except ImportError:
    pass
try:
    import tflearn
    _l_(646950)

except ImportError:
    pass

# reset underlying graph data
_c_(646953, _a_(646952, _n_(646951, "tf", lambda: tf), "reset_default_graph"))
_l_(646954)
# Build neural network
net = _c_(646960, _a_(646956, _n_(646955, "tflearn", lambda: tflearn), "input_data"), shape=[None, _c_(646959, _n_(646957, "len", lambda: len), _n_(646958, "train_x", lambda: train_x)[0])])
_l_(646961)
net = _c_(646965, _a_(646963, _n_(646962, "tflearn", lambda: tflearn), "fully_connected"), _n_(646964, "net", lambda: net), 8)
_l_(646966)
net = _c_(646970, _a_(646968, _n_(646967, "tflearn", lambda: tflearn), "fully_connected"), _n_(646969, "net", lambda: net), 8)
_l_(646971)
net = _c_(646978, _a_(646973, _n_(646972, "tflearn", lambda: tflearn), "fully_connected"), _n_(646974, "net", lambda: net), _c_(646977, _n_(646975, "len", lambda: len), _n_(646976, "train_y", lambda: train_y)), activation='softmax')
_l_(646979)
net = _c_(646983, _a_(646981, _n_(646980, "tflearn", lambda: tflearn), "regression"), _n_(646982, "net", lambda: net))
_l_(646984)

# Define model and setup tensorboard
model = _c_(646988, _a_(646986, _n_(646985, "tflearn", lambda: tflearn), "DNN"), _n_(646987, "net", lambda: net), tensorboard_dir='tflearn_logs')
_l_(646989)
# Start training (apply gradient descent algorithm)
_c_(646994, _a_(646991, _n_(646990, "model", lambda: model), "fit"), _n_(646992, "train_x", lambda: train_x), _n_(646993, "train_y", lambda: train_y), n_epoch=10, batch_size=8, show_metric=True)
_l_(646995)
_c_(646998, _a_(646997, _n_(646996, "model", lambda: model), "save"), 'model.tflearn')
_l_(646999)