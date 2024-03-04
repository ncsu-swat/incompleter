# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import glob
    _l_(62233)

except ImportError:
    pass
try:
    import os
    _l_(62235)

except ImportError:
    pass

#to get the current working directory name
cwd = _c_(62238, _a_(62237, _n_(62236, "os", lambda: os), "getcwd"))
_l_(62239)
#Load the images from images folder.
for f in _c_(62242, _a_(62241, _n_(62240, "glob", lambda: glob), "glob"), 'images\*.jpg'):
    _l_(62253)

    dir_name = _c_(62245, _n_(62243, "get_dir_name", lambda: get_dir_name), _n_(62244, "f", lambda: f))
    _l_(62246)
    image_file_name = _n_(62247, "dir_name", lambda: dir_name) + '.jpg'
    _l_(62248)
    #To print the file name with path (path will be in string)
    _c_(62251, _n_(62249, "print", lambda: print), _n_(62250, "image_file_name", lambda: image_file_name))
    _l_(62252)

_c_(62257, _a_(62255, _n_(62254, "os", lambda: os), "listdir"), _n_(62256, "directory", lambda: directory))
_l_(62258)

