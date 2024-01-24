# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66156700/typeerror-expected-str-bytes-or-os-pathlike-object-not-inmemoryuploadedfile
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Predict(_a_(573348, _n_(573347, "generics", lambda: generics), "CreateAPIView")):
    _l_(573405)

    serializer_class = ImageSerializer
    _l_(573349)
    def post(self, request):
        _l_(573404)

        """
            post:
            API to send leaf image and get its health status or disease.
        """
        data = _c_(573353, _n_(573350, "ImageSerializer", lambda: ImageSerializer), data=_a_(573352, _n_(573351, "request", lambda: request), "data"))
        _l_(573354)
        if _c_(573357, _a_(573356, _n_(573355, "data", lambda: data), "is_valid")):
            _l_(573403)

            photo = _a_(573359, _n_(573358, "request", lambda: request), "data")['photo']
            _l_(573360)
            img = _c_(573364, _a_(573362, _n_(573361, "image", lambda: image), "load_img"), _n_(573363, "photo", lambda: photo), target_size=(224, 224))
            _l_(573365)
            img = _c_(573369, _a_(573367, _n_(573366, "image", lambda: image), "img_to_array"), _n_(573368, "img", lambda: img))
            _l_(573370)
            img = _c_(573374, _a_(573372, _n_(573371, "np", lambda: np), "expand_dims"), _n_(573373, "img", lambda: img), axis=0)
            _l_(573375)
            img = _n_(573376, "img", lambda: img)/255
            _l_(573377)

            with _c_(573380, _a_(573379, _n_(573378, "graph", lambda: graph), "as_default")):
                _l_(573386)

                prediction = _c_(573384, _a_(573382, _n_(573381, "model", lambda: model), "predict"), _n_(573383, "img", lambda: img))
                _l_(573385)

            prediction_flatten = _c_(573389, _a_(573388, _n_(573387, "prediction", lambda: prediction), "flatten"))
            _l_(573390)
            max_val_index = _c_(573394, _a_(573392, _n_(573391, "np", lambda: np), "argmax"), _n_(573393, "prediction_flatten", lambda: prediction_flatten))
            _l_(573395)
            result = _n_(573396, "output_list", lambda: output_list)[_n_(573397, "max_val_index", lambda: max_val_index)]
            _l_(573398)
            aux = _c_(573401, _n_(573399, "Response", lambda: Response), {'result': _n_(573400, "result", lambda: result)})
            _l_(573402)

            return aux