# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60904090/typeerror-float-argument-must-be-a-string-or-a-number-not-module
# load and prepare an image
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def load_image_pixels(filename, shape):
    _l_(557505)

    # load the image to get its shape
    Image_file = _c_(557476, _a_(557474, _n_(557473, "image", lambda: image), "load_img"), _n_(557475, "filename", lambda: filename))
    _l_(557477)
    width, height = _a_(557479, _n_(557478, "Image_file", lambda: Image_file), "size")
    _l_(557480)
    # load the image with the required size
    Image_file = _c_(557485, _a_(557482, _n_(557481, "image", lambda: image), "load_img"), _n_(557483, "filename", lambda: filename), target_size=_n_(557484, "shape", lambda: shape))
    _l_(557486)
    # convert to numpy array
    Image_file = _c_(557490, _a_(557488, _n_(557487, "image", lambda: image), "img_to_array"), _n_(557489, "image", lambda: image))
    _l_(557491)
    # scale pixel values to [0, 1]
    Image_file = _c_(557494, _a_(557493, _n_(557492, "Image_file", lambda: Image_file), "astype"), 'float32')
    _l_(557495)
    Image_file /= 255.0
    _l_(557496)
    # add a dimension so that we have one sample
    Image_file = _c_(557499, _n_(557497, "expand_dims", lambda: expand_dims), _n_(557498, "Image_file", lambda: Image_file), 0)
    _l_(557500)
    aux = _n_(557501, "Image_file", lambda: Image_file), _n_(557502, "width", lambda: width), _n_(557503, "height", lambda: height)
    _l_(557504)
    return aux

# define the expected input shape for the model
input_w, input_h = 416, 416
_l_(557506)
# define our new photo
filename = 'zebra.jpg'
_l_(557507)
# load and prepare image
Image_file, width, height = _c_(557512, _n_(557508, "load_image_pixels", lambda: load_image_pixels), _n_(557509, "filename", lambda: filename), (_n_(557510, "input_w", lambda: input_w), _n_(557511, "input_h", lambda: input_h)))
_l_(557513)