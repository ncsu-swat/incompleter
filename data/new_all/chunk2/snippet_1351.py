# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76026737/attributeerror-str-object-has-no-attribute-decode-when-loading-tensorflow-h
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(452428)

except ImportError:
    pass
try:
    import cv2
    _l_(452430)

except ImportError:
    pass
try:
    from tensorflow.keras.models import load_model
    _l_(452432)

except ImportError:
    pass
model = _c_(452434, _n_(452433, "load_model", lambda: load_model), "my_model_new.h5")
_l_(452435)

while True:
    _l_(452514)

    success, imgOriginal = _c_(452438, _a_(452437, _n_(452436, "cap", lambda: cap), "read"))
    _l_(452439)
    img = _c_(452443, _a_(452441, _n_(452440, "np", lambda: np), "asarray"), _n_(452442, "imgOriginal", lambda: imgOriginal))
    _l_(452444)
    img = _c_(452448, _a_(452446, _n_(452445, "cv2", lambda: cv2), "resize"), _n_(452447, "img", lambda: img), (32, 32))
    _l_(452449)
    img = _c_(452452, _n_(452450, "preprocessing", lambda: preprocessing), _n_(452451, "img", lambda: img))
    _l_(452453)
    _c_(452457, _a_(452455, _n_(452454, "cv2", lambda: cv2), "imshow"), "Processed Image", _n_(452456, "img", lambda: img))
    _l_(452458)
    img = _c_(452461, _a_(452460, _n_(452459, "img", lambda: img), "reshape"), 1, 32, 32, 1)
    _l_(452462)

    predictions = _c_(452466, _a_(452464, _n_(452463, "model", lambda: model), "predict"), _n_(452465, "img", lambda: img))
    _l_(452467)
    classIndex = _c_(452471, _a_(452469, _n_(452468, "np", lambda: np), "argmax"), _n_(452470, "predictions", lambda: predictions))
    _l_(452472)

    predictions = _c_(452476, _a_(452474, _n_(452473, "model", lambda: model), "predict"), _n_(452475, "img", lambda: img))
    _l_(452477)
    probVal= _c_(452481, _a_(452479, _n_(452478, "np", lambda: np), "amax"), _n_(452480, "predictions", lambda: predictions))
    _l_(452482)
    if _n_(452483, "probVal", lambda: probVal) > _n_(452484, "threshold", lambda: threshold):
        _l_(452506)

        _c_(452499, _a_(452486, _n_(452485, "cv2", lambda: cv2), "putText"), _n_(452487, "imgOriginal", lambda: imgOriginal), _c_(452492, _n_(452488, "str", lambda: str), _c_(452491, _n_(452489, "getClassName", lambda: getClassName), _n_(452490, "classIndex", lambda: classIndex)))+" "+ _c_(452495, _n_(452493, "str", lambda: str), _n_(452494, "probVal", lambda: probVal)),(50,50),_n_(452496, "font", lambda: font),1,(0,0,255),1,_a_(452498, _n_(452497, "cv2", lambda: cv2), "LINE_AA"))
        _l_(452500)
        _c_(452504, _a_(452502, _n_(452501, "cv2", lambda: cv2), "imshow"), "Original Image", _n_(452503, "imgOriginal", lambda: imgOriginal))
        _l_(452505)

    if _c_(452509, _a_(452508, _n_(452507, "cv2", lambda: cv2), "waitKey"), 1) and 0xFF == _c_(452511, _n_(452510, "ord", lambda: ord), 'q'):
        _l_(452513)

        break
        _l_(452512)