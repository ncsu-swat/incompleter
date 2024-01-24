# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65463949/getting-type-errorfunction-takes-exactly-6-arguments-5-given-while-using-imag
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i,img in _c_(594870, _n_(594868, "enumerate", lambda: enumerate), _n_(594869, "target_img_path", lambda: target_img_path)):
  _l_(594884)

  tils=_c_(594874, _a_(594872, _n_(594871, "image_slicer", lambda: image_slicer), "slice"), _n_(594873, "img", lambda: img),16)
  _l_(594875)
  _c_(594882, _a_(594877, _n_(594876, "image_slicer", lambda: image_slicer), "save_tiles"), _n_(594878, "tils", lambda: tils), directory='/content/drive/My Drive/tarsplt',prefix=_c_(594881, _a_(594879, '{}', "format"), _n_(594880, "i", lambda: i)) ,format='tiff')
  _l_(594883)