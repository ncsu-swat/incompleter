# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66824172/python-classmethod-type-hint-for-static-builder-returns-nameerror-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Options(_n_(446977, "object", lambda: object)):
    _l_(446988)

    def __init__(self, path: _n_(446978, "str", lambda: str)):
        _l_(446982)

        _n_(446979, "self", lambda: self)._path = _n_(446980, "path", lambda: path)
        _l_(446981)

    @_n_(446983, "property", lambda: property)
    def path(self):
        _l_(446987)

        aux = _a_(446985, _n_(446984, "self", lambda: self), "_path")
        _l_(446986)
        return aux

class Config(_n_(446989, "object", lambda: object)):
    _l_(447004)

    def __init__(self, path: _n_(446990, "str", lambda: str)):
        _l_(446994)

        _n_(446991, "self", lambda: self)._path = _n_(446992, "path", lambda: path)
        _l_(446993)

    @_n_(446995, "classmethod", lambda: classmethod)
    def from_options(cls, options: _n_(446996, "Options", lambda: Options)) -> _n_(446997, "Config", lambda: Config):
        _l_(447003)

        aux = _c_(447001, _n_(446998, "cls", lambda: cls), _a_(447000, _n_(446999, "options", lambda: options), "path"))
        _l_(447002)
        return aux