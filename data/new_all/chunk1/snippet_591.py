# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54284937/python-typeerror-umat-missing-required-argument-ranges-pos-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def detect_face(img):
    _l_(400038)

    imgUMat = _c_(399997, _a_(399995, _n_(399994, "cv2", lambda: cv2), "UMat"), _n_(399996, "img", lambda: img))
    _l_(399998)
    gray = _c_(400004, _a_(400000, _n_(399999, "cv2", lambda: cv2), "cvtColor"), _n_(400001, "imgUMat", lambda: imgUMat), _a_(400003, _n_(400002, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
    _l_(400005)
    face_cascade = _c_(400011, _a_(400007, _n_(400006, "cv2", lambda: cv2), "CascadeClassifier"), _a_(400010, _a_(400009, _n_(400008, "cv2", lambda: cv2), "data"), "haarcascades") + "haarcascade_frontalface_default.xml")
    _l_(400012)
    faces = _c_(400016, _a_(400014, _n_(400013, "face_cascade", lambda: face_cascade), "detectMultiScale"), _n_(400015, "gray", lambda: gray), scaleFactor=1.2, minNeighbors=5)
    _l_(400017)
    if (_c_(400020, _n_(400018, "len", lambda: len), _n_(400019, "faces", lambda: faces))==0):
        _l_(400022)

        aux = None, None
        _l_(400021)
        return aux
    (x, y, w, h) = _n_(400023, "faces", lambda: faces)[0]
    _l_(400024)
    gray = _c_(400027, _a_(400026, _n_(400025, "gray", lambda: gray), "get"))
    _l_(400028)
    aux = _n_(400029, "gray", lambda: gray)[_n_(400030, "y", lambda: y):_n_(400031, "y", lambda: y)+_n_(400032, "h", lambda: h),_n_(400033, "x", lambda: x):_n_(400034, "x", lambda: x)+_n_(400035, "w", lambda: w)], _n_(400036, "faces", lambda: faces)[0]
    _l_(400037)
    return aux

def prepare_training_data():
    _l_(400067)

    faces = []
    _l_(400039)
    labels = []
    _l_(400040)
    for img in _n_(400041, "photo_name_list", lambda: photo_name_list):
        _l_(400063)

        image = _c_(400045, _a_(400043, _n_(400042, "cv2", lambda: cv2), "imread"), _n_(400044, "img", lambda: img))
        _l_(400046)
        face, rect = _c_(400049, _n_(400047, "detect_face", lambda: detect_face), _n_(400048, "image", lambda: image))
        _l_(400050)
        if _n_(400051, "face", lambda: face) is not None:
            _l_(400062)

            _c_(400055, _a_(400053, _n_(400052, "faces", lambda: faces), "append"), _n_(400054, "face", lambda: face))
            _l_(400056)
            _c_(400060, _a_(400058, _n_(400057, "labels", lambda: labels), "append"), _n_(400059, "me", lambda: me))
            _l_(400061)
    aux = _n_(400064, "faces", lambda: faces), _n_(400065, "labels", lambda: labels)
    _l_(400066)
    return aux

def test_photos():
    _l_(400106)

    face_recognizer = _c_(400071, _a_(400070, _a_(400069, _n_(400068, "cv2", lambda: cv2), "face"), "LBPHFaceRecognizer_create"))
    _l_(400072)
    faces, labels = _c_(400074, _n_(400073, "prepare_training_data", lambda: prepare_training_data))
    _l_(400075)
    _c_(400086, _a_(400077, _n_(400076, "face_recognizer", lambda: face_recognizer), "train"), _c_(400081, _a_(400079, _n_(400078, "np", lambda: np), "array"), _n_(400080, "faces", lambda: faces)), _c_(400085, _a_(400083, _n_(400082, "np", lambda: np), "array"), _n_(400084, "labels", lambda: labels)))
    _l_(400087)
    face, rect = _c_(400090, _n_(400088, "detect_face", lambda: detect_face), _n_(400089, "test_photo", lambda: test_photo))
    _l_(400091)
    label = _c_(400095, _a_(400093, _n_(400092, "face_recognizer", lambda: face_recognizer), "predict"), _n_(400094, "face", lambda: face))
    _l_(400096)
    if _n_(400097, "label", lambda: label) == _n_(400098, "me", lambda: me):
        _l_(400105)

        _c_(400100, _n_(400099, "print", lambda: print), "it's me")
        _l_(400101)
    else:
        _c_(400103, _n_(400102, "print", lambda: print), "it's not me")
        _l_(400104)


_c_(400108, _n_(400107, "test_photos", lambda: test_photos))
_l_(400109)