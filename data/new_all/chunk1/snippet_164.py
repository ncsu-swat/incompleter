# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41285969/dropbox-api-v2-trying-to-upload-file-with-files-upload-throws-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import dropbox
    _l_(411391)

except ImportError:
    pass

dbx = _c_(411394, _a_(411393, _n_(411392, "dropbox", lambda: dropbox), "Dropbox"), "my_access_token")
_l_(411395)

data = "asd"
_l_(411396)

_c_(411400, _a_(411398, _n_(411397, "dbx", lambda: dbx), "files_upload"), _n_(411399, "data", lambda: data), '/file.txt')
_l_(411401)