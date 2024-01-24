# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64903387/getting-a-filenotfounderror-errno2-when-moving-files-using-shutil-move-metho
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(605177)

except ImportError:
    pass
try:
    from watchdog.observers import Observer
    _l_(605179)

except ImportError:
    pass
try:
    from watchdog.events import FileSystemEventHandler
    _l_(605181)

except ImportError:
    pass
try:
    import time
    _l_(605183)

except ImportError:
    pass
try:
    import shutil
    _l_(605185)

except ImportError:
    pass

file_extension = ["dmg", "jpg", "pdf", "docx", "zip", "tar", "jpeg", "mp4,", "mp3", "png"]
_l_(605186)
src = '/Users/vibhorsagar/Downloads'
_l_(605187)
path = _c_(605191, _a_(605189, _n_(605188, "os", lambda: os), "listdir"), _n_(605190, "src", lambda: src))
_l_(605192)


class Watcher:
    _l_(605234)


    def __init__(self):
        _l_(605197)

        _n_(605193, "self", lambda: self).observer = _c_(605195, _n_(605194, "Observer", lambda: Observer))
        _l_(605196)

    def run(self):
        _l_(605233)

        handler = _c_(605199, _n_(605198, "Handler", lambda: Handler))
        _l_(605200)
        _c_(605206, _a_(605203, _a_(605202, _n_(605201, "self", lambda: self), "observer"), "schedule"), _n_(605204, "handler", lambda: handler), _n_(605205, "src", lambda: src), recursive=True)
        _l_(605207)
        _c_(605211, _a_(605210, _a_(605209, _n_(605208, "self", lambda: self), "observer"), "start"))
        _l_(605212)
        try:
            _l_(605227)

            while True:
                _l_(605217)

                _c_(605215, _a_(605214, _n_(605213, "time", lambda: time), "sleep"), 5)
                _l_(605216)
        except:
            _l_(605226)

            _c_(605221, _a_(605220, _a_(605219, _n_(605218, "self", lambda: self), "observer"), "stop"))
            _l_(605222)
            _c_(605224, _n_(605223, "print", lambda: print), "Error")
            _l_(605225)

        _c_(605231, _a_(605230, _a_(605229, _n_(605228, "self", lambda: self), "observer"), "join"))
        _l_(605232)


class Handler(_n_(605235, "FileSystemEventHandler", lambda: FileSystemEventHandler)):
    _l_(605287)


    @_n_(605236, "staticmethod", lambda: staticmethod)
    def on_any_event(event):
        _l_(605286)

        if _a_(605238, _n_(605237, "event", lambda: event), "is_directory"):
            _l_(605285)

            aux = None
            _l_(605239)
            return aux

        elif _a_(605241, _n_(605240, "event", lambda: event), "event_type") == 'created':
            _l_(605284)

            _c_(605245, _n_(605242, "print", lambda: print), "Received created event - %s." % _a_(605244, _n_(605243, "event", lambda: event), "src_path"))
            _l_(605246)
            c = _c_(605248, _n_(605247, "Cleaner", lambda: Cleaner))
            _l_(605249)
            for i in _n_(605250, "file_extension", lambda: file_extension):
                _l_(605267)

                if _c_(605255, _a_(605253, _a_(605252, _n_(605251, "event", lambda: event), "src_path"), "endswith"), _n_(605254, "i", lambda: i)):
                    _l_(605266)

                    _c_(605261, _a_(605257, _n_(605256, "c", lambda: c), "clean"), _n_(605258, "i", lambda: i), _a_(605260, _n_(605259, "event", lambda: event), "src_path"))
                    _l_(605262)
                else:
                    _c_(605264, _n_(605263, "print", lambda: print), "Error 2")
                    _l_(605265)

        elif _a_(605269, _n_(605268, "event", lambda: event), "event_type") == 'modified':
            _l_(605283)

            _c_(605273, _n_(605270, "print", lambda: print), "Received modified event - %s." % _a_(605272, _n_(605271, "event", lambda: event), "src_path"))
            _l_(605274)

        elif _a_(605276, _n_(605275, "event", lambda: event), "event_type") == 'moved':
            _l_(605282)

            _c_(605280, _n_(605277, "print", lambda: print), "Received moved event - %s." % _a_(605279, _n_(605278, "event", lambda: event), "src_path"))
            _l_(605281)


class Cleaner():
    _l_(605317)


    def clean(self, file_type, file):
        _l_(605316)

        if _n_(605288, "file_type", lambda: file_type) == "dmg":
            _l_(605294)

            _c_(605292, _a_(605290, _n_(605289, "shutil", lambda: shutil), "move"), _n_(605291, "file", lambda: file), '/Users/vibhorsagar/dmgs')
            _l_(605293)

        if _n_(605295, "file_type", lambda: file_type) == "jpg" or "png" or "jpeg":
            _l_(605301)

            _c_(605299, _a_(605297, _n_(605296, "shutil", lambda: shutil), "move"), _n_(605298, "file", lambda: file), '/Users/vibhorsagar/Pictures')
            _l_(605300)

        if _n_(605302, "file_type", lambda: file_type) == "pdf":
            _l_(605308)

            _c_(605306, _a_(605304, _n_(605303, "shutil", lambda: shutil), "move"), _n_(605305, "file", lambda: file), '/Users/vibhorsagar/pdfs')
            _l_(605307)

        if _n_(605309, "file_type", lambda: file_type) == "docx":
            _l_(605315)

            _c_(605313, _a_(605311, _n_(605310, "shutil", lambda: shutil), "move"), _n_(605312, "file", lambda: file), '/Users/vibhorsagar/docx')
            _l_(605314)


if _n_(605318, "__name__", lambda: __name__) == '__main__':
    _l_(605326)

    w = _c_(605320, _n_(605319, "Watcher", lambda: Watcher))
    _l_(605321)
    _c_(605324, _a_(605323, _n_(605322, "w", lambda: w), "run"))
    _l_(605325)