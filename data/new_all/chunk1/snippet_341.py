# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48600538/attributeerror-nonetype-object-has-no-attribute-dtype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(383285)

except ImportError:
    pass
try:
    import csv
    _l_(383287)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(383289)

except ImportError:
    pass

with _c_(383291, _n_(383290, "open", lambda: open), 'criminal_train.csv') as fp:
    _l_(383307)

    reader = _c_(383295, _a_(383293, _n_(383292, "csv", lambda: csv), "reader"), _n_(383294, "fp", lambda: fp), delimiter=',', quotechar='"')
    _l_(383296)
    train_data = _c_(383301, _a_(383298, _n_(383297, "np", lambda: np), "array"), [_n_(383299, "row", lambda: row) for row in _n_(383300, "reader", lambda: reader)])
    _l_(383302)
    data_X = _n_(383303, "train_data", lambda: train_data)[1:, 1:-1]
    _l_(383304)
    data_Y = _n_(383305, "train_data", lambda: train_data)[1:, -1:]
    _l_(383306)

with _c_(383309, _n_(383308, "open", lambda: open), 'criminal_test.csv') as fp:
    _l_(383323)

    reader = _c_(383313, _a_(383311, _n_(383310, "csv", lambda: csv), "reader"), _n_(383312, "fp", lambda: fp), delimiter=',', quotechar='"')
    _l_(383314)
    test_data = _c_(383319, _a_(383316, _n_(383315, "np", lambda: np), "array"), [_n_(383317, "row", lambda: row) for row in _n_(383318, "reader", lambda: reader)])
    _l_(383320)
    predict_data = _n_(383321, "test_data", lambda: test_data)[1:, 1:]
    _l_(383322)

#Spltting the training data in 80:20
split = _c_(383327, _n_(383324, "int", lambda: int), _a_(383326, _n_(383325, "data_X", lambda: data_X), "shape")[0]*0.8)
_l_(383328)
X_train = _n_(383329, "data_X", lambda: data_X)[:_n_(383330, "split", lambda: split), :]
_l_(383331)
X_test = _n_(383332, "data_X", lambda: data_X)[_n_(383333, "split", lambda: split):, :]
_l_(383334)
Y_train_labels = _n_(383335, "data_Y", lambda: data_Y)[:_n_(383336, "split", lambda: split), :]
_l_(383337)
Y_test_labels = _n_(383338, "data_Y", lambda: data_Y)[_n_(383339, "split", lambda: split):, :]
_l_(383340)

#convert labels to one_hot matrices (classes=2)
Y_train = _c_(383345, _a_(383342, _n_(383341, "np", lambda: np), "zeros"), (_a_(383344, _n_(383343, "Y_train_labels", lambda: Y_train_labels), "shape")[0], 2))
_l_(383346)
_n_(383347, "Y_train", lambda: Y_train)[_c_(383352, _a_(383349, _n_(383348, "np", lambda: np), "arange"), _a_(383351, _n_(383350, "Y_train_labels", lambda: Y_train_labels), "shape")[0]), _c_(383356, _a_(383354, _n_(383353, "Y_train_labels", lambda: Y_train_labels), "astype"), _n_(383355, "int", lambda: int))] = 1
_l_(383357)
Y_test = _c_(383362, _a_(383359, _n_(383358, "np", lambda: np), "zeros"), (_a_(383361, _n_(383360, "Y_test_labels", lambda: Y_test_labels), "shape")[0], 2))
_l_(383363)
_n_(383364, "Y_test", lambda: Y_test)[_c_(383369, _a_(383366, _n_(383365, "np", lambda: np), "arange"), _a_(383368, _n_(383367, "Y_test_labels", lambda: Y_test_labels), "shape")[0]), _c_(383373, _a_(383371, _n_(383370, "Y_test_labels", lambda: Y_test_labels), "astype"), _n_(383372, "int", lambda: int))] = 1
_l_(383374)


