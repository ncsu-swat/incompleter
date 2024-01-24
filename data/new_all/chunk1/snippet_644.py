# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75939176/default-collate-typeerror-batch-must-contain-tensors-numbers-dicts-or-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pathlib import Path
    _l_(408406)

except ImportError:
    pass
try:
    from typing import List
    _l_(408408)

except ImportError:
    pass
try:
    import torch
    _l_(408410)

except ImportError:
    pass
try:
    from torch.utils.data import Dataset
    _l_(408412)

except ImportError:
    pass
try:
    from torchvision.io import read_image
    _l_(408414)

except ImportError:
    pass


class ApplicationDataset(_n_(408415, "Dataset", lambda: Dataset)):
    _l_(408475)

    def __init__(self, slide_ids: _n_(408416, "List", lambda: List)[_n_(408417, "str", lambda: str)], tile_filenames: _n_(408418, "List", lambda: List)[_n_(408419, "Path", lambda: Path)]):
        _l_(408426)

        _n_(408420, "self", lambda: self).slide_ids = _n_(408421, "slide_ids", lambda: slide_ids)
        _l_(408422)
        _n_(408423, "self", lambda: self).tile_filenames = _n_(408424, "tile_filenames", lambda: tile_filenames)
        _l_(408425)

    def __len__(self):
        _l_(408432)

        aux = _c_(408430, _n_(408427, "len", lambda: len), _a_(408429, _n_(408428, "self", lambda: self), "tile_filenames"))
        _l_(408431)
        return aux

    def __getitem__(self, idx):
        _l_(408449)

        image = _c_(408439, _n_(408433, "read_image", lambda: read_image), _c_(408438, _n_(408434, "str", lambda: str), _a_(408436, _n_(408435, "self", lambda: self), "tile_filenames")[_n_(408437, "idx", lambda: idx)]))
        _l_(408440)
        aux = {
            'image': _n_(408441, "image", lambda: image),
            'slide_id': _a_(408443, _n_(408442, "self", lambda: self), "slide_ids")[_n_(408444, "idx", lambda: idx)],
            'filename': _a_(408446, _n_(408445, "self", lambda: self), "tile_filenames")[_n_(408447, "idx", lambda: idx)],
        }
        _l_(408448)
        return aux

    @_n_(408450, "staticmethod", lambda: staticmethod)
    def collate(batch):
        _l_(408474)

        images = [_n_(408451, "batch_item", lambda: batch_item)['image'] for batch_item in _n_(408452, "batch", lambda: batch)]
        _l_(408453)

        images = _c_(408457, _a_(408455, _n_(408454, "torch", lambda: torch), "stack"), _n_(408456, "images", lambda: images), dim=0)
        _l_(408458)
        slide_ids = _c_(408463, _a_(408460, _n_(408459, "torch", lambda: torch), "tensor"), [_n_(408461, "batch_item", lambda: batch_item)['slide_id'] for batch_item in _n_(408462, "batch", lambda: batch)])
        _l_(408464)
        filenames = [_c_(408467, _n_(408465, "str", lambda: str), _n_(408466, "batch_item", lambda: batch_item)['filename']) for batch_item in _n_(408468, "batch", lambda: batch)]
        _l_(408469)
        aux = _n_(408470, "images", lambda: images), _n_(408471, "slide_ids", lambda: slide_ids), _n_(408472, "filenames", lambda: filenames)
        _l_(408473)

        return aux