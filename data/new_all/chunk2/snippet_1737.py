# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59729859/python-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data_list = _c_(468405, _n_(468404, "glob", lambda: glob), 'dataset\\training\\*\\*.jpg')
_l_(468406)
def _load_img():
    _l_(468424)


    for v in _n_(468407, "data_list", lambda: data_list):
        _l_(468421)

   #     print("Converting " + v + " to NumPy Array ...")       
        data = _c_(468414, _a_(468409, _n_(468408, "np", lambda: np), "array"), _c_(468413, _a_(468411, _n_(468410, "Image", lambda: Image), "open"), _n_(468412, "v", lambda: v)))
        _l_(468415)
        data = _c_(468419, _a_(468417, _n_(468416, "data", lambda: data), "reshape"), -1, _n_(468418, "img_size", lambda: img_size))
        _l_(468420)
    aux = _n_(468422, "data", lambda: data)
    _l_(468423)

    return aux

def _load_label():
    _l_(468437)

    labels = []
    _l_(468425)
    for path in _n_(468426, "data_list", lambda: data_list):
        _l_(468434)

        _c_(468432, _a_(468428, _n_(468427, "labels", lambda: labels), "append"), _c_(468431, _n_(468429, "get_label_from_path", lambda: get_label_from_path), _n_(468430, "path", lambda: path)))
        _l_(468433)
    aux = _n_(468435, "labels", lambda: labels)
    _l_(468436)

    return aux