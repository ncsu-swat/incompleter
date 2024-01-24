# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50779554/nameerror-name-gate-op-is-not-defined-tensorflow
from __future__ import absolute_import, print_function, division
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(392476)
try:
    import far_ho as far
    _l_(392478)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(392480)

except ImportError:
    pass
try:
    import far_ho.examples as far_ex
    _l_(392482)

except ImportError:
    pass
try:
    import os
    _l_(392484)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(392486)

except ImportError:
    pass
try:
    import seaborn as sbn
    _l_(392488)

except ImportError:
    pass

_c_(392491, _a_(392490, _n_(392489, "sbn", lambda: sbn), "set_style"), 'whitegrid')
_l_(392492)
#%matplotlib inline

_c_(392495, _a_(392494, _n_(392493, "tf", lambda: tf), "reset_default_graph"))
_l_(392496)
ss = _c_(392499, _a_(392498, _n_(392497, "tf", lambda: tf), "InteractiveSession"))
_l_(392500)

x = _c_(392505, _a_(392502, _n_(392501, "tf", lambda: tf), "placeholder"), _a_(392504, _n_(392503, "tf", lambda: tf), "float32"), shape=(None, 28**2), name='x')
_l_(392506)
y = _c_(392511, _a_(392508, _n_(392507, "tf", lambda: tf), "placeholder"), _a_(392510, _n_(392509, "tf", lambda: tf), "float32"), shape=(None, 10), name='y')
_l_(392512)

# load a small portion of mnist data
datasets = _c_(392522, _a_(392514, _n_(392513, "far_ex", lambda: far_ex), "mnist"), folder=_c_(392521, _a_(392517, _a_(392516, _n_(392515, "os", lambda: os), "path"), "join"), _c_(392520, _a_(392519, _n_(392518, "os", lambda: os), "getcwd")), 'MNIST_DATA'), partitions=(.1, .1,))
_l_(392523)
datasets = _c_(392528, _a_(392526, _a_(392525, _n_(392524, "far_ex", lambda: far_ex), "Datasets"), "from_list"), _n_(392527, "datasets", lambda: datasets))
_l_(392529)
try:
    import tensorflow.contrib.layers as tcl
    _l_(392531)

except ImportError:
    pass

with _c_(392534, _a_(392533, _n_(392532, "tf", lambda: tf), "variable_scope"), 'model'):
    _l_(392558)

    h1 = _c_(392538, _a_(392536, _n_(392535, "tcl", lambda: tcl), "fully_connected"), _n_(392537, "x", lambda: x), 300)
    _l_(392539)
    out = _c_(392546, _a_(392541, _n_(392540, "tcl", lambda: tcl), "fully_connected"), _n_(392542, "h1", lambda: h1), _a_(392545, _a_(392544, _n_(392543, "datasets", lambda: datasets), "train"), "dim_target"))
    _l_(392547)
    _c_(392549, _n_(392548, "print", lambda: print), 'Ground model weights (parameters)')
    _l_(392550)
    [_c_(392553, _n_(392551, "print", lambda: print), _n_(392552, "e", lambda: e)) for e in _c_(392556, _a_(392555, _n_(392554, "tf", lambda: tf), "model_variables"))];
    _l_(392557)
with _c_(392561, _a_(392560, _n_(392559, "tf", lambda: tf), "variable_scope"), 'inital_weight_model'):
    _l_(392590)

    h1_hyp = _c_(392567, _a_(392563, _n_(392562, "tcl", lambda: tcl), "fully_connected"), _n_(392564, "x", lambda: x), 300,
                                 variables_collections=_a_(392566, _n_(392565, "far", lambda: far), "HYPERPARAMETERS_COLLECTIONS"),
                                trainable=False)
    _l_(392568)
    out_hyp = _c_(392577, _a_(392570, _n_(392569, "tcl", lambda: tcl), "fully_connected"), _n_(392571, "h1_hyp", lambda: h1_hyp), _a_(392574, _a_(392573, _n_(392572, "datasets", lambda: datasets), "train"), "dim_target"),
                                 variables_collections=_a_(392576, _n_(392575, "far", lambda: far), "HYPERPARAMETERS_COLLECTIONS"),
                                 trainable=False)
    _l_(392578)
    _c_(392580, _n_(392579, "print", lambda: print), 'Initial model weights (hyperparameters)')
    _l_(392581)
    [_c_(392584, _n_(392582, "print", lambda: print), _n_(392583, "e", lambda: e)) for e in _c_(392588, _a_(392587, _a_(392586, _n_(392585, "far", lambda: far), "utils"), "hyperparameters"))];
    _l_(392589)
