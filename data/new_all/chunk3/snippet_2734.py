# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64895320/attributeerror-shuffledataset-object-has-no-attribute-features
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow_datasets as tfds
    _l_(538291)

except ImportError:
    pass
ds, ds_info = _c_(538294, _a_(538293, _n_(538292, "tfds", lambda: tfds), "load"), 'eurosat/rgb:2.0.0',
                    with_info=True,
                    split='train',
                    data_dir='../input/eurosat',
                    download=False)
_l_(538295)
ds = _c_(538298, _a_(538297, _n_(538296, "ds", lambda: ds), "shuffle"), 1024)
_l_(538299)
_c_(538304, _a_(538301, _n_(538300, "tfds", lambda: tfds), "show_examples"), _n_(538302, "ds", lambda: ds), _n_(538303, "ds_info", lambda: ds_info));
_l_(538305)