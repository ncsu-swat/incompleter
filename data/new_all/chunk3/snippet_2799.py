# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62765658/tensorflow-error-typeerror-tensor-objects-are-only-iterable-when-eager-executi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import tensorflow as tf
  _l_(531377)

except ImportError:
  pass
try:
  import IPython.display as display
  _l_(531379)

except ImportError:
  pass
try:
  import matplotlib.pyplot as plt
  _l_(531381)

except ImportError:
  pass
try:
  import matplotlib as mpl
  _l_(531383)

except ImportError:
  pass
_a_(531385, _n_(531384, "mpl", lambda: mpl), "rcParams")['figure.figsize'] = (12,12)
_l_(531386)
_a_(531388, _n_(531387, "mpl", lambda: mpl), "rcParams")['axes.grid'] = False
_l_(531389)
try:
  import numpy as np
  _l_(531391)

except ImportError:
  pass
try:
  import PIL.Image
  _l_(531393)

except ImportError:
  pass
try:
  import time
  _l_(531395)

except ImportError:
  pass
try:
  import functools
  _l_(531397)

except ImportError:
  pass
    
def tensor_to_image(tensor):
  _l_(531422)

  tensor = _n_(531398, "tensor", lambda: tensor)*255
  _l_(531399)
  tensor = _c_(531405, _a_(531401, _n_(531400, "np", lambda: np), "array"), _n_(531402, "tensor", lambda: tensor), dtype=_a_(531404, _n_(531403, "np", lambda: np), "uint8"))
  _l_(531406)
  if _c_(531410, _a_(531408, _n_(531407, "np", lambda: np), "ndim"), _n_(531409, "tensor", lambda: tensor))>3:
    _l_(531416)

    assert _a_(531412, _n_(531411, "tensor", lambda: tensor), "shape")[0] == 1
    _l_(531413)
    tensor = _n_(531414, "tensor", lambda: tensor)[0]
    _l_(531415)
  aux = _c_(531420, _a_(531418, _a_(531417, PIL, "Image"), "fromarray"), _n_(531419, "tensor", lambda: tensor))
  _l_(531421)
  return aux

content_path = _c_(531427, _a_(531426, _a_(531425, _a_(531424, _n_(531423, "tf", lambda: tf), "keras"), "utils"), "get_file"), 'YellowLabradorLooking_nw4.jpg', 'https://example.com/IMG_20200216_163015.jpg')
_l_(531428)


style_path = _c_(531433, _a_(531432, _a_(531431, _a_(531430, _n_(531429, "tf", lambda: tf), "keras"), "utils"), "get_file"), 'kandinsky3.jpg','https://example.com/download+(2).png')
_l_(531434)


def load_img(path_to_img):
  _l_(531494)

  max_dim = 512
  _l_(531435)
  img = _c_(531440, _a_(531438, _a_(531437, _n_(531436, "tf", lambda: tf), "io"), "read_file"), _n_(531439, "path_to_img", lambda: path_to_img))
  _l_(531441)
  img = _c_(531446, _a_(531444, _a_(531443, _n_(531442, "tf", lambda: tf), "image"), "decode_image"), _n_(531445, "img", lambda: img), channels=3)
  _l_(531447)
  img = _c_(531454, _a_(531450, _a_(531449, _n_(531448, "tf", lambda: tf), "image"), "convert_image_dtype"), _n_(531451, "img", lambda: img), _a_(531453, _n_(531452, "tf", lambda: tf), "float32"))
  _l_(531455)

  shape = _c_(531464, _a_(531457, _n_(531456, "tf", lambda: tf), "cast"), _c_(531461, _a_(531459, _n_(531458, "tf", lambda: tf), "shape"), _n_(531460, "img", lambda: img))[:-1], _a_(531463, _n_(531462, "tf", lambda: tf), "float32"))
  _l_(531465)
  long_dim = _c_(531468, _n_(531466, "max", lambda: max), _n_(531467, "shape", lambda: shape))
  _l_(531469)
  scale = _n_(531470, "max_dim", lambda: max_dim) / _n_(531471, "long_dim", lambda: long_dim)
  _l_(531472)

  new_shape = _c_(531479, _a_(531474, _n_(531473, "tf", lambda: tf), "cast"), _n_(531475, "shape", lambda: shape) * _n_(531476, "scale", lambda: scale), _a_(531478, _n_(531477, "tf", lambda: tf), "int32"))
  _l_(531480)

  img = _c_(531486, _a_(531483, _a_(531482, _n_(531481, "tf", lambda: tf), "image"), "resize"), _n_(531484, "img", lambda: img), _n_(531485, "new_shape", lambda: new_shape))
  _l_(531487)
  img = _n_(531488, "img", lambda: img)[_a_(531490, _n_(531489, "tf", lambda: tf), "newaxis"), :]
  _l_(531491)
  aux = _n_(531492, "img", lambda: img)
  _l_(531493)
  return aux


