# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58278247/attributeerror-list-object-has-no-attribute-dim-when-predicting-in-pytorch
# coding: utf-8

# In[5]:


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import torch
    _l_(410902)

except ImportError:
    pass
try:
    import torchvision
    _l_(410904)

except ImportError:
    pass
try:
    from torchvision import transforms, datasets
    _l_(410906)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(410908)

except ImportError:
    pass
try:
    import torch.nn.functional as F
    _l_(410910)

except ImportError:
    pass
try:
    import torch.utils.data as utils
    _l_(410912)

except ImportError:
    pass
try:
    import numpy as np
    _l_(410914)

except ImportError:
    pass

data_np = _c_(410917, _a_(410916, _n_(410915, "np", lambda: np), "loadtxt"), 'input_preds.csv', delimiter=',')
_l_(410918)




train_ds = _c_(410929, _a_(410920, _n_(410919, "utils", lambda: utils), "TensorDataset"), _c_(410928, _a_(410927, _c_(410926, _a_(410922, _n_(410921, "torch", lambda: torch), "tensor"), _n_(410923, "data_np", lambda: data_np), dtype=_a_(410925, _n_(410924, "torch", lambda: torch), "float32")), "view"), -1,11))
_l_(410930)

trainset = _c_(410936, _a_(410934, _a_(410933, _a_(410932, _n_(410931, "torch", lambda: torch), "utils"), "data"), "DataLoader"), _n_(410935, "train_ds", lambda: train_ds), batch_size=1, shuffle=True)
_l_(410937)



# setting device on GPU if available, else CPU, replace .cuda() with .to(device)
device = _c_(410944, _a_(410939, _n_(410938, "torch", lambda: torch), "device"), 'cuda:0' if _c_(410943, _a_(410942, _a_(410941, _n_(410940, "torch", lambda: torch), "cuda"), "is_available")) else 'cpu')
_l_(410945)

class Net(_a_(410947, _n_(410946, "nn", lambda: nn), "Module")):
    _l_(411005)

    def __init__(self):
        _l_(410972)

        _c_(410950, _a_(410949, _n_(410948, "super", lambda: super)(), "__init__"))
        _l_(410951)
        #self.bn = nn.BatchNorm2d(11)
        _n_(410952, "self", lambda: self).fc1 = _c_(410955, _a_(410954, _n_(410953, "nn", lambda: nn), "Linear"), 11, 22)
        _l_(410956)
        _n_(410957, "self", lambda: self).fc2 = _c_(410960, _a_(410959, _n_(410958, "nn", lambda: nn), "Linear"), 22, 44)
        _l_(410961)
        _n_(410962, "self", lambda: self).fc3 = _c_(410965, _a_(410964, _n_(410963, "nn", lambda: nn), "Linear"), 44, 22)
        _l_(410966)
        _n_(410967, "self", lambda: self).fc4 = _c_(410970, _a_(410969, _n_(410968, "nn", lambda: nn), "Linear"), 22, 11)
        _l_(410971)

    def forward(self, x):
        _l_(411004)

        #x = x.view(-1, 11)
        x = _c_(410979, _a_(410974, _n_(410973, "F", lambda: F), "relu"), _c_(410978, _a_(410976, _n_(410975, "self", lambda: self), "fc1"), _n_(410977, "x", lambda: x)))
        _l_(410980)
        x = _c_(410987, _a_(410982, _n_(410981, "F", lambda: F), "relu"), _c_(410986, _a_(410984, _n_(410983, "self", lambda: self), "fc2"), _n_(410985, "x", lambda: x)))
        _l_(410988)
        x = _c_(410995, _a_(410990, _n_(410989, "F", lambda: F), "relu"), _c_(410994, _a_(410992, _n_(410991, "self", lambda: self), "fc3"), _n_(410993, "x", lambda: x)))
        _l_(410996)
        x = _c_(411000, _a_(410998, _n_(410997, "self", lambda: self), "fc4"), _n_(410999, "x", lambda: x))
        _l_(411001)
        aux = _n_(411002, "x", lambda: x)
        _l_(411003)
        #return F.log_softmax(x, dim=1)
        return aux
model1 = _c_(411008, _a_(411007, _n_(411006, "torch", lambda: torch), "load"), './1e-2')
_l_(411009)
model2 = _c_(411012, _a_(411011, _n_(411010, "torch", lambda: torch), "load"), './1e-3')
_l_(411013)

for data in _n_(411014, "trainset", lambda: trainset):
    _l_(411030)

    X = _n_(411015, "data", lambda: data)  
    _l_(411016)  
    X = _n_(411017, "X", lambda: X)
    _l_(411018)

    output = _c_(411024, _a_(411022, _c_(411021, _n_(411019, "model1", lambda: model1), _n_(411020, "X", lambda: X)), "to"), _n_(411023, "device", lambda: device))
    _l_(411025)
    _c_(411028, _n_(411026, "print", lambda: print), _n_(411027, "output", lambda: output))
    _l_(411029)