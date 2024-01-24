# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41285969/dropbox-api-v2-trying-to-upload-file-with-files-upload-throws-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(419618, _n_(419617, "open", lambda: open), "/home/pi/Desktop/dbox/asd.txt", "rb") as f:
    _l_(419624)

    _c_(419622, _a_(419620, _n_(419619, "dbx", lambda: dbx), "files_upload"), _n_(419621, "f", lambda: f), '/asd.txt', mute = True)
    _l_(419623)