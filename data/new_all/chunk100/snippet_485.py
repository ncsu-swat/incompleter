# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
# Importing Image class from PIL module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(61501)

except ImportError:
    pass

# Opens a image in RGB mode
im = _c_(61504, _a_(61503, _n_(61502, "Image", lambda: Image), "open"), r"C:\Users\System-Pc\Desktop\ybear.jpg")
_l_(61505)

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = _a_(61507, _n_(61506, "im", lambda: im), "size")
_l_(61508)

# Setting the points for cropped image
left = 4
_l_(61509)
top = _n_(61510, "height", lambda: height) / 5
_l_(61511)
right = 154
_l_(61512)
bottom = 3 * _n_(61513, "height", lambda: height) / 5
_l_(61514)

# Cropped image of above dimension
# (It will not change original image)
im1 = _c_(61521, _a_(61516, _n_(61515, "im", lambda: im), "crop"), (_n_(61517, "left", lambda: left), _n_(61518, "top", lambda: top), _n_(61519, "right", lambda: right), _n_(61520, "bottom", lambda: bottom)))
_l_(61522)
newsize = (300, 300)
_l_(61523)
im1 = _c_(61527, _a_(61525, _n_(61524, "im1", lambda: im1), "resize"), _n_(61526, "newsize", lambda: newsize))
_l_(61528)
# Shows the image in image viewer
_c_(61531, _a_(61530, _n_(61529, "im1", lambda: im1), "show"))
_l_(61532)

