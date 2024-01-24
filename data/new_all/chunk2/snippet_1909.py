# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38380270/python3-ftp-file-upload-throws-typeerror-type-str-doesnt-support-the-buffer-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ftplib
    _l_(448344)

except ImportError:
    pass

ftp = _c_(448348, _a_(448346, _n_(448345, "ftplib", lambda: ftplib), "FTP"), _n_(448347, "url", lambda: url))
_l_(448349)
_c_(448354, _a_(448351, _n_(448350, "ftp", lambda: ftp), "login"), _n_(448352, "name", lambda: name), _n_(448353, "password", lambda: password))
_l_(448355)
_c_(448360, _a_(448357, _n_(448356, "ftp", lambda: ftp), "storlines"), "STOR " + "mylog.log", _c_(448359, _n_(448358, "open", lambda: open), "log/mylog.log"))
_l_(448361)
_c_(448364, _a_(448363, _n_(448362, "ftp", lambda: ftp), "close"))
_l_(448365)