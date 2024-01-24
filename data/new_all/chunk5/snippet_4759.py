# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49338590/deep-neural-network-using-tensorflow-typeerror-variancescaling-object-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
n_input = 18
_l_(707367)
n_target = 1
_l_(707368)
n_hl1 = 10
_l_(707369)
n_hl2 = 10
_l_(707370)
n_hl3 = 10 
_l_(707371) 

learning_rate = 0.1
_l_(707372)

batch_size = 100
_l_(707373)

X = _c_(707376, _a_(707375, _n_(707374, "tf", lambda: tf), "placeholder"), 'float')
_l_(707377)
Y = _c_(707380, _a_(707379, _n_(707378, "tf", lambda: tf), "placeholder"), 'float')
_l_(707381)

# Initializers
sigma = 1
_l_(707382)
weight_initializer = _c_(707386, _a_(707384, _n_(707383, "tf", lambda: tf), "variance_scaling_initializer"), mode="fan_avg", distribution="uniform", scale=_n_(707385, "sigma", lambda: sigma))
_l_(707387)
bias_initializer = _c_(707390, _a_(707389, _n_(707388, "tf", lambda: tf), "zeros_initializer"))
_l_(707391)

# Layer 1: Variables for hidden weights and biases
W_hidden_1 = _c_(707397, _a_(707393, _n_(707392, "tf", lambda: tf), "Variable"), _n_(707394, "weight_initializer", lambda: weight_initializer)[_n_(707395, "n_input", lambda: n_input), _n_(707396, "n_hl1", lambda: n_hl1)])
_l_(707398)
bias_hidden_1 = _c_(707404, _a_(707400, _n_(707399, "tf", lambda: tf), "Variable"), _c_(707403, _n_(707401, "bias_initializer", lambda: bias_initializer), [_n_(707402, "n_hl1", lambda: n_hl1)]))
_l_(707405)

# Layer 2: Variables for hidden weights and biases
W_hidden_2 = _c_(707412, _a_(707407, _n_(707406, "tf", lambda: tf), "Variable"), _c_(707411, _n_(707408, "weight_initializer", lambda: weight_initializer), [_n_(707409, "n_hl1", lambda: n_hl1), _n_(707410, "n_hl2", lambda: n_hl2)]))
_l_(707413)
bias_hidden_2 = _c_(707419, _a_(707415, _n_(707414, "tf", lambda: tf), "Variable"), _c_(707418, _n_(707416, "bias_initializer", lambda: bias_initializer), [_n_(707417, "n_hl2", lambda: n_hl2)]))
_l_(707420)

# Layer 3: Variables for hidden weights and biases
W_hidden_3 = _c_(707427, _a_(707422, _n_(707421, "tf", lambda: tf), "Variable"), _c_(707426, _n_(707423, "weight_initializer", lambda: weight_initializer), [_n_(707424, "n_hl2", lambda: n_hl2), _n_(707425, "n_hl3", lambda: n_hl3)]))
_l_(707428)
bias_hidden_3 = _c_(707434, _a_(707430, _n_(707429, "tf", lambda: tf), "Variable"), _c_(707433, _n_(707431, "bias_initializer", lambda: bias_initializer), [_n_(707432, "n_hl3", lambda: n_hl3)]))
_l_(707435)

# Output layer: Variables for output weights and biases
W_out = _c_(707442, _a_(707437, _n_(707436, "tf", lambda: tf), "Variable"), _c_(707441, _n_(707438, "weight_initializer", lambda: weight_initializer), [_n_(707439, "n_hl3", lambda: n_hl3), _n_(707440, "n_target", lambda: n_target)]))
_l_(707443)
bias_out = _c_(707449, _a_(707445, _n_(707444, "tf", lambda: tf), "Variable"), _c_(707448, _n_(707446, "bias_initializer", lambda: bias_initializer), [_n_(707447, "n_target", lambda: n_target)]))
_l_(707450)

# Hidden layer
hidden_1 = _c_(707463, _a_(707453, _a_(707452, _n_(707451, "tf", lambda: tf), "nn"), "relu"), _c_(707462, _a_(707455, _n_(707454, "tf", lambda: tf), "add"), _c_(707460, _a_(707457, _n_(707456, "tf", lambda: tf), "matmul"), _n_(707458, "X", lambda: X), _n_(707459, "W_hidden_1", lambda: W_hidden_1)), _n_(707461, "bias_hidden_1", lambda: bias_hidden_1)))
_l_(707464)
hidden_2 = _c_(707477, _a_(707467, _a_(707466, _n_(707465, "tf", lambda: tf), "nn"), "relu"), _c_(707476, _a_(707469, _n_(707468, "tf", lambda: tf), "add"), _c_(707474, _a_(707471, _n_(707470, "tf", lambda: tf), "matmul"), _n_(707472, "hidden_1", lambda: hidden_1), _n_(707473, "W_hidden_2", lambda: W_hidden_2)), _n_(707475, "bias_hidden_2", lambda: bias_hidden_2)))
_l_(707478)
hidden_3 = _c_(707491, _a_(707481, _a_(707480, _n_(707479, "tf", lambda: tf), "nn"), "relu"), _c_(707490, _a_(707483, _n_(707482, "tf", lambda: tf), "add"), _c_(707488, _a_(707485, _n_(707484, "tf", lambda: tf), "matmul"), _n_(707486, "hidden_2", lambda: hidden_2), _n_(707487, "W_hidden_3", lambda: W_hidden_3)), _n_(707489, "bias_hidden_3", lambda: bias_hidden_3)))
_l_(707492)

