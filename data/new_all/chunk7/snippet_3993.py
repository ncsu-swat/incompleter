# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64350501/tensorflow-filenotfounderror-errno-2-no-such-file-or-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow.keras
    _l_(638518)

except ImportError:
    pass
try:
    from PIL import Image, ImageOps
    _l_(638520)

except ImportError:
    pass
try:
    import numpy as np
    _l_(638522)

except ImportError:
    pass

# Disable scientific notation for clarity
_c_(638525, _a_(638524, _n_(638523, "np", lambda: np), "set_printoptions"), suppress=True)
_l_(638526)

# Load the model
model = _c_(638530, _a_(638529, _a_(638528, _a_(638527, tensorflow, "keras"), "models"), "load_model"), r'C:\Users\royst\Desktop\TF Files\keras_model.h5')
_l_(638531)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = _c_(638536, _a_(638533, _n_(638532, "np", lambda: np), "ndarray"), shape=(1, 224, 224, 3), dtype=_a_(638535, _n_(638534, "np", lambda: np), "float32"))
_l_(638537)

# Replace this with the path to your image
image = _c_(638540, _a_(638539, _n_(638538, "Image", lambda: Image), "open"), r'C:\Users\royst\Desktop\TF Files\test_photo.jpg')
_l_(638541)

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
_l_(638542)
image = _c_(638549, _a_(638544, _n_(638543, "ImageOps", lambda: ImageOps), "fit"), _n_(638545, "image", lambda: image), _n_(638546, "size", lambda: size), _a_(638548, _n_(638547, "Image", lambda: Image), "ANTIALIAS"))
_l_(638550)

#turn the image into a numpy array
image_array = _c_(638554, _a_(638552, _n_(638551, "np", lambda: np), "asarray"), _n_(638553, "image", lambda: image))
_l_(638555)
    
# display the resized image
_c_(638558, _a_(638557, _n_(638556, "image", lambda: image), "show"))
_l_(638559)

# Normalize the image
normalized_image_array = (_c_(638564, _a_(638561, _n_(638560, "image_array", lambda: image_array), "astype"), _a_(638563, _n_(638562, "np", lambda: np), "float32")) / 127.0) - 1
_l_(638565)

# Load the image into the array
_n_(638566, "data", lambda: data)[0] = _n_(638567, "normalized_image_array", lambda: normalized_image_array)
_l_(638568)

# run the inference
prediction = _c_(638572, _a_(638570, _n_(638569, "model", lambda: model), "predict"), _n_(638571, "data", lambda: data))
_l_(638573)
_c_(638576, _n_(638574, "print", lambda: print), _n_(638575, "prediction", lambda: prediction))
_l_(638577)