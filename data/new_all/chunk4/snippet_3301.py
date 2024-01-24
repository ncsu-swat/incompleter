# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75964010/attributeerror-batchdataset-object-has-no-attribute-class-indices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
img_height= 220
_l_(623110)
img_width= 220
_l_(623111)
batch_size= 64
_l_(623112)
train_ds= _c_(623121, _a_(623116, _a_(623115, _a_(623114, _n_(623113, "tf", lambda: tf), "keras"), "preprocessing"), "image_dataset_from_directory"), _n_(623117, "train_path", lambda: train_path),
    validation_split= 0.2,
    subset='training',
    seed=123,
    image_size=(_n_(623118, "img_height", lambda: img_height),_n_(623119, "img_width", lambda: img_width)),
    batch_size= _n_(623120, "batch_size", lambda: batch_size)
)
_l_(623122)

val_ds = _c_(623131, _a_(623126, _a_(623125, _a_(623124, _n_(623123, "tf", lambda: tf), "keras"), "preprocessing"), "image_dataset_from_directory"), _n_(623127, "train_path", lambda: train_path),
    validation_split= 0.2,
    subset='validation',
    seed=123,
    image_size=(_n_(623128, "img_height", lambda: img_height),_n_(623129, "img_width", lambda: img_width)),
    batch_size= _n_(623130, "batch_size", lambda: batch_size),
    shuffle=False
)
_l_(623132)

test_ds = _c_(623141, _a_(623136, _a_(623135, _a_(623134, _n_(623133, "tf", lambda: tf), "keras"), "preprocessing"), "image_dataset_from_directory"), _n_(623137, "test_path", lambda: test_path),
    seed=123,
    image_size=(_n_(623138, "img_height", lambda: img_height),_n_(623139, "img_width", lambda: img_width)),
    batch_size= _n_(623140, "batch_size", lambda: batch_size),
    shuffle=False
)
_l_(623142)