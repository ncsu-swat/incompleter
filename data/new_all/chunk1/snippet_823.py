# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76555136/torch-set-grad-enabledfalse-typeerror-bool-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import torch
    _l_(407166)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(407168)

except ImportError:
    pass
try:
    import torch.nn.functional as F
    _l_(407170)

except ImportError:
    pass
try:
    import collections
    _l_(407172)

except ImportError:
    pass
try:
    import random
    _l_(407174)

except ImportError:
    pass
try:
    import math
    _l_(407176)

except ImportError:
    pass
try:
    import numpy as np
    _l_(407178)

except ImportError:
    pass
try:
    import torch.optim as optim
    _l_(407180)

except ImportError:
    pass
try:
    from typing import Type
    _l_(407182)

except ImportError:
    pass


class CardAgent(_a_(407184, _n_(407183, "nn", lambda: nn), "Module")):
    _l_(407435)

    def __init__(self, params):
        _l_(407224)

        _c_(407187, _a_(407186, _n_(407185, "super", lambda: super)(), "__init__"))
        _l_(407188)
        _n_(407189, "self", lambda: self).first_layer = _n_(407190, "params", lambda: params)["first_layer_size"]
        _l_(407191)
        _n_(407192, "self", lambda: self).second_layer = _n_(407193, "params", lambda: params)["second_layer_size"]
        _l_(407194)
        _n_(407195, "self", lambda: self).third_layer = _n_(407196, "params", lambda: params)["third_layer_size"]
        _l_(407197)
        _n_(407198, "self", lambda: self).gamma = _n_(407199, "params", lambda: params)["gamma"]
        _l_(407200)
        _n_(407201, "self", lambda: self).learning_rate = _n_(407202, "params", lambda: params)["learning_rate"]
        _l_(407203)
        _n_(407204, "self", lambda: self).memory = _c_(407208, _a_(407206, _n_(407205, "collections", lambda: collections), "deque"), maxlen= _n_(407207, "params", lambda: params)["memory_size"])
        _l_(407209)
        _n_(407210, "self", lambda: self).batch_size = _n_(407211, "params", lambda: params)["batch_size"]
        _l_(407212)
        _n_(407213, "self", lambda: self).weights_path = _n_(407214, "params", lambda: params)["weights_path"]
        _l_(407215)
        _n_(407216, "self", lambda: self).optimizer = None
        _l_(407217)
        _n_(407218, "self", lambda: self).mask = None
        _l_(407219)
        _c_(407222, _a_(407221, _n_(407220, "self", lambda: self), "network"))
        _l_(407223)

    def network(self):
        _l_(407259)

        _n_(407225, "self", lambda: self).requires_grad_ = False
        _l_(407226)
        _n_(407227, "self", lambda: self).fc1 = _c_(407232, _a_(407229, _n_(407228, "nn", lambda: nn), "Linear"), 57, _a_(407231, _n_(407230, "self", lambda: self), "first_layer"))
        _l_(407233)
        _n_(407234, "self", lambda: self).fc2 = _c_(407241, _a_(407236, _n_(407235, "nn", lambda: nn), "Linear"), _a_(407238, _n_(407237, "self", lambda: self), "first_layer"), _a_(407240, _n_(407239, "self", lambda: self), "second_layer"))
        _l_(407242)
        _n_(407243, "self", lambda: self).fc3 = _c_(407250, _a_(407245, _n_(407244, "nn", lambda: nn), "Linear"), _a_(407247, _n_(407246, "self", lambda: self), "second_layer"), _a_(407249, _n_(407248, "self", lambda: self), "third_layer"))
        _l_(407251)
        _n_(407252, "self", lambda: self).fc4 = _c_(407257, _a_(407254, _n_(407253, "nn", lambda: nn), "Linear"), _a_(407256, _n_(407255, "self", lambda: self), "third_layer"), 60)
        _l_(407258)


    def forward(self, observation):
        _l_(407313)

        x = _c_(407266, _a_(407261, _n_(407260, "F", lambda: F), "relu"), _c_(407265, _a_(407263, _n_(407262, "self", lambda: self), "fc1"), _n_(407264, "observation", lambda: observation)))
        _l_(407267)
        x = _c_(407274, _a_(407269, _n_(407268, "F", lambda: F), "relu"), _c_(407273, _a_(407271, _n_(407270, "self", lambda: self), "fc2"), _n_(407272, "x", lambda: x)))
        _l_(407275)
        x = _c_(407282, _a_(407277, _n_(407276, "F", lambda: F), "relu"), _c_(407281, _a_(407279, _n_(407278, "self", lambda: self), "fc3"), _n_(407280, "x", lambda: x)))
        _l_(407283)
        x = _c_(407290, _a_(407285, _n_(407284, "F", lambda: F), "relu"), _c_(407289, _a_(407287, _n_(407286, "self", lambda: self), "fc4"), _n_(407288, "x", lambda: x)))
        _l_(407291)
        x = _c_(407298, _a_(407293, _n_(407292, "F", lambda: F), "softmax"), _c_(407297, _a_(407295, _n_(407294, "self", lambda: self), "fc4"), _n_(407296, "x", lambda: x)), dim=-1)
        _l_(407299)

        if _a_(407301, _n_(407300, "self", lambda: self), "mask") is not None:
            _l_(407310)

            _c_(407304, _n_(407302, "print", lambda: print), _n_(407303, "x", lambda: x))
            _l_(407305)
            aux = _n_(407306, "x", lambda: x) * _a_(407308, _n_(407307, "self", lambda: self), "mask")
            _l_(407309)
            return aux
        aux = _n_(407311, "x", lambda: x)
        _l_(407312)
        return aux

    def remember(self, observation, move, reward, next_state, complete):
        _l_(407324)

        _c_(407322, _a_(407316, _a_(407315, _n_(407314, "self", lambda: self), "memory"), "append"), (_n_(407317, "observation", lambda: observation), _n_(407318, "move", lambda: move), _n_(407319, "reward", lambda: reward), _n_(407320, "next_state", lambda: next_state), _n_(407321, "complete", lambda: complete)))
        _l_(407323)

    def train_memory(self, observation, move, reward, next_state, complete):
        _l_(407404)

        _c_(407327, _a_(407326, _n_(407325, "self", lambda: self), "train"))
        _l_(407328)
        _n_(407329, "torch", lambda: torch).set_grad_enabled = True
        _l_(407330)

        state_tensor = _c_(407339, _a_(407332, _n_(407331, "torch", lambda: torch), "tensor"), _c_(407336, _a_(407334, _n_(407333, "np", lambda: np), "expand_dims"), _n_(407335, "observation", lambda: observation), 0), dtype=_a_(407338, _n_(407337, "torch", lambda: torch), "float32"), requires_grad=True)
        _l_(407340)
        next_state_tensor = _c_(407349, _a_(407342, _n_(407341, "torch", lambda: torch), "tensor"), _c_(407346, _a_(407344, _n_(407343, "np", lambda: np), "expand_dims"), _n_(407345, "observation", lambda: observation), 0), dtype=_a_(407348, _n_(407347, "torch", lambda: torch), "float32"), requires_grad = True)
        _l_(407350)

        if not _n_(407351, "complete", lambda: complete):
            _l_(407363)

            target = _n_(407352, "reward", lambda: reward) + _a_(407354, _n_(407353, "self", lambda: self), "gamma") * _c_(407361, _a_(407356, _n_(407355, "torch", lambda: torch), "max"), _c_(407360, _a_(407358, _n_(407357, "self", lambda: self), "forward"), _n_(407359, "next_state_tensor", lambda: next_state_tensor)[0]))
            _l_(407362)

        output = _c_(407367, _a_(407365, _n_(407364, "self", lambda: self), "forward"), _n_(407366, "state_tensor", lambda: state_tensor))
        _l_(407368)
        target_f = _c_(407371, _a_(407370, _n_(407369, "output", lambda: output), "clone"))
        _l_(407372)
        _n_(407373, "target_f", lambda: target_f)[0][_c_(407377, _a_(407375, _n_(407374, "np", lambda: np), "argmax"), _n_(407376, "move", lambda: move))] = _n_(407378, "target", lambda: target)
        _l_(407379)
        _c_(407382, _a_(407381, _n_(407380, "target_f", lambda: target_f), "detach"))
        _l_(407383)
        _c_(407387, _a_(407386, _a_(407385, _n_(407384, "self", lambda: self), "optimizer"), "zero_grad"))
        _l_(407388)
        loss = _c_(407393, _a_(407390, _n_(407389, "F", lambda: F), "mse_loss"), _n_(407391, "output", lambda: output), _n_(407392, "target_f", lambda: target_f))
        _l_(407394)
        _c_(407397, _a_(407396, _n_(407395, "loss", lambda: loss), "backward"))
        _l_(407398)
        _c_(407402, _a_(407401, _a_(407400, _n_(407399, "self", lambda: self), "optimizer"), "step"))
        _l_(407403)

    def replay_exp(self):
        _l_(407434)

        if _c_(407408, _n_(407405, "len", lambda: len), _a_(407407, _n_(407406, "self", lambda: self), "memory")) > _a_(407410, _n_(407409, "self", lambda: self), "batch_size"):
            _l_(407422)

            minibatch = _c_(407417, _a_(407412, _n_(407411, "random", lambda: random), "sample"), _a_(407414, _n_(407413, "self", lambda: self), "memory"), _a_(407416, _n_(407415, "self", lambda: self), "batch_size"))
            _l_(407418)
        else:
            minibatch = _a_(407420, _n_(407419, "self", lambda: self), "memory")
            _l_(407421)

        for observation, move, reward, next_state, complete in _n_(407423, "minibatch", lambda: minibatch):
            _l_(407433)

            _c_(407431, _a_(407425, _n_(407424, "self", lambda: self), "train_memory"), _n_(407426, "observation", lambda: observation), _n_(407427, "move", lambda: move), _n_(407428, "reward", lambda: reward), _n_(407429, "next_state", lambda: next_state), _n_(407430, "complete", lambda: complete))
            _l_(407432)