# Output layer (must be transposed)
out = _c_(707504, _a_(707494, _n_(707493, "tf", lambda: tf), "transpose"), _c_(707503, _a_(707496, _n_(707495, "tf", lambda: tf), "add"), _c_(707501, _a_(707498, _n_(707497, "tf", lambda: tf), "matmul"), _n_(707499, "hidden_3", lambda: hidden_3), _n_(707500, "W_out", lambda: W_out)), _n_(707502, "bias_out", lambda: bias_out)))
_l_(707505)


#prediction = neural_network_model(x)
cost =_c_(707513, _a_(707507, _n_(707506, "tf", lambda: tf), "reduce_mean"), _c_(707512, _a_(707509, _n_(707508, "tf", lambda: tf), "squared_difference"), _n_(707510, "out", lambda: out), _n_(707511, "Y", lambda: Y)))
_l_(707514)

optimizer = _c_(707522, _a_(707520, _c_(707519, _a_(707517, _a_(707516, _n_(707515, "tf", lambda: tf), "train"), "GradientDescentOptimizer"), _n_(707518, "learning_rate", lambda: learning_rate)), "minimize"), _n_(707521, "cost", lambda: cost))  
_l_(707523)  

epochs = 1000
_l_(707524)

with _c_(707527, _a_(707526, _n_(707525, "tf", lambda: tf), "Session")) as sess:
    _l_(707598)

    _c_(707533, _a_(707529, _n_(707528, "sess", lambda: sess), "run"), _c_(707532, _a_(707531, _n_(707530, "tf", lambda: tf), "global_variables_initializer")))
    _l_(707534)

    for e in _c_(707537, _n_(707535, "range", lambda: range), _n_(707536, "epochs", lambda: epochs)):
        _l_(707584)

        # Shuffle training data
        shuffle_indices = _c_(707547, _a_(707540, _a_(707539, _n_(707538, "np", lambda: np), "random"), "permutation"), _c_(707546, _a_(707542, _n_(707541, "np", lambda: np), "arange"), _c_(707545, _n_(707543, "len", lambda: len), _n_(707544, "y_data", lambda: y_data))))
        _l_(707548)
        x_data = _n_(707549, "x_data", lambda: x_data)[_n_(707550, "shuffle_indices", lambda: shuffle_indices)]
        _l_(707551)
        y_data = _n_(707552, "y_data", lambda: y_data)[_n_(707553, "shuffle_indices", lambda: shuffle_indices)]
        _l_(707554)

        # Minibatch training
        for i in _c_(707560, _n_(707555, "range", lambda: range), 0, _c_(707558, _n_(707556, "len", lambda: len), _n_(707557, "y_data", lambda: y_data)) // _n_(707559, "batch_size", lambda: batch_size)):
            _l_(707583)

            start = _n_(707561, "i", lambda: i) * _n_(707562, "batch_size", lambda: batch_size)
            _l_(707563)
            batch_x = _n_(707564, "x_data", lambda: x_data)[_n_(707565, "start", lambda: start):_n_(707566, "start", lambda: start) + _n_(707567, "batch_size", lambda: batch_size)]
            _l_(707568)
            batch_y = _n_(707569, "y_data", lambda: y_data)[_n_(707570, "start", lambda: start):_n_(707571, "start", lambda: start) + _n_(707572, "batch_size", lambda: batch_size)]
            _l_(707573)
            # Run optimizer with batch
            _c_(707581, _a_(707575, _n_(707574, "sess", lambda: sess), "run"), _n_(707576, "optimizer", lambda: optimizer), feed_dict={_n_(707577, "X", lambda: X): _n_(707578, "batch_x", lambda: batch_x), _n_(707579, "Y", lambda: Y): _n_(707580, "batch_y", lambda: batch_y)})  
            _l_(707582)  


    mse_final = _c_(707592, _a_(707586, _n_(707585, "sess", lambda: sess), "run"), _n_(707587, "cost", lambda: cost), feed_dict={_n_(707588, "X", lambda: X): _n_(707589, "x_test", lambda: x_test), _n_(707590, "Y", lambda: Y): _n_(707591, "y_test", lambda: y_test)})
    _l_(707593)
    _c_(707596, _n_(707594, "print", lambda: print), _n_(707595, "mse_final", lambda: mse_final))
    _l_(707597)