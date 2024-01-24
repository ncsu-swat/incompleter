# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59946463/attributeerror-str-object-has-no-attribute-flow-from-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy
    _l_(523035)

except ImportError:
    pass
try:
    import numpy as np
    _l_(523037)

except ImportError:
    pass
try:
    from sklearn.linear_model import LogisticRegression
    _l_(523039)

except ImportError:
    pass
try:
    from tensorflow import keras, metrics
    _l_(523041)

except ImportError:
    pass
try:
    from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
    _l_(523043)

except ImportError:
    pass
try:
    from tensorflow.keras.optimizers import Adam
    _l_(523045)

except ImportError:
    pass
try:
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    _l_(523047)

except ImportError:
    pass
try:
    from tensorflow.keras.models import Model
    _l_(523049)

except ImportError:
    pass
try:
    from sklearn.metrics import confusion_matrix
    _l_(523051)

except ImportError:
    pass
try:
    import itertools
    _l_(523053)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(523055)

except ImportError:
    pass
try:
    from webencodings import labels
    _l_(523057)

except ImportError:
    pass
try:
    from PIL import ImageFile
    _l_(523059)

except ImportError:
    pass

_n_(523060, "ImageFile", lambda: ImageFile).LOAD_TRUNCATED_IMAGES = True
_l_(523061)

train_path=r'C:\Users\Acer\imagerec\BAYBAYIN\TRAIN'
_l_(523062)
valid_path=r'C:\Users\Acer\imagerec\BAYBAYIN\VAL'
_l_(523063)
test_path=r'C:\Users\Acer\imagerec\BAYBAYIN\TEST'
_l_(523064)
batch_size=30
_l_(523065)

class_labels=['A', 'BA', 'KA', 'GA', 'HA', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '31', '32',
              '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44']
_l_(523066)

train_batches=_c_(523076, _a_(523073, _c_(523072, _n_(523067, "ImageDataGenerator", lambda: ImageDataGenerator), preprocessing_function=_a_(523071, _a_(523070, _a_(523069, _n_(523068, "keras", lambda: keras), "applications"), "xception"), "preprocess_input")), "flow_from_directory"), _n_(523074, "train_path", lambda: train_path), target_size=(299,299),classes=_n_(523075, "class_labels", lambda: class_labels),batch_size=5)
_l_(523077)
valid_batches=_c_(523087, _a_(523084, _c_(523083, _n_(523078, "ImageDataGenerator", lambda: ImageDataGenerator), preprocessing_function=_a_(523082, _a_(523081, _a_(523080, _n_(523079, "keras", lambda: keras), "applications"), "xception"), "preprocess_input")), "flow_from_directory"), _n_(523085, "valid_path", lambda: valid_path), target_size=(299,299),classes=_n_(523086, "class_labels", lambda: class_labels),batch_size=5)
_l_(523088)
test_batches=_c_(523098, _a_(523095, _c_(523094, _n_(523089, "ImageDataGenerator", lambda: ImageDataGenerator), preprocessing_function=_a_(523093, _a_(523092, _a_(523091, _n_(523090, "keras", lambda: keras), "applications"), "xception"), "preprocess_input")), "flow_from_directory"), _n_(523096, "test_path", lambda: test_path), target_size=(299,299),classes=_n_(523097, "class_labels", lambda: class_labels),batch_size=5, shuffle=False)
_l_(523099)

base_model=_c_(523104, _a_(523103, _a_(523102, _a_(523101, _n_(523100, "keras", lambda: keras), "applications"), "vgg19"), "VGG19"), include_top=False)
_l_(523105)

x=_a_(523107, _n_(523106, "base_model", lambda: base_model), "output")
_l_(523108)
x=_c_(523112, _c_(523110, _n_(523109, "GlobalAveragePooling2D", lambda: GlobalAveragePooling2D)), _n_(523111, "x", lambda: x))
_l_(523113)
x=_c_(523117, _c_(523115, _n_(523114, "Dense", lambda: Dense), 1024, activation='relu'), _n_(523116, "x", lambda: x))
_l_(523118)
x=_c_(523122, _c_(523120, _n_(523119, "Dense", lambda: Dense), 48, activation='softmax'), _n_(523121, "x", lambda: x))
_l_(523123)
model=_c_(523128, _n_(523124, "Model", lambda: Model), inputs=_a_(523126, _n_(523125, "base_model", lambda: base_model), "input"), outputs=_n_(523127, "x", lambda: x))
_l_(523129)


_n_(523130, "base_model", lambda: base_model).trainable = False
_l_(523131)

N=1
_l_(523132)

_c_(523134, _n_(523133, "print", lambda: print), "HANG ON LEARNING IN PROGRESS...")
_l_(523135)

_c_(523140, _a_(523137, _n_(523136, "model", lambda: model), "compile"), _c_(523139, _n_(523138, "Adam", lambda: Adam), lr=.0001),loss='categorical_crossentropy', metrics=['accuracy'])
_l_(523141)
history=_c_(523147, _a_(523143, _n_(523142, "model", lambda: model), "fit_generator"), _n_(523144, "train_batches", lambda: train_batches), steps_per_epoch=1290, validation_data=_n_(523145, "valid_batches", lambda: valid_batches),
                            validation_steps=90,epochs=_n_(523146, "N", lambda: N),verbose=1)
_l_(523148)

_c_(523150, _n_(523149, "print", lambda: print), "[INFO]evaluating model...")
_l_(523151)

