# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43668452/typeerror-listdir-takes-at-most-1-argument-2-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
mypath2 = _c_(697841, _a_(697840, _a_(697839, _n_(697838, "os", lambda: os), "path"), "join"), 'c:\\trainstcolor2')
_l_(697842)
images2 = _c_(697844, _n_(697843, "list", lambda: list))
_l_(697845)


mypath = _c_(697849, _a_(697848, _a_(697847, _n_(697846, "os", lambda: os), "path"), "join"), 'c:\\trainst2')
_l_(697850)
images = _c_(697852, _n_(697851, "list", lambda: list))
_l_(697853)

for item,item2 in _c_(697858, _a_(697855, _n_(697854, "os", lambda: os), "listdir"), _n_(697856, "mypath", lambda: mypath),_n_(697857, "mypath2", lambda: mypath2)):
   _l_(697891)


   image = _c_(697867, _a_(697860, _n_(697859, "cv2", lambda: cv2), "imread"), _c_(697866, _a_(697863, _a_(697862, _n_(697861, "os", lambda: os), "path"), "join"), _n_(697864, "mypath", lambda: mypath), _n_(697865, "item", lambda: item)))
   _l_(697868)
   image2 = _c_(697877, _a_(697870, _n_(697869, "cv2", lambda: cv2), "imread"), _c_(697876, _a_(697873, _a_(697872, _n_(697871, "os", lambda: os), "path"), "join"), _n_(697874, "mypath2", lambda: mypath2), _n_(697875, "item2", lambda: item2)))
   _l_(697878)

   if _n_(697879, "image", lambda: image) is not None:
      _l_(697890)


      _c_(697883, _a_(697881, _n_(697880, "images", lambda: images), "append"), _n_(697882, "image", lambda: image))
      _l_(697884)
      _c_(697888, _a_(697886, _n_(697885, "images2", lambda: images2), "append"), _n_(697887, "image2", lambda: image2))
      _l_(697889)