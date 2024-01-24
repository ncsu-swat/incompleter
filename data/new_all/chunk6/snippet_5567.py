# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48902575/nameerror-name-random-normal-is-not-defined-tensorflow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(341670)

except ImportError:
    pass
try:
    from tensorflow.examples.tutorials.mnist import input_data
    _l_(341672)

except ImportError:
    pass


mnist = _c_(341675, _a_(341674, _n_(341673, "input_data", lambda: input_data), "read_data_sets"), "/var/data/",one_hot=True)
_l_(341676)

n_nodes_hl1=500
_l_(341677)
n_nodes_hl2=500
_l_(341678)
n_nodes_hl3=500
_l_(341679)

n_classes=10
_l_(341680)
batch_size=100
_l_(341681)

#height* width
x=_c_(341684, _a_(341683, _n_(341682, "tf", lambda: tf), "placeholder"), 'float',[None,784]) #28*28
_l_(341685) #28*28
y=_c_(341688, _a_(341687, _n_(341686, "tf", lambda: tf), "placeholder"), 'float')
_l_(341689)

def neural_network_model(data):
    _l_(341805)

    #(input_data*weight)+biases
    hidden_1_layer={'weight':_c_(341696, _a_(341691, _n_(341690, "tf", lambda: tf), "Variable"), _c_(341695, _a_(341693, _n_(341692, "tf", lambda: tf), "random_normal"), [784, _n_(341694, "n_nodes_hl1", lambda: n_nodes_hl1)])), 'biases':_c_(341702, _a_(341698, _n_(341697, "tf", lambda: tf), "Variable"), _c_(341701, _n_(341699, "random_normal", lambda: random_normal), [_n_(341700, "n_nodes_hl1", lambda: n_nodes_hl1)]))}
    _l_(341703)
    hidden_2_layer={'weight':_c_(341711, _a_(341705, _n_(341704, "tf", lambda: tf), "Variable"), _c_(341710, _a_(341707, _n_(341706, "tf", lambda: tf), "random_normal"), [_n_(341708, "n_nodes_hl1", lambda: n_nodes_hl1), _n_(341709, "n_nodes_hl2", lambda: n_nodes_hl2)])), 'biases':_c_(341717, _a_(341713, _n_(341712, "tf", lambda: tf), "Variable"), _c_(341716, _n_(341714, "random_normal", lambda: random_normal), [_n_(341715, "n_nodes_hl2", lambda: n_nodes_hl2)]))}
    _l_(341718)
    hidden_3_layer={'weight':_c_(341726, _a_(341720, _n_(341719, "tf", lambda: tf), "Variable"), _c_(341725, _a_(341722, _n_(341721, "tf", lambda: tf), "random_normal"), [_n_(341723, "n_nodes_hl2", lambda: n_nodes_hl2), _n_(341724, "n_nodes_hl3", lambda: n_nodes_hl3)])), 'biases':_c_(341732, _a_(341728, _n_(341727, "tf", lambda: tf), "Variable"), _c_(341731, _n_(341729, "random_normal", lambda: random_normal), [_n_(341730, "n_nodes_hl3", lambda: n_nodes_hl3)]))}
    _l_(341733)
    output_layer={'weight':_c_(341741, _a_(341735, _n_(341734, "tf", lambda: tf), "Variable"), _c_(341740, _a_(341737, _n_(341736, "tf", lambda: tf), "random_normal"), [_n_(341738, "n_nodes_hl3", lambda: n_nodes_hl3), _n_(341739, "n_classes", lambda: n_classes)])), 'biases':_c_(341747, _a_(341743, _n_(341742, "tf", lambda: tf), "Variable"), _c_(341746, _n_(341744, "random_normal", lambda: random_normal), [_n_(341745, "n_classes", lambda: n_classes)]))}
    _l_(341748)

    l1=_c_(341757, _a_(341750, _n_(341749, "tf", lambda: tf), "add"), _c_(341755, _a_(341752, _n_(341751, "tf", lambda: tf), "matmul"), _n_(341753, "data", lambda: data),_n_(341754, "hidden_1_layer", lambda: hidden_1_layer)['weight']), _n_(341756, "hidden_1_layer", lambda: hidden_1_layer)[ 'biases'])
    _l_(341758)
    l1=_c_(341763, _a_(341761, _a_(341760, _n_(341759, "tf", lambda: tf), "nn"), "relu"), _n_(341762, "l1", lambda: l1))
    _l_(341764)

    l2=_c_(341773, _a_(341766, _n_(341765, "tf", lambda: tf), "add"), _c_(341771, _a_(341768, _n_(341767, "tf", lambda: tf), "matmul"), _n_(341769, "l1", lambda: l1),_n_(341770, "hidden_2_layer", lambda: hidden_2_layer)['weight']), _n_(341772, "hidden_2_layer", lambda: hidden_2_layer)[ 'biases'])
    _l_(341774)
    l2=_c_(341779, _a_(341777, _a_(341776, _n_(341775, "tf", lambda: tf), "nn"), "relu"), _n_(341778, "l2", lambda: l2))
    _l_(341780)

    l3=_c_(341789, _a_(341782, _n_(341781, "tf", lambda: tf), "add"), _c_(341787, _a_(341784, _n_(341783, "tf", lambda: tf), "matmul"), _n_(341785, "l2", lambda: l2),_n_(341786, "hidden_3_layer", lambda: hidden_3_layer)['weight']), _n_(341788, "hidden_3_layer", lambda: hidden_3_layer)[ 'biases'])
    _l_(341790)
    l3=_c_(341795, _a_(341793, _a_(341792, _n_(341791, "tf", lambda: tf), "nn"), "relu"), _n_(341794, "l3", lambda: l3))
    _l_(341796)

    output=_c_(341800, _n_(341797, "matmul", lambda: matmul), _n_(341798, "l3", lambda: l3),_n_(341799, "output_layer", lambda: output_layer)['weight']), _n_(341801, "output_layer", lambda: output_layer)[ 'biases']
    _l_(341802)
    aux = _n_(341803, "output", lambda: output)   
    _l_(341804)   

    return aux   

