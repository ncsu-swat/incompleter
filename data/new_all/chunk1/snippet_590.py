# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58497957/typeerror-structural-similarity-takes-2-positional-arguments-but-8-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
gray1 = _c_(403202, _a_(403198, _n_(403197, "cv2", lambda: cv2), "cvtColor"), _n_(403199, "frame1", lambda: frame1), _a_(403201, _n_(403200, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
_l_(403203)
gray2 = _c_(403209, _a_(403205, _n_(403204, "cv2", lambda: cv2), "cvtColor"), _n_(403206, "frame2", lambda: frame2), _a_(403208, _n_(403207, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
_l_(403210)
(score, diff) = _c_(403214, _n_(403211, "compare_ssim", lambda: compare_ssim), _n_(403212, "gray1", lambda: gray1), _n_(403213, "gray2", lambda: gray2), full=True)
_l_(403215)