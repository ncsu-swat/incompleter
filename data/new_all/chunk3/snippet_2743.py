# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64714925/retrieving-typeerror-nonetype-object-is-not-callable-socket
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
context = _c_(555848, _a_(555847, _n_(555846, "zmq", lambda: zmq), "Context"))
_l_(555849)
footage_socket = _c_(555854, _a_(555851, _n_(555850, "context", lambda: context), "socket"), _a_(555853, _n_(555852, "zmq", lambda: zmq), "PUB"))
_l_(555855)
_c_(555858, _a_(555857, _n_(555856, "footage_socket", lambda: footage_socket), "connect"), 'tcp://172.168.1.2:5555')
_l_(555859)
videoFile = 'data.mp4'
_l_(555860)
camera = _c_(555864, _a_(555862, _n_(555861, "cv2", lambda: cv2), "VideoCapture"), _n_(555863, "videoFile", lambda: videoFile)) 
_l_(555865) 
length=_c_(555872, _n_(555866, "int", lambda: int), _c_(555871, _a_(555868, _n_(555867, "camera", lambda: camera), "get"), _a_(555870, _n_(555869, "cv2", lambda: cv2), "CAP_PROP_FRAME_COUNT")))
_l_(555873)
while True:
  _l_(555903)

  grabbed, frame = _c_(555876, _a_(555875, _n_(555874, "camera", lambda: camera), "read"))
  _l_(555877)
  try:
    _l_(555887)

    frame = _c_(555881, _a_(555879, _n_(555878, "cv2", lambda: cv2), "resize"), _n_(555880, "frame", lambda: frame), (224, 224))
    _l_(555882)
  except _a_(555884, _n_(555883, "cv2", lambda: cv2), "error"):
    _l_(555886)

    break
    _l_(555885)
  encoded, buffer = _c_(555891, _a_(555889, _n_(555888, "cv2", lambda: cv2), "imencode"), '.jpg', _n_(555890, "frame", lambda: frame))
  _l_(555892)
  jpg_as_text = _c_(555896, _a_(555894, _n_(555893, "base64", lambda: base64), "b64encode"), _n_(555895, "buffer", lambda: buffer))
  _l_(555897)
  _c_(555901, _a_(555899, _n_(555898, "footage_socket", lambda: footage_socket), "send"), _n_(555900, "jpg_as_text", lambda: jpg_as_text))
  _l_(555902)