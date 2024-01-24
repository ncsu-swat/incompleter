# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50222747/attributeerror-application-object-has-no-attribute-tk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(454342)

except ImportError:
    pass

class Application(_a_(454344, _n_(454343, "tk", lambda: tk), "Frame")):
    _l_(454386)


    def __init__(self, master):
        _l_(454381)

        frame = _c_(454348, _a_(454346, _n_(454345, "tk", lambda: tk), "Frame"), _n_(454347, "master", lambda: master))
        _l_(454349)
        _a_(454351, _n_(454350, "frame", lambda: frame), "pack")
        _l_(454352)

        _n_(454353, "self", lambda: self).PRINT = _c_(454360, _a_(454355, _n_(454354, "tk", lambda: tk), "Button"), _n_(454356, "frame", lambda: frame), text = 'Print', fg = 'Red', command = _c_(454359, _a_(454358, _n_(454357, "self", lambda: self), "Print")))
        _l_(454361)
        _c_(454365, _a_(454364, _a_(454363, _n_(454362, "self", lambda: self), "PRINT"), "pack"), side = 'left')    
        _l_(454366)    

        _n_(454367, "self", lambda: self).QUIT = _c_(454374, _a_(454369, _n_(454368, "tk", lambda: tk), "Button"), _n_(454370, "frame", lambda: frame), text = 'Quit', fg = 'Red', command = _c_(454373, _a_(454372, _n_(454371, "self", lambda: self), "quit")))
        _l_(454375)
        _c_(454379, _a_(454378, _a_(454377, _n_(454376, "self", lambda: self), "QUIT"), "pack"), side = 'left')    
        _l_(454380)    

    def Print(self):
        _l_(454385)

        _c_(454383, _n_(454382, "print", lambda: print), 'at least somethings working')
        _l_(454384)

root = _c_(454389, _a_(454388, _n_(454387, "tk", lambda: tk), "Tk"))
_l_(454390)

b = _c_(454393, _n_(454391, "Application", lambda: Application), _n_(454392, "root", lambda: root))    
_l_(454394)    
_c_(454397, _a_(454396, _n_(454395, "root", lambda: root), "mainloop"))
_l_(454398)