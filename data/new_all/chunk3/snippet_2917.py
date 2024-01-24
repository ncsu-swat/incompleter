# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58365301/how-do-i-fix-typeerror-dispatch-missing-1-required-positional-argument-even
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(546081)

except ImportError:
    pass
try:
    from watchdog.observers import Observer
    _l_(546083)

except ImportError:
    pass
try:
    from watchdog.events import FileSystemEventHandler
    _l_(546085)

except ImportError:
    pass
try:
    import time
    _l_(546087)

except ImportError:
    pass
try:
    import json
    _l_(546089)

except ImportError:
    pass

event = None
_l_(546090)

class MyHandler(_n_(546091, "FileSystemEventHandler", lambda: FileSystemEventHandler)):
    _l_(546111)

    i = 1
    _l_(546092)
    def on_modified(self, event):
        _l_(546110)

        for filename in _c_(546096, _a_(546094, _n_(546093, "os", lambda: os), "listdir"), _n_(546095, "folder_to_track", lambda: folder_to_track)):
            _l_(546109)

            src = _n_(546097, "folder_to_track", lambda: folder_to_track) + "/" + _n_(546098, "filename", lambda: filename)
            _l_(546099)
            new_destination = _n_(546100, "folder_destination", lambda: folder_destination) + "/" + _n_(546101, "filename", lambda: filename)
            _l_(546102)
            _c_(546107, _a_(546104, _n_(546103, "os", lambda: os), "rename"), _n_(546105, "src", lambda: src), _n_(546106, "new_destination", lambda: new_destination))
            _l_(546108)

folder_to_track = '/Users/Balduin/Pictures/Florens1019'
_l_(546112)
folder_destination = '/Users/Balduin/Pictures/Florens1019/raw-jpeg'
_l_(546113)
event_handler = _n_(546114, "MyHandler", lambda: MyHandler)
_l_(546115)
observer = _c_(546117, _n_(546116, "Observer", lambda: Observer))
_l_(546118)
_c_(546123, _a_(546120, _n_(546119, "observer", lambda: observer), "schedule"), _n_(546121, "event_handler", lambda: event_handler), _n_(546122, "folder_to_track", lambda: folder_to_track), recursive=True)
_l_(546124)
_c_(546127, _a_(546126, _n_(546125, "observer", lambda: observer), "start"))
_l_(546128)

try:
    _l_(546140)

    while True:
        _l_(546133)

        _c_(546131, _a_(546130, _n_(546129, "time", lambda: time), "sleep"), 10)
        _l_(546132)
except _n_(546134, "KeyboardInterrupt", lambda: KeyboardInterrupt):
    _l_(546139)

    _c_(546137, _a_(546136, _n_(546135, "observer", lambda: observer), "stop"))
    _l_(546138)
_a_(546142, _n_(546141, "observer", lambda: observer), "join")
_l_(546143)