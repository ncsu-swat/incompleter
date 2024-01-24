# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61036421/keras-shape-typeerror-tuple-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_datagen = _c_(672667, _n_(672666, "ImageDataGenerator", lambda: ImageDataGenerator), rescale=1./255,
        validation_split=0.2) # set validation split
_l_(672668) # set validation split

train_generator = _c_(672671, _a_(672670, _n_(672669, "train_datagen", lambda: train_datagen), "flow_from_directory"), directory=r"path_to_the_train_dir",
    target_size=(128, 128),
    class_mode="binary",
    shuffle=True,
    seed=42,
    subset='training' # set as training data
)
_l_(672672)

validation_generator = _c_(672675, _a_(672674, _n_(672673, "train_datagen", lambda: train_datagen), "flow_from_directory"), directory=r"path_to_the_train_dir", # same directory as training data
    target_size=(128, 128),
    class_mode='binary',
    subset='validation') # set as validation data
_l_(672676) # set as validation data