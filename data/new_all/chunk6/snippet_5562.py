# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48902575/nameerror-name-random-normal-is-not-defined-tensorflow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(335263)

except ImportError:
    pass
try:
    from tensorflow.examples.tutorials.mnist import input_data
    _l_(335265)

except ImportError:
    pass


mnist = _c_(335268, _a_(335267, _n_(335266, "input_data", lambda: input_data), "read_data_sets"), "/var/data/",one_hot=True)
_l_(335269)

n_nodes_hl1=500
_l_(335270)
n_nodes_hl2=500
_l_(335271)
n_nodes_hl3=500
_l_(335272)

n_classes=10
_l_(335273)
batch_size=100
_l_(335274)

#height* width
x=_c_(335277, _a_(335276, _n_(335275, "tf", lambda: tf), "placeholder"), 'float',[None,784]) #28*28
_l_(335278) #28*28
y=_c_(335281, _a_(335280, _n_(335279, "tf", lambda: tf), "placeholder"), 'float')
_l_(335282)

def neural_network_model(data):
    _l_(335398)

    #(input_data*weight)+biases
    hidden_1_layer={'weight':_c_(335289, _a_(335284, _n_(335283, "tf", lambda: tf), "Variable"), _c_(335288, _a_(335286, _n_(335285, "tf", lambda: tf), "random_normal"), [784, _n_(335287, "n_nodes_hl1", lambda: n_nodes_hl1)])), 'biases':_c_(335295, _a_(335291, _n_(335290, "tf", lambda: tf), "Variable"), _c_(335294, _n_(335292, "random_normal", lambda: random_normal), [_n_(335293, "n_nodes_hl1", lambda: n_nodes_hl1)]))}
    _l_(335296)
    hidden_2_layer={'weight':_c_(335304, _a_(335298, _n_(335297, "tf", lambda: tf), "Variable"), _c_(335303, _a_(335300, _n_(335299, "tf", lambda: tf), "random_normal"), [_n_(335301, "n_nodes_hl1", lambda: n_nodes_hl1), _n_(335302, "n_nodes_hl2", lambda: n_nodes_hl2)])), 'biases':_c_(335310, _a_(335306, _n_(335305, "tf", lambda: tf), "Variable"), _c_(335309, _n_(335307, "random_normal", lambda: random_normal), [_n_(335308, "n_nodes_hl2", lambda: n_nodes_hl2)]))}
    _l_(335311)
    hidden_3_layer={'weight':_c_(335319, _a_(335313, _n_(335312, "tf", lambda: tf), "Variable"), _c_(335318, _a_(335315, _n_(335314, "tf", lambda: tf), "random_normal"), [_n_(335316, "n_nodes_hl2", lambda: n_nodes_hl2), _n_(335317, "n_nodes_hl3", lambda: n_nodes_hl3)])), 'biases':_c_(335325, _a_(335321, _n_(335320, "tf", lambda: tf), "Variable"), _c_(335324, _n_(335322, "random_normal", lambda: random_normal), [_n_(335323, "n_nodes_hl3", lambda: n_nodes_hl3)]))}
    _l_(335326)
    output_layer={'weight':_c_(335334, _a_(335328, _n_(335327, "tf", lambda: tf), "Variable"), _c_(335333, _a_(335330, _n_(335329, "tf", lambda: tf), "random_normal"), [_n_(335331, "n_nodes_hl3", lambda: n_nodes_hl3), _n_(335332, "n_classes", lambda: n_classes)])), 'biases':_c_(335340, _a_(335336, _n_(335335, "tf", lambda: tf), "Variable"), _c_(335339, _n_(335337, "random_normal", lambda: random_normal), [_n_(335338, "n_classes", lambda: n_classes)]))}
    _l_(335341)

    l1=_c_(335350, _a_(335343, _n_(335342, "tf", lambda: tf), "add"), _c_(335348, _a_(335345, _n_(335344, "tf", lambda: tf), "matmul"), _n_(335346, "data", lambda: data),_n_(335347, "hidden_1_layer", lambda: hidden_1_layer)['weight']), _n_(335349, "hidden_1_layer", lambda: hidden_1_layer)[ 'biases'])
    _l_(335351)
    l1=_c_(335356, _a_(335354, _a_(335353, _n_(335352, "tf", lambda: tf), "nn"), "relu"), _n_(335355, "l1", lambda: l1))
    _l_(335357)

    l2=_c_(335366, _a_(335359, _n_(335358, "tf", lambda: tf), "add"), _c_(335364, _a_(335361, _n_(335360, "tf", lambda: tf), "matmul"), _n_(335362, "l1", lambda: l1),_n_(335363, "hidden_2_layer", lambda: hidden_2_layer)['weight']), _n_(335365, "hidden_2_layer", lambda: hidden_2_layer)[ 'biases'])
    _l_(335367)
    l2=_c_(335372, _a_(335370, _a_(335369, _n_(335368, "tf", lambda: tf), "nn"), "relu"), _n_(335371, "l2", lambda: l2))
    _l_(335373)

    l3=_c_(335382, _a_(335375, _n_(335374, "tf", lambda: tf), "add"), _c_(335380, _a_(335377, _n_(335376, "tf", lambda: tf), "matmul"), _n_(335378, "l2", lambda: l2),_n_(335379, "hidden_3_layer", lambda: hidden_3_layer)['weight']), _n_(335381, "hidden_3_layer", lambda: hidden_3_layer)[ 'biases'])
    _l_(335383)
    l3=_c_(335388, _a_(335386, _a_(335385, _n_(335384, "tf", lambda: tf), "nn"), "relu"), _n_(335387, "l3", lambda: l3))
    _l_(335389)

    output=_c_(335393, _n_(335390, "matmul", lambda: matmul), _n_(335391, "l3", lambda: l3),_n_(335392, "output_layer", lambda: output_layer)['weight']), _n_(335394, "output_layer", lambda: output_layer)[ 'biases']
    _l_(335395)
    aux = _n_(335396, "output", lambda: output)   
    _l_(335397)   

    return aux   

