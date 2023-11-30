# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1548093)

except ImportError:
    pass

def get_file_name(path):
    _l_(1548112)

    if not _c_(1548098, _a_(1548096, _a_(1548095, _n_(1548094, "os", lambda: os), "path"), "isdir"), _n_(1548097, "path", lambda: path)):
        _l_(1548111)

        aux = _c_(1548109, _a_(1548108, _c_(1548107, _a_(1548101, _a_(1548100, _n_(1548099, "os", lambda: os), "path"), "splitext"), _c_(1548106, _a_(1548104, _a_(1548103, _n_(1548102, "os", lambda: os), "path"), "basename"), _n_(1548105, "path", lambda: path)))[0], "split"), ".")[0]
        _l_(1548110)
        return aux


def get_file_extension(path):
    _l_(1548139)

    extensions = []
    _l_(1548113)
    copy_path = _n_(1548114, "path", lambda: path)
    _l_(1548115)
    while True:
        _l_(1548130)

        copy_path, result = _c_(1548120, _a_(1548118, _a_(1548117, _n_(1548116, "os", lambda: os), "path"), "splitext"), _n_(1548119, "copy_path", lambda: copy_path))
        _l_(1548121)
        if _n_(1548122, "result", lambda: result) != '':
            _l_(1548129)

            _c_(1548126, _a_(1548124, _n_(1548123, "extensions", lambda: extensions), "append"), _n_(1548125, "result", lambda: result))
            _l_(1548127)
        else:
            break
            _l_(1548128)
    _c_(1548133, _a_(1548132, _n_(1548131, "extensions", lambda: extensions), "reverse"))
    _l_(1548134)
    aux = _c_(1548137, _a_(1548135, "", "join"), _n_(1548136, "extensions", lambda: extensions))
    _l_(1548138)
    return aux

