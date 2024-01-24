# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72627697/timm-typeerror-builtin-function-or-method-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(442933)

except ImportError:
    pass
try:
    import torch
    _l_(442935)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(442937)

except ImportError:
    pass
try:
    from timm.data.transforms_factory import create_transform
    _l_(442939)

except ImportError:
    pass
a = _c_(442941, _n_(442940, "create_transform", lambda: create_transform), 224, is_training=True)
_l_(442942)
_c_(442945, _n_(442943, "print", lambda: print), _n_(442944, "a", lambda: a))
_l_(442946)
pets_image_paths = './download.png'
_l_(442947)
image = _c_(442951, _a_(442949, _n_(442948, "Image", lambda: Image), "open"), _n_(442950, "pets_image_paths", lambda: pets_image_paths))
_l_(442952)
# We can convert this into a tensor, and transpose the channels into the format that PyTorch expects:
np_image = _c_(442958, _a_(442954, _n_(442953, "np", lambda: np), "array"), _n_(442955, "image", lambda: image), dtype=_a_(442957, _n_(442956, "np", lambda: np), "float32"))
_l_(442959)
image = _c_(442965, _a_(442964, _c_(442963, _a_(442961, _n_(442960, "torch", lambda: torch), "as_tensor"), _n_(442962, "np_image", lambda: np_image)), "transpose"), 2, 0)[None]
_l_(442966)
try:
    from timm.data.transforms import RandomResizedCropAndInterpolation
    _l_(442968)

except ImportError:
    pass
tfm = _c_(442970, _n_(442969, "RandomResizedCropAndInterpolation", lambda: RandomResizedCropAndInterpolation), size=350, interpolation='random')
_l_(442971)
try:
    import matplotlib.pyplot as plt
    _l_(442973)

except ImportError:
    pass
fig, ax = _c_(442976, _a_(442975, _n_(442974, "plt", lambda: plt), "subplots"), 2, 4, figsize=(10, 5))
_l_(442977)
for idx, im in _c_(442984, _n_(442978, "enumerate", lambda: enumerate), [_c_(442981, _n_(442979, "tfm", lambda: tfm), _n_(442980, "image", lambda: image)) for i in _c_(442983, _n_(442982, "range", lambda: range), 4)]):
    _l_(442991)

    _c_(442989, _a_(442987, _n_(442985, "ax", lambda: ax)[0, _n_(442986, "idx", lambda: idx)], "imshow"), _n_(442988, "im", lambda: im))
    _l_(442990)
for idx, im in _c_(442998, _n_(442992, "enumerate", lambda: enumerate), [_c_(442995, _n_(442993, "tfm", lambda: tfm), _n_(442994, "image", lambda: image)) for i in _c_(442997, _n_(442996, "range", lambda: range), 4)]):
    _l_(443005)

    _c_(443003, _a_(443001, _n_(442999, "ax", lambda: ax)[1, _n_(443000, "idx", lambda: idx)], "imshow"), _n_(443002, "im", lambda: im))
    _l_(443004)
_c_(443008, _a_(443007, _n_(443006, "fig", lambda: fig), "tight_layout"))
_l_(443009)
_c_(443012, _a_(443011, _n_(443010, "plt", lambda: plt), "show"))
_l_(443013)