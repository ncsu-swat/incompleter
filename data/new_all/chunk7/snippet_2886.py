# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59774035/attributeerror-tensor-object-has-no-attribute-numpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
DATADIR = r"C:\Users\angesu\Desktop\DOCUMENT_DATA"
_l_(558998)

CATEGORIES = ["resume","transcript","certificate"]
_l_(558999)
IMG_SIZE = 250
_l_(559000)

for category in _n_(559001, "CATEGORIES", lambda: CATEGORIES) :
    _l_(559026)

    path = _c_(559007, _a_(559004, _a_(559003, _n_(559002, "os", lambda: os), "path"), "join"), _n_(559005, "DATADIR", lambda: DATADIR), _n_(559006, "category", lambda: category))
    _l_(559008)
    for img in _c_(559012, _a_(559010, _n_(559009, "os", lambda: os), "listdir"), _n_(559011, "path", lambda: path)):
        _l_(559025)

        img_array = _c_(559023, _a_(559014, _n_(559013, "cv2", lambda: cv2), "imread"), _c_(559020, _a_(559017, _a_(559016, _n_(559015, "os", lambda: os), "path"), "join"), _n_(559018, "path", lambda: path), _n_(559019, "img", lambda: img)), _a_(559022, _n_(559021, "cv2", lambda: cv2), "IMREAD_GRAYSCALE"))
        _l_(559024)

training_data = []
_l_(559027)
def create_training_data():
    _l_(559076)

    for category in _n_(559028, "CATEGORIES", lambda: CATEGORIES) :
        _l_(559075)

        path = _c_(559034, _a_(559031, _a_(559030, _n_(559029, "os", lambda: os), "path"), "join"), _n_(559032, "DATADIR", lambda: DATADIR), _n_(559033, "category", lambda: category))
        _l_(559035)
        class_num = _c_(559039, _a_(559037, _n_(559036, "CATEGORIES", lambda: CATEGORIES), "index"), _n_(559038, "category", lambda: category))
        _l_(559040)
        for img in _c_(559044, _a_(559042, _n_(559041, "os", lambda: os), "listdir"), _n_(559043, "path", lambda: path)):
            _l_(559074)

            try :
                _l_(559073)

                img_array = _c_(559055, _a_(559046, _n_(559045, "cv2", lambda: cv2), "imread"), _c_(559052, _a_(559049, _a_(559048, _n_(559047, "os", lambda: os), "path"), "join"), _n_(559050, "path", lambda: path), _n_(559051, "img", lambda: img)), _a_(559054, _n_(559053, "cv2", lambda: cv2), "IMREAD_GRAYSCALE"))
                _l_(559056)
                new_array = _c_(559062, _a_(559058, _n_(559057, "cv2", lambda: cv2), "resize"), _n_(559059, "img_array", lambda: img_array), (_n_(559060, "IMG_SIZE", lambda: IMG_SIZE), _n_(559061, "IMG_SIZE", lambda: IMG_SIZE)))
                _l_(559063)
                _c_(559068, _a_(559065, _n_(559064, "training_data", lambda: training_data), "append"), [_n_(559066, "new_array", lambda: new_array), _n_(559067, "class_num", lambda: class_num)])
                _l_(559069)
            except _n_(559070, "Exception", lambda: Exception) as e:
                _l_(559072)

                pass
                _l_(559071)
_c_(559078, _n_(559077, "create_training_data", lambda: create_training_data))
_l_(559079)
_c_(559083, _a_(559081, _n_(559080, "random", lambda: random), "shuffle"), _n_(559082, "training_data", lambda: training_data))
_l_(559084)

X = [] #features
_l_(559085) #features
y = [] #labels
_l_(559086) #labels
for features, label in _n_(559087, "training_data", lambda: training_data):
    _l_(559098)

    _c_(559091, _a_(559089, _n_(559088, "X", lambda: X), "append"), _n_(559090, "features", lambda: features))
    _l_(559092)
    _c_(559096, _a_(559094, _n_(559093, "y", lambda: y), "append"), _n_(559095, "label", lambda: label))
    _l_(559097)

X = _c_(559106, _a_(559103, _c_(559102, _a_(559100, _n_(559099, "np", lambda: np), "asarray"), _n_(559101, "X", lambda: X)), "reshape"), -1, _n_(559104, "IMG_SIZE", lambda: IMG_SIZE), _n_(559105, "IMG_SIZE", lambda: IMG_SIZE), 1)
_l_(559107)

clf = _c_(559110, _a_(559109, _n_(559108, "ak", lambda: ak), "ImageClassifier"), max_trials=10)
_l_(559111)
_c_(559116, _a_(559113, _n_(559112, "clf", lambda: clf), "fit"), _n_(559114, "X", lambda: X),_n_(559115, "y", lambda: y),validation_split=0.1)
_l_(559117)

def prepare(file):
    _l_(559139)

    IMG_SIZE = 250
    _l_(559118)
    img_array = _c_(559124, _a_(559120, _n_(559119, "cv2", lambda: cv2), "imread"), _n_(559121, "file", lambda: file), _a_(559123, _n_(559122, "cv2", lambda: cv2), "IMREAD_GRAYSCALE"))
    _l_(559125)
    new_array = _c_(559131, _a_(559127, _n_(559126, "cv2", lambda: cv2), "resize"), _n_(559128, "img_array", lambda: img_array), (_n_(559129, "IMG_SIZE", lambda: IMG_SIZE), _n_(559130, "IMG_SIZE", lambda: IMG_SIZE)))
    _l_(559132)
    aux = _c_(559137, _a_(559134, _n_(559133, "new_array", lambda: new_array), "reshape"), -1, _n_(559135, "IMG_SIZE", lambda: IMG_SIZE), _n_(559136, "IMG_SIZE", lambda: IMG_SIZE), 1)
    _l_(559138)
    return aux

path = r"C:\Users\angesu\Downloads\Garn-Certificate-4.jpg"
_l_(559140)

predicted_y = _c_(559146, _a_(559142, _n_(559141, "clf", lambda: clf), "predict"), _c_(559145, _n_(559143, "prepare", lambda: prepare), _n_(559144, "path", lambda: path)))
_l_(559147)

_c_(559153, _n_(559148, "print", lambda: print), _c_(559152, _a_(559150, _n_(559149, "clf", lambda: clf), "evaluate"), _n_(559151, "test_set", lambda: test_set)))
_l_(559154)