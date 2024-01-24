# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51126531/resizing-to-bigger-resolution-with-skimage-causes-shape-typeerror-in-keras
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for inputs_batch  in _n_(475507, "train_generator", lambda: train_generator):
    _l_(475526)

    features_batch = _c_(475511, _a_(475509, _n_(475508, "vgg_conv", lambda: vgg_conv), "predict"), _n_(475510, "inputs_batch", lambda: inputs_batch))
    _l_(475512)
    _n_(475513, "train_features", lambda: train_features)[_n_(475514, "i", lambda: i) * _n_(475515, "batch_size", lambda: batch_size) : (_n_(475516, "i", lambda: i) + 1) * _n_(475517, "batch_size", lambda: batch_size)] = _n_(475518, "features_batch", lambda: features_batch) 
    _l_(475519) 
    i += 1
    _l_(475520)
    if _n_(475521, "i", lambda: i) * _n_(475522, "batch_size", lambda: batch_size) >= _n_(475523, "nImages", lambda: nImages):
        _l_(475525)

        break
        _l_(475524)