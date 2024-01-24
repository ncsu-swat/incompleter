# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27089880/error-attribute-error-in-tcl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(369538)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(369540)

except ImportError:
    pass
_c_(369544, _a_(369543, _a_(369542, _n_(369541, "sys", lambda: sys), "path"), "insert"), 0, 'home/ashwin/')
_l_(369545)
try:
    import portscanner
    _l_(369547)

except ImportError:
    pass

class App:
    _l_(369844)

    def __init__(self, master):
        _l_(369656)


        _c_(369550, _a_(369549, _n_(369548, "master", lambda: master), "option_add"), '*tearOff', False)
        _l_(369551)
        _c_(369554, _a_(369553, _n_(369552, "master", lambda: master), "resizable"), False,False)
        _l_(369555)

        _n_(369556, "self", lambda: self).nb = _c_(369560, _a_(369558, _n_(369557, "ttk", lambda: ttk), "Notebook"), _n_(369559, "master", lambda: master))
        _l_(369561)
        _c_(369565, _a_(369564, _a_(369563, _n_(369562, "self", lambda: self), "nb"), "pack"))
        _l_(369566)
        _c_(369570, _a_(369569, _a_(369568, _n_(369567, "self", lambda: self), "nb"), "config"), width=720,height=480)
        _l_(369571)

        _n_(369572, "self", lambda: self).zipframe = _c_(369577, _a_(369574, _n_(369573, "ttk", lambda: ttk), "Frame"), _a_(369576, _n_(369575, "self", lambda: self), "nb"))
        _l_(369578)
        _n_(369579, "self", lambda: self).scanframe = _c_(369584, _a_(369581, _n_(369580, "ttk", lambda: ttk), "Frame"), _a_(369583, _n_(369582, "self", lambda: self), "nb"))
        _l_(369585)
        _n_(369586, "self", lambda: self).botframe = _c_(369591, _a_(369588, _n_(369587, "ttk", lambda: ttk), "Frame"), _a_(369590, _n_(369589, "self", lambda: self), "nb"))
        _l_(369592)

        _n_(369593, "self", lambda: self).mb = _c_(369596, _n_(369594, "Menu", lambda: Menu), _n_(369595, "master", lambda: master))
        _l_(369597)
        _c_(369602, _a_(369599, _n_(369598, "master", lambda: master), "config"), menu = _a_(369601, _n_(369600, "self", lambda: self), "mb"))
        _l_(369603)
        file = _c_(369607, _n_(369604, "Menu", lambda: Menu), _a_(369606, _n_(369605, "self", lambda: self), "mb"))
        _l_(369608)
        info = _c_(369612, _n_(369609, "Menu", lambda: Menu), _a_(369611, _n_(369610, "self", lambda: self), "mb"))
        _l_(369613)

        _c_(369618, _a_(369616, _a_(369615, _n_(369614, "self", lambda: self), "mb"), "add_cascade"), menu = _n_(369617, "file", lambda: file), label = 'Tools')
        _l_(369619)
        _c_(369624, _a_(369622, _a_(369621, _n_(369620, "self", lambda: self), "mb"), "add_cascade"), menu = _n_(369623, "info", lambda: info), label = 'Help')
        _l_(369625)

        _c_(369630, _a_(369627, _n_(369626, "file", lambda: file), "add_command"), label='Zip Cracker', command = _a_(369629, _n_(369628, "self", lambda: self), "zipframe_create"))
        _l_(369631)
        _c_(369636, _a_(369633, _n_(369632, "file", lambda: file), "add_command"), label='Port Scanner', command = _a_(369635, _n_(369634, "self", lambda: self), "scanframe_create"))
        _l_(369637)
        _c_(369642, _a_(369639, _n_(369638, "file", lambda: file), "add_command"), label='Bot net', command =_a_(369641, _n_(369640, "self", lambda: self), "botframe_create"))
        _l_(369643)
        _c_(369648, _a_(369645, _n_(369644, "info", lambda: info), "add_command"), label='Usage', command=(lambda:_c_(369647, _n_(369646, "print", lambda: print), 'Usage')))
        _l_(369649)
        _c_(369654, _a_(369651, _n_(369650, "info", lambda: info), "add_command"), label='About', command=(lambda:_c_(369653, _n_(369652, "print", lambda: print), 'About')))
        _l_(369655)

    def zipframe_create(self):
        _l_(369716)


        _c_(369662, _a_(369659, _a_(369658, _n_(369657, "self", lambda: self), "nb"), "add"), _a_(369661, _n_(369660, "self", lambda: self), "zipframe"),text='Zip')
        _l_(369663)
        _c_(369667, _a_(369666, _a_(369665, _n_(369664, "self", lambda: self), "zipframe"), "config"), height=480,width=720)
        _l_(369668)
        zlabel1 = _c_(369675, _a_(369674, _c_(369673, _a_(369670, _n_(369669, "ttk", lambda: ttk), "Label"), _a_(369672, _n_(369671, "self", lambda: self), "zipframe"), text='Select the zip file'), "grid"), row=0,column=0, padx=5, pady=10)
        _l_(369676)
        zlabel2 = _c_(369683, _a_(369682, _c_(369681, _a_(369678, _n_(369677, "ttk", lambda: ttk), "Label"), _a_(369680, _n_(369679, "self", lambda: self), "zipframe"), text='Select the dictionary file'), "grid"), row=2,column=0, padx=5)
        _l_(369684)
        ztext1 = _c_(369691, _a_(369690, _c_(369689, _a_(369686, _n_(369685, "ttk", lambda: ttk), "Entry"), _a_(369688, _n_(369687, "self", lambda: self), "zipframe"), width = 50), "grid"), row=0,column=1,padx=5,pady=10)
        _l_(369692)
        ztext2 = _c_(369699, _a_(369698, _c_(369697, _a_(369694, _n_(369693, "ttk", lambda: ttk), "Entry"), _a_(369696, _n_(369695, "self", lambda: self), "zipframe"), width = 50), "grid"), row=2,column=1,padx=5)
        _l_(369700)
        zoutput = _c_(369706, _a_(369705, _c_(369704, _n_(369701, "Text", lambda: Text), _a_(369703, _n_(369702, "self", lambda: self), "zipframe"), width=80, height=20), "grid"), row=3,column=0,columnspan = 3,padx=5,pady=10)
        _l_(369707)
        zb1 = _c_(369714, _a_(369713, _c_(369712, _a_(369709, _n_(369708, "ttk", lambda: ttk), "Button"), _a_(369711, _n_(369710, "self", lambda: self), "zipframe"), text='Crack', width=10), "grid"), row=0,column=2,padx=5,pady=10)
        _l_(369715)


    def scanframe_create(self):
        _l_(369767)


        _c_(369722, _a_(369719, _a_(369718, _n_(369717, "self", lambda: self), "nb"), "add"), _a_(369721, _n_(369720, "self", lambda: self), "scanframe"),text='Scan')
        _l_(369723)
        _c_(369727, _a_(369726, _a_(369725, _n_(369724, "self", lambda: self), "scanframe"), "config"), height=480,width=720)
        _l_(369728)
        slabel1 = _c_(369735, _a_(369734, _c_(369733, _a_(369730, _n_(369729, "ttk", lambda: ttk), "Label"), _a_(369732, _n_(369731, "self", lambda: self), "scanframe"), text='IP address'), "grid"), row=0,column=0, padx=5, pady=10)
        _l_(369736)
        sin_put = _c_(369743, _a_(369742, _c_(369741, _a_(369738, _n_(369737, "ttk", lambda: ttk), "Entry"), _a_(369740, _n_(369739, "self", lambda: self), "scanframe"), width = 50), "grid"), row=0,column=1,padx=5,pady=10)
        _l_(369744)
        soutput = _c_(369750, _a_(369749, _c_(369748, _n_(369745, "Text", lambda: Text), _a_(369747, _n_(369746, "self", lambda: self), "scanframe"), width=80, height=20), "grid"), row=3,column=0,columnspan = 3,padx=5,pady=10)
        _l_(369751)
        sb1 = _c_(369765, _a_(369764, _c_(369763, _a_(369753, _n_(369752, "ttk", lambda: ttk), "Button"), _a_(369755, _n_(369754, "self", lambda: self), "scanframe"), text='Scan', width=6,command= _c_(369762, _n_(369756, "print", lambda: print), _c_(369761, _a_(369757, 'Content: {}', "format"), _c_(369760, _a_(369759, _n_(369758, "sin_put", lambda: sin_put), "get"))))), "grid"), row=0,column=2,padx=5,pady=10)
        _l_(369766)

    def botframe_create(self):
        _l_(369843)


        _c_(369773, _a_(369770, _a_(369769, _n_(369768, "self", lambda: self), "nb"), "add"), _a_(369772, _n_(369771, "self", lambda: self), "botframe"),text='Bot')
        _l_(369774)
        _c_(369778, _a_(369777, _a_(369776, _n_(369775, "self", lambda: self), "botframe"), "config"), height=480,width=720)
        _l_(369779)
        blabel1 = _c_(369786, _a_(369785, _c_(369784, _a_(369781, _n_(369780, "ttk", lambda: ttk), "Label"), _a_(369783, _n_(369782, "self", lambda: self), "botframe"), text='IP address'), "grid"), row=0,column=0, padx=5, pady=10)
        _l_(369787)
        blabel2 = _c_(369794, _a_(369793, _c_(369792, _a_(369789, _n_(369788, "ttk", lambda: ttk), "Label"), _a_(369791, _n_(369790, "self", lambda: self), "botframe"), text='Username'), "grid"), row=1,column=0, padx=2)
        _l_(369795)
        blabel3 = _c_(369802, _a_(369801, _c_(369800, _a_(369797, _n_(369796, "ttk", lambda: ttk), "Label"), _a_(369799, _n_(369798, "self", lambda: self), "botframe"), text='password'), "grid"), row=2,column=0, padx=2)
        _l_(369803)
        btext1 = _c_(369810, _a_(369809, _c_(369808, _a_(369805, _n_(369804, "ttk", lambda: ttk), "Entry"), _a_(369807, _n_(369806, "self", lambda: self), "botframe"), width = 30), "grid"), row=0,column=1,padx=5,pady=10)
        _l_(369811)
        btext2 = _c_(369818, _a_(369817, _c_(369816, _a_(369813, _n_(369812, "ttk", lambda: ttk), "Entry"), _a_(369815, _n_(369814, "self", lambda: self), "botframe"), width = 30), "grid"), row=1,column=1)
        _l_(369819)
        btext2 = _c_(369826, _a_(369825, _c_(369824, _a_(369821, _n_(369820, "ttk", lambda: ttk), "Entry"), _a_(369823, _n_(369822, "self", lambda: self), "botframe"), width = 30), "grid"), row=2,column=1)
        _l_(369827)
        boutput = _c_(369833, _a_(369832, _c_(369831, _n_(369828, "Text", lambda: Text), _a_(369830, _n_(369829, "self", lambda: self), "botframe"), width=80, height=20), "grid"), row=3,column=0,columnspan = 3,padx=5,pady=10)
        _l_(369834)
        bb1 = _c_(369841, _a_(369840, _c_(369839, _a_(369836, _n_(369835, "ttk", lambda: ttk), "Button"), _a_(369838, _n_(369837, "self", lambda: self), "botframe"), text='Connect', width=8), "grid"), row=2,column=2,padx=5,pady=10)
        _l_(369842)


def main():
    _l_(369856)


    root = _c_(369846, _n_(369845, "Tk", lambda: Tk))
    _l_(369847)
    feedback = _c_(369850, _n_(369848, "App", lambda: App), _n_(369849, "root", lambda: root))
    _l_(369851)
    _c_(369854, _a_(369853, _n_(369852, "root", lambda: root), "mainloop"))
    _l_(369855)

if _n_(369857, "__name__", lambda: __name__) == "__main__":
    _l_(369860)

_c_(369859, _n_(369858, "main", lambda: main)