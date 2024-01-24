# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49338590/deep-neural-network-using-tensorflow-typeerror-variancescaling-object-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
n_input = 18
_l_(682042)
n_target = 1
_l_(682043)
n_hl1 = 10
_l_(682044)
n_hl2 = 10
_l_(682045)
n_hl3 = 10 
_l_(682046) 

learning_rate = 0.1
_l_(682047)

batch_size = 100
_l_(682048)

X = _c_(682051, _a_(682050, _n_(682049, "tf", lambda: tf), "placeholder"), 'float')
_l_(682052)
Y = _c_(682055, _a_(682054, _n_(682053, "tf", lambda: tf), "placeholder"), 'float')
_l_(682056)

# Initializers
sigma = 1
_l_(682057)
weight_initializer = _c_(682061, _a_(682059, _n_(682058, "tf", lambda: tf), "variance_scaling_initializer"), mode="fan_avg", distribution="uniform", scale=_n_(682060, "sigma", lambda: sigma))
_l_(682062)
bias_initializer = _c_(682065, _a_(682064, _n_(682063, "tf", lambda: tf), "zeros_initializer"))
_l_(682066)

# Layer 1: Variables for hidden weights and biases
W_hidden_1 = _c_(682072, _a_(682068, _n_(682067, "tf", lambda: tf), "Variable"), _n_(682069, "weight_initializer", lambda: weight_initializer)[_n_(682070, "n_input", lambda: n_input), _n_(682071, "n_hl1", lambda: n_hl1)])
_l_(682073)
bias_hidden_1 = _c_(682079, _a_(682075, _n_(682074, "tf", lambda: tf), "Variable"), _c_(682078, _n_(682076, "bias_initializer", lambda: bias_initializer), [_n_(682077, "n_hl1", lambda: n_hl1)]))
_l_(682080)

# Layer 2: Variables for hidden weights and biases
W_hidden_2 = _c_(682087, _a_(682082, _n_(682081, "tf", lambda: tf), "Variable"), _c_(682086, _n_(682083, "weight_initializer", lambda: weight_initializer), [_n_(682084, "n_hl1", lambda: n_hl1), _n_(682085, "n_hl2", lambda: n_hl2)]))
_l_(682088)
bias_hidden_2 = _c_(682094, _a_(682090, _n_(682089, "tf", lambda: tf), "Variable"), _c_(682093, _n_(682091, "bias_initializer", lambda: bias_initializer), [_n_(682092, "n_hl2", lambda: n_hl2)]))
_l_(682095)

# Layer 3: Variables for hidden weights and biases
W_hidden_3 = _c_(682102, _a_(682097, _n_(682096, "tf", lambda: tf), "Variable"), _c_(682101, _n_(682098, "weight_initializer", lambda: weight_initializer), [_n_(682099, "n_hl2", lambda: n_hl2), _n_(682100, "n_hl3", lambda: n_hl3)]))
_l_(682103)
bias_hidden_3 = _c_(682109, _a_(682105, _n_(682104, "tf", lambda: tf), "Variable"), _c_(682108, _n_(682106, "bias_initializer", lambda: bias_initializer), [_n_(682107, "n_hl3", lambda: n_hl3)]))
_l_(682110)

# Output layer: Variables for output weights and biases
W_out = _c_(682117, _a_(682112, _n_(682111, "tf", lambda: tf), "Variable"), _c_(682116, _n_(682113, "weight_initializer", lambda: weight_initializer), [_n_(682114, "n_hl3", lambda: n_hl3), _n_(682115, "n_target", lambda: n_target)]))
_l_(682118)
bias_out = _c_(682124, _a_(682120, _n_(682119, "tf", lambda: tf), "Variable"), _c_(682123, _n_(682121, "bias_initializer", lambda: bias_initializer), [_n_(682122, "n_target", lambda: n_target)]))
_l_(682125)

# Hidden layer
hidden_1 = _c_(682138, _a_(682128, _a_(682127, _n_(682126, "tf", lambda: tf), "nn"), "relu"), _c_(682137, _a_(682130, _n_(682129, "tf", lambda: tf), "add"), _c_(682135, _a_(682132, _n_(682131, "tf", lambda: tf), "matmul"), _n_(682133, "X", lambda: X), _n_(682134, "W_hidden_1", lambda: W_hidden_1)), _n_(682136, "bias_hidden_1", lambda: bias_hidden_1)))
_l_(682139)
hidden_2 = _c_(682152, _a_(682142, _a_(682141, _n_(682140, "tf", lambda: tf), "nn"), "relu"), _c_(682151, _a_(682144, _n_(682143, "tf", lambda: tf), "add"), _c_(682149, _a_(682146, _n_(682145, "tf", lambda: tf), "matmul"), _n_(682147, "hidden_1", lambda: hidden_1), _n_(682148, "W_hidden_2", lambda: W_hidden_2)), _n_(682150, "bias_hidden_2", lambda: bias_hidden_2)))
_l_(682153)
hidden_3 = _c_(682166, _a_(682156, _a_(682155, _n_(682154, "tf", lambda: tf), "nn"), "relu"), _c_(682165, _a_(682158, _n_(682157, "tf", lambda: tf), "add"), _c_(682163, _a_(682160, _n_(682159, "tf", lambda: tf), "matmul"), _n_(682161, "hidden_2", lambda: hidden_2), _n_(682162, "W_hidden_3", lambda: W_hidden_3)), _n_(682164, "bias_hidden_3", lambda: bias_hidden_3)))
_l_(682167)

