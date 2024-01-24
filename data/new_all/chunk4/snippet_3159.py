# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36001867/nameerror-name-clear-message-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Tkinter import *
    _l_(637575)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(637577)

except ImportError:
    pass

TITLE_FONT = ("Helvetica", 18, "bold")
_l_(637578)


class SampleApp(_a_(637580, _n_(637579, "tk", lambda: tk), "Tk")):
    _l_(637645)


    def __init__(self, *args, **kwargs):
        _l_(637634)

        _c_(637587, _a_(637583, _a_(637582, _n_(637581, "tk", lambda: tk), "Tk"), "__init__"), _n_(637584, "self", lambda: self), *_n_(637585, "args", lambda: args), **_n_(637586, "kwargs", lambda: kwargs))
        _l_(637588)

        # the container is where I stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = _c_(637592, _a_(637590, _n_(637589, "tk", lambda: tk), "Frame"), _n_(637591, "self", lambda: self))
        _l_(637593)
        _c_(637596, _a_(637595, _n_(637594, "container", lambda: container), "pack"), side="top", fill="both", expand=True)
        _l_(637597)
        _c_(637600, _a_(637599, _n_(637598, "container", lambda: container), "grid_rowconfigure"), 0, weight=1)
        _l_(637601)
        _c_(637604, _a_(637603, _n_(637602, "container", lambda: container), "grid_columnconfigure"), 0, weight=1)
        _l_(637605)

        _n_(637606, "self", lambda: self).frames = {}
        _l_(637607)
        for F in (_n_(637608, "MainPage", lambda: MainPage),_n_(637609, "StorageOrMotor", lambda: StorageOrMotor),_n_(637610, "Storage", lambda: Storage),_n_(637611, "Motor", lambda: Motor)):
            _l_(637629)

            page_name = _a_(637613, _n_(637612, "F", lambda: F), "__name__")
            _l_(637614)
            frame = _c_(637618, _n_(637615, "F", lambda: F), _n_(637616, "container", lambda: container), _n_(637617, "self", lambda: self))
            _l_(637619)
            _a_(637621, _n_(637620, "self", lambda: self), "frames")[_n_(637622, "page_name", lambda: page_name)] = _n_(637623, "frame", lambda: frame)
            _l_(637624)

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            _c_(637627, _a_(637626, _n_(637625, "frame", lambda: frame), "grid"), row=0, column=0, sticky="nsew")
            _l_(637628)

        _c_(637632, _a_(637631, _n_(637630, "self", lambda: self), "show_frame"), "MainPage")
        _l_(637633)

    def show_frame(self, page_name):
        _l_(637644)

        '''Show a frame for the given page name'''
        _l_(637635)
        frame = _a_(637637, _n_(637636, "self", lambda: self), "frames")[_n_(637638, "page_name", lambda: page_name)]
        _l_(637639)
        _c_(637642, _a_(637641, _n_(637640, "frame", lambda: frame), "tkraise"))
        _l_(637643)


class MainPage(_a_(637647, _n_(637646, "tk", lambda: tk), "Frame")):
    _l_(637733)


    global user_key
    _l_(637648)
    global psw_key
    _l_(637649)
    user_key=""
    _l_(637650)
    psw_key=""
    _l_(637651)

#Here is the defined for clear_message `def`   
    def clear_message():
        _l_(637660)

        _c_(637654, _a_(637653, _n_(637652, "user_key", lambda: user_key), "delete"), 0, 'END')
        _l_(637655)
        _c_(637658, _a_(637657, _n_(637656, "psw_key", lambda: psw_key), "delete"), 0, 'END')
        _l_(637659)

    def __init__(self, parent, controller):
        _l_(637732)

        _c_(637666, _a_(637663, _a_(637662, _n_(637661, "tk", lambda: tk), "Frame"), "__init__"), _n_(637664, "self", lambda: self), _n_(637665, "parent", lambda: parent))
        _l_(637667)
        _n_(637668, "self", lambda: self).controller = _n_(637669, "controller", lambda: controller)
        _l_(637670)
        Username = _c_(637674, _a_(637672, _n_(637671, "tk", lambda: tk), "Label"), _n_(637673, "self", lambda: self), text="Username:",font=("Helvetica", "20","bold"))
        _l_(637675)
        _c_(637678, _a_(637677, _n_(637676, "Username", lambda: Username), "grid"), row=2, column=3,columnspan=2)
        _l_(637679)
        Password = _c_(637683, _a_(637681, _n_(637680, "tk", lambda: tk), "Label"), _n_(637682, "self", lambda: self), text="Password:",font=("Helvetica", "20","bold"))
        _l_(637684)
        _c_(637687, _a_(637686, _n_(637685, "Password", lambda: Password), "grid"), row=3, column=3,columnspan=2)
        _l_(637688)

#............        
        Username_key = _c_(637693, _a_(637690, _n_(637689, "tk", lambda: tk), "Entry"), _n_(637691, "self", lambda: self), textvariable = _n_(637692, "user_key", lambda: user_key), width=19, font=("Helvetica", "15"))
        _l_(637694)
        _c_(637697, _a_(637696, _n_(637695, "Username_key", lambda: Username_key), "grid"), row=2, column=5,columnspan=5)
        _l_(637698)
        Password_key = _c_(637703, _a_(637700, _n_(637699, "tk", lambda: tk), "Entry"), _n_(637701, "self", lambda: self), textvariable = _n_(637702, "psw_key", lambda: psw_key), width=19, font=("Helvetica", "15"))
        _l_(637704)
        _c_(637707, _a_(637706, _n_(637705, "Password_key", lambda: Password_key), "grid"), row=3, column=5,columnspan=5)
        _l_(637708)
        log_in = _c_(637715, _a_(637710, _n_(637709, "tk", lambda: tk), "Button"), _n_(637711, "self", lambda: self), width=7, text="Log In", command=lambda: _c_(637714, _a_(637713, _n_(637712, "controller", lambda: controller), "show_frame"), "StorageOrMotor"))
        _l_(637716)
        _c_(637719, _a_(637718, _n_(637717, "log_in", lambda: log_in), "grid"), row=5,column=8,columnspan=2)
        _l_(637720)
#............`I try to create a clear button`
        Clear = _c_(637726, _a_(637722, _n_(637721, "tk", lambda: tk), "Button"), _n_(637723, "self", lambda: self), width=7, text=" Clear " ,command=lambda:_c_(637725, _n_(637724, "clear_message", lambda: clear_message)))
        _l_(637727)
        _c_(637730, _a_(637729, _n_(637728, "Clear", lambda: Clear), "grid"), row=5,column=5,columnspan=2)
        _l_(637731)