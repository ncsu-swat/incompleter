# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71457635/typeerror-init-takes-from-1-to-2-positional-arguments-but-3-were-given-wh
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyClass(_n_(463231, "Tk", lambda: Tk)):
    _l_(463281)

    def __init__(self):
        _l_(463271)

        _c_(463235, _a_(463233, _n_(463232, "Tk", lambda: Tk), "__init__"), _n_(463234, "self", lambda: self))
        _l_(463236)
        container = _c_(463240, _a_(463238, _n_(463237, "ttk", lambda: ttk), "Frame"), _n_(463239, "self", lambda: self))
        _l_(463241)
        _c_(463244, _a_(463243, _n_(463242, "container", lambda: container), "pack"), side='top', fill='both', expand=True)
        _l_(463245)
        _n_(463246, "self", lambda: self).frames = {}
        _l_(463247)
        for F in (_n_(463248, "StartPage", lambda: StartPage), _n_(463249, "LoginPage", lambda: LoginPage), _n_(463250, "FiltersPage", lambda: FiltersPage)):
            _l_(463265)

            frame = _c_(463254, _n_(463251, "F", lambda: F), _n_(463252, "container", lambda: container), _n_(463253, "self", lambda: self))
            _l_(463255)
            _a_(463257, _n_(463256, "self", lambda: self), "frames")[_n_(463258, "F", lambda: F)] = _n_(463259, "frame", lambda: frame)
            _l_(463260)
            _c_(463263, _a_(463262, _n_(463261, "frame", lambda: frame), "grid"), column=0, row=0, sticky="nsew")
            _l_(463264)
        _c_(463269, _a_(463267, _n_(463266, "self", lambda: self), "show_frame"), _n_(463268, "StartPage", lambda: StartPage))
        _l_(463270)

    def show_frame(self, controller):
        _l_(463280)

        frame = _a_(463273, _n_(463272, "self", lambda: self), "frames")[_n_(463274, "controller", lambda: controller)]
        _l_(463275)
        _c_(463278, _a_(463277, _n_(463276, "frame", lambda: frame), "tkraise"))
        _l_(463279)