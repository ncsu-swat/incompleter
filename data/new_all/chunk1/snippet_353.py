# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63554221/typeerror-object-of-type-bytes-is-not-json-serializable-python-3-try-to-pos
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dict_data: _n_(415631, "dict", lambda: dict) = {
  'img': _c_(415639, _a_(415633, _n_(415632, "base64", lambda: base64), "b64encode"), _c_(415638, _a_(415637, _c_(415636, _n_(415634, "urlopen", lambda: urlopen), _n_(415635, "obj", lambda: obj)['recognition_image_path']), "read")))
}
_l_(415640)
json_data: _n_(415641, "str", lambda: str) = _c_(415645, _a_(415643, _n_(415642, "json", lambda: json), "dumps"), _n_(415644, "dict_data", lambda: dict_data))
_l_(415646)