def imshow(image, title=None):
  _l_(531517)

  if _c_(531498, _n_(531495, "len", lambda: len), _a_(531497, _n_(531496, "image", lambda: image), "shape")) > 3:
    _l_(531504)

    image = _c_(531502, _a_(531500, _n_(531499, "tf", lambda: tf), "squeeze"), _n_(531501, "image", lambda: image), axis=0)
    _l_(531503)

  _c_(531508, _a_(531506, _n_(531505, "plt", lambda: plt), "imshow"), _n_(531507, "image", lambda: image))
  _l_(531509)
  if _n_(531510, "title", lambda: title):
    _l_(531516)

    _c_(531514, _a_(531512, _n_(531511, "plt", lambda: plt), "title"), _n_(531513, "title", lambda: title))
    _l_(531515)


content_image = _c_(531520, _n_(531518, "load_img", lambda: load_img), _n_(531519, "content_path", lambda: content_path))
_l_(531521)
style_image = _c_(531524, _n_(531522, "load_img", lambda: load_img), _n_(531523, "style_path", lambda: style_path))
_l_(531525)

_c_(531528, _a_(531527, _n_(531526, "plt", lambda: plt), "subplot"), 1, 2, 1)
_l_(531529)
_c_(531532, _n_(531530, "imshow", lambda: imshow), _n_(531531, "content_image", lambda: content_image), 'Content Image')
_l_(531533)

_c_(531536, _a_(531535, _n_(531534, "plt", lambda: plt), "subplot"), 1, 2, 2)
_l_(531537)
_c_(531540, _n_(531538, "imshow", lambda: imshow), _n_(531539, "style_image", lambda: style_image), 'Style Image')
_l_(531541)
try:
  import tensorflow_hub as hub
  _l_(531543)

except ImportError:
  pass
hub_module = _c_(531546, _a_(531545, _n_(531544, "hub", lambda: hub), "load"), 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/1')
_l_(531547)
stylized_image = _c_(531557, _n_(531548, "hub_module", lambda: hub_module), _c_(531552, _a_(531550, _n_(531549, "tf", lambda: tf), "constant"), _n_(531551, "content_image", lambda: content_image)), _c_(531556, _a_(531554, _n_(531553, "tf", lambda: tf), "constant"), _n_(531555, "style_image", lambda: style_image)))[0]
_l_(531558)
_c_(531561, _n_(531559, "tensor_to_image", lambda: tensor_to_image), _n_(531560, "stylized_image", lambda: stylized_image))
_l_(531562)


file_name = 'stylized-image5.png'
_l_(531563)
_c_(531569, _a_(531567, _c_(531566, _n_(531564, "tensor_to_image", lambda: tensor_to_image), _n_(531565, "stylized_image", lambda: stylized_image)), "save"), _n_(531568, "file_name", lambda: file_name))
_l_(531570)