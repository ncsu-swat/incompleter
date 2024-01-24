# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49908246/opencv-typeerror-int-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(401118)

except ImportError:
    pass

faceDetect = _c_(401121, _a_(401120, _n_(401119, "cv2", lambda: cv2), "CascadeClassifier"), 'haarcascade_frontalface_default.xml')
_l_(401122)
cam = _c_(401125, _a_(401124, _n_(401123, "cv2", lambda: cv2), "VideoCapture"), 0)
_l_(401126)
rec = _c_(401130, _a_(401129, _a_(401128, _n_(401127, "cv2", lambda: cv2), "face"), "createLBPHFaceRecognizer"))
_l_(401131)
_c_(401134, _a_(401133, _n_(401132, "rec", lambda: rec), "load"), 'recognizer/trainningData.yml')
_l_(401135)
id = 0
_l_(401136)
font = _a_(401138, _n_(401137, "cv2", lambda: cv2), "FONT_HERSHEY_SIMPLEX")
_l_(401139)
while True:
    _l_(401204)

    ret, img = _c_(401142, _a_(401141, _n_(401140, "cam", lambda: cam), "read"))
    _l_(401143)
    gray = _c_(401149, _a_(401145, _n_(401144, "cv2", lambda: cv2), "cvtColor"), _n_(401146, "img", lambda: img), _a_(401148, _n_(401147, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
    _l_(401150)
    faces = _c_(401154, _a_(401152, _n_(401151, "faceDetect", lambda: faceDetect), "detectMultiScale"), _n_(401153, "gray", lambda: gray), 1.3, 5)
    _l_(401155)
    for (x, y, w, h) in _n_(401156, "faces", lambda: faces):
        _l_(401191)

        _c_(401166, _a_(401158, _n_(401157, "cv2", lambda: cv2), "rectangle"), _n_(401159, "img", lambda: img), (_n_(401160, "x", lambda: x), _n_(401161, "y", lambda: y)), (_n_(401162, "x", lambda: x) + _n_(401163, "w", lambda: w), _n_(401164, "y", lambda: y) + _n_(401165, "h", lambda: h)), (0, 0, 255), 2)
        _l_(401167)
        id, conf = _c_(401177, _a_(401169, _n_(401168, "rec", lambda: rec), "predict"), _n_(401170, "gray", lambda: gray)[_n_(401171, "y", lambda: y):_n_(401172, "y", lambda: y) + _n_(401173, "h", lambda: h), _n_(401174, "x", lambda: x):_n_(401175, "x", lambda: x) + _n_(401176, "w", lambda: w)])
        _l_(401178)
        _c_(401189, _a_(401180, _n_(401179, "cv2", lambda: cv2), "putText"), _n_(401181, "img", lambda: img), _c_(401184, _n_(401182, "str", lambda: str), _n_(401183, "id", lambda: id)), (_n_(401185, "x", lambda: x), _n_(401186, "y", lambda: y) + _n_(401187, "h", lambda: h)), _n_(401188, "font", lambda: font), 255, (255, 0, 0))
        _l_(401190)
    _c_(401195, _a_(401193, _n_(401192, "cv2", lambda: cv2), "imshow"), "Face", _n_(401194, "img", lambda: img))
    _l_(401196)
    if _c_(401199, _a_(401198, _n_(401197, "cv2", lambda: cv2), "waitKey"), 1) == _c_(401201, _n_(401200, "ord", lambda: ord), 'q'):
        _l_(401203)

        break
        _l_(401202)
_c_(401207, _a_(401206, _n_(401205, "cam", lambda: cam), "release"))
_l_(401208)
_c_(401211, _a_(401210, _n_(401209, "cv2", lambda: cv2), "destroyAllWindows"))
_l_(401212)