# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59116366/typeerror-int-object-is-not-subscriptable-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image, ImageDraw
    _l_(701302)

except ImportError:
    pass
try:
    from numpy import asarray
    _l_(701304)

except ImportError:
    pass
# Load image:
input_image = _c_(701307, _a_(701306, _n_(701305, "Image", lambda: Image), "open"), "Cameraman.tif")
_l_(701308)
input_pixels = _c_(701311, _a_(701310, _n_(701309, "input_image", lambda: input_image), "load"))
_l_(701312)

# Box Blur kernel
box_kernel = ([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])
_l_(701313)


# Select kernel here:
kernel = _n_(701314, "box_kernel", lambda: box_kernel)
_l_(701315)

# Middle of the kernel
offset = _c_(701318, _n_(701316, "len", lambda: len), _n_(701317, "kernel", lambda: kernel)) // 2
_l_(701319)

# Create output image
output_image = _c_(701324, _a_(701321, _n_(701320, "Image", lambda: Image), "new"), "RGB", _a_(701323, _n_(701322, "input_image", lambda: input_image), "size"))
_l_(701325)
draw = _c_(701329, _a_(701327, _n_(701326, "ImageDraw", lambda: ImageDraw), "Draw"), _n_(701328, "output_image", lambda: output_image))
_l_(701330)

# Compute convolution between intensity and kernels
output_image = _c_(701335, _a_(701332, _n_(701331, "Image", lambda: Image), "new"), "RGB", _a_(701334, _n_(701333, "input_image", lambda: input_image), "size"))
_l_(701336)
draw = _c_(701340, _a_(701338, _n_(701337, "ImageDraw", lambda: ImageDraw), "Draw"), _n_(701339, "output_image", lambda: output_image))
_l_(701341)

# Compute convolution with kernel
for x in _c_(701347, _n_(701342, "range", lambda: range), _n_(701343, "offset", lambda: offset), _a_(701345, _n_(701344, "input_image", lambda: input_image), "width") - _n_(701346, "offset", lambda: offset)):
    _l_(701416)

    for y in _c_(701353, _n_(701348, "range", lambda: range), _n_(701349, "offset", lambda: offset), _a_(701351, _n_(701350, "input_image", lambda: input_image), "height") - _n_(701352, "offset", lambda: offset)):
        _l_(701415)

        acc = [0, 0, 0]
        _l_(701354)
        for a in _c_(701359, _n_(701355, "range", lambda: range), _c_(701358, _n_(701356, "len", lambda: len), _n_(701357, "kernel", lambda: kernel))):
            _l_(701399)

            for b in _c_(701364, _n_(701360, "range", lambda: range), _c_(701363, _n_(701361, "len", lambda: len), _n_(701362, "kernel", lambda: kernel))):
                _l_(701398)

                xn = _n_(701365, "x", lambda: x) + _n_(701366, "a", lambda: a) - _n_(701367, "offset", lambda: offset)
                _l_(701368)
                yn = _n_(701369, "y", lambda: y) + _n_(701370, "b", lambda: b) - _n_(701371, "offset", lambda: offset)
                _l_(701372)
                pixel = _n_(701373, "input_pixels", lambda: input_pixels)[_n_(701374, "xn", lambda: xn), _n_(701375, "yn", lambda: yn)]
                _l_(701376)
                _n_(701377, "acc", lambda: acc)[0] = _n_(701378, "acc", lambda: acc)[0] + (_n_(701379, "pixel", lambda: pixel)[0] * _n_(701380, "kernel", lambda: kernel)[_n_(701381, "a", lambda: a)][_n_(701382, "b", lambda: b)])
                _l_(701383)
                _n_(701384, "acc", lambda: acc)[1] = _n_(701385, "acc", lambda: acc)[1] + (_n_(701386, "pixel", lambda: pixel)[1] * _n_(701387, "kernel", lambda: kernel)[_n_(701388, "a", lambda: a)][_n_(701389, "b", lambda: b)])
                _l_(701390)
                _n_(701391, "acc", lambda: acc)[2] = _n_(701392, "acc", lambda: acc)[2] + (_n_(701393, "pixel", lambda: pixel)[2] * _n_(701394, "kernel", lambda: kernel)[_n_(701395, "a", lambda: a)][_n_(701396, "b", lambda: b)])
                _l_(701397)

        _c_(701413, _a_(701401, _n_(701400, "draw", lambda: draw), "point"), (_n_(701402, "x", lambda: x), _n_(701403, "y", lambda: y)), (_c_(701406, _n_(701404, "int", lambda: int), _n_(701405, "acc", lambda: acc)[0]), _c_(701409, _n_(701407, "int", lambda: int), _n_(701408, "acc", lambda: acc)[1]), _c_(701412, _n_(701410, "int", lambda: int), _n_(701411, "acc", lambda: acc)[2])))
        _l_(701414)

_c_(701419, _a_(701418, _n_(701417, "output_image", lambda: output_image), "save"), "Filtered.png")
_l_(701420)

img1arr = _c_(701423, _n_(701421, "asarray", lambda: asarray), _n_(701422, "input_image", lambda: input_image))
_l_(701424)
img2arr = _c_(701427, _n_(701425, "asarray", lambda: asarray), _n_(701426, "output_image", lambda: output_image))
_l_(701428)
im1arrF = _c_(701431, _a_(701430, _n_(701429, "img1arr", lambda: img1arr), "astype"), 'float')
_l_(701432)
im2arrF = _c_(701435, _a_(701434, _n_(701433, "img2arr", lambda: img2arr), "astype"), 'float')
_l_(701436)
additionF = (_n_(701437, "im1arrF", lambda: im1arrF)+_n_(701438, "im2arrF", lambda: im2arrF))/2
_l_(701439)
addition = _c_(701442, _a_(701441, _n_(701440, "additionF", lambda: additionF), "astype"), 'uint8')
_l_(701443)
resultImage = _c_(701447, _a_(701445, _n_(701444, "Image", lambda: Image), "fromarray"), _n_(701446, "addition", lambda: addition))
_l_(701448)
_c_(701451, _a_(701450, _n_(701449, "resultImage", lambda: resultImage), "save"), 'Sharpened.jpg')
_l_(701452)