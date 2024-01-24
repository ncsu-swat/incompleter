# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62054195/python-name-error-when-calling-a-previously-defined-function-in-the-same-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class OurHandler(_n_(523286, "FileSystemEventHandler", lambda: FileSystemEventHandler)):
    _l_(523306)


    # def __init__(self, source):
    #     self.source = source

    def move_epub(self):
        _l_(523296)

        for i in _c_(523291, _a_(523288, _n_(523287, "os", lambda: os), "listdir"), _a_(523290, _n_(523289, "self", lambda: self), "source")):
            _l_(523295)

            _c_(523293, _n_(523292, "print", lambda: print), "Hello World")
            _l_(523294)

    def on_any_event(self, event):
        _l_(523305)

        _c_(523300, _n_(523297, "print", lambda: print), f"\n\n{_n_(523298, 'self', lambda: self)}\t\t {_n_(523299, 'event', lambda: event)}\n\n")
        _l_(523301)
        _c_(523303, _n_(523302, "move_epub", lambda: move_epub))
        _l_(523304)

track_this_folder = "pathname"
_l_(523307)
a = _c_(523309, _n_(523308, "OurHandler", lambda: OurHandler))
_l_(523310)
observer = _c_(523312, _n_(523311, "Observer", lambda: Observer))
_l_(523313)
_c_(523318, _a_(523315, _n_(523314, "observer", lambda: observer), "schedule"), _n_(523316, "a", lambda: a), _n_(523317, "track_this_folder", lambda: track_this_folder))
_l_(523319)
_c_(523322, _a_(523321, _n_(523320, "observer", lambda: observer), "start"))
_l_(523323)
try:
    _l_(523335)

    while True:
        _l_(523328)

        _c_(523326, _a_(523325, _n_(523324, "time", lambda: time), "sleep"), 10)
        _l_(523327)
except _n_(523329, "KeyboardInterrupt", lambda: KeyboardInterrupt):
    _l_(523334)

    _c_(523332, _a_(523331, _n_(523330, "observer", lambda: observer), "stop"))
    _l_(523333)
_c_(523338, _a_(523337, _n_(523336, "observer", lambda: observer), "join"))
_l_(523339)