def random_mini_batches(X, Y, mini_batch_size):
    _l_(383420)

    m = _a_(383376, _n_(383375, "X", lambda: X), "shape")[0]
    _l_(383377)
    perm = _c_(383382, _a_(383380, _a_(383379, _n_(383378, "np", lambda: np), "random"), "permutation"), _n_(383381, "X", lambda: X))
    _l_(383383)
    X = _n_(383384, "X", lambda: X)[_n_(383385, "perm", lambda: perm), :]
    _l_(383386)
    Y = _n_(383387, "Y", lambda: Y)[_n_(383388, "perm", lambda: perm), :]
    _l_(383389)
    num_batches = _c_(383393, _n_(383390, "int", lambda: int), _n_(383391, "m", lambda: m) / _n_(383392, "mini_batch_size", lambda: mini_batch_size)) + 1
    _l_(383394)
    bathces = []
    _l_(383395)
    for k in _c_(383398, _n_(383396, "range", lambda: range), _n_(383397, "num_batches", lambda: num_batches)):
        _l_(383417)

        X_batch = _n_(383399, "X", lambda: X)[_n_(383400, "k", lambda: k)*_n_(383401, "mini_batch_size", lambda: mini_batch_size):(_n_(383402, "k", lambda: k)+1)*_n_(383403, "mini_batch_size", lambda: mini_batch_size), :]
        _l_(383404)
        Y_batch = _n_(383405, "Y", lambda: Y)[_n_(383406, "k", lambda: k)*_n_(383407, "mini_batch_size", lambda: mini_batch_size):(_n_(383408, "k", lambda: k)+1)*_n_(383409, "mini_batch_size", lambda: mini_batch_size), :]
        _l_(383410)
        _c_(383415, _a_(383412, _n_(383411, "batches", lambda: batches), "append"), (_n_(383413, "X_batch", lambda: X_batch), _n_(383414, "Y_batch", lambda: Y_batch)))
        _l_(383416)
    aux = _n_(383418, "batches", lambda: batches)
    _l_(383419)
    return aux

def create_placeholders():
    _l_(383436)

    X = _c_(383425, _a_(383422, _n_(383421, "tf", lambda: tf), "placeholder"), _a_(383424, _n_(383423, "tf", lambda: tf), "float32"), shape=[None,70], name='X')
    _l_(383426)
    Y = _c_(383431, _a_(383428, _n_(383427, "tf", lambda: tf), "placeholder"), _a_(383430, _n_(383429, "tf", lambda: tf), "float32"), shape=[None,2], name='Y')
    _l_(383432)
    aux = _n_(383433, "X", lambda: X), _n_(383434, "Y", lambda: Y)
    _l_(383435)
    return aux

def forward_propagation(X):
    _l_(383467)

    A1 = _c_(383442, _a_(383440, _a_(383439, _a_(383438, _n_(383437, "tf", lambda: tf), "contrib"), "layers"), "fully_connected"), _n_(383441, "X", lambda: X), 100)
    _l_(383443)
    A2 = _c_(383449, _a_(383447, _a_(383446, _a_(383445, _n_(383444, "tf", lambda: tf), "contrib"), "layers"), "fully_connected"), _n_(383448, "A1", lambda: A1), 150)
    _l_(383450)
    A3 = _c_(383456, _a_(383454, _a_(383453, _a_(383452, _n_(383451, "tf", lambda: tf), "contrib"), "layers"), "fully_connected"), _n_(383455, "A2", lambda: A2), 100)
    _l_(383457)
    Z5 = _c_(383463, _a_(383461, _a_(383460, _a_(383459, _n_(383458, "tf", lambda: tf), "contrib"), "layers"), "fully_connected"), _n_(383462, "A3", lambda: A3), 2, activation_fn=None)
    _l_(383464)
    aux = _n_(383465, "Z5", lambda: Z5)
    _l_(383466)
    return aux

def compute_cost(Z5, Y):
    _l_(383478)

    cost = _c_(383476, _a_(383469, _n_(383468, "tf", lambda: tf), "reduce_mean"), _c_(383475, _a_(383472, _a_(383471, _n_(383470, "tf", lambda: tf), "nn"), "softmax_cross_entropy_with_logits"), logits=_n_(383473, "Z5", lambda: Z5), labels=_n_(383474, "Y", lambda: Y)))
    _l_(383477)