test_labels=_a_(523153, _n_(523152, "test_batches", lambda: test_batches), "classes")
_l_(523154)
predictions=_c_(523158, _a_(523156, _n_(523155, "model", lambda: model), "predict_generator"), _n_(523157, "test_batches", lambda: test_batches), steps=28, verbose=1)
_l_(523159)
try:
    import matplotlib.pyplot as plt
    _l_(523161)

except ImportError:
    pass
try:
    import numpy as np
    _l_(523163)

except ImportError:
    pass


_c_(523170, _a_(523165, _n_(523164, "plt", lambda: plt), "imshow"), _c_(523169, _a_(523168, _a_(523167, _n_(523166, "np", lambda: np), "random"), "random"), (48,48)), interpolation='nearest')
_l_(523171)
_c_(523177, _a_(523173, _n_(523172, "plt", lambda: plt), "xticks"), _c_(523176, _a_(523175, _n_(523174, "np", lambda: np), "arange"), 0,48), ['A', 'BA', 'KA', 'GA', 'HA', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '31', '32',
              '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44'])
_l_(523178)
_c_(523184, _a_(523180, _n_(523179, "plt", lambda: plt), "yticks"), _c_(523183, _a_(523182, _n_(523181, "np", lambda: np), "arange"), 0,48),['A', 'BA', 'KA', 'GA', 'HA', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
              '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '31', '32',
              '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44'])
_l_(523185)
try:
    from sklearn.metrics import classification_report
    _l_(523187)

except ImportError:
    pass
try:
    from sklearn.metrics import confusion_matrix
    _l_(523189)

except ImportError:
    pass

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = _c_(523191, _n_(523190, "ImageDataGenerator", lambda: ImageDataGenerator), rescale=1. / 255)
_l_(523192)

train_generator = _c_(523197, _a_(523194, _n_(523193, "train_path", lambda: train_path), "flow_from_directory"), _n_(523195, "train_path", lambda: train_path),
    batch_size=_n_(523196, "batch_size", lambda: batch_size),
    class_mode='categorical')
_l_(523198)

validation_generator = _c_(523203, _a_(523200, _n_(523199, "test_datagen", lambda: test_datagen), "flow_from_directory"), _n_(523201, "valid_path", lambda: valid_path),
    batch_size=_n_(523202, "batch_size", lambda: batch_size),
    class_mode='categorical')
_l_(523204)

_c_(523212, _a_(523206, _n_(523205, "model", lambda: model), "fit_generator"), _n_(523207, "train_generator", lambda: train_generator),
    steps_per_epoch= 52800 // _n_(523208, "batch_size", lambda: batch_size),
    epochs=_n_(523209, "N", lambda: N),
    validation_data=_n_(523210, "validation_generator", lambda: validation_generator),
    validation_steps= 13200 // _n_(523211, "batch_size", lambda: batch_size))
_l_(523213)
try:
    from sklearn.metrics import classification_report
    _l_(523215)

except ImportError:
    pass
try:
    from sklearn.metrics import confusion_matrix
    _l_(523217)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(523219)

except ImportError:
    pass


test_steps_per_epoch = _c_(523227, _a_(523222, _a_(523221, _n_(523220, "numpy", lambda: numpy), "math"), "ceil"), _a_(523224, _n_(523223, "validation_generator", lambda: validation_generator), "samples") / _a_(523226, _n_(523225, "validation_generator", lambda: validation_generator), "batch_size"))
_l_(523228)

predictions = _c_(523233, _a_(523230, _n_(523229, "model", lambda: model), "predict_generator"), _n_(523231, "validation_generator", lambda: validation_generator), steps=_n_(523232, "test_steps_per_epoch", lambda: test_steps_per_epoch))
_l_(523234)
test_steps_per_epoch = _c_(523242, _a_(523237, _a_(523236, _n_(523235, "numpy", lambda: numpy), "math"), "ceil"), _a_(523239, _n_(523238, "validation_generator", lambda: validation_generator), "samples") / _a_(523241, _n_(523240, "validation_generator", lambda: validation_generator), "batch_size"))
_l_(523243)
predicted_classes = _c_(523247, _a_(523245, _n_(523244, "numpy", lambda: numpy), "argmax"), _n_(523246, "predictions", lambda: predictions), axis=1)
_l_(523248)
true_classes = _a_(523250, _n_(523249, "validation_generator", lambda: validation_generator), "classes")
_l_(523251)
class_labels = _c_(523257, _n_(523252, "list", lambda: list), _c_(523256, _a_(523255, _a_(523254, _n_(523253, "validation_generator", lambda: validation_generator), "class_indices"), "keys")))
_l_(523258)
report = _c_(523263, _n_(523259, "classification_report", lambda: classification_report), _n_(523260, "true_classes", lambda: true_classes), _n_(523261, "predicted_classes", lambda: predicted_classes), target_names=_n_(523262, "class_labels", lambda: class_labels))
_l_(523264)
_c_(523267, _n_(523265, "print", lambda: print), _n_(523266, "report", lambda: report))
_l_(523268)

cm=_c_(523272, _n_(523269, "confusion_matrix", lambda: confusion_matrix), _n_(523270, "true_classes", lambda: true_classes),_n_(523271, "predicted_classes", lambda: predicted_classes))
_l_(523273)
_c_(523276, _n_(523274, "print", lambda: print), _n_(523275, "cm", lambda: cm))
_l_(523277)

_c_(523280, _a_(523279, _n_(523278, "plt", lambda: plt), "show"))
_l_(523281)
_c_(523284, _a_(523283, _n_(523282, "model", lambda: model), "save"), "X19baybayin.h5")
_l_(523285)