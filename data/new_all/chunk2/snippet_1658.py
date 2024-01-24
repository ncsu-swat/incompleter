# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66431069/sending-opencv-image-via-flask-socketio-to-client-causes-typeerror-object-of-ty
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
encode_param = [_c_(453183, _n_(453180, "int", lambda: int), _a_(453182, _n_(453181, "cv2", lambda: cv2), "IMWRITE_JPEG_QUALITY")), 90]
_l_(453184)
result, encimg = _c_(453189, _a_(453186, _n_(453185, "cv2", lambda: cv2), "imencode"), '.jpg', _n_(453187, "updated_frame", lambda: updated_frame), _n_(453188, "encode_param", lambda: encode_param))
_l_(453190)
_c_(453194, _a_(453192, _n_(453191, "socketio", lambda: socketio), "emit"), 'response_back', {'image_data': _n_(453193, "encimg", lambda: encimg)}, namespace='/test')
_l_(453195)