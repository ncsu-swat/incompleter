# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66839062/typeerror-keyword-argument-not-understood-input-for-cnn-with-pretrained
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def VGG16_MODEL(img_rows=_n_(641592, "IMG_SIZE", lambda: IMG_SIZE), img_cols=_n_(641593, "IMG_SIZE", lambda: IMG_SIZE), color_type=3):
    _l_(641629)

    # Remove fully connected layer and replace
    # with softmax for classifying 10 classes
    model_vgg16_1 = _c_(641595, _n_(641594, "VGG16", lambda: VGG16), weights="imagenet", include_top=False)
    _l_(641596)

    # Freeze all layers of the pre-trained model
    for layer in _a_(641598, _n_(641597, "model_vgg16_1", lambda: model_vgg16_1), "layers"):
        _l_(641601)

        _n_(641599, "layer", lambda: layer).trainable = False
        _l_(641600)
    x = _a_(641603, _n_(641602, "model_vgg16_1", lambda: model_vgg16_1), "output")
    _l_(641604)
    x = _c_(641608, _c_(641606, _n_(641605, "GlobalAveragePooling2D", lambda: GlobalAveragePooling2D)), _n_(641607, "x", lambda: x))
    _l_(641609)
    x = _c_(641613, _c_(641611, _n_(641610, "Dense", lambda: Dense), 1024, activation='relu'), _n_(641612, "x", lambda: x))
    _l_(641614)
    predictions = _c_(641619, _c_(641617, _n_(641615, "Dense", lambda: Dense), _n_(641616, "CLASSES", lambda: CLASSES), activation = 'softmax'), _n_(641618, "x", lambda: x))
    _l_(641620)

    model = _c_(641625, _n_(641621, "Model", lambda: Model), input = _a_(641623, _n_(641622, "model_vgg16_1", lambda: model_vgg16_1), "input"), output = _n_(641624, "predictions", lambda: predictions))
    _l_(641626)
    aux = _n_(641627, "model", lambda: model)
    _l_(641628)
    
    return aux

_c_(641631, _n_(641630, "print", lambda: print), "Model 1 network...")
_l_(641632)
model_vgg16_1 = _c_(641636, _n_(641633, "VGG16_MODEL", lambda: VGG16_MODEL), img_rows=_n_(641634, "IMG_SIZE", lambda: IMG_SIZE), img_cols=_n_(641635, "IMG_SIZE", lambda: IMG_SIZE))
_l_(641637)

_c_(641640, _a_(641639, _n_(641638, "model_vgg16_1", lambda: model_vgg16_1), "summary"))
_l_(641641)

_c_(641644, _a_(641643, _n_(641642, "model_vgg16_1", lambda: model_vgg16_1), "compile"), loss='categorical_crossentropy',
                         optimizer='rmsprop',
                         metrics=['accuracy'])
_l_(641645)