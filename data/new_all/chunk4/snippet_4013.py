# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63984206/tensorflow-2-3-typeerror-fetch-argument-none-has-invalid-type-class-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(641654, _a_(641653, _a_(641652, _a_(641651, _n_(641650, "tf", lambda: tf), "compat"), "v1"), "Session")) as test_b:
    _l_(641727)

    yolo_outputs = (_c_(641658, _a_(641657, _a_(641656, _n_(641655, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 1], mean=1, stddev=4, seed = 1),
                    _c_(641662, _a_(641661, _a_(641660, _n_(641659, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 2], mean=1, stddev=4, seed = 1),
                    _c_(641666, _a_(641665, _a_(641664, _n_(641663, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 2], mean=1, stddev=4, seed = 1),
                    _c_(641670, _a_(641669, _a_(641668, _n_(641667, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 80], mean=1, stddev=4, seed = 1))
    _l_(641671)
    scores, boxes, classes = _c_(641674, _n_(641672, "yolo_eval", lambda: yolo_eval), _n_(641673, "yolo_outputs", lambda: yolo_outputs))
    _l_(641675)
    _c_(641682, _n_(641676, "print", lambda: print), "scores[2] = " + _c_(641681, _n_(641677, "str", lambda: str), _c_(641680, _a_(641679, _n_(641678, "scores", lambda: scores)[2], "eval"))))
    _l_(641683)
    _c_(641690, _n_(641684, "print", lambda: print), "boxes[2] = " + _c_(641689, _n_(641685, "str", lambda: str), _c_(641688, _a_(641687, _n_(641686, "boxes", lambda: boxes)[2], "eval"))))
    _l_(641691)
    _c_(641698, _n_(641692, "print", lambda: print), "classes[2] = " + _c_(641697, _n_(641693, "str", lambda: str), _c_(641696, _a_(641695, _n_(641694, "classes", lambda: classes)[2], "eval"))))
    _l_(641699)
    _c_(641707, _n_(641700, "print", lambda: print), "scores.shape = " + _c_(641706, _n_(641701, "str", lambda: str), _a_(641705, _c_(641704, _a_(641703, _n_(641702, "scores", lambda: scores), "eval")), "shape")))
    _l_(641708)
    _c_(641716, _n_(641709, "print", lambda: print), "boxes.shape = " + _c_(641715, _n_(641710, "str", lambda: str), _a_(641714, _c_(641713, _a_(641712, _n_(641711, "boxes", lambda: boxes), "eval")), "shape")))
    _l_(641717)
    _c_(641725, _n_(641718, "print", lambda: print), "classes.shape = " + _c_(641724, _n_(641719, "str", lambda: str), _a_(641723, _c_(641722, _a_(641721, _n_(641720, "classes", lambda: classes), "eval")), "shape")))
    _l_(641726)