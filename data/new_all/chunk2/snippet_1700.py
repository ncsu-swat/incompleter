# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62343793/attributeerror-classificadorfinal-object-has-no-attribute-log-softmax-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import torch.nn as nn
    _l_(422313)

except ImportError:
    pass
try:
    from skorch import NeuralNetClassifier
    _l_(422315)

except ImportError:
    pass
try:
    from sklearn.model_selection import cross_val_score,GridSearchCV
    _l_(422317)

except ImportError:
    pass
try:
    from sklearn.preprocessing import LabelEncoder, MinMaxScaler
    _l_(422319)

except ImportError:
    pass
try:
    import torch
    _l_(422321)

except ImportError:
    pass
try:
    import torch.nn.functional as F
    _l_(422323)

except ImportError:
    pass
try:
    from torch import nn,optim
    _l_(422325)

except ImportError:
    pass

class classificadorFinal(_a_(422327, _n_(422326, "nn", lambda: nn), "Module")):
    _l_(422420)

    def __init__(self, activation=_a_(422329, _n_(422328, "F", lambda: F), "tanh"), neurons=16, initializer=_a_(422333, _a_(422332, _a_(422331, _n_(422330, "torch", lambda: torch), "nn"), "init"), "uniform_"), dropout=0.3):
        _l_(422381)

        ##from melhores_parametros
        _c_(422336, _a_(422335, _n_(422334, "super", lambda: super)(), "__init__"))
        _l_(422337)
        _n_(422338, "self", lambda: self).dense0 = _c_(422342, _a_(422340, _n_(422339, "nn", lambda: nn), "Linear"), 4, _n_(422341, "neurons", lambda: neurons))
        _l_(422343)
        _c_(422348, _n_(422344, "initializer", lambda: initializer), _a_(422347, _a_(422346, _n_(422345, "self", lambda: self), "dense0"), "weight"))
        _l_(422349)
        _n_(422350, "self", lambda: self).activation0 = _n_(422351, "activation", lambda: activation)
        _l_(422352)
        _n_(422353, "self", lambda: self).dense1 = _c_(422358, _a_(422355, _n_(422354, "nn", lambda: nn), "Linear"), _n_(422356, "neurons", lambda: neurons), _n_(422357, "neurons", lambda: neurons))
        _l_(422359)
        _c_(422364, _n_(422360, "initializer", lambda: initializer), _a_(422363, _a_(422362, _n_(422361, "self", lambda: self), "dense1"), "weight"))
        _l_(422365)
        _n_(422366, "self", lambda: self).activation1 = _n_(422367, "activation", lambda: activation)
        _l_(422368)
        _n_(422369, "self", lambda: self).dense2 = _c_(422373, _a_(422371, _n_(422370, "nn", lambda: nn), "Linear"), _n_(422372, "neurons", lambda: neurons), 3)
        _l_(422374)

        _n_(422375, "self", lambda: self).dropout = _c_(422379, _a_(422377, _n_(422376, "nn", lambda: nn), "Dropout"), _n_(422378, "dropout", lambda: dropout))
        _l_(422380)

    def forward(self, X):
        _l_(422419)

        X = _c_(422385, _a_(422383, _n_(422382, "self", lambda: self), "dense0"), _n_(422384, "X", lambda: X))
        _l_(422386)
        X = _c_(422390, _a_(422388, _n_(422387, "self", lambda: self), "activation0"), _n_(422389, "X", lambda: X))
        _l_(422391)
        X = _c_(422395, _a_(422393, _n_(422392, "self", lambda: self), "dropout"), _n_(422394, "X", lambda: X))
        _l_(422396)
        X = _c_(422400, _a_(422398, _n_(422397, "self", lambda: self), "dense1"), _n_(422399, "X", lambda: X))
        _l_(422401)
        X = _c_(422405, _a_(422403, _n_(422402, "self", lambda: self), "activation1"), _n_(422404, "X", lambda: X))
        _l_(422406)
        X = _c_(422410, _a_(422408, _n_(422407, "self", lambda: self), "dropout"), _n_(422409, "X", lambda: X))
        _l_(422411)
        X = _c_(422415, _a_(422413, _n_(422412, "self", lambda: self), "dense2"), _n_(422414, "X", lambda: X))
        _l_(422416)
        aux = _n_(422417, "X", lambda: X)
        _l_(422418)
        return aux


criterion = _c_(422423, _a_(422422, _n_(422421, "nn", lambda: nn), "CrossEntropyLoss"))
_l_(422424)
optimizer = _c_(422430, _a_(422426, _n_(422425, "optim", lambda: optim), "Adam"), _c_(422429, _a_(422428, _n_(422427, "classificador", lambda: classificador), "parameters")), lr = 0.001, weight_decay = 0.0001)
_l_(422431)


#treino
for epoch in _c_(422433, _n_(422432, "range", lambda: range), 200):
    _l_(422504)


    running_loss = 0.
    _l_(422434)
    running_accuracy = 0.
    _l_(422435)

    for data in _n_(422436, "train_loader", lambda: train_loader):
        _l_(422489)

        inputs, labels = _n_(422437, "data", lambda: data)
        _l_(422438)

        _c_(422441, _a_(422440, _n_(422439, "optimizer", lambda: optimizer), "zero_grad"))        
        _l_(422442)        

        outputs = _c_(422445, _n_(422443, "classificadorFinal", lambda: classificadorFinal), _n_(422444, "inputs", lambda: inputs))
        _l_(422446)

        loss = _c_(422450, _n_(422447, "criterion", lambda: criterion), _n_(422448, "outputs", lambda: outputs), _n_(422449, "labels", lambda: labels))###erro
        _l_(422451)###erro
        _c_(422454, _a_(422453, _n_(422452, "loss", lambda: loss), "backward"))
        _l_(422455)

        _c_(422458, _a_(422457, _n_(422456, "optimizer", lambda: optimizer), "step"))
        _l_(422459)

        running_loss += _c_(422462, _a_(422461, _n_(422460, "loss", lambda: loss), "item"))
        _l_(422463)

        ps = _c_(422467, _a_(422465, _n_(422464, "F", lambda: F), "softmax"), _n_(422466, "outputs", lambda: outputs))
        _l_(422468)

        top_p, top_class = _c_(422471, _a_(422470, _n_(422469, "ps", lambda: ps), "topk"), k = 1, dim = 1)
        _l_(422472)

        equals = _n_(422473, "top_class", lambda: top_class) == _c_(422478, _a_(422475, _n_(422474, "labels", lambda: labels), "view"), *_a_(422477, _n_(422476, "top_class", lambda: top_class), "shape"))
        _l_(422479)

        running_accuracy += _c_(422487, _a_(422481, _n_(422480, "torch", lambda: torch), "mean"), _c_(422486, _a_(422483, _n_(422482, "equals", lambda: equals), "type"), _a_(422485, _n_(422484, "torch", lambda: torch), "float")))
        _l_(422488)

    _c_(422502, _n_(422490, "print", lambda: print), _c_(422501, _a_(422491, 'Época {:3d}: perda {:3.5f} - precisão {:3.5f}', "format"), _n_(422492, "epoch", lambda: epoch) + 1, _n_(422493, "running_loss", lambda: running_loss)/_c_(422496, _n_(422494, "len", lambda: len), _n_(422495, "train_loader", lambda: train_loader)), _n_(422497, "running_accuracy", lambda: running_accuracy)/_c_(422500, _n_(422498, "len", lambda: len), _n_(422499, "train_loader", lambda: train_loader))))
    _l_(422503)