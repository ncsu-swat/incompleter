# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49158720/updatedtk-root-not-callable-multiple-problems-attributeerror-nonetype-obj
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(704202)

except ImportError:
    pass

Large_font= ("arial", 30)
_l_(704203)

class Myapp(_a_(704205, _n_(704204, "tk", lambda: tk), "Tk")):
    _l_(704275)

    def __init__(self, *args, **kwargs):
        _l_(704265)

        _c_(704212, _a_(704208, _a_(704207, _n_(704206, "tk", lambda: tk), "Tk"), "__init__"), _n_(704209, "self", lambda: self), *_n_(704210, "args", lambda: args), **_n_(704211, "kwargs", lambda: kwargs))
        _l_(704213)
        _c_(704218, _a_(704216, _a_(704215, _n_(704214, "tk", lambda: tk), "Tk"), "wm_title"), _n_(704217, "self", lambda: self), "Payment")
        _l_(704219)
        #root.withdraw()
        _c_(704222, _a_(704221, _n_(704220, "self", lambda: self), "geometry"), "1280x1024")
        _l_(704223)
        container = _c_(704227, _a_(704225, _n_(704224, "tk", lambda: tk), "Frame"), _n_(704226, "self", lambda: self))
        _l_(704228)
        _c_(704231, _a_(704230, _n_(704229, "container", lambda: container), "pack"), side="top", fill="both", expand=True)
        _l_(704232)
        _c_(704235, _a_(704234, _n_(704233, "container", lambda: container), "grid_rowconfigure"), 0, weight=1)
        _l_(704236)
        _c_(704239, _a_(704238, _n_(704237, "container", lambda: container), "grid_columnconfigure"), 0, weight=1)
        _l_(704240)
        _n_(704241, "self", lambda: self).frames = {}
        _l_(704242)
        for F in (_n_(704243, "Homepage", lambda: Homepage), _n_(704244, "PageTwo", lambda: PageTwo)):
            _l_(704259)

            frame = _c_(704248, _n_(704245, "F", lambda: F), _n_(704246, "container", lambda: container), _n_(704247, "self", lambda: self))
            _l_(704249)
            _a_(704251, _n_(704250, "self", lambda: self), "frames")[_n_(704252, "F", lambda: F)] = _n_(704253, "frame", lambda: frame)
            _l_(704254)
            _c_(704257, _a_(704256, _n_(704255, "frame", lambda: frame), "grid"), row=0, column=0, sticky="nsew")
            _l_(704258)
        _c_(704263, _a_(704261, _n_(704260, "self", lambda: self), "show_frame"), _n_(704262, "Homepage", lambda: Homepage))
        _l_(704264)
    def show_frame(self, cont):
        _l_(704274)

        frame = _a_(704267, _n_(704266, "self", lambda: self), "frames")[_n_(704268, "cont", lambda: cont)]
        _l_(704269)
        _c_(704272, _a_(704271, _n_(704270, "frame", lambda: frame), "tkraise"))
        _l_(704273)

class Homepage(_a_(704277, _n_(704276, "tk", lambda: tk), "Frame")):
    _l_(704419)

    def __init__(self, parent, controller, **kwargs):
        _l_(704418)

        _c_(704283, _a_(704279, _n_(704278, "Frame", lambda: Frame), "__init__"), _n_(704280, "self", lambda: self), _n_(704281, "parent", lambda: parent), **_n_(704282, "kwargs", lambda: kwargs))
        _l_(704284)
        _c_(704287, _a_(704286, _n_(704285, "self", lambda: self), "configure"), background='grey')
        _l_(704288)
        f1 = _c_(704292, _a_(704290, _n_(704289, "tk", lambda: tk), "Frame"), _n_(704291, "self", lambda: self), width=1200, height=100, bd=3, bg="grey", relief="raise")
        _l_(704293)
        _c_(704296, _a_(704295, _n_(704294, "f1", lambda: f1), "pack"), side="top")
        _l_(704297)
        lblInfo = _c_(704302, _a_(704299, _n_(704298, "tk", lambda: tk), "Label"), _n_(704300, "f1", lambda: f1), text="MY APP", font=_n_(704301, "Large_font", lambda: Large_font), bg="grey", fg="white")
        _l_(704303)
        _c_(704306, _a_(704305, _n_(704304, "lblInfo", lambda: lblInfo), "pack"), side="top")
        _l_(704307)

