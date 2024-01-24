# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55315275/why-am-i-getting-typeerror-image-data-cannot-be-converted-to-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(421330)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(421332)

except ImportError:
    pass

def load_and_preprocess_jpeg(imagepath):
    _l_(421362)

    img = _c_(421336, _a_(421334, _n_(421333, "tf", lambda: tf), "read_file"), _n_(421335, "imagepath", lambda: imagepath))
    _l_(421337)
    img_tensor = _c_(421342, _a_(421340, _a_(421339, _n_(421338, "tf", lambda: tf), "image"), "decode_jpeg"), _n_(421341, "img", lambda: img))
    _l_(421343)
    _c_(421346, _a_(421345, _n_(421344, "img_tensor", lambda: img_tensor), "set_shape"), [792,1224,1])
    _l_(421347)
    img_tensor = _c_(421351, _a_(421349, _n_(421348, "tf", lambda: tf), "reshape"), _n_(421350, "img_tensor", lambda: img_tensor), [792,1224])
    _l_(421352)
    img_tensor = _c_(421358, _a_(421354, _n_(421353, "tf", lambda: tf), "cast"), _n_(421355, "img_tensor", lambda: img_tensor), _a_(421357, _n_(421356, "tf", lambda: tf), "float32"), name='ImageCast')
    _l_(421359)
    aux = _n_(421360, "img_tensor", lambda: img_tensor)
    _l_(421361)
    #img_tensor /= 255.0 #Tried with and without
    return aux

def read_data(all_filenames):
    _l_(421416)

    path_Dataset = _c_(421368, _a_(421366, _a_(421365, _a_(421364, _n_(421363, "tf", lambda: tf), "data"), "Dataset"), "from_tensor_slices"), _n_(421367, "all_filenames", lambda: all_filenames))
    _l_(421369)
    image_Dataset = _c_(421373, _a_(421371, _n_(421370, "path_Dataset", lambda: path_Dataset), "map"), _n_(421372, "load_and_preprocess_jpeg", lambda: load_and_preprocess_jpeg))
    _l_(421374)
    _c_(421377, _a_(421376, _n_(421375, "plt", lambda: plt), "figure"), figsize=(8,8))
    _l_(421378)
    temp_DS = _c_(421381, _a_(421380, _n_(421379, "image_Dataset", lambda: image_Dataset), "take"), 4)
    _l_(421382)
    itera = _c_(421385, _a_(421384, _n_(421383, "temp_DS", lambda: temp_DS), "make_one_shot_iterator"))
    _l_(421386)
    for n in _c_(421388, _n_(421387, "range", lambda: range), 4):
        _l_(421415)

        image = _c_(421391, _a_(421390, _n_(421389, "itera", lambda: itera), "get_next"))
        _l_(421392)
        _c_(421396, _a_(421394, _n_(421393, "plt", lambda: plt), "subplot"), 2,2,_n_(421395, "n", lambda: n)+1)
        _l_(421397)
        _c_(421401, _a_(421399, _n_(421398, "plt", lambda: plt), "imshow"), _n_(421400, "image", lambda: image))
        _l_(421402)
        _c_(421405, _a_(421404, _n_(421403, "plt", lambda: plt), "grid"), False)
        _l_(421406)
        _c_(421409, _a_(421408, _n_(421407, "plt", lambda: plt), "xticks"), [])
        _l_(421410)
        _c_(421413, _a_(421412, _n_(421411, "plt", lambda: plt), "yticks"), [])
        _l_(421414)