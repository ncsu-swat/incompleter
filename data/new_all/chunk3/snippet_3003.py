# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55146969/filenotfounderror-long-file-path-python-filepath-longer-than-255-characters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, sys
    _l_(556556)

except ImportError:
    pass
try:
    import argparse
    _l_(556558)

except ImportError:
    pass
try:
    import win32api
    _l_(556560)

except ImportError:
    pass
try:
    import win32con
    _l_(556562)

except ImportError:
    pass
try:
    import win32security
    _l_(556564)

except ImportError:
    pass
try:
    from os import walk
    _l_(556566)

except ImportError:
    pass

parser = _c_(556569, _a_(556568, _n_(556567, "argparse", lambda: argparse), "ArgumentParser"), description='Migration Script',
)
_l_(556570)

_c_(556573, _a_(556572, _n_(556571, "parser", lambda: parser), "add_argument"), '-p', '--home_path',  required = True, help='Home Drive Path')
_l_(556574)

args = _c_(556579, _n_(556575, "vars", lambda: vars), _c_(556578, _a_(556577, _n_(556576, "parser", lambda: parser), "parse_args")))
_l_(556580)

if _n_(556581, "args", lambda: args)['home_path']:
    _l_(556593)

    pass
    _l_(556582)
else:
    _c_(556584, _n_(556583, "print", lambda: print), "Usage : script.py -p <path>")
    _l_(556585)
    _c_(556587, _n_(556586, "print", lambda: print), "-p <directory path>/")
    _l_(556588)
    _c_(556591, _a_(556590, _n_(556589, "sys", lambda: sys), "exit"))
    _l_(556592)

dst = (_n_(556594, "args", lambda: args)['home_path'] + '/' + 'long_file_path_dir')
_l_(556595)

for dirname, dirnames, filenames in _c_(556599, _a_(556597, _n_(556596, "os", lambda: os), "walk"), _n_(556598, "args", lambda: args)['home_path']):
    _l_(556616)

    for filename in _n_(556600, "filenames", lambda: filenames):
        _l_(556615)

        file_path = (_n_(556601, "dirname", lambda: dirname) + '/' + _n_(556602, "filename", lambda: filename))
        _l_(556603)
        path_len = _c_(556606, _n_(556604, "len", lambda: len), _n_(556605, "file_path", lambda: file_path))
        _l_(556607)
        if(_n_(556608, "path_len", lambda: path_len) > 255):
            _l_(556614)

            #short_path = win32api.GetShortPathName(file_path)
            _c_(556612, _n_(556609, "copyfile", lambda: copyfile), _n_(556610, "file_path", lambda: file_path), _n_(556611, "dst", lambda: dst), follow_symlinks=True)
            _l_(556613)