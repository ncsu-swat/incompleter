# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59116366/typeerror-int-object-is-not-subscriptable-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image, ImageDraw
    _l_(705870)

except ImportError:
    pass
try:
    from numpy import asarray
    _l_(705872)

except ImportError:
    pass
# Load image:
input_image = _c_(705875, _a_(705874, _n_(705873, "Image", lambda: Image), "open"), "Cameraman.tif")
_l_(705876)
input_pixels = _c_(705879, _a_(705878, _n_(705877, "input_image", lambda: input_image), "load"))
_l_(705880)

# Box Blur kernel
box_kernel = ([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])
_l_(705881)


# Select kernel here:
kernel = _n_(705882, "box_kernel", lambda: box_kernel)
_l_(705883)

# Middle of the kernel
offset = _c_(705886, _n_(705884, "len", lambda: len), _n_(705885, "kernel", lambda: kernel)) // 2
_l_(705887)

# Create output image
output_image = _c_(705892, _a_(705889, _n_(705888, "Image", lambda: Image), "new"), "RGB", _a_(705891, _n_(705890, "input_image", lambda: input_image), "size"))
_l_(705893)
draw = _c_(705897, _a_(705895, _n_(705894, "ImageDraw", lambda: ImageDraw), "Draw"), _n_(705896, "output_image", lambda: output_image))
_l_(705898)

# Compute convolution between intensity and kernels
output_image = _c_(705903, _a_(705900, _n_(705899, "Image", lambda: Image), "new"), "RGB", _a_(705902, _n_(705901, "input_image", lambda: input_image), "size"))
_l_(705904)
draw = _c_(705908, _a_(705906, _n_(705905, "ImageDraw", lambda: ImageDraw), "Draw"), _n_(705907, "output_image", lambda: output_image))
_l_(705909)

# Compute convolution with kernel
for x in _c_(705915, _n_(705910, "range", lambda: range), _n_(705911, "offset", lambda: offset), _a_(705913, _n_(705912, "input_image", lambda: input_image), "width") - _n_(705914, "offset", lambda: offset)):
    _l_(705984)

    for y in _c_(705921, _n_(705916, "range", lambda: range), _n_(705917, "offset", lambda: offset), _a_(705919, _n_(705918, "input_image", lambda: input_image), "height") - _n_(705920, "offset", lambda: offset)):
        _l_(705983)

        acc = [0, 0, 0]
        _l_(705922)
        for a in _c_(705927, _n_(705923, "range", lambda: range), _c_(705926, _n_(705924, "len", lambda: len), _n_(705925, "kernel", lambda: kernel))):
            _l_(705967)

            for b in _c_(705932, _n_(705928, "range", lambda: range), _c_(705931, _n_(705929, "len", lambda: len), _n_(705930, "kernel", lambda: kernel))):
                _l_(705966)

                xn = _n_(705933, "x", lambda: x) + _n_(705934, "a", lambda: a) - _n_(705935, "offset", lambda: offset)
                _l_(705936)
                yn = _n_(705937, "y", lambda: y) + _n_(705938, "b", lambda: b) - _n_(705939, "offset", lambda: offset)
                _l_(705940)
                pixel = _n_(705941, "input_pixels", lambda: input_pixels)[_n_(705942, "xn", lambda: xn), _n_(705943, "yn", lambda: yn)]
                _l_(705944)
                _n_(705945, "acc", lambda: acc)[0] = _n_(705946, "acc", lambda: acc)[0] + (_n_(705947, "pixel", lambda: pixel)[0] * _n_(705948, "kernel", lambda: kernel)[_n_(705949, "a", lambda: a)][_n_(705950, "b", lambda: b)])
                _l_(705951)
                _n_(705952, "acc", lambda: acc)[1] = _n_(705953, "acc", lambda: acc)[1] + (_n_(705954, "pixel", lambda: pixel)[1] * _n_(705955, "kernel", lambda: kernel)[_n_(705956, "a", lambda: a)][_n_(705957, "b", lambda: b)])
                _l_(705958)
                _n_(705959, "acc", lambda: acc)[2] = _n_(705960, "acc", lambda: acc)[2] + (_n_(705961, "pixel", lambda: pixel)[2] * _n_(705962, "kernel", lambda: kernel)[_n_(705963, "a", lambda: a)][_n_(705964, "b", lambda: b)])
                _l_(705965)

        _c_(705981, _a_(705969, _n_(705968, "draw", lambda: draw), "point"), (_n_(705970, "x", lambda: x), _n_(705971, "y", lambda: y)), (_c_(705974, _n_(705972, "int", lambda: int), _n_(705973, "acc", lambda: acc)[0]), _c_(705977, _n_(705975, "int", lambda: int), _n_(705976, "acc", lambda: acc)[1]), _c_(705980, _n_(705978, "int", lambda: int), _n_(705979, "acc", lambda: acc)[2])))
        _l_(705982)

_c_(705987, _a_(705986, _n_(705985, "output_image", lambda: output_image), "save"), "Filtered.png")
_l_(705988)

img1arr = _c_(705991, _n_(705989, "asarray", lambda: asarray), _n_(705990, "input_image", lambda: input_image))
_l_(705992)
img2arr = _c_(705995, _n_(705993, "asarray", lambda: asarray), _n_(705994, "output_image", lambda: output_image))
_l_(705996)
im1arrF = _c_(705999, _a_(705998, _n_(705997, "img1arr", lambda: img1arr), "astype"), 'float')
_l_(706000)
im2arrF = _c_(706003, _a_(706002, _n_(706001, "img2arr", lambda: img2arr), "astype"), 'float')
_l_(706004)
additionF = (_n_(706005, "im1arrF", lambda: im1arrF)+_n_(706006, "im2arrF", lambda: im2arrF))/2
_l_(706007)
addition = _c_(706010, _a_(706009, _n_(706008, "additionF", lambda: additionF), "astype"), 'uint8')
_l_(706011)
resultImage = _c_(706015, _a_(706013, _n_(706012, "Image", lambda: Image), "fromarray"), _n_(706014, "addition", lambda: addition))
_l_(706016)
_c_(706019, _a_(706018, _n_(706017, "resultImage", lambda: resultImage), "save"), 'Sharpened.jpg')
_l_(706020)