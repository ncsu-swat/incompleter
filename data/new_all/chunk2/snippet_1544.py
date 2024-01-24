# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33724910/nameerror-with-defining-command-on-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Add(_a_(469028, _n_(469027, "tk", lambda: tk), "Frame")):
    _l_(469175)

    def __init__(self, parent, controller):
        _l_(469062)

        _c_(469034, _a_(469031, _a_(469030, _n_(469029, "tk", lambda: tk), "Frame"), "__init__"), _n_(469032, "self", lambda: self), _n_(469033, "parent", lambda: parent), background="blue")
        _l_(469035)
        button = _c_(469044, _a_(469037, _n_(469036, "tk", lambda: tk), "Button"), _n_(469038, "self", lambda: self), text="Main Menu", font=_n_(469039, "LARGE_FONT", lambda: LARGE_FONT), background="white",
                           command=lambda: _c_(469043, _a_(469041, _n_(469040, "controller", lambda: controller), "show_frame"), _n_(469042, "Main", lambda: Main)))
        _l_(469045)
        _c_(469048, _a_(469047, _n_(469046, "button", lambda: button), "place"), relx=0.83, rely=0.92)
        _l_(469049)

        button4 = _c_(469056, _a_(469051, _n_(469050, "tk", lambda: tk), "Button"), _n_(469052, "self", lambda: self), text="Start Game", font=_n_(469053, "LARGE_FONT", lambda: LARGE_FONT), background="white",
                           command=_a_(469055, _n_(469054, "self", lambda: self), "time_start"))
        _l_(469057)
        _c_(469060, _a_(469059, _n_(469058, "button4", lambda: button4), "place"), relx=0.42, rely=0.8, relheight=0.1, relwidth=0.2)
        _l_(469061)

    def time_start(self):
        _l_(469124)

        timelabel = _c_(469067, _a_(469064, _n_(469063, "tk", lambda: tk), "Label"), _n_(469065, "self", lambda: self), text="Good luck!", font=_n_(469066, "LARGE_FONT", lambda: LARGE_FONT), background="blue")
        _l_(469068)
        _c_(469071, _a_(469070, _n_(469069, "timelabel", lambda: timelabel), "place"), relx=0.42, rely=0.8, relheight=0.1, relwidth=0.2)
        _l_(469072)

        x = _c_(469077, _n_(469073, "int", lambda: int), _c_(469076, _a_(469075, _n_(469074, "random", lambda: random), "uniform"), 1,10))
        _l_(469078)
        y = _c_(469083, _n_(469079, "int", lambda: int), _c_(469082, _a_(469081, _n_(469080, "random", lambda: random), "uniform"), 50,100))
        _l_(469084)
        z = _c_(469089, _n_(469085, "int", lambda: int), _c_(469088, _a_(469087, _n_(469086, "random", lambda: random), "uniform"), 10,50))
        _l_(469090)
        qlabel = _c_(469098, _a_(469092, _n_(469091, "tk", lambda: tk), "Label"), _n_(469093, "self", lambda: self), text= (_n_(469094, "x", lambda: x),"+",_n_(469095, "y", lambda: y),"+",_n_(469096, "z", lambda: z),"=",), font=_n_(469097, "LARGE_FONT", lambda: LARGE_FONT), bg="blue")
        _l_(469099)
        _c_(469102, _a_(469101, _n_(469100, "qlabel", lambda: qlabel), "pack"))
        _l_(469103)

##        entrylabel = tk.Label(self, text="Answer:", font=LARGE_FONT, background="blue")
##        entrylabel.pack()

        e1 = _c_(469107, _a_(469105, _n_(469104, "tk", lambda: tk), "Entry"), _n_(469106, "self", lambda: self))
        _l_(469108)
        _c_(469111, _a_(469110, _n_(469109, "e1", lambda: e1), "pack"))
        _l_(469112)

        ebutton = _c_(469118, _a_(469114, _n_(469113, "tk", lambda: tk), "Button"), _n_(469115, "self", lambda: self), text="Done", font=_n_(469116, "LARGE_FONT", lambda: LARGE_FONT), background="white",
                            command=_n_(469117, "submit_answer", lambda: submit_answer))
        _l_(469119)
        _c_(469122, _a_(469121, _n_(469120, "ebutton", lambda: ebutton), "pack"))
        _l_(469123)

    def submit_answer(self):
        _l_(469174)

        a = (_n_(469125, "x", lambda: x)+_n_(469126, "y", lambda: y)+_n_(469127, "z", lambda: z))
        _l_(469128)
        if _c_(469133, _n_(469129, "int", lambda: int), _c_(469132, _a_(469131, _n_(469130, "e1", lambda: e1), "get"))) == _n_(469134, "a", lambda: a):
            _l_(469155)

            answerlabel = _c_(469139, _a_(469136, _n_(469135, "tk", lambda: tk), "Label"), _n_(469137, "self", lambda: self), text="Correct!", font=_n_(469138, "LARGE_FONT", lambda: LARGE_FONT), background="blue")
            _l_(469140)
            _c_(469143, _a_(469142, _n_(469141, "answerlable", lambda: answerlable), "pack"))
            _l_(469144)
        else:
            answerlabel = _c_(469149, _a_(469146, _n_(469145, "tk", lambda: tk), "Label"), _n_(469147, "self", lambda: self), text="Incorrect!", font=_n_(469148, "LARGE_FONT", lambda: LARGE_FONT), background="blue")
            _l_(469150)
            _c_(469153, _a_(469152, _n_(469151, "answerlable", lambda: answerlable), "pack"))
            _l_(469154)

        _n_(469156, "self", lambda: self).label = _c_(469161, _a_(469158, _n_(469157, "tk", lambda: tk), "Label"), _n_(469159, "self", lambda: self), text="", width=10, font=_n_(469160, "LARGE_FONT", lambda: LARGE_FONT))
        _l_(469162)
        _c_(469166, _a_(469165, _a_(469164, _n_(469163, "self", lambda: self), "label"), "place"), relx=0.1, rely=0.1)
        _l_(469167)
        _n_(469168, "self", lambda: self).remaining = 0
        _l_(469169)
        _c_(469172, _a_(469171, _n_(469170, "self", lambda: self), "countdown"), 5)
        _l_(469173)