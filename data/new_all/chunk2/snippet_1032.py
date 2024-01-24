# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52125954/nameerror-name-classifier-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import numpy as np
  _l_(454741)

except ImportError:
  pass
try:
  from keras.preprocessing import image
  _l_(454743)

except ImportError:
  pass
test_image = _c_(454746, _a_(454745, _n_(454744, "image", lambda: image), "load_img"), 'dataset/single_prediction/1.jpg', target_size = (64, 64))
_l_(454747)
test_image = _c_(454751, _a_(454749, _n_(454748, "image", lambda: image), "img_to_array"), _n_(454750, "test_image", lambda: test_image))
_l_(454752)
test_image = _c_(454756, _a_(454754, _n_(454753, "np", lambda: np), "expand_dims"), _n_(454755, "test_image", lambda: test_image), axis = 0)
_l_(454757)
result = _c_(454761, _a_(454759, _n_(454758, "classifier", lambda: classifier), "predict"), _n_(454760, "test_image", lambda: test_image))
_l_(454762)
_a_(454764, _n_(454763, "training_set", lambda: training_set), "class_indices")
_l_(454765)
if _n_(454766, "result", lambda: result)[0][0] == 1:
  _l_(454769)

  prediction = 'nsfw'
  _l_(454767)
else:
  prediction = 'sfw'
  _l_(454768)