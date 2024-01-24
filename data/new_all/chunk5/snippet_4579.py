# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55066875/typeerror-register-user-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(655093)

except ImportError:
    pass
try:
    import os
    _l_(655095)

except ImportError:
    pass
try:
    import tkinter.messagebox as tm
    _l_(655097)

except ImportError:
    pass

class SampleApp(_a_(655099, _n_(655098, "tk", lambda: tk), "Tk")):
    _l_(655114)

    def __init__(self):
        _l_(655113)

        _c_(655104, _a_(655102, _a_(655101, _n_(655100, "tk", lambda: tk), "Tk"), "__init__"), _n_(655103, "self", lambda: self))
        _l_(655105)
        _n_(655106, "self", lambda: self)._frame = None
        _l_(655107)
        _c_(655111, _a_(655109, _n_(655108, "self", lambda: self), "switch_frame"), _n_(655110, "StartPage", lambda: StartPage))
        _l_(655112)

def switch_frame(self, frame_class):
    _l_(655135)

    """Destroys current frame and replaces it with a new one."""
    new_frame = _c_(655117, _n_(655115, "frame_class", lambda: frame_class), _n_(655116, "self", lambda: self))
    _l_(655118)
    if _a_(655120, _n_(655119, "self", lambda: self), "_frame") is not None:
        _l_(655126)

        _c_(655124, _a_(655123, _a_(655122, _n_(655121, "self", lambda: self), "_frame"), "destroy"))
        _l_(655125)
    _n_(655127, "self", lambda: self)._frame = _n_(655128, "new_frame", lambda: new_frame)
    _l_(655129)
    _c_(655133, _a_(655132, _a_(655131, _n_(655130, "self", lambda: self), "_frame"), "pack"))
    _l_(655134)

class StartPage(_a_(655137, _n_(655136, "tk", lambda: tk), "Frame")):
    _l_(655175)

    def __init__(self, master):
        _l_(655174)

        _c_(655143, _a_(655140, _a_(655139, _n_(655138, "tk", lambda: tk), "Frame"), "__init__"), _n_(655141, "self", lambda: self), _n_(655142, "master", lambda: master))
        _l_(655144)
        _c_(655150, _a_(655149, _c_(655148, _a_(655146, _n_(655145, "tk", lambda: tk), "Label"), _n_(655147, "self", lambda: self), text="Please select an option below"), "pack"), side="top", fill="x", pady=10)
        _l_(655151)
        _c_(655161, _a_(655160, _c_(655159, _a_(655153, _n_(655152, "tk", lambda: tk), "Button"), _n_(655154, "self", lambda: self), text="Register",
                  command=lambda: _c_(655158, _a_(655156, _n_(655155, "master", lambda: master), "switch_frame"), _n_(655157, "register_screen", lambda: register_screen))), "pack"))
        _l_(655162)
        _c_(655172, _a_(655171, _c_(655170, _a_(655164, _n_(655163, "tk", lambda: tk), "Button"), _n_(655165, "self", lambda: self), text="Login",
                  command=lambda: _c_(655169, _a_(655167, _n_(655166, "master", lambda: master), "switch_frame"), _n_(655168, "login_screen", lambda: login_screen))), "pack"))
        _l_(655173)