#=========SUM UP==========
        f3 = _c_(704311, _a_(704309, _n_(704308, "tk", lambda: tk), "Frame"), _n_(704310, "self", lambda: self), width=400, height=800, bd=3, bg="grey", relief="raise")
        _l_(704312)
        _c_(704315, _a_(704314, _n_(704313, "f3", lambda: f3), "pack"), side="right")
        _l_(704316)

        def uiPrint():
            _l_(704327)

            _c_(704318, _n_(704317, "print", lambda: print), "")
            _l_(704319)
            _c_(704322, _n_(704320, "print", lambda: print), _n_(704321, "clickcount", lambda: clickcount))
            _l_(704323)
            _c_(704325, _n_(704324, "blankLine", lambda: blankLine))
            _l_(704326)

        _n_(704328, "self", lambda: self).click = _c_(704331, _a_(704330, _n_(704329, "tk", lambda: tk), "IntVar"))
        _l_(704332)
        _c_(704336, _a_(704335, _a_(704334, _n_(704333, "self", lambda: self), "click"), "set"), "6");
        _l_(704337)

        def blankLine():
            _l_(704344)

            for i in _c_(704339, _n_(704338, "range", lambda: range), 0):
                _l_(704343)

                _c_(704341, _n_(704340, "print", lambda: print), "")
                _l_(704342)

        def buttonCommand():
            _l_(704361)

            global clickcount
            _l_(704345)
            global click
            _l_(704346)
            global mult
            _l_(704347)
            clickcount += 2 * _n_(704348, "mult", lambda: (mult))
            _l_(704349)
            _c_(704356, _a_(704352, _a_(704351, _n_(704350, "self", lambda: self), "click"), "set"), _c_(704355, _n_(704353, "str", lambda: str), _n_(704354, "clickcount", lambda: clickcount)));  # Update score
            _l_(704357)# Update score
            _c_(704359, _n_(704358, "uiPrint", lambda: uiPrint))
            _l_(704360)

        def buttonCommand1():
            _l_(704378)

            global clickcount
            _l_(704362)
            global click
            _l_(704363)
            global mult
            _l_(704364)
            clickcount -= 1 * _n_(704365, "mult", lambda: (mult))
            _l_(704366)
            _c_(704373, _a_(704369, _a_(704368, _n_(704367, "self", lambda: self), "click"), "set"), _c_(704372, _n_(704370, "str", lambda: str), _n_(704371, "clickcount", lambda: clickcount)));
            _l_(704374)
            _c_(704376, _n_(704375, "uiPrint", lambda: uiPrint))
            _l_(704377)

        l = _c_(704383, _a_(704380, _n_(704379, "tk", lambda: tk), "Label"), _n_(704381, "f3", lambda: f3), textvariable=_n_(704382, "click", lambda: click))  # Score
        _l_(704384)  # Score
        _c_(704387, _a_(704386, _n_(704385, "l", lambda: l), "pack"))
        _l_(704388)
        plusButton = _c_(704393, _a_(704390, _n_(704389, "tk", lambda: tk), "Button"), _n_(704391, "f3", lambda: f3), command = _n_(704392, "buttonCommand", lambda: buttonCommand), text="+")
        _l_(704394)
        minusButton = _c_(704399, _a_(704396, _n_(704395, "tk", lambda: tk), "Button"), _n_(704397, "f3", lambda: f3), command = _n_(704398, "buttonCommand1", lambda: buttonCommand1), text="-")
        _l_(704400)
        _c_(704403, _a_(704402, _n_(704401, "plusButton", lambda: plusButton), "pack"), padx=10, pady=10)
        _l_(704404)
        _c_(704407, _a_(704406, _n_(704405, "minusButton", lambda: minusButton), "pack"), padx=10, pady=10)
        _l_(704408)
        btn1 = _c_(704412, _a_(704410, _n_(704409, "tk", lambda: tk), "Button"), _n_(704411, "f3", lambda: f3), padx=20, pady=20, bd=8, fg="white", bg="green", font=('arial', 30, 'bold'),
                  text="NEXT")
        _l_(704413)
        _c_(704416, _a_(704415, _n_(704414, "btn1", lambda: btn1), "pack"), padx=10, pady=10)
        _l_(704417)


clickcount = (6)
_l_(704420)
mult = 1
_l_(704421)
dcp1 = 0
_l_(704422)

class PageTwo(_a_(704424, _n_(704423, "tk", lambda: tk), "Frame")):
    _l_(704446)

    def __init__(self, parent, controller):
        _l_(704445)

        _c_(704430, _a_(704427, _a_(704426, _n_(704425, "tk", lambda: tk), "Frame"), "__init__"), _n_(704428, "self", lambda: self), _n_(704429, "parent", lambda: parent))
        _l_(704431)
        _c_(704434, _a_(704433, _n_(704432, "self", lambda: self), "configure"), background='grey')
        _l_(704435)
        f1 = _c_(704439, _a_(704437, _n_(704436, "tk", lambda: tk), "Frame"), _n_(704438, "self", lambda: self), width=600, height=100, bd=3, bg="grey", relief="raise")
        _l_(704440)
        _c_(704443, _a_(704442, _n_(704441, "f1", lambda: f1), "pack"))
        _l_(704444)


app = _c_(704448, _n_(704447, "Myapp", lambda: Myapp))
_l_(704449)
_c_(704452, _a_(704451, _n_(704450, "app", lambda: app), "mainloop"))
_l_(704453)