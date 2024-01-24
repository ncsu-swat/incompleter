# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62761517/typeerror-invalid-shape-100-100-1-for-image-data-when-plot-image
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sample_training_images, _ = _c_(398853, _n_(398851, "next", lambda: next), _n_(398852, "traindata", lambda: traindata))
_l_(398854)
def plotImages(images_arr):
    _l_(398890)

    fig, axes = _c_(398857, _a_(398856, _n_(398855, "plt", lambda: plt), "subplots"), 1, 5, figsize=(20,20))
    _l_(398858)
    axes = _c_(398861, _a_(398860, _n_(398859, "axes", lambda: axes), "flatten"))
    _l_(398862)
    for img, ax in _c_(398866, _n_(398863, "zip", lambda: zip), _n_(398864, "images_arr", lambda: images_arr), _n_(398865, "axes", lambda: axes)):
        _l_(398876)

        _c_(398870, _a_(398868, _n_(398867, "ax", lambda: ax), "imshow"), _n_(398869, "img", lambda: img))
        _l_(398871)
        _c_(398874, _a_(398873, _n_(398872, "ax", lambda: ax), "axis"), 'off')
        _l_(398875)
    _c_(398879, _a_(398878, _n_(398877, "plt", lambda: plt), "tight_layout"))
    _l_(398880)
    _c_(398884, _a_(398882, _n_(398881, "plt", lambda: plt), "plot"), _n_(398883, "images_arr", lambda: images_arr))
    _l_(398885)
    _c_(398888, _a_(398887, _n_(398886, "plt", lambda: plt), "show"))
    _l_(398889)

_c_(398893, _n_(398891, "plotImages", lambda: plotImages), _n_(398892, "sample_training_images", lambda: sample_training_images)[:5])
_l_(398894)