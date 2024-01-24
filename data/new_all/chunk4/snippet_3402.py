# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74892413/why-this-typeerror-msg-in-python3-script-checking-files-timestamps
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime as dt
    _l_(596915)

except ImportError:
    pass
try:
    import os , send2trash, timedelta
    _l_(596917)

except ImportError:
    pass

myuser=_c_(596920, _a_(596919, _n_(596918, "os", lambda: os), "getlogin"))
_l_(596921)

# set paths
archivePath=rf"C:\Users\{_n_(596922, 'myuser', lambda: myuser)}\Pictures\Saved Pictures\2022.11.zip"
_l_(596923)
logPath=rf"C:\Users\{_n_(596924, 'myuser', lambda: myuser)}\Downloads\screenshots\TEST"
_l_(596925)

# a list of ONLY old files based on 'last modified' time (since Epoch).
if _c_(596930, _a_(596928, _a_(596927, _n_(596926, "os", lambda: os), "path"), "isfile"), _n_(596929, "archivePath", lambda: archivePath)):
    _l_(596992)

    _c_(596932, _n_(596931, "print", lambda: print), "Archive already exists, deleting copies in TEST folder.\n")
    _l_(596933)
    _c_(596937, _a_(596935, _n_(596934, "os", lambda: os), "chdir"), _n_(596936, "logPath", lambda: logPath))
    _l_(596938)
    old=[]
    _l_(596939)
    for file in _c_(596945, _n_(596940, "sorted", lambda: sorted), _c_(596944, _a_(596942, _n_(596941, "os", lambda: os), "listdir"), _n_(596943, "logPath", lambda: logPath))):
        _l_(596973)

        modified=_c_(596953, _a_(596947, _n_(596946, "dt", lambda: dt), "fromtimestamp"), _a_(596952, _c_(596951, _a_(596949, _n_(596948, "os", lambda: os), "stat"), _n_(596950, "file", lambda: file)), "st_mtime")) ## a float nr?
        _l_(596954) ## a float nr?
        ## conditions to be met: 
        if _c_(596957, _a_(596956, _n_(596955, "modified", lambda: modified), "date")) <= _c_(596960, _a_(596959, _n_(596958, "dt", lambda: dt), "date"), 2022,4,30):
            _l_(596972)

            _c_(596964, _a_(596962, _n_(596961, "old", lambda: old), "append"), _n_(596963, "file", lambda: file))
            _l_(596965)
        else:
            _c_(596970, _n_(596966, "print", lambda: print), _c_(596969, _n_(596967, "str", lambda: str), _n_(596968, "file", lambda: file)), ': conditions NOT met.')
            _l_(596971)
    ## mv to trashcan
    numberFiles=_c_(596976, _n_(596974, "len", lambda: len), _n_(596975, "old", lambda: old))
    _l_(596977)
    _c_(596980, _n_(596978, "print", lambda: print), f"Deleting {_n_(596979, 'numberFiles', lambda: numberFiles)} file.")
    _l_(596981)
    for oldFile in _n_(596982, "old", lambda: old):
        _l_(596988)

        _c_(596986, _a_(596984, _n_(596983, "send2trash", lambda: send2trash), "send2trash"), _n_(596985, "oldFile", lambda: oldFile))
        _l_(596987)
else:
    _c_(596990, _n_(596989, "print", lambda: print), 'No files deleted.')
    _l_(596991)