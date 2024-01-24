# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38399601/attributeerror-type-object-class-has-no-attribute-stringvar
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(448107)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(448109)

except ImportError:
    pass

LARGE_FONT = ("Verdana", 12)
_l_(448110)


class ManyPagesApp(_a_(448112, _n_(448111, "tk", lambda: tk), "Tk")):
    _l_(448172)


    def __init__(self, *args, **kwargs):
        _l_(448162)

        _c_(448119, _a_(448115, _a_(448114, _n_(448113, "tk", lambda: tk), "Tk"), "__init__"), _n_(448116, "self", lambda: self), *_n_(448117, "args", lambda: args), **_n_(448118, "kwargs", lambda: kwargs))
        _l_(448120)
        container = _c_(448124, _a_(448122, _n_(448121, "tk", lambda: tk), "Frame"), _n_(448123, "self", lambda: self))
        _l_(448125)
        _c_(448128, _a_(448127, _n_(448126, "container", lambda: container), "pack"), side="top", fill="both", expand=True)
        _l_(448129)
        _c_(448132, _a_(448131, _n_(448130, "container", lambda: container), "grid_rowconfigure"), 0, weight=1)
        _l_(448133)
        _c_(448136, _a_(448135, _n_(448134, "container", lambda: container), "grid_columnconfigure"), 0, weight=1)
        _l_(448137)
        _n_(448138, "self", lambda: self).frames = {}
        _l_(448139)

        # This loop adds the pages into the frame
        for F in (_n_(448140, "Page1", lambda: Page1), _n_(448141, "Page2", lambda: Page2)):
            _l_(448156)

            frame = _c_(448145, _n_(448142, "F", lambda: F), _n_(448143, "container", lambda: container), _n_(448144, "self", lambda: self))
            _l_(448146)
            _a_(448148, _n_(448147, "self", lambda: self), "frames")[_n_(448149, "F", lambda: F)] = _n_(448150, "frame", lambda: frame)
            _l_(448151)
            _c_(448154, _a_(448153, _n_(448152, "frame", lambda: frame), "grid"), row=0, column=0, sticky="nsew")
            _l_(448155)
        _c_(448160, _a_(448158, _n_(448157, "self", lambda: self), "show_frame"), _n_(448159, "Page1", lambda: Page1))
        _l_(448161)

    # This function raises the page to the "top" level of the frame
    def show_frame(self, cont):
        _l_(448171)

        frame = _a_(448164, _n_(448163, "self", lambda: self), "frames")[_n_(448165, "cont", lambda: cont)]
        _l_(448166)
        _c_(448169, _a_(448168, _n_(448167, "frame", lambda: frame), "tkraise"))
        _l_(448170)


