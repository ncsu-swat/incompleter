# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59615257/i-want-to-make-a-gui-but-i-get-this-error-self-frame-gridrow-0-column-0-stic
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(654321)

except ImportError:
    pass

LARGE_FONT= ("Verdana", 12)
_l_(654322)

class SeaofBTCapp(_a_(654324, _n_(654323, "tk", lambda: tk), "Tk")):
    _l_(654385)


    def __init__(self, *args, **kwargs):
        _l_(654375)

        _c_(654331, _a_(654327, _a_(654326, _n_(654325, "tk", lambda: tk), "Tk"), "__init__"), _n_(654328, "self", lambda: self), *_n_(654329, "args", lambda: args), **_n_(654330, "kwargs", lambda: kwargs))
        _l_(654332)
        container = _c_(654336, _a_(654334, _n_(654333, "tk", lambda: tk), "Frame"), _n_(654335, "self", lambda: self))
        _l_(654337)

        _c_(654340, _a_(654339, _n_(654338, "container", lambda: container), "pack"), side="top", fill="both", expand=True)
        _l_(654341)

        _c_(654344, _a_(654343, _n_(654342, "container", lambda: container), "grid_rowconfigure"), 0, weight=1)
        _l_(654345)
        _c_(654348, _a_(654347, _n_(654346, "container", lambda: container), "grid_columnconfigure"), 0, weight=1)
        _l_(654349)

        _n_(654350, "self", lambda: self).frames = {}
        _l_(654351)

        for F in (_n_(654352, "MainWindow", lambda: MainWindow), _n_(654353, "Game", lambda: Game), _n_(654354, "Difficulty", lambda: Difficulty)):
            _l_(654369)

            frame = _c_(654358, _n_(654355, "F", lambda: F), _n_(654356, "container", lambda: container), _n_(654357, "self", lambda: self))
            _l_(654359)

            _a_(654361, _n_(654360, "self", lambda: self), "frames")[_n_(654362, "F", lambda: F)] = _n_(654363, "frame", lambda: frame)
            _l_(654364)

            _c_(654367, _a_(654366, _n_(654365, "frame", lambda: frame), "grid"), row=0, column=0, sticky="nsew")
            _l_(654368)

        _c_(654373, _a_(654371, _n_(654370, "self", lambda: self), "show_frame"), _n_(654372, "StartPage", lambda: StartPage))
        _l_(654374)

    def show_frame(self, cont):
        _l_(654384)

        frame = _a_(654377, _n_(654376, "self", lambda: self), "frames")[_n_(654378, "cont", lambda: cont)]
        _l_(654379)
        _c_(654382, _a_(654381, _n_(654380, "frame", lambda: frame), "tkraise"))
        _l_(654383)


class MainWindow(_a_(654387, _n_(654386, "tk", lambda: tk), "Tk")):
    _l_(654456)

    def __init__(self, parent, controller):
        _l_(654451)

        _c_(654393, _a_(654390, _a_(654389, _n_(654388, "tk", lambda: tk), "Frame"), "__init__"), _n_(654391, "self", lambda: self), _n_(654392, "parent", lambda: parent))
        _l_(654394)
        label = _c_(654399, _a_(654396, _n_(654395, "tk", lambda: tk), "Label"), _n_(654397, "self", lambda: self), text="Welcom to TIC TAC TOE", font=_n_(654398, "LARGE_FONT", lambda: LARGE_FONT))
        _l_(654400)
        _c_(654403, _a_(654402, _n_(654401, "label", lambda: label), "pack"), pady=10, padx=10)
        _l_(654404)

        button1 = _c_(654412, _a_(654406, _n_(654405, "tk", lambda: tk), "Button"), _n_(654407, "self", lambda: self), text="Start",
                            command=lambda: _c_(654411, _a_(654409, _n_(654408, "controller", lambda: controller), "show_frame"), _n_(654410, "Game", lambda: Game)))
        _l_(654413)
        _c_(654416, _a_(654415, _n_(654414, "button1", lambda: button1), "pack"))
        _l_(654417)

        button2 = _c_(654425, _a_(654419, _n_(654418, "tk", lambda: tk), "Button"), _n_(654420, "self", lambda: self), text="Diffeculty",
                            command=lambda: _c_(654424, _a_(654422, _n_(654421, "controller", lambda: controller), "show_frame"), _n_(654423, "Difficulty", lambda: Difficulty)))
        _l_(654426)
        _c_(654429, _a_(654428, _n_(654427, "button2", lambda: button2), "pack"))
        _l_(654430)

        button3 = _c_(654436, _a_(654432, _n_(654431, "tk", lambda: tk), "Button"), _n_(654433, "self", lambda: self), text="Quit", command=_a_(654435, _n_(654434, "self", lambda: self), "Quit"))
        _l_(654437)
        _c_(654440, _a_(654439, _n_(654438, "button3", lambda: button3), "pack"))
        _l_(654441)

        label1 = _c_(654445, _a_(654443, _n_(654442, "tk", lambda: tk), "Label"), _n_(654444, "self", lambda: self), text="Made by VindictaOG")
        _l_(654446)
        _c_(654449, _a_(654448, _n_(654447, "label1", lambda: label1), "pack"))
        _l_(654450)

    def Quit(self):
        _l_(654455)

        aux = ""
        _l_(654454)
        exit(aux)


