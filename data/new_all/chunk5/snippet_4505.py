# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56519945/i-want-to-write-json-files-with-data-that-i-scraped-with-a-webscraper-and-an-api
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PythonObjectEncoder(_n_(680174, "JSONEncoder", lambda: JSONEncoder)):
    _l_(680200)

    def default(self, obj):
        _l_(680199)

        if _c_(680186, _n_(680175, "isinstance", lambda: isinstance), _n_(680176, "obj", lambda: obj), (_n_(680177, "list", lambda: list), _n_(680178, "dict", lambda: dict), _n_(680179, "str", lambda: str), _n_(680180, "unicode", lambda: unicode), _n_(680181, "int", lambda: int), _n_(680182, "float", lambda: float), _n_(680183, "bool", lambda: bool), _c_(680185, _n_(680184, "type", lambda: type), None))):
            _l_(680193)

            aux = _c_(680191, _a_(680188, _n_(680187, "JSONEncoder", lambda: JSONEncoder), "default"), _n_(680189, "self", lambda: self), _n_(680190, "obj", lambda: obj))
            _l_(680192)
            return aux
        aux = {'_python_object': _c_(680197, _a_(680195, _n_(680194, "pickle", lambda: pickle), "dumps"), _n_(680196, "obj", lambda: obj))}
        _l_(680198)
        return aux

def as_python_object(dct):
    _l_(680212)

    if '_python_object' in _n_(680201, "dct", lambda: dct):
        _l_(680209)

        aux = _c_(680207, _a_(680203, _n_(680202, "pickle", lambda: pickle), "loads"), _c_(680206, _n_(680204, "str", lambda: str), _n_(680205, "dct", lambda: dct)['_python_object']))
        _l_(680208)
        return aux
    aux = _n_(680210, "dct", lambda: dct)
    _l_(680211)
    return aux