# Output layer (must be transposed)
out = _c_(682179, _a_(682169, _n_(682168, "tf", lambda: tf), "transpose"), _c_(682178, _a_(682171, _n_(682170, "tf", lambda: tf), "add"), _c_(682176, _a_(682173, _n_(682172, "tf", lambda: tf), "matmul"), _n_(682174, "hidden_3", lambda: hidden_3), _n_(682175, "W_out", lambda: W_out)), _n_(682177, "bias_out", lambda: bias_out)))
_l_(682180)


#prediction = neural_network_model(x)
cost =_c_(682188, _a_(682182, _n_(682181, "tf", lambda: tf), "reduce_mean"), _c_(682187, _a_(682184, _n_(682183, "tf", lambda: tf), "squared_difference"), _n_(682185, "out", lambda: out), _n_(682186, "Y", lambda: Y)))
_l_(682189)

optimizer = _c_(682197, _a_(682195, _c_(682194, _a_(682192, _a_(682191, _n_(682190, "tf", lambda: tf), "train"), "GradientDescentOptimizer"), _n_(682193, "learning_rate", lambda: learning_rate)), "minimize"), _n_(682196, "cost", lambda: cost))  
_l_(682198)  

epochs = 1000
_l_(682199)

with _c_(682202, _a_(682201, _n_(682200, "tf", lambda: tf), "Session")) as sess:
    _l_(682273)

    _c_(682208, _a_(682204, _n_(682203, "sess", lambda: sess), "run"), _c_(682207, _a_(682206, _n_(682205, "tf", lambda: tf), "global_variables_initializer")))
    _l_(682209)

    for e in _c_(682212, _n_(682210, "range", lambda: range), _n_(682211, "epochs", lambda: epochs)):
        _l_(682259)

        # Shuffle training data
        shuffle_indices = _c_(682222, _a_(682215, _a_(682214, _n_(682213, "np", lambda: np), "random"), "permutation"), _c_(682221, _a_(682217, _n_(682216, "np", lambda: np), "arange"), _c_(682220, _n_(682218, "len", lambda: len), _n_(682219, "y_data", lambda: y_data))))
        _l_(682223)
        x_data = _n_(682224, "x_data", lambda: x_data)[_n_(682225, "shuffle_indices", lambda: shuffle_indices)]
        _l_(682226)
        y_data = _n_(682227, "y_data", lambda: y_data)[_n_(682228, "shuffle_indices", lambda: shuffle_indices)]
        _l_(682229)

        # Minibatch training
        for i in _c_(682235, _n_(682230, "range", lambda: range), 0, _c_(682233, _n_(682231, "len", lambda: len), _n_(682232, "y_data", lambda: y_data)) // _n_(682234, "batch_size", lambda: batch_size)):
            _l_(682258)

            start = _n_(682236, "i", lambda: i) * _n_(682237, "batch_size", lambda: batch_size)
            _l_(682238)
            batch_x = _n_(682239, "x_data", lambda: x_data)[_n_(682240, "start", lambda: start):_n_(682241, "start", lambda: start) + _n_(682242, "batch_size", lambda: batch_size)]
            _l_(682243)
            batch_y = _n_(682244, "y_data", lambda: y_data)[_n_(682245, "start", lambda: start):_n_(682246, "start", lambda: start) + _n_(682247, "batch_size", lambda: batch_size)]
            _l_(682248)
            # Run optimizer with batch
            _c_(682256, _a_(682250, _n_(682249, "sess", lambda: sess), "run"), _n_(682251, "optimizer", lambda: optimizer), feed_dict={_n_(682252, "X", lambda: X): _n_(682253, "batch_x", lambda: batch_x), _n_(682254, "Y", lambda: Y): _n_(682255, "batch_y", lambda: batch_y)})  
            _l_(682257)  


    mse_final = _c_(682267, _a_(682261, _n_(682260, "sess", lambda: sess), "run"), _n_(682262, "cost", lambda: cost), feed_dict={_n_(682263, "X", lambda: X): _n_(682264, "x_test", lambda: x_test), _n_(682265, "Y", lambda: Y): _n_(682266, "y_test", lambda: y_test)})
    _l_(682268)
    _c_(682271, _n_(682269, "print", lambda: print), _n_(682270, "mse_final", lambda: mse_final))
    _l_(682272)