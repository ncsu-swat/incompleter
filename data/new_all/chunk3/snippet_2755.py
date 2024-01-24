# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64282076/using-pretrained-model-with-keras-attributeerror-nonetype-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
top_model_weight_path = 'feat_extr_model.h5'
_l_(542772)
train_data_dir = 'data/train'
_l_(542773)
validation_data_dir = 'data/validation'
_l_(542774)
nb_train_samples = 54
_l_(542775)
nb_validation_samples = 6
_l_(542776)
epochs = 10
_l_(542777)
batch_size = 16    
_l_(542778)    

base_model = _c_(542780, _n_(542779, "VGG16", lambda: VGG16), weights='imagenet', include_top=False, input_shape=(224, 224, 3))
_l_(542781)

top_model = _c_(542783, _n_(542782, "Sequential", lambda: Sequential))
_l_(542784)
_c_(542791, _a_(542786, _n_(542785, "top_model", lambda: top_model), "add"), _c_(542790, _n_(542787, "Flatten", lambda: Flatten), input_shape=_a_(542789, _n_(542788, "base_model", lambda: base_model), "output_shape")[1:]))
_l_(542792)
_c_(542797, _a_(542794, _n_(542793, "top_model", lambda: top_model), "add"), _c_(542796, _n_(542795, "Dense", lambda: Dense), 256, activation='relu'))
_l_(542798)
_c_(542803, _a_(542800, _n_(542799, "top_model", lambda: top_model), "add"), _c_(542802, _n_(542801, "Dropout", lambda: Dropout), 0.5))
_l_(542804)
_c_(542809, _a_(542806, _n_(542805, "top_model", lambda: top_model), "add"), _c_(542808, _n_(542807, "Dense", lambda: Dense), 1, activation='sigmoid'))
_l_(542810)
# note that it is necessary to start with a fully-trained
# classifier, including the top classifier,
# in order to successfully do fine-tuning
_c_(542814, _a_(542812, _n_(542811, "top_model", lambda: top_model), "load_weights"), _n_(542813, "top_model_weight_path", lambda: top_model_weight_path))
_l_(542815)

model = _c_(542823, _n_(542816, "Model", lambda: Model), inputs=_a_(542818, _n_(542817, "base_model", lambda: base_model), "input"), outputs=_c_(542822, _n_(542819, "top_model", lambda: top_model), _a_(542821, _n_(542820, "base_model", lambda: base_model), "output")))
_l_(542824)

for l in _a_(542826, _n_(542825, "model", lambda: model), "layers")[:15]:
    _l_(542829)

    _n_(542827, "l", lambda: l).trainable = False
    _l_(542828)
_c_(542835, _a_(542831, _n_(542830, "model", lambda: model), "compile"), loss='binary_crossentropy',
              optimizer=_c_(542834, _a_(542833, _n_(542832, "optimizers", lambda: optimizers), "SGD"), lr=1e-4, momentum=0.9),
              metrics=['accuracy'])
_l_(542836)

train_datagen = _c_(542838, _n_(542837, "ImageDataGenerator", lambda: ImageDataGenerator), rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
_l_(542839)
test_datagen = _c_(542841, _n_(542840, "ImageDataGenerator", lambda: ImageDataGenerator), rescale=1./255)
_l_(542842)

train_generator = _c_(542847, _a_(542844, _n_(542843, "train_datagen", lambda: train_datagen), "flow_from_directory"), _n_(542845, "train_data_dir", lambda: train_data_dir),
                                                    target_size=(224, 224),
                                                    batch_size=_n_(542846, "batch_size", lambda: batch_size),
                                                    class_mode=None)
_l_(542848)
validation_generator = _c_(542853, _a_(542850, _n_(542849, "test_datagen", lambda: test_datagen), "flow_from_directory"), _n_(542851, "validation_data_dir", lambda: validation_data_dir),
                                                        target_size=(224,224),
                                                        batch_size=_n_(542852, "batch_size", lambda: batch_size),
                                                        class_mode=None)
_l_(542854)

_c_(542857, _a_(542856, _n_(542855, "model", lambda: model), "summary"))
_l_(542858)

# fine-tune the model
_c_(542864, _a_(542860, _n_(542859, "model", lambda: model), "fit_generator"), _n_(542861, "train_generator", lambda: train_generator),
    epochs=_n_(542862, "epochs", lambda: epochs),
    validation_data=_n_(542863, "validation_generator", lambda: validation_generator),
    verbose=2)
_l_(542865)