def model(X_train, X_test, Y_train, Y_test, learning_rate=0.3, beta1=0.9, beta2=0.999, mini_batch_size=32, epochs=1500):
    _l_(383592)

    X, Y = _c_(383480, _n_(383479, "create_placeholders", lambda: create_placeholders))
    _l_(383481)
    Z5 = _c_(383484, _n_(383482, "forward_propagation", lambda: forward_propagation), _n_(383483, "X", lambda: X))
    _l_(383485)
    cost = _c_(383489, _n_(383486, "compute_cost", lambda: compute_cost), _n_(383487, "Z5", lambda: Z5), _n_(383488, "Y", lambda: Y))
    _l_(383490)
    optimizer = _c_(383500, _a_(383498, _c_(383497, _a_(383493, _a_(383492, _n_(383491, "tf", lambda: tf), "train"), "AdamOptimizer"), learning_rate=_n_(383494, "learning_rate", lambda: learning_rate), beta1=_n_(383495, "beta1", lambda: beta1), beta2=_n_(383496, "beta2", lambda: beta2)), "minimize"), _n_(383499, "cost", lambda: cost))
    _l_(383501)
    init = _c_(383504, _a_(383503, _n_(383502, "tf", lambda: tf), "global_variables_initializer"))
    _l_(383505)

    with _c_(383508, _a_(383507, _n_(383506, "tf", lambda: tf), "Session")) as sess:
        _l_(383591)

        _c_(383512, _a_(383510, _n_(383509, "sess", lambda: sess), "run"), _n_(383511, "init", lambda: init))
        _l_(383513)
        for epoch in _c_(383516, _n_(383514, "range", lambda: range), 1,_n_(383515, "epochs", lambda: epochs)+1):
            _l_(383549)

            batches = _c_(383521, _n_(383517, "random_mini_batches", lambda: random_mini_batches), _n_(383518, "X_train", lambda: X_train), _n_(383519, "Y_train", lambda: Y_train), _n_(383520, "mini_batch_size", lambda: mini_batch_size))
            _l_(383522)
            epoch_cost = 0
            _l_(383523)
            for (X_batch, Y_batch) in _n_(383524, "batches", lambda: batches):
                _l_(383537)

                _, cost = _c_(383533, _a_(383526, _n_(383525, "sess", lambda: sess), "run"), [_n_(383527, "optimizer", lambda: optimizer),_n_(383528, "cost", lambda: cost)], feed_dict={_n_(383529, "X", lambda: X):_n_(383530, "X_batch", lambda: X_batch), _n_(383531, "Y", lambda: Y):_n_(383532, "Y_batch", lambda: Y_batch)})
                _l_(383534)
                epoch_cost += _n_(383535, "cost", lambda: cost)
                _l_(383536)
            if _n_(383538, "epoch", lambda: epoch)%100 == 0:
                _l_(383548)

                _c_(383546, _n_(383539, "print", lambda: print), 'Cost in epoch '+_c_(383542, _n_(383540, "str", lambda: str), _n_(383541, "epoch", lambda: epoch))+' is '+_c_(383545, _n_(383543, "str", lambda: str), _n_(383544, "epoch_cost", lambda: epoch_cost)))
                _l_(383547)
        correct_prediction = _c_(383560, _a_(383551, _n_(383550, "tf", lambda: tf), "equal"), _c_(383555, _a_(383553, _n_(383552, "tf", lambda: tf), "argmax"), _n_(383554, "Z5", lambda: Z5)), _c_(383559, _a_(383557, _n_(383556, "tf", lambda: tf), "argmax"), _n_(383558, "Y", lambda: Y)))
        _l_(383561)
        accuracy = _c_(383565, _a_(383563, _n_(383562, "tf", lambda: tf), "reducce_mean"), _n_(383564, "correct_prediction", lambda: correct_prediction), 'float')
        _l_(383566)

        _c_(383577, _n_(383567, "print", lambda: print), 'Train Accuray '+_c_(383576, _n_(383568, "str", lambda: str), _c_(383575, _a_(383570, _n_(383569, "accuracy", lambda: accuracy), "eval"), feed_dict={_n_(383571, "X", lambda: X):_n_(383572, "X_train", lambda: X_train), _n_(383573, "Y", lambda: Y):_n_(383574, "Y_train", lambda: Y_train)})))
        _l_(383578)
        _c_(383589, _n_(383579, "print", lambda: print), 'Test Accuray '+_c_(383588, _n_(383580, "str", lambda: str), _c_(383587, _a_(383582, _n_(383581, "accuracy", lambda: accuracy), "eval"), feed_dict={_n_(383583, "X", lambda: X):_n_(383584, "X_test", lambda: X_test), _n_(383585, "Y", lambda: Y):_n_(383586, "Y_test", lambda: Y_test)})))
        _l_(383590)

_c_(383598, _n_(383593, "model", lambda: model), _n_(383594, "X_train", lambda: X_train), _n_(383595, "X_test", lambda: X_test), _n_(383596, "Y_train", lambda: Y_train), _n_(383597, "Y_test", lambda: Y_test))
_l_(383599)