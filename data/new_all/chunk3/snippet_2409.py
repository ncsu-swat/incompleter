# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45692594/opencv-fisherfacerecognizers-train-function-shows-typeerror-src-is-not-a-num
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fishface = _c_(526692, _a_(526691, _a_(526690, _n_(526689, "cv2", lambda: cv2), "face"), "createFisherFaceRecognizer"))
_l_(526693)
emotions = ["True", "Glasses"]
_l_(526694)

detector = _c_(526697, _a_(526696, _n_(526695, "dlib", lambda: dlib), "get_frontal_face_detector"))
_l_(526698)
predictor = _c_(526701, _a_(526700, _n_(526699, "dlib", lambda: dlib), "shape_predictor"), "shape_predictor_68_face_landmarks.dat")
_l_(526702)

def get_landmarks(image):
    _l_(526863)

    gray = _c_(526708, _a_(526704, _n_(526703, "cv2", lambda: cv2), "cvtColor"), _n_(526705, "image", lambda: image), _a_(526707, _n_(526706, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
    _l_(526709)
    clahe = _c_(526712, _a_(526711, _n_(526710, "cv2", lambda: cv2), "createCLAHE"), clipLimit=2.0, tileGridSize=(8, 8))
    _l_(526713)
    cimage = _c_(526717, _a_(526715, _n_(526714, "clahe", lambda: clahe), "apply"), _n_(526716, "gray", lambda: gray))
    _l_(526718)
    detections = _c_(526721, _n_(526719, "detector", lambda: detector), _n_(526720, "cimage", lambda: cimage), 1)
    _l_(526722)
    landmarks_vectorised = []
    _l_(526723)
    for k, d in _c_(526726, _n_(526724, "enumerate", lambda: enumerate), _n_(526725, "detections", lambda: detections)):
        _l_(526860)


        shape = _c_(526730, _n_(526727, "predictor", lambda: predictor), _n_(526728, "cimage", lambda: cimage), _n_(526729, "d", lambda: d))  # Draw Facial Landmarks with the predictor class
        _l_(526731)  # Draw Facial Landmarks with the predictor class
        xlist = []
        _l_(526732)
        ylist = []
        _l_(526733)
        for i in _c_(526735, _n_(526734, "range", lambda: range), 1, 68):
            _l_(526758)

            _c_(526745, _a_(526737, _n_(526736, "xlist", lambda: xlist), "append"), _c_(526744, _n_(526738, "float", lambda: float), _a_(526743, _c_(526742, _a_(526740, _n_(526739, "shape", lambda: shape), "part"), _n_(526741, "i", lambda: i)), "x")))
            _l_(526746)
            _c_(526756, _a_(526748, _n_(526747, "ylist", lambda: ylist), "append"), _c_(526755, _n_(526749, "float", lambda: float), _a_(526754, _c_(526753, _a_(526751, _n_(526750, "shape", lambda: shape), "part"), _n_(526752, "i", lambda: i)), "y")))
            _l_(526757)

        xmean = _c_(526762, _a_(526760, _n_(526759, "np", lambda: np), "mean"), _n_(526761, "xlist", lambda: xlist))  # Get the mean of both axes to determine centre of gravity
        _l_(526763)  # Get the mean of both axes to determine centre of gravity
        ymean = _c_(526767, _a_(526765, _n_(526764, "np", lambda: np), "mean"), _n_(526766, "ylist", lambda: ylist))
        _l_(526768)
        xcentral = [(_n_(526769, "x", lambda: x) - _n_(526770, "xmean", lambda: xmean)) for x in _n_(526771, "xlist", lambda: xlist)]  # get distance between each point and the central point in both axes
        _l_(526772)  # get distance between each point and the central point in both axes
        ycentral = [(_n_(526773, "y", lambda: y) - _n_(526774, "ymean", lambda: ymean)) for y in _n_(526775, "ylist", lambda: ylist)]
        _l_(526776)

        if _n_(526777, "xlist", lambda: xlist)[26] == _n_(526778, "xlist", lambda: xlist)[
            29]:
            _l_(526792)

            anglenose = 0
            _l_(526779)
        else:
            anglenose = _c_(526790, _n_(526780, "int", lambda: int), _c_(526787, _a_(526782, _n_(526781, "math", lambda: math), "atan"), (_n_(526783, "ylist", lambda: ylist)[26] - _n_(526784, "ylist", lambda: ylist)[29]) / (_n_(526785, "xlist", lambda: xlist)[26] - _n_(526786, "xlist", lambda: xlist)[29])) * 180 / _a_(526789, _n_(526788, "math", lambda: math), "pi"))
            _l_(526791)

        if _n_(526793, "anglenose", lambda: anglenose) < 0:
            _l_(526796)

            anglenose += 90
            _l_(526794)
        else:
            anglenose -= 90
            _l_(526795)

        landmarks_vectorised = []
        _l_(526797)

        if _c_(526800, _n_(526798, "len", lambda: len), _n_(526799, "detections", lambda: detections)) < 1:
            _l_(526802)

            landmarks_vectorised = "error"
            _l_(526801)

        for x, y, w, z in _c_(526808, _n_(526803, "zip", lambda: zip), _n_(526804, "xcentral", lambda: xcentral), _n_(526805, "ycentral", lambda: ycentral), _n_(526806, "xlist", lambda: xlist), _n_(526807, "ylist", lambda: ylist)):
            _l_(526859)

            _c_(526812, _a_(526810, _n_(526809, "landmarks_vectorised", lambda: landmarks_vectorised), "append"), _n_(526811, "x", lambda: x))
            _l_(526813)
            _c_(526817, _a_(526815, _n_(526814, "landmarks_vectorised", lambda: landmarks_vectorised), "append"), _n_(526816, "y", lambda: y))
            _l_(526818)
            meannp = _c_(526823, _a_(526820, _n_(526819, "np", lambda: np), "asarray"), (_n_(526821, "ymean", lambda: ymean), _n_(526822, "xmean", lambda: xmean)))
            _l_(526824)
            coornp = _c_(526829, _a_(526826, _n_(526825, "np", lambda: np), "asarray"), (_n_(526827, "z", lambda: z), _n_(526828, "w", lambda: w)))
            _l_(526830)
            dist = _c_(526836, _a_(526833, _a_(526832, _n_(526831, "np", lambda: np), "linalg"), "norm"), _n_(526834, "coornp", lambda: coornp) - _n_(526835, "meannp", lambda: meannp))
            _l_(526837)
            anglerelative = (_c_(526844, _a_(526839, _n_(526838, "math", lambda: math), "atan"), (_n_(526840, "z", lambda: z) - _n_(526841, "ymean", lambda: ymean)) / (_n_(526842, "w", lambda: w) - _n_(526843, "xmean", lambda: xmean))) * 180 / _a_(526846, _n_(526845, "math", lambda: math), "pi")) - _n_(526847, "anglenose", lambda: anglenose)
            _l_(526848)
            _c_(526852, _a_(526850, _n_(526849, "landmarks_vectorised", lambda: landmarks_vectorised), "append"), _n_(526851, "dist", lambda: dist))
            _l_(526853)
            _c_(526857, _a_(526855, _n_(526854, "landmarks_vectorised", lambda: landmarks_vectorised), "append"), _n_(526856, "anglerelative", lambda: anglerelative))
            _l_(526858)
    aux = _n_(526861, "landmarks_vectorised", lambda: landmarks_vectorised)
    _l_(526862)
    return aux


def make_sets(labels):
    _l_(526930)

    training_data = []
    _l_(526864)
    training_labels = []
    _l_(526865)
    for label in _n_(526866, "labels", lambda: labels):
        _l_(526923)

        training = _c_(526870, _a_(526868, _n_(526867, "glob", lambda: glob), "glob"), "data\\%s\\*" % _n_(526869, "label", lambda: label))
        _l_(526871)
        _c_(526876, _n_(526872, "print", lambda: print), _c_(526875, _n_(526873, "len", lambda: len), _n_(526874, "training", lambda: training)))
        _l_(526877)

        for item in _n_(526878, "training", lambda: training):
            _l_(526922)

            try:
                _l_(526886)

                image = _c_(526882, _a_(526880, _n_(526879, "cv2", lambda: cv2), "imread"), _n_(526881, "item", lambda: item))
                _l_(526883)
            except:
                _l_(526885)

                continue
                _l_(526884)
            _c_(526889, _n_(526887, "print", lambda: print), _n_(526888, "item", lambda: item))
            _l_(526890)

            landmarks_vectorised = _c_(526893, _n_(526891, "get_landmarks", lambda: get_landmarks), _n_(526892, "image", lambda: image))
            _l_(526894)

            if _n_(526895, "landmarks_vectorised", lambda: landmarks_vectorised) == "error":
                _l_(526921)

                _c_(526897, _n_(526896, "print", lambda: print), "error with landmarks")
                _l_(526898)
                pass
                _l_(526899)
            else:
                _c_(526903, _a_(526901, _n_(526900, "training_data", lambda: training_data), "append"), _n_(526902, "landmarks_vectorised", lambda: landmarks_vectorised))
                _l_(526904)
                if _c_(526907, _n_(526905, "str", lambda: str), _n_(526906, "label", lambda: label)) == "True":
                    _l_(526920)

                    _c_(526910, _a_(526909, _n_(526908, "training_labels", lambda: training_labels), "append"), 2)
                    _l_(526911)
                elif _c_(526914, _n_(526912, "str", lambda: str), _n_(526913, "label", lambda: label)) == "Glasses":
                    _l_(526919)

                    _c_(526917, _a_(526916, _n_(526915, "training_labels", lambda: training_labels), "append"), 1)
                    _l_(526918)

    _c_(526925, _n_(526924, "print", lambda: print), "sets created")
    _l_(526926)
    aux = _n_(526927, "training_data", lambda: training_data), _n_(526928, "training_labels", lambda: training_labels)
    _l_(526929)
    return aux

def make_sets(labels):
    _l_(526997)

    training_data = []
    _l_(526931)
    training_labels = []
    _l_(526932)
    for label in _n_(526933, "labels", lambda: labels):
        _l_(526990)

        training = _c_(526937, _a_(526935, _n_(526934, "glob", lambda: glob), "glob"), "data\\%s\\*" % _n_(526936, "label", lambda: label))
        _l_(526938)
        _c_(526943, _n_(526939, "print", lambda: print), _c_(526942, _n_(526940, "len", lambda: len), _n_(526941, "training", lambda: training)))
        _l_(526944)

        for item in _n_(526945, "training", lambda: training):
            _l_(526989)

            try:
                _l_(526953)

                image = _c_(526949, _a_(526947, _n_(526946, "cv2", lambda: cv2), "imread"), _n_(526948, "item", lambda: item))
                _l_(526950)
            except:
                _l_(526952)

                continue
                _l_(526951)
            _c_(526956, _n_(526954, "print", lambda: print), _n_(526955, "item", lambda: item))
            _l_(526957)

            landmarks_vectorised = _c_(526960, _n_(526958, "get_landmarks", lambda: get_landmarks), _n_(526959, "image", lambda: image))
            _l_(526961)

            if _n_(526962, "landmarks_vectorised", lambda: landmarks_vectorised) == "error":
                _l_(526988)

                _c_(526964, _n_(526963, "print", lambda: print), "error with landmarks")
                _l_(526965)
                pass
                _l_(526966)
            else:
                _c_(526970, _a_(526968, _n_(526967, "training_data", lambda: training_data), "append"), _n_(526969, "landmarks_vectorised", lambda: landmarks_vectorised))
                _l_(526971)
                if _c_(526974, _n_(526972, "str", lambda: str), _n_(526973, "label", lambda: label)) == "True":
                    _l_(526987)

                    _c_(526977, _a_(526976, _n_(526975, "training_labels", lambda: training_labels), "append"), 2)
                    _l_(526978)
                elif _c_(526981, _n_(526979, "str", lambda: str), _n_(526980, "label", lambda: label)) == "Glasses":
                    _l_(526986)

                    _c_(526984, _a_(526983, _n_(526982, "training_labels", lambda: training_labels), "append"), 1)
                    _l_(526985)

    _c_(526992, _n_(526991, "print", lambda: print), "sets created")
    _l_(526993)
    aux = _n_(526994, "training_data", lambda: training_data), _n_(526995, "training_labels", lambda: training_labels)
    _l_(526996)
    return aux


def run_recognizer(emotions):
    _l_(527036)

    training_data, training_labels = _c_(527000, _n_(526998, "make_sets", lambda: make_sets), _n_(526999, "emotions", lambda: emotions))
    _l_(527001)
    _c_(527003, _n_(527002, "print", lambda: print), "training fisher face classifier")
    _l_(527004)
    _c_(527009, _n_(527005, "print", lambda: print), _c_(527008, _n_(527006, "type", lambda: type), _n_(527007, "training_data", lambda: training_data)))
    _l_(527010)
    _c_(527015, _n_(527011, "print", lambda: print), _c_(527014, _n_(527012, "type", lambda: type), _n_(527013, "training_labels", lambda: training_labels)))
    _l_(527016)

    npar_train = _c_(527020, _a_(527018, _n_(527017, "np", lambda: np), "array"), _n_(527019, "training_data", lambda: training_data))
    _l_(527021)
    npar_trainlabs = _c_(527025, _a_(527023, _n_(527022, "np", lambda: np), "array"), _n_(527024, "training_labels", lambda: training_labels))
    _l_(527026)
    _c_(527034, _a_(527028, _n_(527027, "fishface", lambda: fishface), "train"), _c_(527032, _a_(527030, _n_(527029, "np", lambda: np), "array"), _n_(527031, "training_data", lambda: training_data)), _n_(527033, "npar_trainlabs", lambda: npar_trainlabs))
    _l_(527035)

def update(emotions):
    _l_(527045)

    _c_(527039, _n_(527037, "run_recognizer", lambda: run_recognizer), _n_(527038, "emotions", lambda: emotions))
    _l_(527040)
    _c_(527043, _a_(527042, _n_(527041, "fishface", lambda: fishface), "save"), "glasses.xml")
    _l_(527044)

_c_(527048, _n_(527046, "update", lambda: update), _n_(527047, "emotions", lambda: emotions))
_l_(527049)