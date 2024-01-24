# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import namedtuple
    _l_(577042)

except ImportError:
    pass

def multilayer_perceptron():
    _l_(577230)

    _c_(577045, _a_(577044, _n_(577043, "tf", lambda: tf), "reset_default_graph"))
    _l_(577046)
    inputs = _c_(577053, _a_(577048, _n_(577047, "tf", lambda: tf), "placeholder"), _a_(577050, _n_(577049, "tf", lambda: tf), "float32"), shape=[None,_a_(577052, _n_(577051, "train_x", lambda: train_x), "shape")[1]])
    _l_(577054)
    y = _c_(577059, _a_(577056, _n_(577055, "tf", lambda: tf), "placeholder"), _a_(577058, _n_(577057, "tf", lambda: tf), "float32"), shape=[None, 1])
    _l_(577060)
    weights = {
    'h1': _c_(577069, _a_(577062, _n_(577061, "tf", lambda: tf), "Variable"), _c_(577068, _a_(577064, _n_(577063, "tf", lambda: tf), "random_normal"), [_a_(577066, _n_(577065, "train_x", lambda: train_x), "shape")[1], _n_(577067, "n_hidden_1", lambda: n_hidden_1)])),
    'h2': _c_(577077, _a_(577071, _n_(577070, "tf", lambda: tf), "Variable"), _c_(577076, _a_(577073, _n_(577072, "tf", lambda: tf), "random_normal"), [_n_(577074, "n_hidden_1", lambda: n_hidden_1), _n_(577075, "n_hidden_2", lambda: n_hidden_2)])),
    'out': _c_(577084, _a_(577079, _n_(577078, "tf", lambda: tf), "Variable"), _c_(577083, _a_(577081, _n_(577080, "tf", lambda: tf), "random_normal"), [_n_(577082, "n_hidden_2", lambda: n_hidden_2), 1]))
    }
    _l_(577085)
    biases = {
    'b1': _c_(577092, _a_(577087, _n_(577086, "tf", lambda: tf), "Variable"), _c_(577091, _a_(577089, _n_(577088, "tf", lambda: tf), "random_normal"), [_n_(577090, "n_hidden_1", lambda: n_hidden_1)])),
    'b2': _c_(577099, _a_(577094, _n_(577093, "tf", lambda: tf), "Variable"), _c_(577098, _a_(577096, _n_(577095, "tf", lambda: tf), "random_normal"), [_n_(577097, "n_hidden_2", lambda: n_hidden_2)])),
    'out': _c_(577105, _a_(577101, _n_(577100, "tf", lambda: tf), "Variable"), _c_(577104, _a_(577103, _n_(577102, "tf", lambda: tf), "random_normal"), [1]))
    }
    _l_(577106)
    # Hidden layer con funzione di attivazione ReLU
    layer_1 = _c_(577115, _a_(577108, _n_(577107, "tf", lambda: tf), "add"), _c_(577113, _a_(577110, _n_(577109, "tf", lambda: tf), "matmul"), _n_(577111, "inputs", lambda: inputs), _n_(577112, "weights", lambda: weights)['h1']), _n_(577114, "biases", lambda: biases)['b1'])
    _l_(577116)
    layer_1 = _c_(577121, _a_(577119, _a_(577118, _n_(577117, "tf", lambda: tf), "nn"), "relu"), _n_(577120, "layer_1", lambda: layer_1))
    _l_(577122)
    # Hidden layer with ReLU activation
    layer_2 = _c_(577131, _a_(577124, _n_(577123, "tf", lambda: tf), "add"), _c_(577129, _a_(577126, _n_(577125, "tf", lambda: tf), "matmul"), _n_(577127, "layer_1", lambda: layer_1), _n_(577128, "weights", lambda: weights)['h2']), _n_(577130, "biases", lambda: biases)['b2'])
    _l_(577132)
    layer_2 = _c_(577137, _a_(577135, _a_(577134, _n_(577133, "tf", lambda: tf), "nn"), "relu"), _n_(577136, "layer_2", lambda: layer_2))
    _l_(577138)
    # Output layer with linear activation
    out_layer = _c_(577143, _a_(577140, _n_(577139, "tf", lambda: tf), "matmul"), _n_(577141, "layer_2", lambda: layer_2), _n_(577142, "weights", lambda: weights)['out']) + _n_(577144, "biases", lambda: biases)['out']
    _l_(577145)
    learning_rate = _c_(577150, _a_(577147, _n_(577146, "tf", lambda: tf), "placeholder"), _a_(577149, _n_(577148, "tf", lambda: tf), "float32"))
    _l_(577151)
    is_training=_c_(577156, _a_(577153, _n_(577152, "tf", lambda: tf), "Variable"), True,dtype=_a_(577155, _n_(577154, "tf", lambda: tf), "bool")) 
    _l_(577157) 
    cross_entropy = _c_(577163, _a_(577160, _a_(577159, _n_(577158, "tf", lambda: tf), "nn"), "sigmoid_cross_entropy_with_logits"), labels=_n_(577161, "y", lambda: y),logits=_n_(577162, "out_layer", lambda: out_layer) )
    _l_(577164)
    cost = _c_(577168, _a_(577166, _n_(577165, "tf", lambda: tf), "reduce_mean"), _n_(577167, "cross_entropy", lambda: cross_entropy))  
    _l_(577169)  
    with _c_(577178, _a_(577171, _n_(577170, "tf", lambda: tf), "control_dependencies"), _c_(577177, _a_(577173, _n_(577172, "tf", lambda: tf), "get_collection"), _a_(577176, _a_(577175, _n_(577174, "tf", lambda: tf), "GraphKeys"), "UPDATE_OPS"))):
        _l_(577188)

        optimizer = _c_(577186, _a_(577184, _c_(577183, _a_(577181, _a_(577180, _n_(577179, "tf", lambda: tf), "train"), "AdamOptimizer"), learning_rate=_n_(577182, "learning_rate", lambda: learning_rate)), "minimize"), _n_(577185, "cost", lambda: cost))
        _l_(577187)
    predicted = _c_(577193, _a_(577191, _a_(577190, _n_(577189, "tf", lambda: tf), "nn"), "sigmoid"), _n_(577192, "out_layer", lambda: out_layer)) 
    _l_(577194) 
    correct_pred = _c_(577202, _a_(577196, _n_(577195, "tf", lambda: tf), "equal"), _c_(577200, _a_(577198, _n_(577197, "tf", lambda: tf), "round"), _n_(577199, "predicted", lambda: predicted)), _n_(577201, "y", lambda: y))
    _l_(577203)
    accuracy = _c_(577212, _a_(577205, _n_(577204, "tf", lambda: tf), "reduce_mean"), _c_(577211, _a_(577207, _n_(577206, "tf", lambda: tf), "cast"), _n_(577208, "correct_pred", lambda: correct_pred), _a_(577210, _n_(577209, "tf", lambda: tf), "float32")))
    _l_(577213)
    # Export the nodes 
    export_nodes = ['inputs', 'y', 'learning_rate','is_training', 'out_layer',
                    'cost', 'optimizer', 'predicted',  'accuracy'] 
    _l_(577214) 
    Graph = _c_(577217, _n_(577215, "namedtuple", lambda: namedtuple), 'Graph', _n_(577216, "export_nodes", lambda: export_nodes))
    _l_(577218)
    local_dict = _c_(577220, _n_(577219, "locals", lambda: locals))
    _l_(577221)
    graph = _c_(577226, _n_(577222, "Graph", lambda: Graph), *[_n_(577223, "local_dict", lambda: local_dict)[_n_(577224, "each", lambda: each)] for each in _n_(577225, "export_nodes", lambda: export_nodes)])
    _l_(577227)
    aux = _n_(577228, "graph", lambda: graph)
    _l_(577229)
    return aux

pred1 = _c_(577232, _n_(577231, "multilayer_perceptron", lambda: multilayer_perceptron))
_l_(577233)