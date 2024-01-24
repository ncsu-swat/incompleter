# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60612655/attribute-error-running-opencv-and-imutils
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
image = _c_(648759, _a_(648758, _n_(648757, "cv2", lambda: cv2), "imread"), "jp.png")
_l_(648760)
(h, w, d) = _a_(648762, _n_(648761, "image", lambda: image), "shape")
_l_(648763)
_c_(648770, _n_(648764, "print", lambda: print), _c_(648769, _a_(648765, "width={}, height={}, depth={}", "format"), _n_(648766, "w", lambda: w), _n_(648767, "h", lambda: h), _n_(648768, "d", lambda: d)))
_l_(648771)
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
_c_(648775, _a_(648773, _n_(648772, "cv2", lambda: cv2), "imshow"), "Image", _n_(648774, "image", lambda: image))
_l_(648776)
_c_(648779, _a_(648778, _n_(648777, "cv2", lambda: cv2), "waitKey"), 0)
_l_(648780)