class register_screen(_a_(655177, _n_(655176, "tk", lambda: tk), "Frame")):
    _l_(655259)


    def __init__(self, master):
        _l_(655258)

        _c_(655183, _a_(655180, _a_(655179, _n_(655178, "tk", lambda: tk), "Frame"), "__init__"), _n_(655181, "self", lambda: self), _n_(655182, "master", lambda: master))
        _l_(655184)

        global username
        _l_(655185)
        global password
        _l_(655186)
        global username_entry
        _l_(655187)
        global password_entry
        _l_(655188)

        _n_(655189, "self", lambda: self).username = _c_(655191, _n_(655190, "StringVar", lambda: StringVar))
        _l_(655192)
        _n_(655193, "self", lambda: self).password = _c_(655195, _n_(655194, "StringVar", lambda: StringVar))
        _l_(655196)

        _c_(655201, _a_(655200, _c_(655199, _n_(655197, "Label", lambda: Label), _n_(655198, "self", lambda: self), text="Please enter details below"), "pack"))
        _l_(655202)
        _c_(655207, _a_(655206, _c_(655205, _n_(655203, "Label", lambda: Label), _n_(655204, "self", lambda: self), text=""), "pack"))
        _l_(655208)
        username_lable = _c_(655211, _n_(655209, "Label", lambda: Label), _n_(655210, "self", lambda: self), text="Username * ")
        _l_(655212)
        _c_(655215, _a_(655214, _n_(655213, "username_lable", lambda: username_lable), "pack"))
        _l_(655216)
        username_entry = _c_(655221, _n_(655217, "Entry", lambda: Entry), _n_(655218, "self", lambda: self), textvariable=_a_(655220, _n_(655219, "self", lambda: self), "username"))
        _l_(655222)
        _c_(655225, _a_(655224, _n_(655223, "username_entry", lambda: username_entry), "pack"))
        _l_(655226)
        password_lable = _c_(655229, _n_(655227, "Label", lambda: Label), _n_(655228, "self", lambda: self), text="Password * ")
        _l_(655230)
        _c_(655233, _a_(655232, _n_(655231, "password_lable", lambda: password_lable), "pack"))
        _l_(655234)
        password_entry = _c_(655239, _n_(655235, "Entry", lambda: Entry), _n_(655236, "self", lambda: self), textvariable=_a_(655238, _n_(655237, "self", lambda: self), "password"), show='*')
        _l_(655240)
        _c_(655243, _a_(655242, _n_(655241, "password_entry", lambda: password_entry), "pack"))
        _l_(655244)
        _c_(655249, _a_(655248, _c_(655247, _n_(655245, "Label", lambda: Label), _n_(655246, "self", lambda: self), text=""), "pack"))
        _l_(655250)
        _c_(655256, _a_(655255, _c_(655254, _n_(655251, "Button", lambda: Button), _n_(655252, "self", lambda: self), text="Register", width=10, height=1, command = _n_(655253, "register_user", lambda: register_user)), "pack"))
        _l_(655257)

class login_screen(_a_(655261, _n_(655260, "tk", lambda: tk), "Frame")):
    _l_(655338)


    def __init__(self, master):
        _l_(655337)

        _c_(655267, _a_(655264, _a_(655263, _n_(655262, "tk", lambda: tk), "Frame"), "__init__"), _n_(655265, "self", lambda: self), _n_(655266, "master", lambda: master))
        _l_(655268)
        _c_(655274, _a_(655273, _c_(655272, _a_(655270, _n_(655269, "tk", lambda: tk), "Label"), _n_(655271, "self", lambda: self), text="Login Page"), "grid"), row=0)
        _l_(655275)

        global username_verify
        _l_(655276)
        global password_verify
        _l_(655277)

        _n_(655278, "self", lambda: self).username_verify = _c_(655280, _n_(655279, "StringVar", lambda: StringVar))
        _l_(655281)
        _n_(655282, "self", lambda: self).password_verify = _c_(655284, _n_(655283, "StringVar", lambda: StringVar))
        _l_(655285)

        global username_entry1
        _l_(655286)
        global password_entry1
        _l_(655287)

        _c_(655294, _a_(655292, _c_(655291, _a_(655289, _n_(655288, "tk", lambda: tk), "Label"), _n_(655290, "self", lambda: self), text = "Username"), "grid"), row = 3, sticky=_n_(655293, "E", lambda: E))
        _l_(655295)
        username_entry1 = _c_(655299, _n_(655296, "Entry", lambda: Entry), _n_(655297, "self", lambda: self),textvariable = _n_(655298, "username_verify", lambda: username_verify)) 
        _l_(655300) 
        _c_(655303, _a_(655302, _n_(655301, "username_entry1", lambda: username_entry1), "grid"), row = 3, column = 1)
        _l_(655304)

        _c_(655311, _a_(655309, _c_(655308, _a_(655306, _n_(655305, "tk", lambda: tk), "Label"), _n_(655307, "self", lambda: self), text = "Password"), "grid"), row = 6, sticky=_n_(655310, "E", lambda: E))
        _l_(655312)
        password_entry1 = _c_(655316, _n_(655313, "Entry", lambda: Entry), _n_(655314, "self", lambda: self),show="*",textvariable = _n_(655315, "password_verify", lambda: password_verify))
        _l_(655317)
        _c_(655320, _a_(655319, _n_(655318, "password_entry1", lambda: password_entry1), "grid"), row = 6, column = 1)
        _l_(655321)

        _c_(655327, _a_(655326, _c_(655325, _a_(655323, _n_(655322, "tk", lambda: tk), "Checkbutton"), _n_(655324, "self", lambda: self), text = "Keep Me Logged In"), "grid"), columnspan = 2) 
        _l_(655328) 
        _c_(655335, _a_(655334, _c_(655333, _a_(655330, _n_(655329, "tk", lambda: tk), "Button"), _n_(655331, "self", lambda: self),text= "Login", command= _n_(655332, "login_verify", lambda: login_verify)), "grid"), row = 8) 
        _l_(655336) 