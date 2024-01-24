# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58203138/typeerror-flow-from-directory-got-an-unexpected-keyword-argument-train-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_datagenerator = _c_(548543, _n_(548542, "ImageDataGenerator", lambda: ImageDataGenerator), rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2)
_l_(548544)
train_generator = _c_(548550, _a_(548546, _n_(548545, "train_datagenerator", lambda: train_datagenerator), "flow_from_directory"), train_data_dir = '.\\Images\\data',
    target_size=(_n_(548547, "image_size", lambda: image_size), _n_(548548, "image_size", lambda: image_size)), 
    batch_size=_n_(548549, "BATCH_SIZE_TRAINING", lambda: BATCH_SIZE_TRAINING),
    class_mode='categorical', subset='training') 
_l_(548551) 
validation_generator = _c_(548557, _a_(548553, _n_(548552, "train_datagenerator", lambda: train_datagenerator), "flow_from_directory"), train_data_dir = '.\\Images\\data', 
    target_size=(_n_(548554, "image_size", lambda: image_size), _n_(548555, "image_size", lambda: image_size)), 
    batch_size=_n_(548556, "BATCH_SIZE_TRAINING", lambda: BATCH_SIZE_TRAINING),
    class_mode='categorical', subset='validation')
_l_(548558)