#     far.utils.remove_from_collection(far.GraphKeys.MODEL_VARIABLES, *far.utils.hyperparameters())

# get an hyperparameter for weighting the examples for the inner objective loss (training error)
weights = _c_(392599, _a_(392592, _n_(392591, "far", lambda: far), "get_hyperparameter"), 'ex_weights', _c_(392598, _a_(392594, _n_(392593, "tf", lambda: tf), "zeros"), _a_(392597, _a_(392596, _n_(392595, "datasets", lambda: datasets), "train"), "num_examples")))
_l_(392600)

# build loss and accuracy
# inner objective (training error), weighted mean of cross entropy errors (with sigmoid to be sure is > 0)
with _c_(392603, _a_(392602, _n_(392601, "tf", lambda: tf), "name_scope"), 'errors'):
    _l_(392628)

    tr_loss = _c_(392616, _a_(392605, _n_(392604, "tf", lambda: tf), "reduce_mean"), _c_(392609, _a_(392607, _n_(392606, "tf", lambda: tf), "sigmoid"), _n_(392608, "weights", lambda: weights))*_c_(392615, _a_(392612, _a_(392611, _n_(392610, "tf", lambda: tf), "nn"), "softmax_cross_entropy_with_logits"), labels=_n_(392613, "y", lambda: y), logits=_n_(392614, "out", lambda: out)))
    _l_(392617)
    # outer objective (validation error) (not weighted)
    val_loss = _c_(392626, _a_(392619, _n_(392618, "tf", lambda: tf), "reduce_mean"), _c_(392625, _a_(392622, _a_(392621, _n_(392620, "tf", lambda: tf), "nn"), "softmax_cross_entropy_with_logits"), labels=_n_(392623, "y", lambda: y), logits=_n_(392624, "out", lambda: out)))
    _l_(392627)
accuracy = _c_(392647, _a_(392630, _n_(392629, "tf", lambda: tf), "reduce_mean"), _c_(392646, _a_(392632, _n_(392631, "tf", lambda: tf), "cast"), _c_(392643, _a_(392634, _n_(392633, "tf", lambda: tf), "equal"), _c_(392638, _a_(392636, _n_(392635, "tf", lambda: tf), "argmax"), _n_(392637, "y", lambda: y), 1), _c_(392642, _a_(392640, _n_(392639, "tf", lambda: tf), "argmax"), _n_(392641, "out", lambda: out), 1)), _a_(392645, _n_(392644, "tf", lambda: tf), "float32")))
_l_(392648)

# optimizers
# get an hyperparameter for the learning rate
lr = _c_(392651, _a_(392650, _n_(392649, "far", lambda: far), "get_hyperparameter"), 'lr', 0.01)
_l_(392652)
io_optim = _c_(392656, _a_(392654, _n_(392653, "far", lambda: far), "GradientDescentOptimizer"), _n_(392655, "lr", lambda: lr))  # for training error minimization an optimizer from far_ho is needed
_l_(392657)  # for training error minimization an optimizer from far_ho is needed
oo_optim = _c_(392661, _a_(392659, _n_(392658, "far", lambda: far), "GradientOracle"), _n_(392660, "lr", lambda: lr))
_l_(392662)
#oo_optim = tf.train.AdamOptimizer()  # for outer objective optimizer all optimizers from tf are valid

_c_(392664, _n_(392663, "print", lambda: print), 'hyperparameters to optimize')
_l_(392665)
[_c_(392668, _n_(392666, "print", lambda: print), _n_(392667, "h", lambda: h)) for h in _c_(392671, _a_(392670, _n_(392669, "far", lambda: far), "hyperparameters"))];
_l_(392672)

# build hyperparameter optimizer
farho = _c_(392675, _a_(392674, _n_(392673, "far", lambda: far), "HyperOptimizer"))
_l_(392676)
run = _c_(392694, _a_(392678, _n_(392677, "farho", lambda: farho), "minimize"), _n_(392679, "val_loss", lambda: val_loss), _n_(392680, "oo_optim", lambda: oo_optim), _n_(392681, "tr_loss", lambda: tr_loss), _n_(392682, "io_optim", lambda: io_optim),
                     init_dynamics_dict={_n_(392683, "v", lambda: v): _n_(392684, "h", lambda: h) for v, h in _c_(392693, _n_(392685, "zip", lambda: zip), _c_(392688, _a_(392687, _n_(392686, "tf", lambda: tf), "model_variables")), _c_(392692, _a_(392691, _a_(392690, _n_(392689, "far", lambda: far), "utils"), "hyperparameters"))[:4])})
