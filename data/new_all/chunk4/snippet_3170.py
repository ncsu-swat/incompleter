# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29923129/why-am-i-getting-typeerror-init-missing-1-required-positional-argument
#Imports#
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(606365)

except ImportError:
    pass
_c_(606369, _a_(606368, _a_(606367, _n_(606366, "sys", lambda: sys), "path"), "append"), "F:\A2\Computing\Comp 4\Python34\Lib\site-packages")
_l_(606370)
try:
    from tkinter import *
    _l_(606372)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(606374)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(606376)

except ImportError:
    pass

#Main Code#


class GUIImage(_a_(606378, _n_(606377, "tk", lambda: tk), "Tk")):
    _l_(606488)

    def __init__(self, master, *pargs):
        _l_(606449)

        _c_(606385, _a_(606381, _a_(606380, _n_(606379, "tk", lambda: tk), "Tk"), "__init__"), _n_(606382, "self", lambda: self), _n_(606383, "master", lambda: master), *_n_(606384, "pargs", lambda: pargs))
        _l_(606386)

        _n_(606387, "self", lambda: self).image = _c_(606390, _a_(606389, _n_(606388, "Image", lambda: Image), "open"), "F:\A2\Computing\Comp 4\Code\main.jpg")
        _l_(606391)
        _n_(606392, "self", lambda: self).img_copy= _c_(606396, _a_(606395, _a_(606394, _n_(606393, "self", lambda: self), "image"), "copy"))
        _l_(606397)

        _n_(606398, "self", lambda: self).background_image = _c_(606403, _a_(606400, _n_(606399, "ImageTk", lambda: ImageTk), "PhotoImage"), _a_(606402, _n_(606401, "self", lambda: self), "image"))
        _l_(606404)

        _n_(606405, "self", lambda: self).background = _c_(606410, _n_(606406, "Label", lambda: Label), _n_(606407, "self", lambda: self), image=_a_(606409, _n_(606408, "self", lambda: self), "background_image"))
        _l_(606411)
        _c_(606417, _a_(606414, _a_(606413, _n_(606412, "self", lambda: self), "background"), "pack"), fill=_n_(606415, "BOTH", lambda: BOTH), expand=_n_(606416, "YES", lambda: YES))
        _l_(606418)
        _c_(606424, _a_(606421, _a_(606420, _n_(606419, "self", lambda: self), "background"), "bind"), '<Configure>', _a_(606423, _n_(606422, "self", lambda: self), "_resize_image"))
        _l_(606425)

        _n_(606426, "self", lambda: self).frames={}
        _l_(606427)

        for F in(_n_(606428, "mainMenuGUI", lambda: mainMenuGUI),_n_(606429, "addUserGUI", lambda: addUserGUI),_n_(606430, "delUserGUI", lambda: delUserGUI),_n_(606431, "visitorGUI", lambda: visitorGUI),_n_(606432, "prechkGUI", lambda: prechkGUI),_n_(606433, "userManual", lambda: userManual)):
            _l_(606448)

            frame = _c_(606437, _n_(606434, "F", lambda: F), _n_(606435, "container", lambda: container), _n_(606436, "self", lambda: self))
            _l_(606438)
            _a_(606440, _n_(606439, "self", lambda: self), "frames")[_n_(606441, "Frames", lambda: Frames)] = _n_(606442, "frame", lambda: frame)
            _l_(606443)
            _c_(606446, _a_(606445, _n_(606444, "frame", lambda: frame), "grid"), row=0,column=0,sticky="nsew")
            _l_(606447)

    def show_frame(self, cont):
        _l_(606458)

        frame = _a_(606451, _n_(606450, "self", lambda: self), "frames")[_n_(606452, "cont", lambda: cont)]
        _l_(606453)
        _c_(606456, _a_(606455, _n_(606454, "frame", lambda: frame), "tkraise"))
        _l_(606457)

    def _resize_image(self,event):
        _l_(606487)


        new_width = _a_(606460, _n_(606459, "event", lambda: event), "width")
        _l_(606461)
        new_height = _a_(606463, _n_(606462, "event", lambda: event), "height")
        _l_(606464)

        _n_(606465, "self", lambda: self).image = _c_(606471, _a_(606468, _a_(606467, _n_(606466, "self", lambda: self), "img_copy"), "resize"), (_n_(606469, "new_width", lambda: new_width), _n_(606470, "new_height", lambda: new_height)))
        _l_(606472)

        _n_(606473, "self", lambda: self).background_image = _c_(606478, _a_(606475, _n_(606474, "ImageTk", lambda: ImageTk), "PhotoImage"), _a_(606477, _n_(606476, "self", lambda: self), "image"))
        _l_(606479)
        _c_(606485, _a_(606482, _a_(606481, _n_(606480, "self", lambda: self), "background"), "configure"), image =  _a_(606484, _n_(606483, "self", lambda: self), "background_image"))
        _l_(606486)


