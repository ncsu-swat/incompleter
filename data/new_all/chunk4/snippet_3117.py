# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66839062/typeerror-keyword-argument-not-understood-input-for-cnn-with-pretrained
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def VGG16_MODEL(img_rows=_n_(623212, "IMG_SIZE", lambda: IMG_SIZE), img_cols=_n_(623213, "IMG_SIZE", lambda: IMG_SIZE), color_type=3):
    _l_(623249)

    # Remove fully connected layer and replace
    # with softmax for classifying 10 classes
    model_vgg16_1 = _c_(623215, _n_(623214, "VGG16", lambda: VGG16), weights="imagenet", include_top=False)
    _l_(623216)

    # Freeze all layers of the pre-trained model
    for layer in _a_(623218, _n_(623217, "model_vgg16_1", lambda: model_vgg16_1), "layers"):
        _l_(623221)

        _n_(623219, "layer", lambda: layer).trainable = False
        _l_(623220)
    x = _a_(623223, _n_(623222, "model_vgg16_1", lambda: model_vgg16_1), "output")
    _l_(623224)
    x = _c_(623228, _c_(623226, _n_(623225, "GlobalAveragePooling2D", lambda: GlobalAveragePooling2D)), _n_(623227, "x", lambda: x))
    _l_(623229)
    x = _c_(623233, _c_(623231, _n_(623230, "Dense", lambda: Dense), 1024, activation='relu'), _n_(623232, "x", lambda: x))
    _l_(623234)
    predictions = _c_(623239, _c_(623237, _n_(623235, "Dense", lambda: Dense), _n_(623236, "CLASSES", lambda: CLASSES), activation = 'softmax'), _n_(623238, "x", lambda: x))
    _l_(623240)

    model = _c_(623245, _n_(623241, "Model", lambda: Model), input = _a_(623243, _n_(623242, "model_vgg16_1", lambda: model_vgg16_1), "input"), output = _n_(623244, "predictions", lambda: predictions))
    _l_(623246)
    aux = _n_(623247, "model", lambda: model)
    _l_(623248)
    
    return aux

_c_(623251, _n_(623250, "print", lambda: print), "Model 1 network...")
_l_(623252)
model_vgg16_1 = _c_(623256, _n_(623253, "VGG16_MODEL", lambda: VGG16_MODEL), img_rows=_n_(623254, "IMG_SIZE", lambda: IMG_SIZE), img_cols=_n_(623255, "IMG_SIZE", lambda: IMG_SIZE))
_l_(623257)

_c_(623260, _a_(623259, _n_(623258, "model_vgg16_1", lambda: model_vgg16_1), "summary"))
_l_(623261)

_c_(623264, _a_(623263, _n_(623262, "model_vgg16_1", lambda: model_vgg16_1), "compile"), loss='categorical_crossentropy',
                         optimizer='rmsprop',
                         metrics=['accuracy'])
_l_(623265)