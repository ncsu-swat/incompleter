# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63828775/attributeerror-directoryiterator-object-has-no-attribute-map
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
datagen = _c_(403267, _a_(403266, _a_(403265, _a_(403264, _a_(403263, _n_(403262, "tf", lambda: tf), "keras"), "preprocessing"), "image"), "ImageDataGenerator"), vertical_flip=True)
_l_(403268)
training_set = _c_(403271, _a_(403270, _n_(403269, "datagen", lambda: datagen), "flow_from_directory"), '/home/train/',target_size=(224, 224), batch_size = 2)
_l_(403272)

train_dataset = _c_(403280, _a_(403274, _n_(403273, "training_set", lambda: training_set), "map"), _n_(403275, "gaussian_filter", lambda: gaussian_filter), num_parallel_calls=_a_(403279, _a_(403278, _a_(403277, _n_(403276, "tf", lambda: tf), "data"), "experimental"), "AUTOTUNE"))
_l_(403281)