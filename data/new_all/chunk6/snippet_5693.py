# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63472025/typeerror-init-got-an-unexpected-keyword-argument-dir
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from threading import Timer
    _l_(342184)

except ImportError:
    pass

message_archive_dir = "achivedir"
_l_(342185)
message_archive_format = "zip"
_l_(342186)
archive_timer = _c_(342192, _n_(342187, "Timer", lambda: Timer), 86400, _a_(342189, _n_(342188, "messageachiver", lambda: messageachiver), "archive"), dir = _n_(342190, "message_archive_dir", lambda: message_archive_dir), fmt = _n_(342191, "message_archive_format", lambda: message_archive_format))
_l_(342193)
_c_(342196, _a_(342195, _n_(342194, "archive_timer", lambda: archive_timer), "start"))
_l_(342197)


class messageachiver(_n_(342198, "object", lambda: object)):
    _l_(342220)

    def __init__(self, **kwargs):
        _l_(342205)

        _n_(342199, "self", lambda: self).message_archive_dir = _n_(342200, "dir", lambda: dir)
        _l_(342201)
        _n_(342202, "self", lambda: self).message_archive_format = _n_(342203, "fmt", lambda: fmt)
        _l_(342204)

    def archive(self):
        _l_(342219)

        _c_(342209, _n_(342206, "print", lambda: print), "message_archive_dir is " + _a_(342208, _n_(342207, "self", lambda: self), "message_archive_dir"))
        _l_(342210)
        _c_(342214, _n_(342211, "print", lambda: print), "message_archive_format is " + _a_(342213, _n_(342212, "self", lambda: self), "message_archive_format"))
        _l_(342215)
        _c_(342217, _n_(342216, "print", lambda: print), "Archiving trade messages")
        _l_(342218)