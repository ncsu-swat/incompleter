# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63472025/typeerror-init-got-an-unexpected-keyword-argument-dir
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from threading import Timer
    _l_(337916)

except ImportError:
    pass

message_archive_dir = "achivedir"
_l_(337917)
message_archive_format = "zip"
_l_(337918)
archive_timer = _c_(337924, _n_(337919, "Timer", lambda: Timer), 86400, _a_(337921, _n_(337920, "messageachiver", lambda: messageachiver), "archive"), dir = _n_(337922, "message_archive_dir", lambda: message_archive_dir), fmt = _n_(337923, "message_archive_format", lambda: message_archive_format))
_l_(337925)
_c_(337928, _a_(337927, _n_(337926, "archive_timer", lambda: archive_timer), "start"))
_l_(337929)


class messageachiver(_n_(337930, "object", lambda: object)):
    _l_(337952)

    def __init__(self, **kwargs):
        _l_(337937)

        _n_(337931, "self", lambda: self).message_archive_dir = _n_(337932, "dir", lambda: dir)
        _l_(337933)
        _n_(337934, "self", lambda: self).message_archive_format = _n_(337935, "fmt", lambda: fmt)
        _l_(337936)

    def archive(self):
        _l_(337951)

        _c_(337941, _n_(337938, "print", lambda: print), "message_archive_dir is " + _a_(337940, _n_(337939, "self", lambda: self), "message_archive_dir"))
        _l_(337942)
        _c_(337946, _n_(337943, "print", lambda: print), "message_archive_format is " + _a_(337945, _n_(337944, "self", lambda: self), "message_archive_format"))
        _l_(337947)
        _c_(337949, _n_(337948, "print", lambda: print), "Archiving trade messages")
        _l_(337950)