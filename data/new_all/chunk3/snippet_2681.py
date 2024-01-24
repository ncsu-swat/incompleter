# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66994103/python-checking-for-empty-list-on-a-path-subclass-is-returning-attributeerror
#!/usr/bin/env python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(552111)

except ImportError:
    pass
try:
    import pathlib
    _l_(552113)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(552115)

except ImportError:
    pass
try:
    from typing import Union
    _l_(552117)

except ImportError:
    pass

class WalkPath(_c_(552122, _n_(552118, "type", lambda: type), _c_(552121, _a_(552120, _n_(552119, "pathlib", lambda: pathlib), "Path")))):
    _l_(552223)

    def __new__(cls, *args, **kwargs):
        _l_(552132)

        aux = _c_(552130, _a_(552126, _n_(552123, "super", lambda: super)(_n_(552124, "WalkPath", lambda: WalkPath), _n_(552125, "cls", lambda: cls)), "__new__"), _n_(552127, "cls", lambda: cls), *_n_(552128, "args", lambda: args), **_n_(552129, "kwargs", lambda: kwargs))
        _l_(552131)
        return aux
    
    def __init__(self, *args, dirs: []=[], files: []=[]):
        _l_(552151)

        """Initialize WalkPath object.

        Args:
            dirs (list):        Dirs provided by os.walk(), defauls to []
                                         
            files (list):       Files provided by os.walk(), defaults to []
        """
        
        _c_(552135, _a_(552134, _n_(552133, "super", lambda: super)(), "__init__"))
        _l_(552136)
        _n_(552137, "self", lambda: self).dirs: [_n_(552138, "WalkPath", lambda: WalkPath)] = [_c_(552141, _n_(552139, "WalkPath", lambda: WalkPath), _n_(552140, "d", lambda: d)) for d in _n_(552142, "dirs", lambda: dirs)]
        _l_(552143)
        _n_(552144, "self", lambda: self).files: [_n_(552145, "WalkPath", lambda: WalkPath)] = [_c_(552148, _n_(552146, "WalkPath", lambda: WalkPath), _n_(552147, "f", lambda: f)) for f in _n_(552149, "files", lambda: files)]
        _l_(552150)
    
    @_n_(552152, "property", lambda: property)
    def is_terminus(self):
        _l_(552159)

        aux = _c_(552155, _a_(552154, _n_(552153, "self", lambda: self), "is_file")) or not _a_(552157, _n_(552156, "self", lambda: self), "dirs")
        _l_(552158)
        return aux
    
    @_n_(552160, "property", lambda: property)
    def dirs_abs(self):
        _l_(552168)

        aux = [_c_(552164, _a_(552162, _n_(552161, "self", lambda: self), "joinpath"), _n_(552163, "d", lambda: d)) for d in _a_(552166, _n_(552165, "self", lambda: self), "dirs")]
        _l_(552167)
        return aux
    
    @_n_(552169, "property", lambda: property)
    def files_abs(self):
        _l_(552177)

        aux = [_c_(552173, _a_(552171, _n_(552170, "self", lambda: self), "joinpath"), _n_(552172, "f", lambda: f)) for f in _a_(552175, _n_(552174, "self", lambda: self), "files")]
        _l_(552176)
        return aux
    class Utils:
        _l_(552222)


        @_n_(552178, "staticmethod", lambda: staticmethod)
        def find_deep(path: _n_(552179, "Union", lambda: Union)[_n_(552180, "str", lambda: str), _n_(552181, "Path", lambda: Path), 'WalkPath']) -> ['WalkPath']:
            _l_(552221)

            """Deeply search the specified dir and return all files and subdirs.
            If path passed is a file, return a list with that single file.

            Args:
                path (str or Path): Root path to search for files.
                
            Returns:
                A filtered list of files or an empty list.
            """

            _path = _c_(552184, _n_(552182, "WalkPath", lambda: WalkPath), _n_(552183, "path", lambda: path)) # Coerce to WalkPath
            _l_(552185) # Coerce to WalkPath
            # print(_path)
            
            if _c_(552188, _a_(552187, _n_(552186, "_path", lambda: _path), "is_file")):
                _l_(552191)

                aux = [_n_(552189, "_path", lambda: _path)]
                _l_(552190)
                return aux

            for root, dirs, files in _c_(552195, _a_(552193, _n_(552192, "os", lambda: os), "walk"), _n_(552194, "path", lambda: path)):
                _l_(552220)

                wp = _c_(552200, _n_(552196, "WalkPath", lambda: WalkPath), _n_(552197, "root", lambda: root), dirs=_n_(552198, "dirs", lambda: dirs), files=_n_(552199, "files", lambda: files))
                _l_(552201)
                for d in _a_(552203, _n_(552202, "wp", lambda: wp), "dirs_abs"):
                    _l_(552212)

                    yield _n_(552204, "d", lambda: d)
                    _l_(552205)
                    _c_(552210, _a_(552208, _a_(552207, _n_(552206, "WalkPath", lambda: WalkPath), "Utils"), "find_deep"), _n_(552209, "d", lambda: d))
                    _l_(552211)

                for f in _a_(552214, _n_(552213, "wp", lambda: wp), "files_abs"):
                    _l_(552219)

                    yield _c_(552217, _n_(552215, "WalkPath", lambda: WalkPath), _n_(552216, "f", lambda: f))
                    _l_(552218)

paths = _c_(552231, _a_(552226, _a_(552225, _n_(552224, "WalkPath", lambda: WalkPath), "Utils"), "find_deep"), _c_(552230, _a_(552229, _c_(552228, _n_(552227, "Path", lambda: Path), '/tests/files'), "resolve")))
_l_(552232)
paths = _c_(552240, _n_(552233, "sorted", lambda: sorted), _n_(552234, "paths", lambda: paths), key=lambda p: _c_(552239, _a_(552238, _c_(552237, _n_(552235, "str", lambda: str), _n_(552236, "p", lambda: p)), "lower")))
_l_(552241)

for p in _n_(552242, "paths", lambda: paths):
    _l_(552250)

    _c_(552248, _n_(552243, "print", lambda: print), _a_(552245, _n_(552244, "p", lambda: p), "parent"), _a_(552247, _n_(552246, "p", lambda: p), "dirs"))
    _l_(552249)