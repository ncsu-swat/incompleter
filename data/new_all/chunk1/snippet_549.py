# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60740315/typeerror-deserialize-got-an-unexpected-keyword-argument-partial-in-marshm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from marshmallow import Schema, fields
    _l_(420058)

except ImportError:
    pass
try:
    from werkzeug.datastructures import FileStorage
    _l_(420060)

except ImportError:
    pass
try:
    from marshmallow import Schema, fields
    _l_(420062)

except ImportError:
    pass
try:
    from werkzeug.datastructures import FileStorage
    _l_(420064)

except ImportError:
    pass


class FileStorageField(_a_(420066, _n_(420065, "fields", lambda: fields), "Field")):
    _l_(420084)

    default_error_messages = {
        "invalid": "Not a valid image."
    }
    _l_(420067)

    def _deserialize(self, value, attr, data) -> _n_(420068, "FileStorage", lambda: FileStorage):
        _l_(420083)

        if _n_(420069, "value", lambda: value) is None:
            _l_(420071)

            aux = None
            _l_(420070)
            return aux

        if not _c_(420075, _n_(420072, "isinstance", lambda: isinstance), _n_(420073, "value", lambda: value), _n_(420074, "FileStorage", lambda: FileStorage)):
            _l_(420080)

            _c_(420078, _a_(420077, _n_(420076, "self", lambda: self), "fail"), "invalid")
            _l_(420079)
        aux = _n_(420081, "value", lambda: value)
        _l_(420082)

        return aux


class ImageSchema(_n_(420085, "Schema", lambda: Schema)):
    _l_(420089)

    image = _c_(420087, _n_(420086, "FileStorageField", lambda: FileStorageField), required=True)
    _l_(420088)