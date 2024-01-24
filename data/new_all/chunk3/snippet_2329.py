# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50349213/attributeerror-str-object-has-no-attribute-ndim-unable-to-use-model-predic
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
features = {}
_l_(544878)
for images in _c_(544882, _a_(544880, _n_(544879, "os", lambda: os), "listdir"), _n_(544881, "args", lambda: args)["image"]):
    _l_(544923)

    filename = _n_(544883, "args", lambda: args)["image"] + '/' + _n_(544884, "images", lambda: images)
    _l_(544885)
    image = _c_(544889, _n_(544886, "load_img", lambda: load_img), _n_(544887, "filename", lambda: filename), target_size = _n_(544888, "inputShape", lambda: inputShape))
    _l_(544890)
    image = _c_(544893, _n_(544891, "img_to_array", lambda: img_to_array), _n_(544892, "image", lambda: image))
    _l_(544894)
    image = _c_(544898, _a_(544896, _n_(544895, "np", lambda: np), "expand_dims"), _n_(544897, "image", lambda: image), axis = 0)
    _l_(544899)
    image = _c_(544902, _n_(544900, "preprocess", lambda: preprocess), _n_(544901, "image", lambda: image))
    _l_(544903)
    pred = _c_(544907, _a_(544905, _n_(544904, "resnet", lambda: resnet), "predict"), _n_(544906, "image", lambda: image))
    _l_(544908)
    image_id = _c_(544911, _a_(544910, _n_(544909, "images", lambda: images), "split"), '.')[0]
    _l_(544912)
    _n_(544913, "features", lambda: features)[_n_(544914, "image_id", lambda: image_id)] = _n_(544915, "pred", lambda: pred)
    _l_(544916)
    _c_(544921, _n_(544917, "print", lambda: print), _c_(544920, _a_(544918, '>{}', "format"), _n_(544919, "images", lambda: images)))
    _l_(544922)