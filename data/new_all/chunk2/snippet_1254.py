# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62783857/pytorch-typeerror-totensor-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from torchvision import datasets
    _l_(449035)

except ImportError:
    pass
try:
    import torch.utils.data
    _l_(449037)

except ImportError:
    pass
try:
    from torch.utils.data import DataLoader
    _l_(449039)

except ImportError:
    pass
try:
    from torchvision import transforms
    _l_(449041)

except ImportError:
    pass
try:
    from dataset2 import CellsDataset
    _l_(449043)

except ImportError:
    pass
try:
    from torchvision import datasets
    _l_(449045)

except ImportError:
    pass
try:
    import torch
    _l_(449047)

except ImportError:
    pass
try:
    import torchvision
    _l_(449049)

except ImportError:
    pass
try:
    import torchvision.transforms as transforms
    _l_(449051)

except ImportError:
    pass


class ImageFolderWithPaths(_a_(449053, _n_(449052, "datasets", lambda: datasets), "ImageFolder")):
    _l_(449054)

    """Custom dataset that includes image file paths. Extends
    torchvision.datasets.ImageFolder
    """

# override the __getitem__ method. this is the method that dataloader calls
def __getitem__(self, index):
    _l_(449071)

    # this is what ImageFolder normally returns 
    original_tuple = _c_(449060, _a_(449058, _n_(449055, "super", lambda: super)(_n_(449056, "ImageFolderWithPaths", lambda: ImageFolderWithPaths), _n_(449057, "self", lambda: self)), "__getitem__"), _n_(449059, "index", lambda: index))
    _l_(449061)
    # the image file path
    path = _a_(449063, _n_(449062, "self", lambda: self), "imgs")[_n_(449064, "index", lambda: index)][0]
    _l_(449065)
    # make a new tuple that includes original and the path
    tuple_with_path = (_n_(449066, "original_tuple", lambda: original_tuple) + (_n_(449067, "path", lambda: path),))
    _l_(449068)
    aux = _n_(449069, "tuple_with_path", lambda: tuple_with_path)
    _l_(449070)
    return aux

# EXAMPLE USAGE:
# instantiate the dataset and dataloader
data_dir = "/Users/nubstech/Documents/GitHub/CellCountingDirectCount/Eddata/"
_l_(449072)
dataset = _c_(449075, _n_(449073, "ImageFolderWithPaths", lambda: ImageFolderWithPaths), _n_(449074, "data_dir", lambda: data_dir)) # our custom dataset
_l_(449076) # our custom dataset
#dataloader = DataLoader(dataset)
transform = _c_(449082, _a_(449078, _n_(449077, "transforms", lambda: transforms), "Compose"), [
    # you can add other transformations in this list
    _c_(449081, _a_(449080, _n_(449079, "transforms", lambda: transforms), "ToTensor"))
])
_l_(449083)
dataset = _c_(449092, _n_(449084, "DataLoader", lambda: DataLoader), _n_(449085, "data_dir", lambda: data_dir), _c_(449091, _a_(449087, _n_(449086, "transforms", lambda: transforms), "Compose"), _c_(449090, _a_(449089, _n_(449088, "transforms", lambda: transforms), "ToTensor"))))
_l_(449093)
dataloader = _c_(449097, _a_(449095, _a_(449094, torch, "utils"), "DataLoader"), _n_(449096, "dataset", lambda: dataset))
_l_(449098)

# iterate over data
for inputs, labels, paths in _n_(449099, "dataloader", lambda: dataloader):
    _l_(449106)

     # use the above variables freely
    _c_(449104, _n_(449100, "print", lambda: print), _n_(449101, "inputs", lambda: inputs), _n_(449102, "labels", lambda: labels), _n_(449103, "paths", lambda: paths))
    _l_(449105)