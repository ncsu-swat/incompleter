# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66431069/sending-opencv-image-via-flask-socketio-to-client-causes-typeerror-object-of-ty
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
image = _c_(475631, _a_(475630, _c_(475629, _a_(475627, '{}', "format"), _n_(475628, "image64", lambda: image64)), "split"), ',')[1]
_l_(475632)

im_bytes = _c_(475636, _a_(475634, _n_(475633, "base64", lambda: base64), "b64decode"), _n_(475635, "image", lambda: image))
_l_(475637)
im_arr = _c_(475643, _a_(475639, _n_(475638, "np", lambda: np), "frombuffer"), _n_(475640, "im_bytes", lambda: im_bytes), dtype=_a_(475642, _n_(475641, "np", lambda: np), "uint8"))  # im_arr is one-dim Numpy array
_l_(475644)  # im_arr is one-dim Numpy array
frame = _c_(475650, _a_(475646, _n_(475645, "cv2", lambda: cv2), "imdecode"), _n_(475647, "im_arr", lambda: im_arr), flags=_a_(475649, _n_(475648, "cv2", lambda: cv2), "IMREAD_COLOR"))
_l_(475651)