def train_neural_network(x):
    _l_(335503)

    prediction=_c_(335401, _n_(335399, "neural_network_model", lambda: neural_network_model), _n_(335400, "x", lambda: x))
    _l_(335402)
    cost=_c_(335411, _a_(335404, _n_(335403, "tf", lambda: tf), "reduce_mean"), _c_(335410, _a_(335407, _a_(335406, _n_(335405, "tf", lambda: tf), "nn"), "softmax_cross_entropy_logits"), _n_(335408, "prediction", lambda: prediction),_n_(335409, "y", lambda: y)))
    _l_(335412)

    optimizer=_c_(335419, _a_(335417, _c_(335416, _a_(335415, _a_(335414, _n_(335413, "tf", lambda: tf), "train"), "AdamOptimizer")), "minimize"), _n_(335418, "cost", lambda: cost))
    _l_(335420)

    hm_epochs=10
    _l_(335421)

    with _c_(335424, _a_(335423, _n_(335422, "tf", lambda: tf), "Session")) as sess:
        _l_(335502)

        _c_(335430, _a_(335426, _n_(335425, "sess", lambda: sess), "run"), _c_(335429, _a_(335428, _n_(335427, "tf", lambda: tf), "initialize_all_variables")))
        _l_(335431)

        for epoch in _n_(335432, "hm_epochs", lambda: hm_epochs):
            _l_(335467)

            epoch_loss=0
            _l_(335433)
            for _ in _c_(335441, _n_(335434, "range", lambda: range), _c_(335440, _n_(335435, "int", lambda: int), _a_(335438, _a_(335437, _n_(335436, "mnist", lambda: mnist), "train"), "num_examples")/_n_(335439, "batch_size", lambda: batch_size))):
                _l_(335460)

                epoch_x, epoch_y =_c_(335446, _a_(335444, _a_(335443, _n_(335442, "mnist", lambda: mnist), "train"), "next_batch"), _n_(335445, "batch_size", lambda: batch_size))
                _l_(335447)
                _, c =_n_(335448, "sess", lambda: sess),_c_(335456, _n_(335449, "run", lambda: run), [_n_(335450, "optimizer", lambda: optimizer),_n_(335451, "cost", lambda: cost)], feed_dict ={_n_(335452, "x", lambda: x): _n_(335453, "epoch_x", lambda: epoch_x), _n_(335454, "y", lambda: y): _n_(335455, "epoch_y", lambda: epoch_y)})
                _l_(335457)
                epoch_loss += _n_(335458, "c", lambda: c)
                _l_(335459)
            _c_(335465, _n_(335461, "print", lambda: print), 'Epoch',_n_(335462, "epoch", lambda: epoch), 'complete out of', _n_(335463, "hm_epochs", lambda: hm_epochs), 'loss',_n_(335464, "epoch_loss", lambda: epoch_loss))
            _l_(335466)
        correct= _c_(335478, _a_(335469, _n_(335468, "tf", lambda: tf), "equal"), _c_(335473, _a_(335471, _n_(335470, "tf", lambda: tf), "argmax"), _n_(335472, "prediction", lambda: prediction),1), _c_(335477, _a_(335475, _n_(335474, "tf", lambda: tf), "argmx"), _n_(335476, "y", lambda: y),1))
        _l_(335479)
        accuracy= _c_(335486, _a_(335481, _n_(335480, "tf", lambda: tf), "reduce_mean"), _c_(335485, _a_(335483, _n_(335482, "tf", lambda: tf), "cast"), _n_(335484, "correct", lambda: correct), 'float'))
        _l_(335487)
        _c_(335500, _n_(335488, "print", lambda: print), 'Accuracy:', _c_(335499, _a_(335490, _n_(335489, "accuracy", lambda: accuracy), "eval"), {_n_(335491, "x", lambda: x):_a_(335494, _a_(335493, _n_(335492, "mnist", lambda: mnist), "test"), "images"), _n_(335495, "y", lambda: y):_a_(335498, _a_(335497, _n_(335496, "mnist", lambda: mnist), "test"), "labels")}))
        _l_(335501)



_c_(335506, _n_(335504, "train_neural_network", lambda: train_neural_network), _n_(335505, "x", lambda: x))
_l_(335507)