# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52096549/when-using-tensor-flow-i-am-getting-error-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(666621)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(666623)

except ImportError:
    pass


# Input data files are available in the "../input/" directory.
# Any results you write to the current directory are saved as output.
#from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))


train = _c_(666626, _a_(666625, _n_(666624, "pd", lambda: pd), "read_csv"), 'C:/Users/gunjit.bedi/Desktop/Tensor Flow/input/train.csv')
_l_(666627)
_c_(666632, _n_(666628, "print", lambda: print), _c_(666631, _a_(666630, _n_(666629, "train", lambda: train), "head")))
_l_(666633)
try:
    import nltk as nl
    _l_(666635)

except ImportError:
    pass
_n_(666636, "train", lambda: train)['tokens'] = [_c_(666640, _a_(666638, _n_(666637, "nl", lambda: nl), "word_tokenize"), _n_(666639, "sentences", lambda: sentences)) for sentences in _a_(666642, _n_(666641, "train", lambda: train), "text")]
_l_(666643)
words = []
_l_(666644)
for item in _a_(666646, _n_(666645, "train", lambda: train), "tokens"):
    _l_(666652)

    _c_(666650, _a_(666648, _n_(666647, "words", lambda: words), "extend"), _n_(666649, "item", lambda: item))
    _l_(666651)

stemmer = _c_(666657, _a_(666656, _a_(666655, _a_(666654, _n_(666653, "nl", lambda: nl), "stem"), "lancaster"), "LancasterStemmer"))
_l_(666658)
words = [_c_(666662, _a_(666660, _n_(666659, "stemmer", lambda: stemmer), "stem"), _n_(666661, "word", lambda: word)) for word in _n_(666663, "words", lambda: words)]
_l_(666664)


filtered_words = [_n_(666665, "word", lambda: word) for word in _n_(666666, "words", lambda: words) if _n_(666667, "word", lambda: word) not in _c_(666672, _a_(666671, _a_(666670, _a_(666669, _n_(666668, "nl", lambda: nl), "corpus"), "stopwords"), "words"), 'english')]
_l_(666673)
try:
    import gensim
    _l_(666675)

except ImportError:
    pass
# let X be a list of tokenized texts (i.e. list of lists of tokens)
model = _c_(666680, _a_(666678, _a_(666677, _n_(666676, "gensim", lambda: gensim), "models"), "Word2Vec"), _n_(666679, "filtered_words", lambda: filtered_words), size=100)
_l_(666681)
w2v = _c_(666691, _n_(666682, "dict", lambda: dict), _c_(666690, _n_(666683, "zip", lambda: zip), _a_(666686, _a_(666685, _n_(666684, "model", lambda: model), "wv"), "index2word"), _a_(666689, _a_(666688, _n_(666687, "model", lambda: model), "wv"), "syn0")))
_l_(666692)

_c_(666695, _n_(666693, "print", lambda: print), _n_(666694, "w2v", lambda: w2v)['h'])
_l_(666696)

training = []
_l_(666697)
for index, item in _c_(666700, _a_(666699, _n_(666698, "train", lambda: train), "iterrows")):
    _l_(666747)

    vec = _c_(666703, _a_(666702, _n_(666701, "np", lambda: np), "zeros"), 100)
    _l_(666704)
    token_words = [_c_(666708, _a_(666706, _n_(666705, "stemmer", lambda: stemmer), "stem"), _n_(666707, "word", lambda: word)) for word in _n_(666709, "item", lambda: item)['tokens']]
    _l_(666710)
    token_words = [_n_(666711, "word", lambda: word) for word in _n_(666712, "token_words", lambda: token_words) if _n_(666713, "word", lambda: word) not in _c_(666718, _a_(666717, _a_(666716, _a_(666715, _n_(666714, "nl", lambda: nl), "corpus"), "stopwords"), "words"), 'english')]
    _l_(666719)
    for w in _n_(666720, "token_words", lambda: token_words):
        _l_(666727)

        if _n_(666721, "w", lambda: w) in _n_(666722, "w2v", lambda: w2v):
            _l_(666726)

            vec += _n_(666723, "w2v", lambda: w2v)[_n_(666724, "w", lambda: w)]
            _l_(666725)
    norm = _c_(666732, _a_(666730, _a_(666729, _n_(666728, "np", lambda: np), "linalg"), "norm"), _n_(666731, "vec", lambda: vec))
    _l_(666733)
    if _n_(666734, "norm", lambda: norm) != 0:
        _l_(666741)

        vec /= _c_(666739, _a_(666737, _a_(666736, _n_(666735, "np", lambda: np), "linalg"), "norm"), _n_(666738, "vec", lambda: vec))
        _l_(666740)

    _c_(666745, _a_(666743, _n_(666742, "training", lambda: training), "append"), _n_(666744, "vec", lambda: vec))
    _l_(666746)

