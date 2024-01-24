# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56865740/hyperparameter-optimization-using-kerasclassifier-randomizedsearchcv-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def neural_network(num_neurons=64,num_layers=4,input_dim=8,
                   output_dim=2,learning_rate=1.0e-05,act='relu',
                   dropout=0.3):
    _l_(388393)

    model = _c_(388345, _n_(388344, "Sequential", lambda: Sequential))
    _l_(388346)

    _c_(388353, _a_(388348, _n_(388347, "model", lambda: model), "add"), _c_(388352, _n_(388349, "Dense", lambda: Dense), _n_(388350, "num_neurons", lambda: num_neurons),activation='relu',input_dim=_n_(388351, "input_dim", lambda: input_dim)))
    _l_(388354)

    for i in _c_(388357, _n_(388355, "range", lambda: range), 1,_n_(388356, "num_layers", lambda: num_layers)):
        _l_(388366)

        _c_(388364, _a_(388359, _n_(388358, "model", lambda: model), "add"), _c_(388363, _n_(388360, "Dense", lambda: Dense), _n_(388361, "num_neurons", lambda: num_neurons),activation=_n_(388362, "act", lambda: act)))
        _l_(388365)

    _c_(388372, _a_(388368, _n_(388367, "model", lambda: model), "add"), _c_(388371, _n_(388369, "Dropout", lambda: Dropout), _n_(388370, "dropout", lambda: dropout)))
    _l_(388373)

    _c_(388379, _a_(388375, _n_(388374, "model", lambda: model), "add"), _c_(388378, _n_(388376, "Dense", lambda: Dense), _n_(388377, "output_dim", lambda: output_dim),activation='softmax'))
    _l_(388380)

    adam = _c_(388384, _a_(388382, _n_(388381, "optimizers", lambda: optimizers), "Adam"), lr=_n_(388383, "learning_rate", lambda: learning_rate))
    _l_(388385)

    _c_(388389, _a_(388387, _n_(388386, "model", lambda: model), "compile"), _n_(388388, "adam", lambda: adam),
                  loss='categorical_crossentropy',
                  metrics=['accuracy']
                 )
    _l_(388390)
    aux = _n_(388391, "model", lambda: model)
    _l_(388392)
    return aux
create_model = _n_(388394, "neural_network", lambda: neural_network)
_l_(388395)
model = _c_(388398, _n_(388396, "KerasClassifier", lambda: KerasClassifier), build_fn=_n_(388397, "create_model", lambda: create_model),verbose=0)
_l_(388399)
batch_size = [16,32,64]
_l_(388400)
epochs = [200,300,500]
_l_(388401)
num_neurons = [64,128,256]
_l_(388402)
num_layers= [2,4,6]
_l_(388403)
learning_rate = [0.001, 0.01, 0.1, 0.2, 0.3]
_l_(388404)
dropout = [0.1,0.3,0.5]
_l_(388405)
param_grid = _c_(388413, _n_(388406, "dict", lambda: dict), batch_size=_n_(388407, "batch_size", lambda: batch_size),epochs=_n_(388408, "epochs", lambda: epochs),
                      num_neurons=_n_(388409, "num_neurons", lambda: num_neurons),
                      num_layers=_n_(388410, "num_layers", lambda: num_layers),
                      learning_rate=_n_(388411, "learning_rate", lambda: learning_rate),
                      dropout=_n_(388412, "dropout", lambda: dropout)
                     )
_l_(388414)
grid = _c_(388418, _n_(388415, "RandomizedSearchCV", lambda: RandomizedSearchCV), estimator=_n_(388416, "model", lambda: model),param_distributions=_n_(388417, "param_grid", lambda: param_grid),cv=3,n_iter=3)
_l_(388419)
grid_result = _c_(388426, _a_(388421, _n_(388420, "grid", lambda: grid), "fit"), _n_(388422, "x", lambda: x),_n_(388423, "y", lambda: y),epochs=_n_(388424, "epochs", lambda: epochs),batch_size=_n_(388425, "batch_size", lambda: batch_size))
_l_(388427)