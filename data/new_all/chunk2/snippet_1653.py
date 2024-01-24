# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66721562/python-multiprocessing-typeerror-cannot-pickle-tkinter-tkapp-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Main(_a_(470839, _n_(470838, "tk", lambda: tk), "Tk")):
    _l_(470906)


    def __init__(self, *args, **kwargs):
        _l_(470896)

        
        _c_(470846, _a_(470842, _a_(470841, _n_(470840, "tk", lambda: tk), "Tk"), "__init__"), _n_(470843, "self", lambda: self), *_n_(470844, "args", lambda: args), **_n_(470845, "kwargs", lambda: kwargs))
        _l_(470847)
        container = _c_(470851, _a_(470849, _n_(470848, "tk", lambda: tk), "Frame"), _n_(470850, "self", lambda: self))
        _l_(470852)
        _c_(470855, _a_(470854, _n_(470853, "self", lambda: self), "attributes"), '-fullscreen', True) 
        _l_(470856) 
        _c_(470859, _a_(470858, _n_(470857, "container", lambda: container), "pack"), side="top", fill="both", expand = True)
        _l_(470860)
        _c_(470863, _a_(470862, _n_(470861, "container", lambda: container), "grid_rowconfigure"), 0, weight=1)
        _l_(470864)
        _c_(470867, _a_(470866, _n_(470865, "container", lambda: container), "grid_columnconfigure"), 0, weight=1)
        _l_(470868)

        _n_(470869, "self", lambda: self).frames = {}
        _l_(470870)

        for F in (_a_(470872, _n_(470871, "startPage", lambda: startPage), "startPage"), _a_(470874, _n_(470873, "experimentPage", lambda: experimentPage), "experimentPage")):
            _l_(470889)


            frame = _c_(470878, _n_(470875, "F", lambda: F), _n_(470876, "container", lambda: container), _n_(470877, "self", lambda: self))
            _l_(470879)

            _a_(470881, _n_(470880, "self", lambda: self), "frames")[_n_(470882, "F", lambda: F)] = _n_(470883, "frame", lambda: frame)
            _l_(470884)

            _c_(470887, _a_(470886, _n_(470885, "frame", lambda: frame), "grid"), row=0, column=0, sticky="nsew")
            _l_(470888)

        _c_(470894, _a_(470891, _n_(470890, "self", lambda: self), "show_frame"), _a_(470893, _n_(470892, "startPage", lambda: startPage), "startPage"))
        _l_(470895)

    def show_frame(self, cont):
        _l_(470905)


        frame = _a_(470898, _n_(470897, "self", lambda: self), "frames")[_n_(470899, "cont", lambda: cont)]
        _l_(470900)
        _c_(470903, _a_(470902, _n_(470901, "frame", lambda: frame), "tkraise"))
        _l_(470904)

app = _c_(470908, _n_(470907, "Main", lambda: Main))
_l_(470909)
_c_(470912, _a_(470911, _n_(470910, "app", lambda: app), "mainloop"))
_l_(470913)