class mainMenuGUI(_a_(606490, _n_(606489, "tk", lambda: tk), "Frame")):
    _l_(606571)

    def __init__(self,parent,controller):
        _l_(606570)

        _c_(606496, _a_(606493, _a_(606492, _n_(606491, "tk", lambda: tk), "Frame"), "__init"), _n_(606494, "self", lambda: self),_n_(606495, "parent", lambda: parent))
        _l_(606497)
        mainMenuGUI = _c_(606500, _n_(606498, "GUIImage", lambda: GUIImage), _n_(606499, "App", lambda: App))
        _l_(606501)
        _c_(606506, _a_(606503, _n_(606502, "mainMenuGUI", lambda: mainMenuGUI), "pack"), fill=_n_(606504, "BOTH", lambda: BOTH), expand=_n_(606505, "YES", lambda: YES))
        _l_(606507)
        MMText = _c_(606512, _a_(606511, _c_(606510, _n_(606508, "Label", lambda: Label), _n_(606509, "self", lambda: self), text ="Main Menu",bg ="#FD7F17", font = ("Arial Black",18)), "place"), relx=.40, rely=.05)
        _l_(606513)
        MMButton1= _c_(606522, _a_(606521, _c_(606520, _n_(606514, "Button", lambda: Button), _n_(606515, "self", lambda: self), text = "Add User", fg = "white",bg = "dark grey", command = lambda:_c_(606519, _a_(606517, _n_(606516, "controller", lambda: controller), "show_frame"), _n_(606518, "addUserGUI", lambda: addUserGUI)),height = "1", width ="10", font = ("Arial Black",14)), "place"), relx =.38 , rely=.14)
        _l_(606523)
        MMButton2= _c_(606532, _a_(606531, _c_(606530, _n_(606524, "Button", lambda: Button), _n_(606525, "self", lambda: self), text = "Delete User", fg = "white",bg = "dark grey", command = lambda:_c_(606529, _a_(606527, _n_(606526, "controller", lambda: controller), "show_frame"), _n_(606528, "delUserGUI", lambda: delUserGUI)),height = "1", width ="10", font = ("Arial Black",14)), "place"), relx =.38 , rely=.28)
        _l_(606533)
        MMButton3= _c_(606542, _a_(606541, _c_(606540, _n_(606534, "Button", lambda: Button), _n_(606535, "self", lambda: self), text = "Add Visitor", fg = "white",bg = "dark grey", command = lambda:_c_(606539, _a_(606537, _n_(606536, "controller", lambda: controller), "show_frame"), _n_(606538, "VisitorGUI", lambda: VisitorGUI)),height = "1", width ="10", font = ("Arial Black",14)), "place"), relx =.38 , rely=.42)
        _l_(606543)
        MMButton4= _c_(606552, _a_(606551, _c_(606550, _n_(606544, "Button", lambda: Button), _n_(606545, "self", lambda: self), text = "Premises Check", fg = "white",bg = "dark grey", command =   lambda:_c_(606549, _a_(606547, _n_(606546, "controller", lambda: controller), "show_frame"), _n_(606548, "prechkGUI", lambda: prechkGUI)) ,height = "1", width ="14", font = ("Arial Black",14)), "place"), relx =.32 , rely=.56)
        _l_(606553)
        MMButton5= _c_(606558, _a_(606557, _c_(606556, _n_(606554, "Button", lambda: Button), _n_(606555, "self", lambda: self), text = "Vehicle Check", fg = "white",bg = "dark grey", command = "navVehChe",height = "1", width ="14", font = ("Arial Black",14)), "place"), relx =.32 , rely=.70)
        _l_(606559)
        MMButton6= _c_(606568, _a_(606567, _c_(606566, _n_(606560, "Button", lambda: Button), _n_(606561, "self", lambda: self), text = "User Manual", fg = "white",bg = "dark grey", command =  lambda:_c_(606565, _a_(606563, _n_(606562, "controller", lambda: controller), "show_frame"), _n_(606564, "userManual", lambda: userManual)),height = "1", width ="10", font = ("Arial Black",14)), "place"), relx =.38 , rely=.84)
        _l_(606569)

App = _c_(606573, _n_(606572, "GUIImage", lambda: GUIImage))
_l_(606574)
_c_(606577, _a_(606576, _n_(606575, "App", lambda: App), "mainloop"))
_l_(606578)