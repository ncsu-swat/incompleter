# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55536101/typeerror-cannot-concatenate-str-and-int-objects-in-face-detection-using-ha
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(534699)

except ImportError:
    pass
cam = _c_(534702, _a_(534701, _n_(534700, "cv2", lambda: cv2), "VideoCapture"), 0)
_l_(534703)
detector=_c_(534706, _a_(534705, _n_(534704, "cv2", lambda: cv2), "CascadeClassifier"), 'haarcascade_frontalface_default.xml')
_l_(534707)

Id=_c_(534709, _n_(534708, "input", lambda: input), 'enter your id....')
_l_(534710)
sampleNum=0
_l_(534711)
while(True):
    _l_(534773)

    ret, img = _c_(534714, _a_(534713, _n_(534712, "cam", lambda: cam), "read"))
    _l_(534715)
    gray = _c_(534721, _a_(534717, _n_(534716, "cv2", lambda: cv2), "cvtColor"), _n_(534718, "img", lambda: img), _a_(534720, _n_(534719, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
    _l_(534722)
    faces = _c_(534726, _a_(534724, _n_(534723, "detector", lambda: detector), "detectMultiScale"), _n_(534725, "gray", lambda: gray), 1.3, 5)
    _l_(534727)
    for (x, y, w, h) in _n_(534728, "faces", lambda: faces):
        _l_(534762)

        _c_(534738, _a_(534730, _n_(534729, "cv2", lambda: cv2), "rectangle"), _n_(534731, "img", lambda: img), (_n_(534732, "x", lambda: x), _n_(534733, "y", lambda: y)), (_n_(534734, "x", lambda: x)+_n_(534735, "w", lambda: w), _n_(534736, "y", lambda: y)+_n_(534737, "h", lambda: h)), (255, 0, 0), 2)
        _l_(534739)

        sampleNum=_n_(534740, "sampleNum", lambda: sampleNum)+1
        _l_(534741)
        _c_(534755, _a_(534743, _n_(534742, "cv2", lambda: cv2), "imwrite"), "dataSet/User."+_n_(534744, "Id", lambda: Id) +'.'+ _c_(534747, _n_(534745, "str", lambda: str), _n_(534746, "sampleNum", lambda: sampleNum)) + ".jpg", _n_(534748, "gray", lambda: gray)[_n_(534749, "y", lambda: y):_n_(534750, "y", lambda: y)+_n_(534751, "h", lambda: h),_n_(534752, "x", lambda: x):_n_(534753, "x", lambda: x)+_n_(534754, "w", lambda: w)])
        _l_(534756)
        _c_(534760, _a_(534758, _n_(534757, "cv2", lambda: cv2), "imshow"), 'frame',_n_(534759, "img", lambda: img))
        _l_(534761)
    #wait for 100 miliseconds 
    if _c_(534765, _a_(534764, _n_(534763, "cv2", lambda: cv2), "waitKey"), 100) & 0xFF == _c_(534767, _n_(534766, "ord", lambda: ord), 'q'):
        _l_(534772)

        break
        _l_(534768)
    # break if the sample number is morethan 20
    elif _n_(534769, "sampleNum", lambda: sampleNum)>20:
        _l_(534771)

        break
        _l_(534770)
_c_(534776, _a_(534775, _n_(534774, "cam", lambda: cam), "release"))
_l_(534777)
_c_(534780, _a_(534779, _n_(534778, "cv2", lambda: cv2), "destroyAllWindows"))
_l_(534781)