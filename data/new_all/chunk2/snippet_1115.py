# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53693999/torch-utils-data-dataloader-outputs-typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import torch
    _l_(447892)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(447894)

except ImportError:
    pass
try:
    import torch.nn.functional as F
    _l_(447896)

except ImportError:
    pass
try:
    import torch.optim as optom
    _l_(447898)

except ImportError:
    pass
try:
    from torchvision import datasets, transforms
    _l_(447900)

except ImportError:
    pass
try:
    from torch.autograd import Variable
    _l_(447902)

except ImportError:
    pass
kwargs={}
_l_(447903)
train=_c_(447921, _a_(447907, _a_(447906, _a_(447905, _n_(447904, "torch", lambda: torch), "utils"), "data"), "dataloader"), _c_(447919, _a_(447909, _n_(447908, "datasets", lambda: datasets), "MNIST"), "mnist",train=True,download=True,transform=_c_(447918, _a_(447911, _n_(447910, "transforms", lambda: transforms), "Compose"), [_c_(447914, _a_(447913, _n_(447912, "transforms", lambda: transforms), "ToTensor")),_c_(447917, _a_(447916, _n_(447915, "transforms", lambda: transforms), "Normalize"), (0.1307),(0.3081,) )] ) ),batch_size=64, shuffle=True, **_n_(447920, "kwargs", lambda: kwargs))
_l_(447922)