class Game(_a_(654458, _n_(654457, "tk", lambda: tk), "Tk")):
    _l_(654489)

    def __init__(self, parent, controller):
        _l_(654488)

        _c_(654464, _a_(654461, _a_(654460, _n_(654459, "tk", lambda: tk), "Frame"), "__init__"), _n_(654462, "self", lambda: self), _n_(654463, "parent", lambda: parent))
        _l_(654465)
        button1 = _c_(654469, _a_(654467, _n_(654466, "tk", lambda: tk), "Button"), _n_(654468, "self", lambda: self), text="New Game")
        _l_(654470)
        _c_(654473, _a_(654472, _n_(654471, "button1", lambda: button1), "pack"))
        _l_(654474)

        button2= _c_(654482, _a_(654476, _n_(654475, "tk", lambda: tk), "Button"), _n_(654477, "self", lambda: self), text="Back to homescreen",
                           command=lambda: _c_(654481, _a_(654479, _n_(654478, "controller", lambda: controller), "show_frame"), _n_(654480, "MainWindow", lambda: MainWindow)))
        _l_(654483)
        _c_(654486, _a_(654485, _n_(654484, "button2", lambda: button2), "pack"))
        _l_(654487)


class Difficulty(_a_(654491, _n_(654490, "tk", lambda: tk), "Tk")):
    _l_(654526)

    def __init__(self, parent, controller):
        _l_(654525)

        _c_(654497, _a_(654494, _a_(654493, _n_(654492, "tk", lambda: tk), "Frame"), "__init__"), _n_(654495, "self", lambda: self), _n_(654496, "parent", lambda: parent))
        _l_(654498)
        button1 = _c_(654506, _a_(654500, _n_(654499, "tk", lambda: tk), "Button"), _n_(654501, "self", lambda: self), text="1V1", command=lambda: _c_(654505, _a_(654503, _n_(654502, "controller", lambda: controller), "show_frame"), _n_(654504, "MainWindow", lambda: MainWindow)))
        _l_(654507)
        _c_(654510, _a_(654509, _n_(654508, "button1", lambda: button1), "pack"))
        _l_(654511)

        button2 = _c_(654519, _a_(654513, _n_(654512, "tk", lambda: tk), "Button"), _n_(654514, "self", lambda: self), text="Back to homescreen",
                            command=lambda: _c_(654518, _a_(654516, _n_(654515, "controller", lambda: controller), "show_frame"), _n_(654517, "Game", lambda: Game)))
        _l_(654520)
        _c_(654523, _a_(654522, _n_(654521, "button2", lambda: button2), "pack"))
        _l_(654524)

gui = _c_(654528, _n_(654527, "SeaofBTCapp", lambda: SeaofBTCapp)) 
_l_(654529) 
_c_(654532, _a_(654531, _n_(654530, "gui", lambda: gui), "mainloop"))
_l_(654533)