training_new = _c_(666751, _a_(666749, _n_(666748, "np", lambda: np), "array"), _n_(666750, "training", lambda: training))
_l_(666752)
try:
    from numpy import array
    _l_(666754)

except ImportError:
    pass
try:
    from sklearn.preprocessing import LabelEncoder
    _l_(666756)

except ImportError:
    pass
try:
    from sklearn.preprocessing import OneHotEncoder
    _l_(666758)

except ImportError:
    pass

# integer encode
label_encoder = _c_(666760, _n_(666759, "LabelEncoder", lambda: LabelEncoder))
_l_(666761)
integer_encoded = _c_(666765, _a_(666763, _n_(666762, "label_encoder", lambda: label_encoder), "fit_transform"), _n_(666764, "training_new", lambda: training_new)[:,1])
_l_(666766)

# binary encode
onehot_encoder = _c_(666768, _n_(666767, "OneHotEncoder", lambda: OneHotEncoder), sparse=False)
_l_(666769)
integer_encoded = _c_(666775, _a_(666771, _n_(666770, "integer_encoded", lambda: integer_encoded), "reshape"), _c_(666774, _n_(666772, "len", lambda: len), _n_(666773, "integer_encoded", lambda: integer_encoded)), 1)
_l_(666776)
onehot_encoded = _c_(666780, _a_(666778, _n_(666777, "onehot_encoder", lambda: onehot_encoder), "fit_transform"), _n_(666779, "integer_encoded", lambda: integer_encoded))
_l_(666781)

train_y = _n_(666782, "onehot_encoded", lambda: onehot_encoded)
_l_(666783)

train_x = _c_(666786, _n_(666784, "list", lambda: list), _n_(666785, "training_new", lambda: training_new)[:,0])
_l_(666787)

_c_(666792, _n_(666788, "print", lambda: print), _c_(666791, _n_(666789, "len", lambda: len), _n_(666790, "train_x", lambda: train_x)))
_l_(666793)
_c_(666798, _n_(666794, "print", lambda: print), _c_(666797, _n_(666795, "type", lambda: type), _n_(666796, "train_x", lambda: train_x)))
_l_(666799)
try:
    import tensorflow as tf
    _l_(666801)

except ImportError:
    pass
try:
    import tflearn
    _l_(666803)

except ImportError:
    pass

# reset underlying graph data
_c_(666806, _a_(666805, _n_(666804, "tf", lambda: tf), "reset_default_graph"))
_l_(666807)
# Build neural network
net = _c_(666813, _a_(666809, _n_(666808, "tflearn", lambda: tflearn), "input_data"), shape=[None, _c_(666812, _n_(666810, "len", lambda: len), _n_(666811, "train_x", lambda: train_x)[0])])
_l_(666814)
net = _c_(666818, _a_(666816, _n_(666815, "tflearn", lambda: tflearn), "fully_connected"), _n_(666817, "net", lambda: net), 8)
_l_(666819)
net = _c_(666823, _a_(666821, _n_(666820, "tflearn", lambda: tflearn), "fully_connected"), _n_(666822, "net", lambda: net), 8)
_l_(666824)
net = _c_(666831, _a_(666826, _n_(666825, "tflearn", lambda: tflearn), "fully_connected"), _n_(666827, "net", lambda: net), _c_(666830, _n_(666828, "len", lambda: len), _n_(666829, "train_y", lambda: train_y)), activation='softmax')
_l_(666832)
net = _c_(666836, _a_(666834, _n_(666833, "tflearn", lambda: tflearn), "regression"), _n_(666835, "net", lambda: net))
_l_(666837)

# Define model and setup tensorboard
model = _c_(666841, _a_(666839, _n_(666838, "tflearn", lambda: tflearn), "DNN"), _n_(666840, "net", lambda: net), tensorboard_dir='tflearn_logs')
_l_(666842)
# Start training (apply gradient descent algorithm)
_c_(666847, _a_(666844, _n_(666843, "model", lambda: model), "fit"), _n_(666845, "train_x", lambda: train_x), _n_(666846, "train_y", lambda: train_y), n_epoch=10, batch_size=8, show_metric=True)
_l_(666848)
_c_(666851, _a_(666850, _n_(666849, "model", lambda: model), "save"), 'model.tflearn')
_l_(666852)