_l_(392695)

_c_(392697, _n_(392696, "print", lambda: print), 'Variables (or tensors) that will store the values of the hypergradients')
_l_(392698)
_c_(392703, _n_(392699, "print", lambda: print), *_c_(392702, _a_(392701, _n_(392700, "far", lambda: far), "hypergradients")), sep='\n')
_l_(392704)

# run hyperparameter optimization
T = 200 # performs 200 iteraitons of gradient descent on the training error (rise this values for better performances)
_l_(392705) # performs 200 iteraitons of gradient descent on the training error (rise this values for better performances)
# get data suppliers (could also be stochastic for SGD)
tr_supplier = _c_(392711, _a_(392708, _a_(392707, _n_(392706, "datasets", lambda: datasets), "train"), "create_supplier"), _n_(392709, "x", lambda: x), _n_(392710, "y", lambda: y))
_l_(392712)
val_supplier = _c_(392718, _a_(392715, _a_(392714, _n_(392713, "datasets", lambda: datasets), "validation"), "create_supplier"), _n_(392716, "x", lambda: x), _n_(392717, "y", lambda: y))
_l_(392719)
_c_(392724, _a_(392723, _c_(392722, _a_(392721, _n_(392720, "tf", lambda: tf), "global_variables_initializer")), "run"))
_l_(392725)

_c_(392732, _n_(392726, "print", lambda: print), 'training accuracy', _c_(392731, _a_(392728, _n_(392727, "accuracy", lambda: accuracy), "eval"), _c_(392730, _n_(392729, "tr_supplier", lambda: tr_supplier))))
_l_(392733)
_c_(392740, _n_(392734, "print", lambda: print), 'validation accuracy', _c_(392739, _a_(392736, _n_(392735, "accuracy", lambda: accuracy), "eval"), _c_(392738, _n_(392737, "val_supplier", lambda: val_supplier))))
_l_(392741)
_c_(392743, _n_(392742, "print", lambda: print), '-'*50)
_l_(392744)

tr_accs, val_accs = [], []
_l_(392745)
for _ in _c_(392747, _n_(392746, "range", lambda: range), 20):
    _l_(392797)

    _c_(392752, _n_(392748, "run", lambda: run), _n_(392749, "T", lambda: T), inner_objective_feed_dicts=_n_(392750, "tr_supplier", lambda: tr_supplier), outer_objective_feed_dicts=_n_(392751, "val_supplier", lambda: val_supplier))
    _l_(392753)
    _c_(392761, _a_(392755, _n_(392754, "tr_accs", lambda: tr_accs), "append"), _c_(392760, _a_(392757, _n_(392756, "accuracy", lambda: accuracy), "eval"), _c_(392759, _n_(392758, "tr_supplier", lambda: tr_supplier)))), _c_(392769, _a_(392763, _n_(392762, "val_accs", lambda: val_accs), "append"), _c_(392768, _a_(392765, _n_(392764, "accuracy", lambda: accuracy), "eval"), _c_(392767, _n_(392766, "val_supplier", lambda: val_supplier))))
    _l_(392770)
    _c_(392773, _n_(392771, "print", lambda: print), 'training accuracy', _n_(392772, "tr_accs", lambda: tr_accs)[-1])
    _l_(392774)
    _c_(392777, _n_(392775, "print", lambda: print), 'validation accuracy', _n_(392776, "val_accs", lambda: val_accs)[-1])
    _l_(392778)
    _c_(392783, _n_(392779, "print", lambda: print), 'learning rate', _c_(392782, _a_(392781, _n_(392780, "lr", lambda: lr), "eval")))
    _l_(392784)
    _c_(392792, _n_(392785, "print", lambda: print), 'norm of examples weight', _c_(392791, _a_(392790, _c_(392789, _a_(392787, _n_(392786, "tf", lambda: tf), "norm"), _n_(392788, "weights", lambda: weights)), "eval")))
    _l_(392793)
    _c_(392795, _n_(392794, "print", lambda: print), '-'*50)
    _l_(392796)