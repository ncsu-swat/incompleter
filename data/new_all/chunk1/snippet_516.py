# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61038174/python3-nameerror-name-open-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Contoller:
    _l_(404894)


    ...
    _l_(404883)

    def __del__(self):
        _l_(404893)

        store = {}
        _l_(404884)
        ...
        _l_(404885)
        _c_(404891, _a_(404887, _n_(404886, "pickle", lambda: pickle), "dump"), _n_(404888, "store", lambda: store), _c_(404890, _n_(404889, "open", lambda: open), 'data.p', 'wb'))    
        _l_(404892)    

class MyWindow(_a_(404896, _n_(404895, "Gtk", lambda: Gtk), "Window")):
    _l_(404919)


    def __init__(self):
        _l_(404911)

        ...
        _l_(404897)
        _n_(404898, "self", lambda: self).controller = _c_(404901, _n_(404899, "Contoller", lambda: Contoller), _n_(404900, "self", lambda: self))
        _l_(404902)
        ...
        _l_(404903)
        _c_(404908, _a_(404905, _n_(404904, "self", lambda: self), "connect"), "delete-event", _a_(404907, _n_(404906, "self", lambda: self), "quit"))
        _l_(404909)
        ...
        _l_(404910)

    ...
    _l_(404912)

    def quit(self, widget, event):
        _l_(404918)

        del self.controller
        _l_(404913)
        _c_(404916, _a_(404915, _n_(404914, "Gtk", lambda: Gtk), "main_quit"))
        _l_(404917)