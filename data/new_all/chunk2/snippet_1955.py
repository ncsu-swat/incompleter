# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75848999/attributeerror-module-torchvision-datasets-has-no-attribute-kinetics400
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from torchvision import datasets, transforms
    _l_(463495)

except ImportError:
    pass
try:
    from torch.utils.data import DataLoader, Dataset
    _l_(463497)

except ImportError:
    pass
try:
    import syft as sy
    _l_(463499)

except ImportError:
    pass