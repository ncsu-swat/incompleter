# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63984206/tensorflow-2-3-typeerror-fetch-argument-none-has-invalid-type-class-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(582843, _a_(582842, _a_(582841, _a_(582840, _n_(582839, "tf", lambda: tf), "compat"), "v1"), "Session")) as test_b:
    _l_(582916)

    yolo_outputs = (_c_(582847, _a_(582846, _a_(582845, _n_(582844, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 1], mean=1, stddev=4, seed = 1),
                    _c_(582851, _a_(582850, _a_(582849, _n_(582848, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 2], mean=1, stddev=4, seed = 1),
                    _c_(582855, _a_(582854, _a_(582853, _n_(582852, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 2], mean=1, stddev=4, seed = 1),
                    _c_(582859, _a_(582858, _a_(582857, _n_(582856, "tf", lambda: tf), "random"), "normal"), [19, 19, 5, 80], mean=1, stddev=4, seed = 1))
    _l_(582860)
    scores, boxes, classes = _c_(582863, _n_(582861, "yolo_eval", lambda: yolo_eval), _n_(582862, "yolo_outputs", lambda: yolo_outputs))
    _l_(582864)
    _c_(582871, _n_(582865, "print", lambda: print), "scores[2] = " + _c_(582870, _n_(582866, "str", lambda: str), _c_(582869, _a_(582868, _n_(582867, "scores", lambda: scores)[2], "eval"))))
    _l_(582872)
    _c_(582879, _n_(582873, "print", lambda: print), "boxes[2] = " + _c_(582878, _n_(582874, "str", lambda: str), _c_(582877, _a_(582876, _n_(582875, "boxes", lambda: boxes)[2], "eval"))))
    _l_(582880)
    _c_(582887, _n_(582881, "print", lambda: print), "classes[2] = " + _c_(582886, _n_(582882, "str", lambda: str), _c_(582885, _a_(582884, _n_(582883, "classes", lambda: classes)[2], "eval"))))
    _l_(582888)
    _c_(582896, _n_(582889, "print", lambda: print), "scores.shape = " + _c_(582895, _n_(582890, "str", lambda: str), _a_(582894, _c_(582893, _a_(582892, _n_(582891, "scores", lambda: scores), "eval")), "shape")))
    _l_(582897)
    _c_(582905, _n_(582898, "print", lambda: print), "boxes.shape = " + _c_(582904, _n_(582899, "str", lambda: str), _a_(582903, _c_(582902, _a_(582901, _n_(582900, "boxes", lambda: boxes), "eval")), "shape")))
    _l_(582906)
    _c_(582914, _n_(582907, "print", lambda: print), "classes.shape = " + _c_(582913, _n_(582908, "str", lambda: str), _a_(582912, _c_(582911, _a_(582910, _n_(582909, "classes", lambda: classes), "eval")), "shape")))
    _l_(582915)