# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64350501/tensorflow-filenotfounderror-errno-2-no-such-file-or-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow.keras
    _l_(632572)

except ImportError:
    pass
try:
    from PIL import Image, ImageOps
    _l_(632574)

except ImportError:
    pass
try:
    import numpy as np
    _l_(632576)

except ImportError:
    pass

# Disable scientific notation for clarity
_c_(632579, _a_(632578, _n_(632577, "np", lambda: np), "set_printoptions"), suppress=True)
_l_(632580)

# Load the model
model = _c_(632584, _a_(632583, _a_(632582, _a_(632581, tensorflow, "keras"), "models"), "load_model"), r'C:\Users\royst\Desktop\TF Files\keras_model.h5')
_l_(632585)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = _c_(632590, _a_(632587, _n_(632586, "np", lambda: np), "ndarray"), shape=(1, 224, 224, 3), dtype=_a_(632589, _n_(632588, "np", lambda: np), "float32"))
_l_(632591)

# Replace this with the path to your image
image = _c_(632594, _a_(632593, _n_(632592, "Image", lambda: Image), "open"), r'C:\Users\royst\Desktop\TF Files\test_photo.jpg')
_l_(632595)

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
_l_(632596)
image = _c_(632603, _a_(632598, _n_(632597, "ImageOps", lambda: ImageOps), "fit"), _n_(632599, "image", lambda: image), _n_(632600, "size", lambda: size), _a_(632602, _n_(632601, "Image", lambda: Image), "ANTIALIAS"))
_l_(632604)

#turn the image into a numpy array
image_array = _c_(632608, _a_(632606, _n_(632605, "np", lambda: np), "asarray"), _n_(632607, "image", lambda: image))
_l_(632609)
    
# display the resized image
_c_(632612, _a_(632611, _n_(632610, "image", lambda: image), "show"))
_l_(632613)

# Normalize the image
normalized_image_array = (_c_(632618, _a_(632615, _n_(632614, "image_array", lambda: image_array), "astype"), _a_(632617, _n_(632616, "np", lambda: np), "float32")) / 127.0) - 1
_l_(632619)

# Load the image into the array
_n_(632620, "data", lambda: data)[0] = _n_(632621, "normalized_image_array", lambda: normalized_image_array)
_l_(632622)

# run the inference
prediction = _c_(632626, _a_(632624, _n_(632623, "model", lambda: model), "predict"), _n_(632625, "data", lambda: data))
_l_(632627)
_c_(632630, _n_(632628, "print", lambda: print), _n_(632629, "prediction", lambda: prediction))
_l_(632631)