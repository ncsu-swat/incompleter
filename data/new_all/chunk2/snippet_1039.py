# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51027713/attributeerror-in-python-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy import exp, array, random, dot
    _l_(467520)

except ImportError:
    pass

class neural_network:
    _l_(467560)

    def _init_(self):
        _l_(467530)

        _c_(467523, _a_(467522, _n_(467521, "random", lambda: random), "seed"), 1)
        _l_(467524)
        _n_(467525, "self", lambda: self).weights = 2 * _c_(467528, _a_(467527, _n_(467526, "random", lambda: random), "random"), (2, 1)) - 1
        _l_(467529)

    def train(self, inputs, outputs, num):
        _l_(467552)

        for iteration in _c_(467533, _n_(467531, "range", lambda: range), _n_(467532, "num", lambda: num)):
            _l_(467551)

            output = _c_(467537, _a_(467535, _n_(467534, "self", lambda: self), "think"), _n_(467536, "inputs", lambda: inputs))
            _l_(467538)
            error = _n_(467539, "outputs", lambda: outputs) - _n_(467540, "output", lambda: output)
            _l_(467541)
            adjustment = 0.01*_c_(467546, _n_(467542, "dot", lambda: dot), _a_(467544, _n_(467543, "inputs", lambda: inputs), "T"), _n_(467545, "error", lambda: error))
            _l_(467547)
            _n_(467548, "self", lambda: self).weights += _n_(467549, "adjustment", lambda: adjustment)
            _l_(467550)

    def think(self, inputs):
        _l_(467559)

        aux = _c_(467557, _n_(467553, "dot", lambda: dot), _n_(467554, "inputs", lambda: inputs), _a_(467556, _n_(467555, "self", lambda: self), "weights"))
        _l_(467558)
        return aux



neural = _c_(467562, _n_(467561, "neural_network", lambda: neural_network))
_l_(467563)

# The training set
inputs = _c_(467565, _n_(467564, "array", lambda: array), [[2, 3], [1, 1], [5, 2], [12, 3]])
_l_(467566)
outputs = _a_(467569, _c_(467568, _n_(467567, "array", lambda: array), [[10, 4, 14, 30]]), "T")
_l_(467570)

# Training the neural network using the training set.
_c_(467575, _a_(467572, _n_(467571, "neural", lambda: neural), "train"), _n_(467573, "inputs", lambda: inputs), _n_(467574, "outputs", lambda: outputs), 10000)
_l_(467576)

# Ask the neural network the output
_c_(467583, _n_(467577, "print", lambda: print), _c_(467582, _a_(467579, _n_(467578, "neural", lambda: neural), "think"), _c_(467581, _n_(467580, "array", lambda: array), [15, 2])))
_l_(467584)