def train_neural_network(x):
    _l_(341910)

    prediction=_c_(341808, _n_(341806, "neural_network_model", lambda: neural_network_model), _n_(341807, "x", lambda: x))
    _l_(341809)
    cost=_c_(341818, _a_(341811, _n_(341810, "tf", lambda: tf), "reduce_mean"), _c_(341817, _a_(341814, _a_(341813, _n_(341812, "tf", lambda: tf), "nn"), "softmax_cross_entropy_logits"), _n_(341815, "prediction", lambda: prediction),_n_(341816, "y", lambda: y)))
    _l_(341819)

    optimizer=_c_(341826, _a_(341824, _c_(341823, _a_(341822, _a_(341821, _n_(341820, "tf", lambda: tf), "train"), "AdamOptimizer")), "minimize"), _n_(341825, "cost", lambda: cost))
    _l_(341827)

    hm_epochs=10
    _l_(341828)

    with _c_(341831, _a_(341830, _n_(341829, "tf", lambda: tf), "Session")) as sess:
        _l_(341909)

        _c_(341837, _a_(341833, _n_(341832, "sess", lambda: sess), "run"), _c_(341836, _a_(341835, _n_(341834, "tf", lambda: tf), "initialize_all_variables")))
        _l_(341838)

        for epoch in _n_(341839, "hm_epochs", lambda: hm_epochs):
            _l_(341874)

            epoch_loss=0
            _l_(341840)
            for _ in _c_(341848, _n_(341841, "range", lambda: range), _c_(341847, _n_(341842, "int", lambda: int), _a_(341845, _a_(341844, _n_(341843, "mnist", lambda: mnist), "train"), "num_examples")/_n_(341846, "batch_size", lambda: batch_size))):
                _l_(341867)

                epoch_x, epoch_y =_c_(341853, _a_(341851, _a_(341850, _n_(341849, "mnist", lambda: mnist), "train"), "next_batch"), _n_(341852, "batch_size", lambda: batch_size))
                _l_(341854)
                _, c =_n_(341855, "sess", lambda: sess),_c_(341863, _n_(341856, "run", lambda: run), [_n_(341857, "optimizer", lambda: optimizer),_n_(341858, "cost", lambda: cost)], feed_dict ={_n_(341859, "x", lambda: x): _n_(341860, "epoch_x", lambda: epoch_x), _n_(341861, "y", lambda: y): _n_(341862, "epoch_y", lambda: epoch_y)})
                _l_(341864)
                epoch_loss += _n_(341865, "c", lambda: c)
                _l_(341866)
            _c_(341872, _n_(341868, "print", lambda: print), 'Epoch',_n_(341869, "epoch", lambda: epoch), 'complete out of', _n_(341870, "hm_epochs", lambda: hm_epochs), 'loss',_n_(341871, "epoch_loss", lambda: epoch_loss))
            _l_(341873)
        correct= _c_(341885, _a_(341876, _n_(341875, "tf", lambda: tf), "equal"), _c_(341880, _a_(341878, _n_(341877, "tf", lambda: tf), "argmax"), _n_(341879, "prediction", lambda: prediction),1), _c_(341884, _a_(341882, _n_(341881, "tf", lambda: tf), "argmx"), _n_(341883, "y", lambda: y),1))
        _l_(341886)
        accuracy= _c_(341893, _a_(341888, _n_(341887, "tf", lambda: tf), "reduce_mean"), _c_(341892, _a_(341890, _n_(341889, "tf", lambda: tf), "cast"), _n_(341891, "correct", lambda: correct), 'float'))
        _l_(341894)
        _c_(341907, _n_(341895, "print", lambda: print), 'Accuracy:', _c_(341906, _a_(341897, _n_(341896, "accuracy", lambda: accuracy), "eval"), {_n_(341898, "x", lambda: x):_a_(341901, _a_(341900, _n_(341899, "mnist", lambda: mnist), "test"), "images"), _n_(341902, "y", lambda: y):_a_(341905, _a_(341904, _n_(341903, "mnist", lambda: mnist), "test"), "labels")}))
        _l_(341908)



_c_(341913, _n_(341911, "train_neural_network", lambda: train_neural_network), _n_(341912, "x", lambda: x))
_l_(341914)