# Creates what shows in start page
class Page1(_a_(448174, _n_(448173, "tk", lambda: tk), "Frame")):
    _l_(448246)


    def __init__(self, parent, controller):
        _l_(448238)

        _c_(448180, _a_(448177, _a_(448176, _n_(448175, "tk", lambda: tk), "Frame"), "__init__"), _n_(448178, "self", lambda: self), _n_(448179, "parent", lambda: parent))
        _l_(448181)

        button1 = _c_(448189, _a_(448183, _n_(448182, "ttk", lambda: ttk), "Button"), _n_(448184, "self", lambda: self), text="Go to Page 2", command=lambda: _c_(448188, _a_(448186, _n_(448185, "controller", lambda: controller), "show_frame"), _n_(448187, "Page2", lambda: Page2)))
        _l_(448190)
        _c_(448193, _a_(448192, _n_(448191, "button1", lambda: button1), "pack"))
        _l_(448194)

        button2 = _c_(448201, _a_(448196, _n_(448195, "ttk", lambda: ttk), "Button"), _n_(448197, "self", lambda: self), text="THIS BUTTON CHANGES LABEL ON PAGE 1",
                         command=lambda: _c_(448200, _a_(448199, _n_(448198, "self", lambda: self), "labelChanger"), 'This label was changed by using button 2'))
        _l_(448202)
        _c_(448205, _a_(448204, _n_(448203, "button2", lambda: button2), "pack"))
        _l_(448206)

        label = _c_(448211, _a_(448208, _n_(448207, "ttk", lambda: ttk), "Label"), _n_(448209, "self", lambda: self), text='This is Page 1', font=_n_(448210, "LARGE_FONT", lambda: LARGE_FONT))
        _l_(448212)
        _c_(448215, _a_(448214, _n_(448213, "label", lambda: label), "pack"), pady=10, padx=10)
        _l_(448216)

        _n_(448217, "self", lambda: self).labelVariable1 = _c_(448220, _a_(448219, _n_(448218, "tk", lambda: tk), "StringVar"))
        _l_(448221)
        _c_(448225, _a_(448224, _a_(448223, _n_(448222, "self", lambda: self), "labelVariable1"), "set"), 'This label will be changed')
        _l_(448226)
        label = _c_(448232, _a_(448228, _n_(448227, "tk", lambda: tk), "Label"), _n_(448229, "self", lambda: self), textvariable= _a_(448231, _n_(448230, "self", lambda: self), "labelVariable1"))
        _l_(448233)
        _c_(448236, _a_(448235, _n_(448234, "label", lambda: label), "pack"))
        _l_(448237)

    def labelChanger(self, text):
        _l_(448245)

        _c_(448243, _a_(448241, _a_(448240, _n_(448239, "self", lambda: self), "labelVariable1"), "set"), _n_(448242, "text", lambda: text))
        _l_(448244)

class Page2(_a_(448248, _n_(448247, "tk", lambda: tk), "Frame")):
    _l_(448295)


    def __init__(self, parent, controller):
        _l_(448294)

        _c_(448254, _a_(448251, _a_(448250, _n_(448249, "tk", lambda: tk), "Frame"), "__init__"), _n_(448252, "self", lambda: self), _n_(448253, "parent", lambda: parent))
        _l_(448255)
        objectofpage1 = _n_(448256, "Page1", lambda: Page1)
        _l_(448257)

        button1 = _c_(448265, _a_(448259, _n_(448258, "ttk", lambda: ttk), "Button"), _n_(448260, "self", lambda: self), text="Goes to page 1", command=lambda: _c_(448264, _a_(448262, _n_(448261, "controller", lambda: controller), "show_frame"), _n_(448263, "Page1", lambda: Page1)))
        _l_(448266)
        _c_(448269, _a_(448268, _n_(448267, "button1", lambda: button1), "pack"))
        _l_(448270)

        button2 = _c_(448278, _a_(448272, _n_(448271, "ttk", lambda: ttk), "Button"), _n_(448273, "self", lambda: self), text="Changes Label 2 in page 1",
                         command=lambda: _c_(448277, _a_(448275, _n_(448274, "objectofpage1", lambda: objectofpage1), "labelChanger"), _n_(448276, "objectofpage1", lambda: objectofpage1), 'You have changed the label in page 1'))
        _l_(448279)
        _c_(448282, _a_(448281, _n_(448280, "button2", lambda: button2), "pack"))
        _l_(448283)

        label = _c_(448288, _a_(448285, _n_(448284, "ttk", lambda: ttk), "Label"), _n_(448286, "self", lambda: self), text='This is page 2', font=_n_(448287, "LARGE_FONT", lambda: LARGE_FONT))
        _l_(448289)
        _c_(448292, _a_(448291, _n_(448290, "label", lambda: label), "pack"), pady=10, padx=10)
        _l_(448293)



# Runs everything
if _n_(448296, "__name__", lambda: __name__) == "__main__":
    _l_(448304)

    app = _c_(448298, _n_(448297, "ManyPagesApp", lambda: ManyPagesApp))
    _l_(448299)
    _c_(448302, _a_(448301, _n_(448300, "app", lambda: app), "mainloop"))
    _l_(448303)