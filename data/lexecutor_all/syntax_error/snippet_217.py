# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1546221)

except ImportError:
    pass


def files_in_dir(path, extension=''):
    _l_(1546236)

    """
       Generator: yields all of the files in <path> ending with
       <extension>

       \param   path       Absolute or relative path to inspect,
       \param   extension  [optional] Only yield files matching this,

       \yield              [filenames]
    """


    for _, dirs, files in _c_(1546225, _a_(1546223, _n_(1546222, "os", lambda: os), "walk"), _n_(1546224, "path", lambda: path)):
        _l_(1546235)

        _n_(1546226, "dirs", lambda: dirs)[:] = []  # do not recurse directories.
        _l_(1546227)  # do not recurse directories.
        yield from [_n_(1546228, "f", lambda: f) for f in _n_(1546229, "files", lambda: files) if _c_(1546233, _a_(1546231, _n_(1546230, "f", lambda: f), "endswith"), _n_(1546232, "extension", lambda: extension))]
        _l_(1546234)

# Example: print all the .py files in './python'
for filename in _c_(1546238, _n_(1546237, "files_in_dir", lambda: files_in_dir), './python', '*.py'):
    _l_(1546243)

    _c_(1546241, _n_(1546239, "print", lambda: print), "-", _n_(1546240, "filename", lambda: filename))
    _l_(1546242)

path, ext = "./python", ext = ".py"
_l_(1546244)
for _, _, dirfiles in _c_(1546248, _a_(1546246, _n_(1546245, "os", lambda: os), "walk"), _n_(1546247, "path", lambda: path)):
    _l_(1546257)

    matches = (_n_(1546249, "f", lambda: f) for f in _n_(1546250, "dirfiles", lambda: dirfiles) if _c_(1546254, _a_(1546252, _n_(1546251, "f", lambda: f), "endswith"), _n_(1546253, "ext", lambda: ext)))
    _l_(1546255)
    break
    _l_(1546256)

for filename in _n_(1546258, "matches", lambda: matches):
    _l_(1546270)

    _c_(1546261, _n_(1546259, "print", lambda: print), "-", _n_(1546260, "filename", lambda: filename))
    _l_(1546262)

    matches = [_n_(1546263, "f", lambda: f) for f in _n_(1546264, "dirfiles", lambda: dirfiles) if _c_(1546268, _a_(1546266, _n_(1546265, "f", lambda: f), "endswith"), _n_(1546267, "ext", lambda: ext))]
    _l_(1546269)

